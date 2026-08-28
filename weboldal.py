# -*- coding: utf-8 -*-
"""A projektweboldal generálása.

Az oldalak számai az `osszesites.json`-ból jönnek, így új kérdőívadat esetén
elég újrafuttatni ezt a szkriptet.

Futtatás a projekt gyökeréből:
    python3 eszkozok/weboldal.py
"""
import os
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import adatok  # noqa: E402

GYOKER = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WEB = os.path.join(GYOKER, "produktum", "weboldal")
DIAGRAM_FORRAS = os.path.join(GYOKER, "produktum", "kerdoiv", "diagramok")
DIAGRAM_CEL = os.path.join(WEB, "kepek", "diagramok")

A = adatok.keszit()
if not A["van_adat"]:
    sys.exit("Előbb futtasd az elemzést: python3 produktum/kerdoiv/elemzes.py")

N = A["n"]
SAV = ""

MENU = [("index.html", "Kezdőlap"), ("taplalkozas.html", "Táplálkozás"),
        ("mozgas.html", "Mozgás"), ("alvas.html", "Alvás és képernyő"),
        ("kutatas.html", "Kutatásunk"), ("forrasok.html", "Források")]


def fejlec(fajl, cim, leiras):
    elemek = ""
    for href, nev in MENU:
        akt = ' active" aria-current="page' if href == fajl else ''
        elemek += f'        <li class="nav-item"><a class="nav-link{akt}" href="{href}">{nev}</a></li>\n'
    return f'''<!DOCTYPE html>
<html lang="hu">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{cim} | Egészséges életmód – IKT projektmunka</title>
<meta name="description" content="{leiras}">
<meta name="author" content="Gerecze Ádám">
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700&family=Karla:wght@400;500;700&display=swap" rel="stylesheet">
<link href="css/style.css" rel="stylesheet">
</head>
<body>

<nav class="navbar navbar-expand-lg sticky-top">
  <div class="container">
    <a class="navbar-brand" href="index.html">
      <span class="brand-jel">EÉ</span> Egészséges életmód
    </a>
    <button class="navbar-toggler border-0" type="button" data-bs-toggle="collapse" data-bs-target="#menu" aria-controls="menu" aria-expanded="false" aria-label="Menü megnyitása">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="menu">
      <ul class="navbar-nav ms-auto">
{elemek}      </ul>
    </div>
  </div>
</nav>
{SAV}'''


LABLEC = '''
<footer>
  <div class="container">
    <div class="row g-4">
      <div class="col-lg-5">
        <h4>Egészséges életmód</h4>
        <p class="mb-2">IKT Projektmunka I. osztályozó vizsga házi dolgozat, 1/13. Sz. évfolyam.</p>
        <p class="mb-0">Készítette: <strong>Gerecze Ádám</strong> · 2026. augusztus</p>
      </div>
      <div class="col-6 col-lg-3">
        <h4>Oldalak</h4>
        <ul class="list-unstyled">
          <li><a href="index.html">Kezdőlap</a></li>
          <li><a href="taplalkozas.html">Táplálkozás</a></li>
          <li><a href="mozgas.html">Mozgás</a></li>
          <li><a href="alvas.html">Alvás és képernyő</a></li>
          <li><a href="kutatas.html">Kutatásunk</a></li>
          <li><a href="forrasok.html">Források</a></li>
        </ul>
      </div>
      <div class="col-6 col-lg-4">
        <h4>Fontos</h4>
        <p class="mb-0">Ez az oldal iskolai projekt keretében készült, tájékoztató célból.
        Nem helyettesíti az orvosi tanácsadást. Egészségügyi kérdésekkel fordulj
        háziorvoshoz vagy iskolaorvoshoz.</p>
      </div>
    </div>
    <div class="zaro d-flex flex-wrap justify-content-between gap-2">
      <span>© <span id="ev">2026</span> Gerecze Ádám</span>
      <span>Bootstrap 5.3 · saját CSS · saját SVG ábrák</span>
    </div>
  </div>
</footer>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
<script src="js/script.js"></script>
</body>
</html>
'''


def oldalfej(rovat, cim, bevezeto):
    return f'''
<header class="oldal-fej">
  <div class="container">
    <span class="rovat">{rovat}</span>
    <h1>{cim}</h1>
    <p class="mt-3">{bevezeto}</p>
  </div>
</header>
'''


def adatcsik(tetelek):
    dobozok = ""
    for szam, leiras in tetelek:
        dobozok += (f'      <div class="col-6 col-lg-3"><span class="szam">{szam}</span>'
                    f'<span class="leiras">{leiras}</span></div>\n')
    return f'''
<section class="adatcsik">
  <div class="container">
    <span class="cimke">A saját felmérésünkből · {N} kitöltő</span>
    <div class="row g-4">
{dobozok}    </div>
  </div>
</section>
'''


def diagram(fajl, alt, felirat, oszlop="col-lg-6"):
    return f'''      <div class="{oszlop}">
        <figure class="diagram">
          <img src="kepek/diagramok/{fajl}" alt="{alt}">
          <figcaption>{felirat}</figcaption>
        </figure>
      </div>
'''


def ir(fajl, cim, leiras, torzs):
    with open(os.path.join(WEB, fajl), "w", encoding="utf-8") as f:
        f.write(fejlec(fajl, cim, leiras) + torzs + LABLEC)
    print("  ✔", fajl)


