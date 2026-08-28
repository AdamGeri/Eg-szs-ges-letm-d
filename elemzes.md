# A kérdőív eredményeinek elemzése

**Projekt:** Egészséges életmód – digitális projektmunka
**Készítette:** Gerecze Ádám
**Minta:** 22 fő, 14–19 éves fiatalok
**Eszközök:** Google Űrlapok (adatgyűjtés) · Python – pandas, matplotlib (feldolgozás)

---

## 0. A legfontosabb megállapítás egy mondatban

A megkérdezett fiatalok **lényegesen aktívabbak és tudatosabbak**, mint amire a
kérdőív összeállításakor számítottam — mégis van két terület, ahol szinte mindenki
elmarad az ajánlástól: a **zöldség- és gyümölcsfogyasztás** és az **alvás**.

---

## 1. A minta összetétele

A kérdőívet **22 fő** töltötte ki: 10 férfi és 12 nő.
A legnépesebb korcsoport a **18–19 évesek** köre (13 fő), tehát
a minta a felső középiskolás korosztály felé tolódik.

> ⚠️ **A minta korlátai — ezt fontos elöljáróban tisztázni.**
> A felmérés **nem reprezentatív**. Kényelmi mintavétellel készült: a válaszadók a
> saját iskolai és ismeretségi körömből származnak. Ez különösen fontos itt, mert a
> minta feltűnően sportos (18 fő mozog legalább heti háromszor),
> ami valószínűleg nem a korosztály egészére, hanem az én környezetemre jellemző.
> Az eredmények tehát **erről a 22 emberről** szólnak, nem a magyar fiatalokról.

![Nemek megoszlása](diagramok/01_nemek.png)
![Életkori megoszlás](diagramok/02_eletkor.png)

---

## 2. Táplálkozási szokások

### Reggeli — jobb, mint vártam

A válaszadók közül **19 fő a 21-ből
(90%) mindig vagy gyakran reggelizik** iskolanapokon, és
egyetlen ember sem jelölte azt, hogy soha. Ez lényegesen jobb arány, mint amire
a szakirodalom alapján számítottam.

*(Egy válaszadó ezt a kérdést üresen hagyta, ezért itt 21 a
viszonyítási alap.)*

![Reggeli](diagramok/03_reggeli.png)

### Zöldség és gyümölcs — a felmérés leggyengébb pontja

Itt viszont éles a kép: a WHO ajánlása napi legalább 400 gramm, azaz körülbelül
5 adag zöldség és gyümölcs. Ezt **22 emberből mindössze 1
közelíti meg**, miközben **7 fő legfeljebb napi egyszer** eszik
ilyet.

Ez azért különösen érdekes, mert ugyanez a minta minden más táplálkozási kérdésben jól
teljesít. A zöldségfogyasztás tehát nem általános igénytelenségből marad el, hanem
önmagában, konkrét vakfoltként.

![Zöldség-gyümölcs](diagramok/04_zoldseg_gyumolcs.png)

### Folyadék és cukor — meglepően jó eredmények

- **18 fő (82%) iszik naponta legalább 5 pohár vizet**,
  és senki nem jelölte a legalacsonyabb kategóriát.
- **11 fő (50%) ritkán vagy soha nem iszik
  cukros üdítőt.** Ugyanakkor 4 ember naponta fogyaszt ilyet —
  ők egy kicsi, de jól elkülönülő csoport.
- **16 fő (73%)** legfeljebb havonta 1–2
  alkalommal eszik gyorséttermi vagy rendelt ételt.

![Cukros üdítő](diagramok/05_cukros_udito.png)
![Vízfogyasztás](diagramok/06_vizfogyasztas.png)
![Gyorsétterem](diagramok/07_gyorsetterem.png)

---

## 3. Testmozgás

Ez a minta legerősebb területe: **18 fő (82%)
mozog legalább heti három alkalommal** a testnevelési órán kívül, közülük
17 szinte naponta. Mindössze 2 ember jelölte,
hogy szinte soha nem sportol.

A választott mozgásformák:

- **Futás** – 16 fő
- **Konditerem, erősítés** – 14 fő
- **Kerékpározás** – 14 fő
- **Egyéb sporttevékenység** – 13 fő
- **Séta, túrázás** – 5 fő
- **Nem sportolok** – 1 fő

A legnépszerűbb a **futás** (16 fő). Figyelemre
méltó, hogy a válaszadók többsége több mozgásformát is megjelölt, tehát nem egyetlen
sportághoz kötődnek.

![Sportolási gyakoriság](diagramok/08_sport_gyakorisag.png)
![Mozgásformák](diagramok/09_mozgasformak.png)

---

## 4. Alvás, képernyőidő, közérzet

### Alvás — a másik vakfolt

