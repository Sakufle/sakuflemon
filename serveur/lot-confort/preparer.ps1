# Télécharge la sélection du 30/10 (Minecraft 1.21.1) depuis Modrinth et écrit rapport.json
# Usage : powershell -ExecutionPolicy Bypass -File preparer.ps1 -Out "$env:USERPROFILE\Documents\sakuflemon-lot-confort"
param([string]$Out = "$env:USERPROFILE\Documents\sakuflemon-lot-confort")
$ErrorActionPreference = 'Stop'
$api = 'https://api.modrinth.com/v2'
$h = @{ 'User-Agent' = 'Sakufle/sakuflemon (lot-confort)' }
$slugs = @(
 'cobblemon-safepastures','more-cobblemon-tweaks','catch-rate-display','cobblemon-droploottables','cobblemon-cobblestats',
 'cobblemon-pasture-loot','cobblemon-pasture-loot-fix','cobblemonextras','invview','vanish','death-backup','styledplayerlist',
 'carpet','servercore','krypton','clumps','mouse-tweaks','appleskin','inventory-sorting',
 'cobblethemes','cobblemon-playerxp','missingmons-cobblemon','cobblemon-journey-mounts','cobblemotion',
 'winterglides-extra-animations-cobblemon','better-caps','yungs-better-dungeons','yungs-better-mineshafts',
 'yungs-better-strongholds','repurposed-structures-fabric','when-dungeons-arise','mes-moogs-end-structures','lootrmon'
)
New-Item -ItemType Directory -Force -Path $Out | Out-Null
Add-Type -AssemblyName System.IO.Compression.FileSystem
$done = @{}; $rapport = @()
$queue = [System.Collections.Queue]::new(); $slugs | ForEach-Object { $queue.Enqueue(@($_, 'choisi')) }
while ($queue.Count) {
  $slug, $why = $queue.Dequeue()
  try {
    $p = Invoke-RestMethod -Headers $h "$api/project/$slug"
    if ($done[$p.id]) { continue }; $done[$p.id] = 1
    $vs = Invoke-RestMethod -Headers $h ("$api/project/$($p.id)/version?game_versions=" + [uri]::EscapeDataString('["1.21.1"]'))
    $v = $vs | Where-Object { $_.loaders -contains 'fabric' } | Select-Object -First 1
    if (-not $v) { $v = $vs | Where-Object { $_.loaders -contains 'datapack' } | Select-Object -First 1 }
    if (-not $v) { $v = $vs | Select-Object -First 1 }
    if (-not $v) { $rapport += [pscustomobject]@{slug=$p.slug; raison=$why; erreur='aucune version 1.21.1'}; continue }
    $f = $v.files | Where-Object primary | Select-Object -First 1; if (-not $f) { $f = $v.files[0] }
    $dir = Join-Path $Out $p.project_type; New-Item -ItemType Directory -Force -Path $dir | Out-Null
    $dest = Join-Path $dir $f.filename
    Invoke-WebRequest -Headers $h -Uri $f.url -OutFile $dest
    $sha = (Get-FileHash -Algorithm SHA512 $dest).Hash.ToLower()
    $dep = ''; $brk = ''
    if ($f.filename -like '*.jar') {
      $z = [IO.Compression.ZipFile]::OpenRead($dest)
      $e = $z.GetEntry('fabric.mod.json')
      if ($e) { $j = (New-Object IO.StreamReader($e.Open())).ReadToEnd() | ConvertFrom-Json
        $dep = ($j.depends | ConvertTo-Json -Compress); $brk = ($j.breaks | ConvertTo-Json -Compress) }
      $z.Dispose()
    }
    foreach ($d in $v.dependencies | Where-Object dependency_type -eq 'required') {
      if ($d.project_id -and -not $done[$d.project_id]) { $queue.Enqueue(@($d.project_id, "dependance de $($p.slug)")) }
    }
    $rapport += [pscustomobject]@{slug=$p.slug; raison=$why; type=$p.project_type; client=$p.client_side; serveur=$p.server_side;
      project_id=$p.id; version_id=$v.id; version=$v.version_number; loaders=($v.loaders -join ','); date=$v.date_published;
      fichier=$f.filename; url=$f.url; sha512=$sha; sha512_ok=($sha -eq $f.hashes.sha512); depends=$dep; breaks=$brk}
    Write-Host "OK  $($p.slug) $($v.version_number) [$($v.loaders -join ',')]"
  } catch { $rapport += [pscustomobject]@{slug=$slug; raison=$why; erreur=$_.Exception.Message}; Write-Host "ERR $slug $($_.Exception.Message)" }
}
$rapport | ConvertTo-Json -Depth 4 | Set-Content -Encoding UTF8 (Join-Path $Out 'rapport.json')
Write-Host "Rapport : $(Join-Path $Out 'rapport.json')"