# =======================================================================
# KEZDŐLAP
# =======================================================================
index = f'''
<header class="hero">
  <div class="container">
    <div class="row align-items-center g-5">
      <div class="col-lg-6">
        <span class="rovat">IKT Projektmunka I. · 1/13. Sz.</span>
        <h1>Jól élsz — de két dolog kimarad.</h1>
        <p class="bevezeto mt-3">
          Megkérdeztem {N} fiatalt arról, hogyan élnek. Aktívabbak és tudatosabbak,
          mint gondoltam — mégis van két terület, ahol szinte mindenki elmarad az
          ajánlástól. Ez az oldal arról szól, melyik ez a kettő, és mit lehet vele kezdeni.
        </p>
        <div class="d-flex flex-wrap gap-2 mt-4">
          <a href="kutatas.html" class="btn btn-zold">Mit mutatnak az adatok?</a>
          <a href="#pillerek" class="btn btn-vonalas">A négy terület</a>
        </div>
      </div>
      <div class="col-lg-6">
        <img src="kepek/hero.svg" alt="Az egészséges életmód négy pillére: táplálkozás, mozgás, alvás és folyadékfogyasztás" class="hero-kep">
        <p class="forrasjel mt-2 mb-0">Saját szerkesztésű ábra (SVG), Gerecze Ádám, 2026.</p>
      </div>
    </div>
  </div>
</header>
''' + adatcsik([
    (f"{A['sport_gyakori_sz']}%", "mozog legalább heti három alkalommal"),
    (f"{A['zoldseg_sok_fo']} fő", f"eszik napi 4-szer zöldséget vagy gyümölcsöt – a {N}-ből"),
    (f"{A['alvas_keves_sz']}%", "7 óránál kevesebbet alszik iskolanapokon"),
    (f"{A['faradt_rendszeres_sz']}%", "érzi magát legalább hetente többször fáradtnak"),
]) + f'''
<section class="szakasz szakasz-vilagos" id="pillerek">
  <div class="container">
    <div class="row mb-4">
      <div class="col-lg-8">
        <span class="rovat">Témák</span>
        <h2>Négy terület, ami tényleg számít</h2>
        <p class="text-secondary mb-0">
          A felmérésem szerint a megkérdezettek a mozgásban és a folyadékfogyasztásban
          erősek, a zöldségfogyasztásban és az alvásban viszont majdnem mindenki
          elmarad. Mindegyik témánál megmutatom, mit mond a szakirodalom, és mit
          mutattak a saját adataim.
        </p>
      </div>
    </div>
    <div class="row g-4">
      <div class="col-md-6 col-lg-3">
        <article class="kartya">
          <div class="kartya-ikon">🍎</div>
          <h3>Táplálkozás</h3>
          <p class="text-secondary">A tányérmodell és a felmérés leggyengébb pontja: a zöldség- és gyümölcsfogyasztás.</p>
          <a href="taplalkozas.html">Tovább →</a>
        </article>
      </div>
      <div class="col-md-6 col-lg-3">
        <article class="kartya">
          <div class="kartya-ikon">🏃</div>
          <h3>Mozgás</h3>
          <p class="text-secondary">A minta legerősebb területe — és miért nem véd meg a mozgás mindentől.</p>
          <a href="mozgas.html">Tovább →</a>
        </article>
      </div>
      <div class="col-md-6 col-lg-3">
        <article class="kartya">
          <div class="kartya-ikon">🌙</div>
          <h3>Alvás és képernyő</h3>
          <p class="text-secondary">A második vakfolt, és a felmérés legmarkánsabb összefüggése.</p>
          <a href="alvas.html">Tovább →</a>
        </article>
      </div>
      <div class="col-md-6 col-lg-3">
        <article class="kartya">
          <div class="kartya-ikon">📊</div>
          <h3>Kutatásunk</h3>
          <p class="text-secondary">16 kérdés, {N} kitöltő, 18 diagram — és amit ezekből meg lehet tanulni.</p>
          <a href="kutatas.html">Tovább →</a>
        </article>
      </div>
    </div>
  </div>
</section>

<section class="szakasz">
  <div class="container">
    <div class="row g-5 align-items-center">
      <div class="col-lg-5">
        <span class="rovat">Kezdés</span>
        <h2>Öt lépés, ami ma elkezdhető</h2>
        <p class="text-secondary">
          A felmérésem szerint a megkérdezettek nagy része már sportol, vizet iszik és
          reggelizik. Éppen ezért nem életmódváltást javaslok, hanem öt olyan apróságot,
          ami pont a két hiányzó területre — a zöldségre és az alvásra — irányul.
        </p>
        <p class="text-secondary mb-0">
          Ezek egyikéhez sem kell külön időt szánni vagy pénzt költeni. Mindegyik egy
          döntés, nem egy program.
        </p>
      </div>
      <div class="col-lg-7">
        <img src="kepek/lepesek.svg" alt="Öt kis lépés: egy pohár víz reggel, egy gyümölcs a táskába, heti kétszer húsz perc séta, telefon félretétele lefekvés előtt, fix lefekvési idő" class="img-fluid">
        <p class="forrasjel mt-2 mb-0">Saját szerkesztésű ábra (SVG), Gerecze Ádám, 2026.</p>
      </div>
    </div>
  </div>
</section>

<section class="szakasz szakasz-vilagos">
  <div class="container">
    <div class="row g-5">
      <div class="col-lg-6">
        <span class="rovat">Interaktív</span>
        <h2>Hogy állsz ma?</h2>
        <p class="text-secondary">
          Pipáld ki, amit ma már megtettél. Nem verseny — csak egy visszajelzés arról,
          hol tartasz. Az eredményt nem mentjük el sehova.
        </p>
        <div class="tipp mt-4">
          <h3>Miért a napi szint?</h3>
          <p class="mb-0">Egy szokás akkor rögzül, ha kicsi és ismételhető. A „hétfőtől
          teljesen új életet kezdek" tervek jellemzően a második héten elhalnak.</p>
        </div>
      </div>
      <div class="col-lg-6">
        <div class="kartya">
          <h3 class="mb-3">Napi ellenőrzőlista</h3>
          <div id="lista">
            <div class="form-check mb-2"><input class="form-check-input" type="checkbox" id="p1"><label class="form-check-label" for="p1">Reggeliztem</label></div>
            <div class="form-check mb-2"><input class="form-check-input" type="checkbox" id="p2"><label class="form-check-label" for="p2">Legalább 5 pohár vizet ittam</label></div>
            <div class="form-check mb-2"><input class="form-check-input" type="checkbox" id="p3"><label class="form-check-label" for="p3">Ettem legalább 2 adag zöldséget vagy gyümölcsöt</label></div>
            <div class="form-check mb-2"><input class="form-check-input" type="checkbox" id="p4"><label class="form-check-label" for="p4">Mozogtam legalább 20 percet</label></div>
            <div class="form-check mb-2"><input class="form-check-input" type="checkbox" id="p5"><label class="form-check-label" for="p5">Nem ittam cukros üdítőt vagy energiaitalt</label></div>
            <div class="form-check mb-2"><input class="form-check-input" type="checkbox" id="p6"><label class="form-check-label" for="p6">Tegnap legalább 7 órát aludtam</label></div>
          </div>
          <hr>
          <div class="progress mb-2" style="height:10px" role="progressbar" aria-label="Teljesített pontok" aria-valuemin="0" aria-valuemax="6">
            <div class="progress-bar" id="sav" style="width:0%;background:#1F7A5C"></div>
          </div>
          <p class="mb-0" id="visszajelzes" aria-live="polite"><strong>0 / 6</strong> — Jelöld be, amit ma már megtettél.</p>
        </div>
      </div>
    </div>
  </div>
</section>
'''

ir("index.html", "Kezdőlap",
   "Iskolai projektweboldal a fiatalok egészséges életmódjáról: táplálkozás, mozgás, alvás "
   f"és egy {N} fős saját kérdőíves felmérés eredményei.", index)