A 14–19 éves korosztály számára ajánlott alvásmennyiség 8–10 óra. Ezt
**1 ember éri el** a 22-ből. Ennél is beszédesebb, hogy
**10 fő (45%) 7 óránál kevesebbet alszik** egy
átlagos iskolai éjszakán, közülük 2 hat óránál is kevesebbet.

Vagyis miközben ez a minta sportol, vizet iszik és reggelizik, az alvás területén
majdnem a fele elmarad a minimumtól is.

![Alvás](diagramok/10_alvas.png)

### Képernyőidő

**12 fő (55%) tölt naponta több mint 4 órát
képernyő előtt** szabadidőben — ez az iskolai és tanulási képernyőidőn felül értendő.

![Képernyőidő](diagramok/11_kepernyoido.png)

### Fáradtság

**14 fő (64%) érzi magát legalább
hetente többször fáradtnak** napközben, 5 ember pedig szinte
minden nap. Ez az arány feltűnően magas egy ilyen aktív mintában — és éppen ez teszi
érdekessé a következő fejezetet.

![Fáradtság](diagramok/12_faradtsag.png)

### Energiaital

**14 fő (64%) soha nem fogyaszt
energiaitalt**, 8 ember pedig legalább alkalmanként. Napi
fogyasztót a mintában nem találtam. Ez lényegesen kedvezőbb kép, mint amit a téma
médiavisszhangja alapján vártam.

![Energiaital](diagramok/13_energiaital.png)

### Egészség-önértékelés

A válaszadók **átlagosan 3,82-re** értékelték saját életmódjuk
egészségességét az 1–5-ös skálán. Ez magas érték, és összhangban van azzal, amit a
mozgásra és a folyadékfogyasztásra vonatkozó válaszok mutatnak.

![Önértékelés](diagramok/14_onertekeles.png)

---

## 5. Két összefüggés

### A) Képernyőidő és a rendszeres fáradtság — a felmérés fő eredménye

| Napi képernyőidő | Válaszadó | Legalább hetente többször fáradt | Arány |
|---|---|---|---|
| < 2 óra | 1 fő | 0 fő | 0% |
| 2–4 óra | 9 fő | 3 fő | 33% |
| 4–6 óra | 10 fő | 9 fő | 90% |
| 6+ óra | 2 fő | 2 fő | 100% |

Két csoportra összevonva a kép még élesebb:

- **Napi 4 óránál kevesebb képernyőidő:** 10 főből
  3 fáradt rendszeresen — **30%**
- **Napi 4 óránál több képernyőidő:** 12 főből
  11 fáradt rendszeresen — **92%**

Az összefüggés monoton: minél több a képernyőidő, annál nagyobb a rendszeres
fáradtság aránya. Ez azért fontos, mert ez a minta egyébként rendkívül aktív — vagyis
**a sportolás önmagában nem védi meg őket a fáradtságtól**.

![Képernyőidő és fáradtság](diagramok/17_kepernyo_faradtsag.png)

> **Módszertani megjegyzés:** ez **együttjárás, nem bizonyított ok-okozat**.
> Elképzelhető, hogy a hosszú képernyőidő okozza a fáradtságot (például késői
> lefekvés vagy rosszabb alvásminőség miatt), de az is, hogy a fáradt ember választja
> a passzív képernyőzést más tevékenység helyett. A felmérésem keresztmetszeti:
> egyetlen időpontban kérdez, tehát az irányt nem tudja megállapítani. A szélső
> kategóriákban ráadásul csak 1, illetve 2 válaszadó van, ezért a középső két
> kategória összehasonlítása megbízhatóbb.

### B) Alvásmennyiség és egészség-önértékelés

| Alvásmennyiség | Válaszadó | Átlagos önértékelés (1–5) |
|---|---|---|
| 8 óránál többet | 1 fő | 4,00 |
| 7–8 órát | 11 fő | 4,00 |
| 6–7 órát | 8 fő | 3,75 |
| 6 óránál kevesebbet | 2 fő | 3,00 |

A tendencia iránya megfelel a várakozásnak: aki többet alszik, magasabbra értékeli a
saját egészségét. **A különbség azonban kicsi, és az alcsoportok nagyon kis
elemszámúak** (a legkevesebbet alvók csoportjában mindössze 2 ember
van). Ebből komoly következtetést nem vonok le — tendenciaként érdemes kezelni.

![Alvás és önértékelés](diagramok/18_alvas_onertekeles.png)

### Amit meg akartam nézni, de nem lehetett

Eredetileg a **sportolás és az önértékelés** kapcsolatát terveztem központi
összefüggésnek. Az adatok ezt nem tették lehetővé:

| Sportolási gyakoriság | Válaszadó | Átlagos önértékelés |
|---|---|---|
| Szinte naponta | 17 fő | 4,00 |
| Hetente 3–4 alkalommal | 1 fő | 4,00 |
| Hetente 1–2 alkalommal | 2 fő | 2,50 |
| Szinte soha | 2 fő | 3,50 |

