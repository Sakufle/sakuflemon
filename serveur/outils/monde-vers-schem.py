"""Exporte une zone d'un monde 1.21.11 en .schem Sponge v2 pour 1.21.1 (DataVersion 3955)."""
import sys, zlib, io, glob, math, json, collections
import numpy as np, nbtlib
from nbtlib import Compound, List, Int, String, Short, ByteArray, IntArray
reg, blocks_json, out = sys.argv[1], sys.argv[2], sys.argv[3]
X0, X1, Z0, Z1, Y0, Y1 = map(int, sys.argv[4:10])
W, L, H = X1-X0+1, Z1-Z0+1, Y1-Y0+1
B = json.load(open(blocks_json))
RENAME = {'iron_chain': 'chain', 'bedrock': 'stone'}
vol = np.zeros((H, L, W), np.int32)
pal = {'minecraft:air': 0}; issues = collections.Counter(); bents = []
def fix_state(p):
    n = str(p['Name']).split(':')[1]
    if n == 'barrier':
        return 'minecraft:water[level=0]' if str(p.get('Properties', {}).get('waterlogged', 'false')) == 'true' else 'minecraft:air'
    n = RENAME.get(n, n)
    if n not in B: issues['bloc inconnu '+n] += 1; return 'minecraft:air'
    props, default = B[n]
    given = {k: str(v) for k, v in p.get('Properties', {}).items()}
    st = {}
    for k, vals in props.items():
        v = given.get(k, default[k])
        if v not in vals: issues[f'prop {n}.{k}={v}'] += 1; v = default[k]
        st[k] = v
    for k in given:
        if k not in props: issues[f'prop retirée {n}.{k}'] += 1
    return f'minecraft:{n}' + ('[' + ','.join(f'{k}={v}' for k, v in sorted(st.items())) + ']' if st else '')
def txt(v):
    if isinstance(v, String): s = str(v); return s if s[:1] in '{["' else json.dumps(s)
    return json.dumps(nbt_to_py(v))
def nbt_to_py(v):
    if isinstance(v, dict): return {k: nbt_to_py(x) for k, x in v.items()}
    if isinstance(v, list): return [nbt_to_py(x) for x in v]
    return v.unpack() if hasattr(v, 'unpack') else v
def chunks_of(path):
    data = open(path, 'rb').read()
    for i in range(1024):
        off = int.from_bytes(data[i*4:i*4+3], 'big')
        if not off: continue
        p = off*4096; ln = int.from_bytes(data[p:p+4], 'big'); ct = data[p+4]
        raw = data[p+5:p+4+ln]; raw = zlib.decompress(raw) if ct == 2 else raw
        yield nbtlib.File.parse(io.BytesIO(raw))
for f in glob.glob(reg+'/*.mca'):
    rx, rz = map(int, f.split('/')[-1].split('.')[1:3])
    if rx*512 > X1 or rx*512+511 < X0 or rz*512 > Z1 or rz*512+511 < Z0: continue
    for c in chunks_of(f):
        cx, cz = int(c['xPos']), int(c['zPos'])
        if cx*16 > X1 or cx*16+15 < X0 or cz*16 > Z1 or cz*16+15 < Z0: continue
        for s in c.get('sections', []):
            bs = s.get('block_states'); sy = int(s['Y'])
            if not bs or sy*16 > Y1 or sy*16+15 < Y0: continue
            loc = [pal.setdefault(fs, len(pal)) for fs in (fix_state(p) for p in bs['palette'])]
            if len(loc) == 1: idx = np.zeros(4096, np.int64)
            else:
                bits = max(4, math.ceil(math.log2(len(loc)))); per = 64//bits; mask = (1 << bits)-1
                arr = np.array([int(l) & ((1 << 64)-1) for l in bs['data']], dtype=np.uint64)
                idx = np.stack([(arr >> np.uint64(k*bits)) & np.uint64(mask) for k in range(per)], 1).reshape(-1)[:4096].astype(np.int64)
            g = np.array(loc, np.int32)[idx].reshape(16, 16, 16)
            for ly in range(16):
                y = sy*16+ly-Y0
                if not 0 <= y < H: continue
                xs = slice(max(0, X0-cx*16), min(16, X1-cx*16+1)); zs = slice(max(0, Z0-cz*16), min(16, Z1-cz*16+1))
                vol[y, cz*16+zs.start-Z0:cz*16+zs.stop-Z0, cx*16+xs.start-X0:cx*16+xs.stop-X0] = g[ly, zs, xs]
        for t in c.get('block_entities', []):
            x, y, z = int(t['x']), int(t['y']), int(t['z'])
            if not (X0 <= x <= X1 and Y0 <= y <= Y1 and Z0 <= z <= Z1): continue
            d = Compound({k: v for k, v in t.items() if k not in ('x', 'y', 'z', 'id', 'keepPacked')})
            for side in ('front_text', 'back_text'):
                if side in d and 'messages' in d[side]:
                    d[side]['messages'] = List[String]([String(txt(m)) for m in d[side]['messages']])
            d['Pos'] = IntArray([x-X0, y-Y0, z-Z0]); d['Id'] = String(t['id'])
            bents.append(d)
flat = vol.reshape(-1)
buf = bytearray()
for v in flat.tolist():
    while v > 127: buf.append((v & 127) | 128); v >>= 7
    buf.append(v)
root = Compound({'Version': Int(2), 'DataVersion': Int(3955), 'Width': Short(W), 'Height': Short(H), 'Length': Short(L),
    'Offset': IntArray([0, 0, 0]), 'PaletteMax': Int(len(pal)), 'Palette': Compound({k: Int(v) for k, v in pal.items()}),
    'BlockData': ByteArray(np.frombuffer(bytes(buf), np.int8)), 'BlockEntities': List[Compound](bents),
    'Metadata': Compound({'WEOffsetX': Int(0), 'WEOffsetY': Int(0), 'WEOffsetZ': Int(0)})})
nbtlib.File({'Schematic': root}).save(out, gzipped=True) if False else nbtlib.File(root, root_name='Schematic').save(out, gzipped=True)
print('taille', W, H, L, 'palette', len(pal), 'block entities', len(bents)); print('problèmes', issues.most_common(20))