# =======================================================================
# TÁPLÁLKOZÁS
# =======================================================================
taplalkozas = oldalfej(
    "1. téma", "Táplálkozás",
    "A felmérésem szerint a megkérdezettek reggeliznek, vizet isznak és ritkán "
    "rendelnek. Egyetlen dolog marad ki majdnem mindenkinél: a zöldség.") + adatcsik([
        (f"{A['reggeli_rendszeres_sz']}%", "rendszeresen reggelizik iskolanapokon"),
        (f"{A['viz_sok_sz']}%", "iszik naponta legalább 5 pohár vizet"),
        (f"{A['udito_ritkan_sz']}%", "ritkán vagy soha nem iszik cukros üdítőt"),
        (f"{A['zoldseg_sok_fo']} fő", f"eszik napi 4-szer zöldséget vagy gyümölcsöt – a {N}-ből"),
    ]) + f'''
<section class="szakasz szakasz-vilagos">
  <div class="container">
    <div class="row g-5 align-items-center">
      <div class="col-lg-6">
        <span class="rovat">Alapszabály</span>
        <h2>A tányérmodell</h2>
        <p>Nincs szükség kalóriaszámolásra ahhoz, hogy jól egyél. Elég egyetlen kép:
        nézd meg a tányérodat, és kérdezd meg, mennyi rajta a zöldség.</p>
        <ul class="pipa-lista">
          <li><strong>A tányér fele</strong> zöldség és gyümölcs — ez a legfontosabb szabály, a többi ehhez képest részletkérdés.</li>
          <li><strong>A negyede</strong> teljes értékű gabona: barna rizs, teljes kiőrlésű kenyér, zabpehely, tészta.</li>
          <li><strong>A negyede</strong> fehérje: hús, hal, tojás, tejtermék, hüvelyesek.</li>
          <li><strong>Mellé víz</strong>, nem üdítő. Ez az egyetlen csere, ami önmagában is sokat számít.</li>
        </ul>
        <p class="mb-0">Az Egészségügyi Világszervezet ajánlása napi legalább <strong>400 gramm</strong>
        zöldség és gyümölcs, ami körülbelül 5 adagot jelent. A felmérésemben ezt
        {N} emberből mindössze <strong>{A['zoldseg_sok_fo']}</strong> közelítette meg, miközben
        {A['zoldseg_keves_fo']} fő legfeljebb napi egyszer eszik ilyet. Ez a felmérés
        leggyengébb eredménye — és azért különösen érdekes, mert ugyanezek az emberek
        minden más táplálkozási kérdésben jól teljesítenek.</p>
      </div>
      <div class="col-lg-6">
        <img src="kepek/tanyer.svg" alt="Az egészséges tányér modell: a tányér fele zöldség és gyümölcs, negyede teljes értékű gabona, negyede fehérje" class="img-fluid">
        <p class="forrasjel mt-2 mb-0">Saját szerkesztésű ábra (SVG) a WHO és a Harvard T. H. Chan
        School of Public Health tányérmodellje alapján. Gerecze Ádám, 2026.</p>
      </div>
    </div>
  </div>
</section>

<section class="szakasz">
  <div class="container">
    <span class="rovat">Reggeli</span>
    <h2>Ezt már tudjátok — de érdemes tudni, miért</h2>
    <p class="text-secondary" style="max-width:64ch">A felmérésemben
    {A['reggeli_rendszeres_fo']} ember a {A['reggeli_valaszolt']}-ből rendszeresen
    reggelizik, és senki nem jelölte, hogy soha. Ez jobb arány, mint amire számítottam.
    Íme, miért éri meg így maradnia.</p>
    <div class="row g-4 mt-1">
      <div class="col-md-4">
        <div class="kartya">
          <div class="kartya-ikon">🧠</div>
          <h3>Koncentráció</h3>
          <p class="text-secondary mb-0">Az agy szinte kizárólag glükózból dolgozik. Éjszakai
          böjt után az első két-három tanóra érezhetően nehezebb üres gyomorral.</p>
        </div>
      </div>
      <div class="col-md-4">
        <div class="kartya">
          <div class="kartya-ikon">🍫</div>
          <h3>Délutáni túlevés</h3>
          <p class="text-secondary mb-0">A kihagyott reggeli jellemzően nem marad ki: délután
          jön vissza, csak csokiban és chipsben, nem zabkásában.</p>
        </div>
      </div>
      <div class="col-md-4">
        <div class="kartya">
          <div class="kartya-ikon">⏱️</div>
          <h3>„Nincs rá időm"</h3>
          <p class="text-secondary mb-0">Egy joghurt és egy banán 90 másodperc. Nem kell meleg
          reggeli ahhoz, hogy reggelinek számítson.</p>
        </div>
      </div>
    </div>

    <div class="row g-4 mt-3">
      <div class="col-lg-6">
        <div class="tipp">
          <h3>Három reggeli, ami tényleg belefér</h3>
          <ul class="mb-0">
            <li><strong>Zabkása mikróban</strong> – zab + tej + fagyasztott gyümölcs, 2 perc.</li>
            <li><strong>Görög joghurt</strong> + egy marék dió + méz.</li>
            <li><strong>Teljes kiőrlésű szendvics</strong> tojással, este előkészítve.</li>
          </ul>
        </div>
      </div>
      <div class="col-lg-6">
        <div class="figyelem">
          <h3>Amiről kevesebb szó esik: a folyékony cukor</h3>
          <p class="mb-0">Egy fél literes cukros üdítőben nagyjából <strong>13 kockacukornyi</strong>
          cukor van. Ez ugyanannyi kalória, mint egy tízórai — csak nem laktat, és
          20 perc múlva már éhes leszel tőle. A felmérésemben a többség
          ({A['udito_ritkan_fo']} fő) ritkán vagy soha nem iszik ilyet, de
          {A['udito_naponta_fo']} ember <em>naponta</em> — ők egy kicsi, de jól
          elkülönülő csoport.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="szakasz szakasz-vilagos">
  <div class="container">
    <span class="rovat">Cserék</span>
    <h2>Nem lemondás — csere</h2>
    <p class="text-secondary" style="max-width:62ch">A „soha többé nem eszem X-et" típusú
    fogadalmak nem tartanak sokáig. Ami működik, az a csere: ugyanaz a helyzet,
    ugyanaz a szokás, kicsit jobb választás.</p>
    <div class="tabla mt-4">
      <table class="table mb-0">
        <thead><tr><th>Helyzet</th><th>Szokásos választás</th><th>Csere</th><th>Miért jobb?</th></tr></thead>
        <tbody>
          <tr><td>Büfé szünetben</td><td>Cukros üdítő</td><td>Ásványvíz vagy cukrozatlan tea</td><td>Kb. 150–200 kcal folyékony cukor kiesik</td></tr>
          <tr><td>Tízórai</td><td>Csokis péksütemény</td><td>Banán + egy marék dió</td><td>Rost és fehérje, tovább laktat</td></tr>
          <tr><td>Este a gép előtt</td><td>Chips a zacskóból</td><td>Chips kis tálkába szedve</td><td>Nem a zacskó mérete szabja meg az adagot</td></tr>
          <tr><td>Ebéd a menzán</td><td>Csak a második fogás</td><td>Elsőként a savanyúság vagy saláta</td><td>Egy adag zöldség szinte ingyen</td></tr>
          <tr><td>Rendelés</td><td>Heti több alkalommal</td><td>Heti egyszer, tudatosan</td><td>Élmény marad, nem alap lesz</td></tr>
        </tbody>
      </table>
    </div>
    <p class="forrasjel mt-3">A táblázat saját összeállítás a forrásjegyzékben szereplő szakmai anyagok alapján.</p>
  </div>
</section>
'''

ir("taplalkozas.html", "Táplálkozás",
   "A tányérmodell, a reggeli szerepe és a cukros üdítők – gyakorlati tanácsok fiataloknak.",
   taplalkozas)