A válaszadók 17-en egyetlen kategóriába (szinte naponta) estek,
a többi három csoportban összesen 1–2 ember van. **Ekkora alcsoportokból nem lehet
átlagot értelmezni**: egyetlen ember válasza az egész csoportátlagot eltolja. Ezért
ezt az összefüggést nem ábrázoltam diagramon, és nem is építettem rá következtetést.

Ez maga is tanulság: egy homogén minta bizonyos kérdésekre egyszerűen nem tud
válaszolni, mert nincs benne elég változatosság.

---

## 6. Tájékozódás

- **Közösségi média** – 14 fő
- **Család, barátok** – 10 fő
- **Orvos, szakember** – 9 fő
- **Szakmai weboldalak** – 5 fő
- **Iskola, tanárok** – 2 fő

A **közösségi média** vezet (14 fő), de a kép kiegyensúlyozottabb,
mint amire számítottam: **orvostól vagy szakembertől 9 ember**
tájékozódik, és senki nem jelölte, hogy sehonnan.

Ez fontos árnyalat. A közösségi média valóban a leggyakoribb forrás, de nem kizárólagos:
a válaszadók többsége több forrásból is tájékozódik, és a szakmai források is jelen
vannak. A forráskritika tehát továbbra is fontos, de a helyzet nem olyan rossz, mint a
téma szokásos beállítása sugallja.

![Információforrás](diagramok/15_informacioforras.png)

---

## 7. Változtatási hajlandóság

**12 fő (55%) szeretne változtatni** az életmódján,
közülük 4 nem tudja, hol kezdje.
**10 fő (45%) elégedett** a
jelenlegi életmódjával — ami ebben az aktív mintában nem meglepő.

![Változtatás](diagramok/16_valtoztatas.png)

---

## 8. Következtetések

1. **A minta lényegesen egészségesebben él, mint vártam.**
   82% mozog legalább heti háromszor, 82% iszik
   elég vizet, majdnem mindenki rendszeresen reggelizik, és az átlagos önértékelés
   3,82. A kiinduló feltételezésem, hogy a fiatalok általánosan
   rosszul élnek, ebben a körben **nem igazolódott**.

2. **A zöldség- és gyümölcsfogyasztás önálló vakfolt.** 22 emberből
   1 közelíti meg az ajánlott mennyiséget. Ez azért figyelemre
   méltó, mert ugyanezek az emberek minden más táplálkozási kérdésben jól teljesítenek.

3. **Az alvás a másik vakfolt.** A minta 45%-a 7 óránál kevesebbet
   alszik. A jó szokások — sport, víz, reggeli — **nem kompenzálják** az alváshiányt.

4. **A képernyőidő és a rendszeres fáradtság szorosan együtt jár.** 4 óra alatt
   30%, 4 óra felett 92% a rendszeresen
   fáradtak aránya. Ez a felmérés legmarkánsabb eredménye — de együttjárás, nem
   bizonyított okozat.

5. **A tájékozódás kiegyensúlyozottabb a vártnál.** A közösségi média vezet, de a
   szakmai források is jelen vannak, és senki nem tájékozódik sehonnan.

6. **A többség változtatna**, ugyanakkor 10 ember elégedett.
   Vagyis nem egyetlen üzenet kell, hanem kettő: az elégedetteknek a két vakfolt
   (alvás, zöldség) megmutatása, a változtatni akaróknak konkrét első lépés.

---

## 9. Javaslatok

A felmérés eredményeiből következően a javaslataim **nem az egész életmód
átalakítására** irányulnak — erre ebben a körben nincs is szükség —, hanem a két
azonosított vakfoltra és a képernyőidőre:

| Terület | Miért ez? | Javasolt első lépés |
|---|---|---|
| **Zöldség, gyümölcs** | 22 emberből csak 1 éri el az ajánlást | Napi 1 gyümölcs a táskába; a menzán a saláta elsőként |
| **Alvás** | a minta 45%-a 7 óra alatt alszik | Fix lefekvési idő hétvégén is; koffeinstop délután 4 után |
| **Képernyőidő** | 4 óra felett 92% a rendszeres fáradtság | Lefekvés előtt 30 perccel a telefon félretétele |
| **Cukros üdítő** | 4 ember naponta iszik | A nap első felében víz az üdítő helyett |
| **Tájékozódás** | a közösségi média a leggyakoribb forrás | Három kérdés minden tanács előtt: ki mondja, mire hivatkozik, mit akar eladni? |

Ezek a javaslatok kerültek be a projekt weboldalának almenüibe és a prezentáció
záró szakaszába.

---

*Ez a dokumentum az `eszkozok/elemzes_szoveg.py` szkripttel, az `osszesites.json`
adataiból automatikusan generálódott. Kézzel szerkeszteni nem érdemes: új adat esetén
felülíródik.*
