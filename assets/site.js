(function () {
  var c = window.SAKUFLEMON;
  var ip = c.port === 25565 ? c.adresse : c.adresse + ":" + c.port;

  document.querySelectorAll("[data-ip]").forEach(function (el) { el.textContent = ip; });
  document.querySelectorAll("[data-version]").forEach(function (el) { el.textContent = c.version; });
  document.querySelectorAll("[data-prism]").forEach(function (el) { el.href = c.instancePrism; });

  document.querySelectorAll("[data-copy-ip]").forEach(function (btn) {
    btn.addEventListener("click", function () {
      navigator.clipboard.writeText(ip).then(function () {
        var t = btn.textContent;
        btn.textContent = "Copié !";
        setTimeout(function () { btn.textContent = t; }, 1500);
      });
    });
  });

  var statut = document.getElementById("statut");
  if (statut && c.adresse !== "IP_PUBLIQUE") {
    fetch("https://api.mcsrvstat.us/3/" + ip)
      .then(function (r) { return r.json(); })
      .then(function (d) {
        if (d.online) {
          statut.innerHTML = "<b>" + d.players.online + "</b> joueurs en ligne";
        } else {
          statut.textContent = "Serveur hors ligne";
        }
      })
      .catch(function () { statut.textContent = "Statut indisponible"; });
  }

  var path = location.pathname.split("/").pop() || "index.html";
  document.querySelectorAll("nav a").forEach(function (a) {
    if (a.getAttribute("href").split("/").pop() === path) a.setAttribute("aria-current", "page");
  });
})();