# =======================================================================
# MOZGÁS
# =======================================================================
mozgas = oldalfej(
    "2. téma", "Mozgás",
    "Ez a felmérésem legerősebb területe. A megkérdezettek túlnyomó többsége "
    "rendszeresen mozog — de mint kiderült, ez önmagában nem véd meg mindentől.") + adatcsik([
        (f"{A['sport_gyakori_sz']}%", "mozog legalább heti három alkalommal"),
        (f"{A['sport_naponta_fo']} fő", "szinte naponta sportol a tesiórán kívül"),
        (f"{A['sport_soha_fo']} fő", "az, aki szinte soha nem mozog"),
        (f"{A['mozgas_elso_fo']} fő", f"választotta a leggyakoribb mozgásformát: {A['mozgas_elso'].lower()}"),
    ]) + f'''
<section class="szakasz szakasz-vilagos">
  <div class="container">
    <div class="row g-5 align-items-center">
      <div class="col-lg-6">
        <img src="kepek/mozgas-piramis.svg" alt="Mozgáspiramis: az alapot a mindennapi hétköznapi mozgás adja, felette az edzés, a nyújtás, a csúcson a hosszú ülés" class="img-fluid">
        <p class="forrasjel mt-2 mb-0">Saját szerkesztésű ábra (SVG) a WHO fizikai aktivitási
        ajánlása alapján. Gerecze Ádám, 2026.</p>
      </div>
      <div class="col-lg-6">
        <span class="rovat">Mennyi az elég?</span>
        <h2>Napi 60 perc — de nem egyben</h2>
        <p>A WHO ajánlása 5–17 éves korosztályra napi átlagosan <strong>60 perc</strong>
        közepes vagy erős intenzitású mozgás. Ez elsőre soknak hangzik, de nem
        edzésről van szó: ide számít a gyaloglás, a lépcsőzés, a biciklizés és a
        tesióra is.</p>
        <ul class="pipa-lista">
          <li><strong>Nem kell egyben letudni.</strong> Három darab 20 perc ugyanannyit ér, mint egy 60 perces blokk.</li>
          <li><strong>Nem kell eszköz.</strong> A felmérésemben a legnépszerűbb mozgásforma a {A['mozgas_elso'].lower()} volt ({A['mozgas_elso_fo']} fő), és a többség több mozgásformát is megjelölt.</li>
          <li><strong>Nem kell tehetség.</strong> A cél nem a versenysport, hanem az, hogy a tested naponta használva legyen.</li>
          <li><strong>Heti kétszer</strong> érdemes valamilyen erősítő jellegű mozgást is beiktatni.</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="szakasz">
  <div class="container">
    <span class="rovat">Miért éri meg?</span>
    <h2>Amit a mozgás valójában csinál</h2>
    <div class="row g-4 mt-1">
      <div class="col-md-6 col-lg-3">
        <div class="kartya">
          <div class="kartya-ikon">😴</div>
          <h3>Jobb alvás</h3>
          <p class="text-secondary mb-0">A nappali mozgás mélyebbé teszi az alvást — és a mélyalvás az, ami valóban regenerál.</p>
        </div>
      </div>
      <div class="col-md-6 col-lg-3">
        <div class="kartya">
          <div class="kartya-ikon">🙂</div>
          <h3>Hangulat</h3>
          <p class="text-secondary mb-0">A rendszeres mozgás bizonyítottan csökkenti a szorongás és a depresszió tüneteit.</p>
        </div>
      </div>
      <div class="col-md-6 col-lg-3">
        <div class="kartya">
          <div class="kartya-ikon">📚</div>
          <h3>Tanulás</h3>
          <p class="text-secondary mb-0">Mozgás után javul a figyelem és a memória — ezért jó ötlet séta után nekiülni tanulni.</p>
        </div>
      </div>
      <div class="col-md-6 col-lg-3">
        <div class="kartya">
          <div class="kartya-ikon">🦴</div>
          <h3>Csontok</h3>
          <p class="text-secondary mb-0">A csonttömeg nagy része serdülőkorban épül fel. Amit most kihagysz, azt később nehéz pótolni.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="szakasz szakasz-vilagos">
  <div class="container">
    <span class="rovat">Kezdés</span>
    <h2>Négyhetes belépő terv</h2>
    <p class="text-secondary" style="max-width:62ch">Ez a terv nulláról indul. Nem edzésterv,
    hanem szokásépítés: a lényeg nem a terhelés, hanem hogy a negyedik hét végén
    még mindig csinálod.</p>
    <div class="tabla mt-4">
      <table class="table mb-0">
        <thead><tr><th style="width:14%">Hét</th><th>Cél</th><th>Konkrétan</th></tr></thead>
        <tbody>
          <tr><td><strong>1.</strong></td><td>Elindulni</td><td>Heti 2× 20 perc séta. Bármikor, bárhol. Ennyi.</td></tr>
          <tr><td><strong>2.</strong></td><td>Ritmust adni</td><td>Heti 3× 25 perc séta vagy kerékpár, fix napokon.</td></tr>
          <tr><td><strong>3.</strong></td><td>Intenzitást hozni</td><td>Heti 3× 30 perc, ebből egyszer gyorsabb tempó vagy kocogás.</td></tr>
          <tr><td><strong>4.</strong></td><td>Erőt beépíteni</td><td>Heti 3× 30 perc mozgás + 2× 15 perc saját testsúlyos gyakorlat.</td></tr>
        </tbody>
      </table>
    </div>
    <div class="row g-4 mt-3">
      <div class="col-lg-6">
        <div class="tipp">
          <h3>Ami segít, hogy ne álljon le</h3>
          <ul class="mb-0">
            <li>Írd be a naptárba, mint egy órát — ne „ha lesz időm" alapon.</li>
            <li>Hívj valakit magaddal. Egyedül könnyebb kihagyni.</li>
            <li>Egy kihagyott nap nem bukás. Két kihagyott hét már az.</li>
          </ul>
        </div>
      </div>
      <div class="col-lg-6">
        <div class="figyelem">
          <h3>Mielőtt belevágsz</h3>
          <p class="mb-0">Ha bármilyen krónikus betegséged van, korábbi sérülésed, vagy
          mozgás közben mellkasi fájdalmat, szédülést tapasztalsz, előbb beszélj
          háziorvossal vagy iskolaorvossal. Ez az oldal nem orvosi tanács.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="szakasz">
  <div class="container">
    <div class="row g-5 align-items-center">
      <div class="col-lg-7">
        <span class="rovat">Amit az adatok mutattak</span>
        <h2>A mozgás nem véd meg mindentől</h2>
        <p>Ez a felmérés egyik legérdekesebb tanulsága. A megkérdezettek
        {A['sport_gyakori_sz']}%-a mozog legalább heti háromszor — mégis
        {A['faradt_rendszeres_fo']} ember ({A['faradt_rendszeres_sz']}%) érzi magát
        legalább hetente többször fáradtnak napközben.</p>
        <p class="mb-0">Vagyis a rendszeres sportolás önmagában nem kompenzálja a
        kevés alvást vagy a sok képernyőidőt. A három terület külön-külön is számít.
        Erről szól az <a href="alvas.html">alvás és képernyőidő</a> oldal.</p>
      </div>
      <div class="col-lg-5">
        <div class="tipp">
          <h3>Egy összefüggést nem tudtam megvizsgálni</h3>
          <p class="mb-0">Eredetileg azt terveztem, hogy összevetem a sportolás
          gyakoriságát az egészség-önértékeléssel. Ez nem volt lehetséges: a
          válaszadók közül {A['sport_naponta_fo']}-en egyetlen kategóriába estek, a
          többi csoportban 1–2 ember van. Ekkora alcsoportokból nem lehet átlagot
          értelmezni, ezért ezt az összehasonlítást nem is közlöm.</p>
        </div>
      </div>
    </div>
  </div>
</section>
'''

