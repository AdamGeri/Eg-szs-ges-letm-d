/* =========================================================
   Egészséges életmód – projektweboldal
   script.js – Készítette: Gerecze Ádám, 2026.
   ========================================================= */

document.addEventListener("DOMContentLoaded", function () {

  /* --- Aktuális évszám a láblécben --- */
  var ev = document.getElementById("ev");
  if (ev) { ev.textContent = new Date().getFullYear(); }

  /* --- Napi ellenőrzőlista (csak a kezdőlapon) --- */
  var lista = document.getElementById("lista");
  if (lista) {
    var dobozok = lista.querySelectorAll('input[type="checkbox"]');
    var sav = document.getElementById("sav");
    var uzenet = document.getElementById("visszajelzes");

    var szovegek = [
      "Jelöld be, amit ma már megtettél.",
      "Megvan az első — ez a legnehezebb.",
      "Jó úton haladsz.",
      "Fele kész. Ez már egy jó nap.",
      "Ez már nagyon rendben van.",
      "Alig maradt ki valami.",
      "Mind a hat megvan. Ilyen egy jó nap."
    ];

    function frissit() {
      var db = 0;
      dobozok.forEach(function (d) { if (d.checked) { db++; } });
      var szazalek = Math.round((db / dobozok.length) * 100);
      sav.style.width = szazalek + "%";
      sav.style.background = db >= 5 ? "#1F7A5C" : (db >= 3 ? "#7FB89A" : "#E9873F");
      sav.parentElement.setAttribute("aria-valuenow", db);
      uzenet.innerHTML = "<strong>" + db + " / " + dobozok.length + "</strong> — " + szovegek[db];
    }

    dobozok.forEach(function (d) { d.addEventListener("change", frissit); });
    frissit();
  }

  /* --- Sima görgetés a belső hivatkozásokra --- */
  var mozgasKerules = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  document.querySelectorAll('a[href^="#"]').forEach(function (link) {
    link.addEventListener("click", function (e) {
      var cel = document.querySelector(link.getAttribute("href"));
      if (cel) {
        e.preventDefault();
        cel.scrollIntoView({ behavior: mozgasKerules ? "auto" : "smooth", block: "start" });
      }
    });
  });

});
