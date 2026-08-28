# Egészséges életmód

**IKT Projektmunka I. – osztályozó vizsga házi dolgozat**
1/13. Sz. évfolyam · 2026. augusztus

> *„Jól élnek. Két dolog mégis kimarad."*

---

## A projekt rövid bemutatása

A projekt kiinduló kérdése az volt, hogy **mennyire élnek egészségesen a körülöttem
lévő fiatalok, és hol maradnak el az ajánlásoktól?**

Ezt nem lehet internetes cikkek olvasásával eldönteni, ezért saját, 16 kérdésből álló
online kérdőívet készítettem a 14–19 éves korosztálynak. **22 fő töltötte ki**, a
válaszokat pedig Python szkripttel dolgoztam fel. Az eredmények alapján épült fel a
projektweboldal és a prezentáció.

A felmérés legfontosabb eredménye, hogy **a megkérdezettek lényegesen aktívabbak és
tudatosabbak, mint amire számítottam**: 82%-uk mozog legalább heti háromszor, 82%-uk
iszik naponta legalább 5 pohár vizet, és szinte mindenki rendszeresen reggelizik.
Mégis van **két terület, ahol majdnem mindenki elmarad az ajánlástól**:

- **Zöldség és gyümölcs:** 22 emberből 1 közelíti meg a WHO napi ajánlását.
- **Alvás:** a minta 45%-a 7 óránál kevesebbet alszik iskolanapokon.

Ezért a produktum nem az általános életmódról szól, hanem erről a két vakfoltról —
és a képernyőidőről, amely szorosan együtt jár a rendszeres nappali fáradtsággal.

---

## Készítők

| Név | Szerep |
|---|---|
| **Gerecze Ádám** | projektvezetés, kutatás, fejlesztés, dokumentáció — a projekt teljes tartalma |

A feladatkiírás 2–3 fős csoportokat ír elő. A csoportbeosztás során nem alakult ki
több fős csapat, ezért a projekt minden elemét egyedül készítettem el. Az önálló munka
indoklása és értékelése a [projekttervben](projektterv/projektterv.md) és a
[projektbeszámolóban](dokumentacio/projektbeszamolo.md) olvasható.

---

## Az elkészült elemek

| Elem | Típus | Hol található? |
|---|---|---|
| **Projektweboldal** | kötelező elem | [`produktum/weboldal/`](produktum/weboldal/) |
| **Online kérdőív és elemzés** | választott feladat **D)** | [`produktum/kerdoiv/`](produktum/kerdoiv/) |
| **Prezentáció** | választott feladat **A)** | [`produktum/prezentacio/`](produktum/prezentacio/) |

### Projektweboldal
6 aloldal (kezdőlap, táplálkozás, mozgás, alvás és képernyőidő, kutatásunk, források),
navigációs menü, Bootstrap 5.3 keretrendszer saját stíluslappal, 5 saját készítésű
SVG illusztráció, 18 diagram és egy interaktív napi ellenőrzőlista. Reszponzív,
billentyűzettel is használható.

**Megnyitás:** `produktum/weboldal/index.html`

### Online kérdőív és elemzés
16 kérdés öt témakörben, Google Űrlapokban, 22 kitöltő. A válaszok feldolgozása Python
szkripttel (pandas, matplotlib): 18 diagram és írásos elemzés következtetésekkel.

### Prezentáció
16 dia saját diamintával (világos és sötét változat), natív PowerPoint-diagramokkal,
áttűnésekkel és belépő animációkkal. Minden diához tartozik előadói jegyzet.

---

## A repository szerkezete

```
.
├── README.md                    ← ez a fájl
├── projektterv/
│   ├── projektterv.md           cél, célközönség, feladatok, feladatmegosztás
│   └── gantt.png                az ütemterv Gantt-diagramja
├── produktum/
│   ├── weboldal/                a projektweboldal (index.html a belépési pont)
│   │   ├── css/, js/, kepek/
│   │   └── *.html               6 aloldal
│   ├── kerdoiv/
│   │   ├── kerdoiv_kerdesek.md  a 16 kérdés és a válaszlehetőségek
│   │   ├── urlap_utmutato.md    hogyan készült el a Google Űrlap
│   │   ├── valaszok.csv         a nyers válaszok (Google Űrlapok exportja, 22 sor)
│   │   ├── elemzes.py           az adatfeldolgozó szkript
│   │   ├── elemzes.md           az írásos elemzés
│   │   ├── osszesites.json      a számok gépi formában
│   │   └── diagramok/           18 diagram
│   └── prezentacio/
│       └── egeszseges_eletmod.pptx
├── dokumentacio/
│   └── projektbeszamolo.md      cél, folyamat, problémák, önértékelés
├── bemutato_video/
│   └── forgatokonyv.md          a szóbeli bemutató forgatókönyve
├── forrasok/
│   └── forrasok.md              a felhasznált források jegyzéke
└── eszkozok/                    generátor szkriptek
    ├── adatok.py                közös adatbetöltő
    ├── weboldal.py              a weboldal generálása
    ├── prezi.js                 a prezentáció generálása
    ├── animacio.py              áttűnések és animációk hozzáadása
    ├── elemzes_szoveg.py        az elemzés szövegének generálása
    └── gantt.py                 az ütemterv rajzolása
```