ir("mozgas.html", "Mozgás",
   "Mennyi mozgás elég valójában, mit ad a testnek, és egy négyhetes belépő terv nulláról.",
   mozgas)


# =======================================================================
# ALVÁS ÉS KÉPERNYŐ
# =======================================================================
kf = A["kepernyo_faradtsag"]
kf_sorok = ""
for cimke, e in kf.items():
    ossz, far = e["osszes"], e["faradt"]
    arany = f"{round(far / ossz * 100)}%" if ossz else "–"
    kf_sorok += f"              <tr><td>{cimke}</td><td>{ossz}</td><td>{far} ({arany})</td></tr>\n"

alvas = oldalfej(
    "3. téma", "Alvás és képernyőidő",
    "Itt van a második vakfolt — és a felmérésem legmarkánsabb összefüggése: "
    "a képernyőidő és a rendszeres nappali fáradtság kapcsolata.") + adatcsik([
        (f"{A['alvas_keves_sz']}%", "7 óránál kevesebbet alszik iskolanapokon"),
        (f"{A['alvas_ajanlott_fo']} fő", f"éri el az ajánlott 8 órát – a {N}-ből"),
        (f"{A['kepernyo_sok_sz']}%", "tölt naponta több mint 4 órát képernyő előtt"),
        (f"{A['faradt_rendszeres_sz']}%", "érzi magát legalább hetente többször fáradtnak"),
    ]) + f'''
<section class="szakasz szakasz-vilagos">
  <div class="container">
    <div class="row g-5 align-items-center">
      <div class="col-lg-6">
        <span class="rovat">Alapok</span>
        <h2>Az alvás nem kikapcsolás</h2>
        <p>Alvás közben az agy nem pihen, hanem dolgozik: rendszerezi a nap során
        tanultakat, kitakarítja az anyagcsere-melléktermékeket, és növekedési
        hormont termel. Ez nem opcionális háttérfolyamat — ez a regeneráció maga.</p>
        <p>Az éjszaka <strong>90 perces ciklusokból</strong> áll, és a mély alvás nagy része
        az éjszaka <em>első</em> felére esik. Ezért nem lehet a hét közben kialvatlanul
        töltött éjszakákat hétvégi délig alvással bepótolni: a hiányzó mélyalvás
        egyszerűen nem jön vissza.</p>
        <p class="mb-0">A 14–19 éves korosztály számára ajánlott alvásmennyiség
        <strong>8–10 óra</strong>. A felmérésemben ezt {N} emberből
        <strong>{A['alvas_ajanlott_fo']}</strong> érte el, és
        {A['alvas_keves_fo']} fő ({A['alvas_keves_sz']}%) 7 óránál is kevesebbet alszik.
        Ez a második terület — a zöldségfogyasztás mellett —, ahol ez az egyébként
        aktív minta egyértelműen elmarad az ajánlástól.</p>
      </div>
      <div class="col-lg-6">
        <img src="kepek/alvasciklus.svg" alt="Egy éjszaka alvásszerkezete: négy körülbelül 90 perces ciklus, a mély alvás az éjszaka első felében sűrűbb" class="img-fluid">
        <p class="forrasjel mt-2 mb-0">Saját szerkesztésű ábra (SVG) alvásélettani szakirodalom
        alapján. Gerecze Ádám, 2026.</p>
      </div>
    </div>
  </div>
</section>

<section class="szakasz">
  <div class="container">
    <span class="rovat">A felmérés fő eredménye</span>
    <h2>Képernyőidő és rendszeres fáradtság</h2>
    <div class="row g-5 align-items-center mt-1">
      <div class="col-lg-7">
        <figure class="diagram">
          <img src="kepek/diagramok/17_kepernyo_faradtsag.png" alt="Oszlopdiagram a napi képernyőidő és a rendszeres nappali fáradtság kapcsolatáról">
          <figcaption>Saját felmérés, n={N}, 2026. augusztus. Készült Python (matplotlib) segítségével.</figcaption>
        </figure>
      </div>
      <div class="col-lg-5">
        <div class="tabla">
          <table class="table mb-0">
            <thead><tr><th>Napi képernyőidő</th><th>Fő</th><th>Rendszeresen fáradt</th></tr></thead>
            <tbody>
{kf_sorok}            </tbody>
          </table>
        </div>
        <p class="text-secondary mt-3 mb-0">Két csoportra összevonva: a napi 4 óránál
        kevesebbet képernyőzők közül <strong>{A['kep_also_faradt_sz']}%</strong>
        ({A['kep_also_faradt_fo']} / {A['kep_also_fo']} fő), a 4 óránál többet
        képernyőzők közül <strong>{A['kep_felso_faradt_sz']}%</strong>
        ({A['kep_felso_faradt_fo']} / {A['kep_felso_fo']} fő) fáradt rendszeresen.</p>
        <div class="figyelem mt-4">
          <h3>Amit ebből nem szabad kiolvasni</h3>
          <p class="mb-0">Ez <strong>együttjárás, nem bizonyított ok-okozat</strong>. Lehet, hogy
          a képernyőzés fáraszt el; de az is lehet, hogy a fáradt ember választja a
          passzív képernyőzést. {N} fős, nem reprezentatív mintán ennél erősebb
          állítást nem tehetek — a két szélső kategóriában ráadásul mindössze 1, illetve
          2 válaszadó van.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="szakasz szakasz-vilagos">
  <div class="container">
    <span class="rovat">Amivel nem lett baj</span>
    <h2>Az energiaital ördögi köre — itt éppen nem működik</h2>
    <p class="text-secondary" style="max-width:64ch">A fáradtságra adott szokásos válasz
    az energiaital lenne, aminek a koffeinje 5–6 óráig hat: a délután 4-kor megivott
    doboz este 10-kor még mindig aktív, tehát maga termeli újra a fáradtságot.
    A felmérésemben viszont <strong>{A['energiaital_soha_fo']} ember
    ({A['energiaital_soha_sz']}%) soha nem iszik energiaitalt</strong>, és napi fogyasztó
    egyáltalán nincs a mintában. Ez lényegesen jobb kép, mint amire a téma
    médiavisszhangja alapján számítottam. A fáradtság oka tehát máshol keresendő —
    valószínűleg az alvásban és a képernyőidőben.</p>
    <div class="row g-4 mt-2">
      <div class="col-md-4">
        <div class="kartya">
          <div class="kartya-ikon">📱</div>
          <h3>30 perc telefonmentes</h3>
          <p class="text-secondary mb-0">Lefekvés előtt fél órával tedd le. A kék fény
          hatásánál is fontosabb, hogy a tartalom felpörget — a végtelen görgetés
          nem hagyja lenyugodni az agyat.</p>
        </div>
      </div>
      <div class="col-md-4">
        <div class="kartya">
          <div class="kartya-ikon">⏰</div>
          <h3>Fix ébredés</h3>
          <p class="text-secondary mb-0">A szervezet a felkelési időhöz igazodik, nem a
          lefekvéshez. Ha hétvégén is nagyjából ugyanakkor kelsz, hétfőn nem kell
          újratanulnia a ritmust.</p>
        </div>
      </div>
      <div class="col-md-4">
        <div class="kartya">
          <div class="kartya-ikon">☕</div>
          <h3>Koffeinstop délután</h3>
          <p class="text-secondary mb-0">Délután 4 után se kávé, se energiaital, se
          erős tea. Ez az egyetlen szabály sokaknál látványosan javítja az
          elalvást.</p>
        </div>
      </div>
    </div>
    <div class="tipp mt-4">
      <h3>Ha nem megy az elalvás</h3>
      <ul class="mb-0">
        <li>Sötét, hűvös szoba — 18–20 °C körül a legjobb.</li>
        <li>Ne az ágyban tanulj vagy nézz sorozatot: az agy társítsa az ágyat az alvással.</li>
        <li>Ha 20 perc után sem alszol el, kelj fel, csinálj valami unalmasat, aztán feküdj vissza.</li>
        <li>Ha hetekig tartósan nem tudsz aludni, az már nem szokás kérdése — beszélj orvossal.</li>
      </ul>
    </div>
  </div>
</section>
'''