---

## Használt eszközök

| Eszköz | Mire? |
|---|---|
| Google Űrlapok, Google Táblázatok | a kérdőív és a válaszok exportja |
| Python 3 – pandas, matplotlib | adatfeldolgozás, 18 diagram, Gantt-diagram |
| HTML5, CSS3, JavaScript | a projektweboldal |
| Bootstrap 5.3 | reszponzív rácsrendszer, navigáció |
| Google Fonts – Outfit, Karla | tipográfia |
| SVG | saját vektoros illusztrációk |
| pptxgenjs, Microsoft PowerPoint | a prezentáció |
| Git, GitHub | verziókezelés, beadás |
| Visual Studio Code | fejlesztés |

---

## Hogyan lehet frissíteni a projektet új kérdőívadattal?

A projekt **adatvezérelt**: minden szám egyetlen forrásból, az elemzés kimenetéből
(`osszesites.json`) származik. Így kizárt, hogy a weboldalon más érték szerepeljen,
mint a prezentációban.

Ha új válaszok érkeznek:

```bash
# 1. Töltsd le a Google Űrlapok exportját, és mentsd ide:
#    produktum/kerdoiv/valaszok.csv

# 2. Futtasd az elemzést (diagramok + osszesites.json)
python3 produktum/kerdoiv/elemzes.py

# 3. Generáld újra az írásos elemzést
python3 eszkozok/elemzes_szoveg.py

# 4. Generáld újra a weboldalt
python3 eszkozok/weboldal.py

# 5. Generáld újra a prezentációt
node eszkozok/prezi.js
python3 eszkozok/animacio.py
```

**Függőségek:** Python 3 (`pip install pandas matplotlib`), Node.js
(`npm install pptxgenjs`).

> **Megjegyzés:** a szkript a kérdések elején álló sorszám alapján ismeri fel az
> oszlopokat, ezért az űrlapon minden kérdésnek sorszámmal kell kezdődnie
> (pl. `3. Reggelizel iskolanapokon?`).

---

## Eredmények összefoglalása

A felmérés hat fő következtetése:

1. **A minta jobban él, mint vártam.** 82% mozog rendszeresen, 82% iszik elég vizet,
   az átlagos egészség-önértékelés 3,82 az ötös skálán. A kiinduló feltételezésem nem
   igazolódott.

2. **A zöldség- és gyümölcsfogyasztás önálló vakfolt.** 22 emberből 1 közelíti meg az
   ajánlott mennyiséget — miközben ugyanezek az emberek minden más táplálkozási
   kérdésben jól teljesítenek.

3. **Az alvás a másik vakfolt.** A minta 45%-a 7 óránál kevesebbet alszik. A jó
   szokások — sport, víz, reggeli — ezt nem kompenzálják.

4. **A képernyőidő és a rendszeres fáradtság szorosan együtt jár.** Napi 4 óra alatt
   30%, 4 óra felett 92% a rendszeresen fáradtak aránya. Ez a legmarkánsabb eredmény —
   de együttjárás, nem bizonyított okozat.

5. **A tájékozódás kiegyensúlyozottabb a vártnál.** A közösségi média vezet, de
   orvostól is 9 ember tájékozódik, és senki nem jelölte, hogy sehonnan.

6. **Kétféle üzenet kell.** 12 fő változtatna, 10 viszont elégedett — utóbbiaknak nem
   tanács kell, hanem a két vakfolt megmutatása.

A pontos számok, a diagramok és a módszertani korlátok az
[elemzésben](produktum/kerdoiv/elemzes.md) olvashatók.

---

## Fontos megjegyzések

**A minta korlátai.** A felmérés nem reprezentatív: kényelmi mintavétellel készült, a
válaszadók a saját iskolai és ismeretségi körömből származnak. Ez itt különösen fontos,
mert a minta feltűnően sportos (22-ből 18 mozog legalább heti háromszor), ami
valószínűleg nem a korosztályra, hanem az én környezetemre jellemző. Az eredmények
**erről a 22 emberről** szólnak.

**Együttjárás, nem ok-okozat.** A képernyőidő és a fáradtság közötti összefüggés
markáns, de az irányát ez a vizsgálat nem tudja megállapítani.

**Egy kérdés kimaradt.** Az űrlap véglegesítésekor kimaradt egy tervezett kérdés az
egészséges életmód akadályairól. Emiatt az eredetileg tervezett kutatási kérdésre nem
tudok válaszolni; ezt a szűkítést a dokumentációban végig jeleztem.

**Nem orvosi tanács.** A projekt iskolai feladat keretében, tájékoztató céllal
készült. Nem helyettesíti a szakorvosi véleményt.

**Adatkezelés.** A kérdőív anonim volt, személyazonosításra alkalmas adatot nem
gyűjtöttem. A válaszokat kizárólag összesítve, iskolai projekt keretében használtam fel.

---

## GitHub-link

>   https://github.com/AdamGeri/Eg-szs-ges-letm-d