ir("alvas.html", "Alvás és képernyőidő",
   f"Alvásciklusok, képernyőidő és fáradtság összefüggése egy {N} fős saját felmérés alapján.",
   alvas)


# =======================================================================
# KUTATÁS
# =======================================================================
kutatas = oldalfej(
    "A projekt kutatási része", "A kérdőíves felmérésünk",
    f"16 kérdés, {N} kitöltő, 18 diagram. Itt látható a teljes eredmény — beleértve "
    "azt is, amit a felmérés <em>nem</em> tud bizonyítani.") + f'''
<section class="szakasz szakasz-vilagos">
  <div class="container">
    <div class="row g-5">
      <div class="col-lg-7">
        <span class="rovat">Módszertan</span>
        <h2>Hogyan készült?</h2>
        <p>A kérdőívet Google Űrlapok segítségével állítottam össze, és online linken
        keresztül osztottam meg osztálytársaimmal és ismerőseimmel. A kitöltés
        anonim és önkéntes volt, körülbelül három percet vett igénybe. A nyers
        válaszokat CSV-be exportáltam, majd Python nyelven (pandas és matplotlib
        könyvtárak) dolgoztam fel és ábrázoltam.</p>
        <div class="figyelem">
          <h3>A minta korlátai — ezt fontos elöljáróban tisztázni</h3>
          <p class="mb-0">A felmérés <strong>nem reprezentatív</strong>. Kényelmi mintavétellel
          készült: a válaszadók a saját iskolai és ismeretségi körömből származnak,
          összesen {N}-en. Ez itt különösen fontos, mert a minta feltűnően sportos
          ({A['sport_gyakori_fo']} fő mozog legalább heti háromszor) — ami
          valószínűleg nem a korosztályra, hanem az én környezetemre jellemző.
          Az eredmények tehát <strong>erről a {N} emberről</strong> szólnak.</p>
        </div>
      </div>
      <div class="col-lg-5">
        <div class="kartya">
          <h3 class="mb-3">A felmérés adatlapja</h3>
          <table class="table table-borderless mb-0">
            <tbody>
              <tr><td class="ps-0"><strong>Kérdések száma</strong></td><td class="text-end pe-0">16</td></tr>
              <tr><td class="ps-0"><strong>Kitöltők</strong></td><td class="text-end pe-0">{N} fő</td></tr>
              <tr><td class="ps-0"><strong>Életkor</strong></td><td class="text-end pe-0">14–19 év</td></tr>
              <tr><td class="ps-0"><strong>Eszköz</strong></td><td class="text-end pe-0">Google Űrlapok</td></tr>
              <tr><td class="ps-0"><strong>Feldolgozás</strong></td><td class="text-end pe-0">Python, pandas</td></tr>
              <tr><td class="ps-0"><strong>Diagramok</strong></td><td class="text-end pe-0">18</td></tr>
              <tr><td class="ps-0"><strong>Mintavétel</strong></td><td class="text-end pe-0">kényelmi</td></tr>
              <tr><td class="ps-0"><strong>Anonimitás</strong></td><td class="text-end pe-0">teljes</td></tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="szakasz">
  <div class="container">
    <span class="rovat">Eredmények · 1</span>
    <h2>Kik töltötték ki?</h2>
    <div class="row g-4 mt-1">
''' + diagram("01_nemek.png", "Fánkdiagram a kitöltők nemek szerinti megoszlásáról",
              f"1. ábra – Nemek szerinti megoszlás. Saját felmérés, n={N}.") + \
    diagram("02_eletkor.png", "Oszlopdiagram az életkori megoszlásról",
            f"2. ábra – Életkori megoszlás. Saját felmérés, n={N}.") + f'''    </div>

    <div class="mt-5"></div>
    <span class="rovat">Eredmények · 2</span>
    <h2>Táplálkozás</h2>
    <p class="text-secondary" style="max-width:64ch">Ezen a területen a minta jól
    teljesít — egyetlen kivétellel, a zöldség- és gyümölcsfogyasztással.</p>
    <div class="row g-4 mt-1">
''' + diagram("03_reggeli.png", "Fánkdiagram a reggelizési szokásokról",
              f"3. ábra – Reggelizés iskolanapokon. Saját felmérés, {A['reggeli_valaszolt']} válasz.") + \
    diagram("04_zoldseg_gyumolcs.png", "Oszlopdiagram a napi zöldség- és gyümölcsfogyasztásról",
            f"4. ábra – Napi zöldség- és gyümölcsfogyasztás. Saját felmérés, n={N}.") + \
    diagram("05_cukros_udito.png", "Oszlopdiagram a cukros üdítő fogyasztásáról",
            f"5. ábra – Cukros üdítő fogyasztása. Saját felmérés, n={N}.") + \
    diagram("06_vizfogyasztas.png", "Oszlopdiagram a napi vízfogyasztásról",
            f"6. ábra – Napi vízfogyasztás. Saját felmérés, n={N}.") + \
    diagram("07_gyorsetterem.png", "Oszlopdiagram a gyorséttermi étkezés gyakoriságáról",
            f"7. ábra – Gyorséttermi vagy rendelt étel fogyasztása. Saját felmérés, n={N}.") + f'''    </div>

    <div class="mt-5"></div>
    <span class="rovat">Eredmények · 3</span>
    <h2>Mozgás</h2>
    <p class="text-secondary" style="max-width:64ch">A minta legerősebb területe:
    {A['sport_gyakori_fo']} fő mozog legalább heti három alkalommal.</p>
    <div class="row g-4 mt-1">
''' + diagram("08_sport_gyakorisag.png", "Oszlopdiagram a sportolás gyakoriságáról",
              f"8. ábra – Testmozgás gyakorisága a tesiórán kívül. Saját felmérés, n={N}.") + \
    diagram("09_mozgasformak.png", "Vízszintes oszlopdiagram a választott mozgásformákról",
            f"9. ábra – Választott mozgásformák (többválaszos). Saját felmérés, n={N}.") + f'''    </div>

    <div class="mt-5"></div>
    <span class="rovat">Eredmények · 4</span>
    <h2>Alvás, képernyő, közérzet</h2>
    <p class="text-secondary" style="max-width:64ch">Itt található a második vakfolt:
    {A['alvas_keves_fo']} fő 7 óránál kevesebbet alszik, és
    {A['faradt_rendszeres_fo']} fő rendszeresen fáradt.</p>
    <div class="row g-4 mt-1">
''' + diagram("10_alvas.png", "Fánkdiagram az alvásidőről",
              f"10. ábra – Alvásidő iskolai éjszakán. Saját felmérés, n={N}.") + \
    diagram("11_kepernyoido.png", "Oszlopdiagram a napi képernyőidőről",
            f"11. ábra – Napi szabadidős képernyőidő. Saját felmérés, n={N}.") + \
    diagram("12_faradtsag.png", "Oszlopdiagram a nappali fáradtság gyakoriságáról",
            f"12. ábra – Nappali fáradtság gyakorisága. Saját felmérés, n={N}.") + \
    diagram("13_energiaital.png", "Fánkdiagram az energiaital-fogyasztásról",
            f"13. ábra – Energiaital-fogyasztás. Saját felmérés, n={N}.") + f'''    </div>

    <div class="mt-5"></div>
    <span class="rovat">Eredmények · 5</span>
    <h2>Attitűd és tájékozódás</h2>
    <div class="row g-4 mt-1">
''' + diagram("14_onertekeles.png", "Oszlopdiagram az egészség-önértékelésről",
              f"14. ábra – Egészség-önértékelés 1–5 skálán, átlag: {A['onertekeles_atlag']}. Saját felmérés, n={N}.") + \
    diagram("15_informacioforras.png", "Vízszintes oszlopdiagram a tájékozódási forrásokról",
            f"15. ábra – Információforrások (többválaszos). Saját felmérés, n={N}.") + \
    diagram("16_valtoztatas.png", "Fánkdiagram a változtatási szándékról",
            f"16. ábra – Szeretnél változtatni az életmódodon? Saját felmérés, n={N}.") + f'''    </div>

    <div class="mt-5"></div>
    <span class="rovat">Eredmények · 6</span>
    <h2>Összefüggések</h2>
    <p class="text-secondary" style="max-width:64ch">Két kereszttáblát készítettem.
    Mindkettőnél fontos, hogy <strong>együttjárásról</strong> van szó: a felmérés
    keresztmetszeti, tehát az ok-okozati irányt nem tudja megállapítani.</p>
    <div class="row g-4 mt-1">
''' + diagram("17_kepernyo_faradtsag.png", "Oszlopdiagram a képernyőidő és a rendszeres fáradtság kapcsolatáról",
              f"17. ábra – Képernyőidő és rendszeres nappali fáradtság. Saját felmérés, n={N}.") + \
    diagram("18_alvas_onertekeles.png", "Oszlopdiagram az alvásmennyiség és az önértékelés kapcsolatáról",
            "18. ábra – Alvásmennyiség és egészség-önértékelés. Az alcsoportok kis elemszámúak, ezért csak tendenciaként értelmezhető.") + f'''    </div>
  </div>
</section>

<section class="szakasz szakasz-vilagos">
  <div class="container">
    <span class="rovat">Összegzés</span>
    <h2>Hat következtetés</h2>
    <div class="row g-4 mt-1">
      <div class="col-md-6 col-lg-4">
        <div class="kartya"><h3>1. Jobb a vártnál</h3>
        <p class="text-secondary mb-0">{A['sport_gyakori_sz']}% mozog rendszeresen,
        {A['viz_sok_sz']}% iszik elég vizet, az önértékelés átlaga
        {A['onertekeles_atlag']}. A kiinduló feltételezésem nem igazolódott.</p></div>
      </div>
      <div class="col-md-6 col-lg-4">
        <div class="kartya"><h3>2. Zöldség: vakfolt</h3>
        <p class="text-secondary mb-0">{N} emberből {A['zoldseg_sok_fo']} közelíti meg
        az ajánlott mennyiséget, miközben minden más táplálkozási kérdésben jól
        teljesítenek.</p></div>
      </div>
      <div class="col-md-6 col-lg-4">
        <div class="kartya"><h3>3. Alvás: vakfolt</h3>
        <p class="text-secondary mb-0">A minta {A['alvas_keves_sz']}%-a 7 óránál
        kevesebbet alszik. A jó szokások ezt nem kompenzálják.</p></div>
      </div>
      <div class="col-md-6 col-lg-4">
        <div class="kartya"><h3>4. Képernyő és fáradtság</h3>
        <p class="text-secondary mb-0">4 óra alatt {A['kep_also_faradt_sz']}%,
        4 óra felett {A['kep_felso_faradt_sz']}% a rendszeresen fáradtak aránya.
        A felmérés legmarkánsabb eredménye.</p></div>
      </div>
      <div class="col-md-6 col-lg-4">
        <div class="kartya"><h3>5. Kiegyensúlyozott tájékozódás</h3>
        <p class="text-secondary mb-0">A közösségi média vezet
        ({A['info_elso_fo']} fő), de orvostól is {A['info_orvos_fo']} ember
        tájékozódik, és senki nem jelölte, hogy sehonnan.</p></div>
      </div>
      <div class="col-md-6 col-lg-4">
        <div class="kartya"><h3>6. Kétféle üzenet kell</h3>
        <p class="text-secondary mb-0">{A['valtoztat_fo']} fő változtatna,
        {A['valtoztat_elegedett_fo']} viszont elégedett. Utóbbiaknak nem tanács kell,
        hanem a két vakfolt megmutatása.</p></div>
      </div>
    </div>
  </div>
</section>
'''

ir("kutatas.html", "Kutatásunk",
   f"Egy {N} fős, 16 kérdéses kérdőíves felmérés teljes eredménye 18 diagrammal.",
   kutatas)


# =======================================================================
# FORRÁSOK
# =======================================================================
forrasok = oldalfej(
    "A projektről", "Források és készítők",
    "Minden állítás mögött van forrás, minden ábra mögött van készítő. "
    "Itt található mindkettő.") + f'''
<section class="szakasz szakasz-vilagos">
  <div class="container">
    <div class="row g-5">
      <div class="col-lg-7">
        <span class="rovat">Felhasznált szakirodalom</span>
        <h2>Források</h2>
        <p class="text-secondary">Az oldalon szereplő szakmai állítások az alábbi
        forrásokon alapulnak. Törekedtem arra, hogy elsődleges, intézményi forrásokat
        használjak másodközlő cikkek helyett.</p>

        <ol class="mt-4">
          <li class="mb-3"><strong>World Health Organization (WHO):</strong>
            <em>Healthy diet</em> – tájékoztató adatlap. Elérhető:
            <a href="https://www.who.int/news-room/fact-sheets/detail/healthy-diet" target="_blank" rel="noopener">who.int</a>.
            <br><span class="forrasjel">Felhasználva: a napi 400 g zöldség-gyümölcs ajánlás, a cukorbevitelre vonatkozó adatok.</span></li>

          <li class="mb-3"><strong>World Health Organization (WHO):</strong>
            <em>Physical activity</em> – tájékoztató adatlap és a fizikai aktivitásra
            vonatkozó globális ajánlások. Elérhető:
            <a href="https://www.who.int/news-room/fact-sheets/detail/physical-activity" target="_blank" rel="noopener">who.int</a>.
            <br><span class="forrasjel">Felhasználva: a 5–17 évesekre vonatkozó napi 60 perces ajánlás, a mozgáspiramis felépítése.</span></li>

          <li class="mb-3"><strong>Harvard T. H. Chan School of Public Health:</strong>
            <em>The Nutrition Source – Healthy Eating Plate</em>. Elérhető:
            <a href="https://nutritionsource.hsph.harvard.edu/healthy-eating-plate/" target="_blank" rel="noopener">nutritionsource.hsph.harvard.edu</a>.
            <br><span class="forrasjel">Felhasználva: a tányérmodell arányai és logikája.</span></li>

          <li class="mb-3"><strong>Nemzeti Népegészségügyi és Gyógyszerészeti Központ (NNGYK):</strong>
            táplálkozási és egészségfejlesztési ajánlások, magyar népegészségügyi adatok.
            Elérhető: <a href="https://www.nnk.gov.hu/" target="_blank" rel="noopener">nnk.gov.hu</a>.
            <br><span class="forrasjel">Felhasználva: hazai kontextus, magyar fiatalok táplálkozási helyzete.</span></li>

          <li class="mb-3"><strong>Sleep Foundation:</strong>
            <em>Teens and Sleep</em> – korosztályi alvásajánlások és alvásélettani összefoglaló.
            Elérhető: <a href="https://www.sleepfoundation.org/teens-and-sleep" target="_blank" rel="noopener">sleepfoundation.org</a>.
            <br><span class="forrasjel">Felhasználva: a 8–10 órás ajánlás, az alvásciklusok szerkezete, a képernyőhasználat és az elalvás kapcsolata.</span></li>

          <li class="mb-3"><strong>European Food Safety Authority (EFSA):</strong>
            <em>Scientific Opinion on the safety of caffeine</em>. Elérhető:
            <a href="https://www.efsa.europa.eu/en/efsajournal/pub/4102" target="_blank" rel="noopener">efsa.europa.eu</a>.
            <br><span class="forrasjel">Felhasználva: a koffein felezési ideje, a serdülőkori energiaital-fogyasztás kockázatai.</span></li>

          <li class="mb-0"><strong>Saját kérdőíves felmérés:</strong>
            Gerecze Ádám (2026): <em>Egészséges életmód a középiskolások körében</em>.
            Online kérdőív, Google Űrlapok, n={N}.
            <br><span class="forrasjel">A weboldalon szereplő összes százalékos és átlagadat ebből a felmérésből származik.</span></li>
        </ol>
      </div>

      <div class="col-lg-5">
        <div class="kartya mb-4">
          <span class="rovat">Készítő</span>
          <h3>Gerecze Ádám</h3>
          <p class="text-secondary">1/13. Sz. évfolyam · IKT Projektmunka I.</p>
          <p class="text-secondary mb-0">A projektet önállóan készítettem, mivel a
          csoportbeosztás során nem alakult ki több fős csapat. Így a projekttervezés,
          az információgyűjtés, a kérdőív összeállítása és elemzése, a weboldal
          fejlesztése, a prezentáció és a dokumentáció is a saját munkám.</p>
        </div>

        <div class="tipp mb-4">
          <h3>Képek és ábrák forrása</h3>
          <p class="mb-2">Az oldalon szereplő <strong>összes illusztráció saját
          szerkesztés</strong>, külső képet nem használtam fel:</p>
          <ul class="mb-0">
            <li>A vektoros ábrák (SVG) kézzel készültek.</li>
            <li>A diagramok a saját kérdőívem adataiból, Python matplotlib könyvtárral készültek.</li>
            <li>A tányérmodell és a mozgáspiramis a fenti 2. és 3. forrás tartalmi ajánlásait követi, de a grafika saját munka.</li>
          </ul>
        </div>

        <div class="kartya">
          <span class="rovat">Használt eszközök</span>
          <h3>Technológia</h3>
          <ul class="mb-0 text-secondary">
            <li>HTML5, CSS3, JavaScript</li>
            <li>Bootstrap 5.3 (keretrendszer)</li>
            <li>Google Fonts – Outfit, Karla</li>
            <li>Google Űrlapok (kérdőív)</li>
            <li>Python 3 – pandas, matplotlib</li>
            <li>Microsoft PowerPoint (prezentáció)</li>
            <li>Git és GitHub (verziókezelés)</li>
            <li>Visual Studio Code (fejlesztés)</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="szakasz">
  <div class="container">
    <span class="rovat">Jogi és etikai megjegyzés</span>
    <h2>Amit fontos tudni erről az oldalról</h2>
    <div class="row g-4 mt-1">
      <div class="col-md-4">
        <div class="figyelem h-100">
          <h3>Nem orvosi tanács</h3>
          <p class="mb-0">Az oldal iskolai projekt keretében, tájékoztató céllal készült.
          Nem helyettesíti a szakorvosi véleményt. Panasz esetén fordulj
          háziorvoshoz vagy iskolaorvoshoz.</p>
        </div>
      </div>
      <div class="col-md-4">
        <div class="tipp h-100">
          <h3>Adatkezelés</h3>
          <p class="mb-0">A kérdőív anonim volt, személyazonosításra alkalmas adatot nem
          gyűjtöttem. A válaszokat kizárólag összesítve, iskolai projekt keretében
          használtam fel.</p>
        </div>
      </div>
      <div class="col-md-4">
        <div class="tipp h-100">
          <h3>Forráskritika</h3>
          <p class="mb-0">A felmérésem szerint a fiatalok többsége közösségi médiából
          tájékozódik. Bármilyen egészségügyi tippnél érdemes megnézni: ki mondja,
          mire hivatkozik, és mit akar eladni.</p>
        </div>
      </div>
    </div>
  </div>
</section>
'''

ir("forrasok.html", "Források és készítők",
   "A projekt forrásjegyzéke, a képek forrásmegjelölése, a felhasznált eszközök listája.",
   forrasok)


# --- diagramok másolása a weboldalra ---
os.makedirs(DIAGRAM_CEL, exist_ok=True)
for f in os.listdir(DIAGRAM_CEL):
    os.remove(os.path.join(DIAGRAM_CEL, f))
db = 0
for f in sorted(os.listdir(DIAGRAM_FORRAS)):
    if f.endswith(".png"):
        shutil.copy2(os.path.join(DIAGRAM_FORRAS, f), os.path.join(DIAGRAM_CEL, f))
        db += 1
print(f"  ✔ {db} diagram másolva a weboldalra")
print("\nA weboldal elkészült.")
