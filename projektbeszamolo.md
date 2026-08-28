# Projektbeszámoló

**Projekt:** Egészséges életmód – digitális projektmunka
**Tantárgy:** IKT Projektmunka I., 1/13. Sz. évfolyam
**Készítette:** Gerecze Ádám
**Időszak:** 2026. augusztus 23. – augusztus 28.

---

## 1. A projekt célja

A projekt kiindulópontja egy egyszerű kérdés volt: **mennyire élnek egészségesen a
körülöttem lévő fiatalok, és hol maradnak el az ajánlásoktól?**

Ezt nem lehet internetes cikkek olvasásával eldönteni, ezért a projekt középpontjába
egy **saját kérdőíves felmérést** tettem. A projekt három célja:

1. felmérni a környezetemben élő 14–19 évesek életmódbeli szokásait;
2. azonosítani azokat a területeket, ahol a legnagyobb az elmaradás;
3. az adatokra épülő, gyakorlatias digitális produktumot készíteni.

A célközönség elsősorban a **14–19 éves középiskolások**, másodsorban a pedagógusok
és a szülők.

### A kutatási kérdés menet közben szűkült

Eredetileg egy élesebb kérdést terveztem: *„a tudás hiánya akadályozza a fiatalokat,
vagy valami más?"* Ehhez a kérdőívben szerepelt volna egy tétel az akadályokról
(időhiány, motiváció, ár, ismerethiány). **Ez a kérdés az űrlap véglegesítésekor
kimaradt**, ezért erre a kérdésre nem tudok válaszolni.

Ahelyett, hogy az akadályokra vonatkozó következtetést a meglévő adatokból
„kikövetkeztettem" volna, szűkítettem a kutatási kérdést a ténylegesen mért
szokásokra. Ez kevésbé látványos, de az adatokkal alátámasztható.

---

## 2. A tervezési folyamat

### 2.1 Témaválasztás

A választható témák közül az *Egészséges életmód* mellett azért döntöttem, mert ez az
egyetlen olyan téma, amelyről **saját, mérhető adatot** tudok gyűjteni a saját
korosztályomtól. Az „iskola digitális bemutatása" vagy a „helyi értékek" témák
elsősorban leíró jellegűek lettek volna; itt viszont lehetett kutatási kérdést
megfogalmazni és arra választ keresni.

### 2.2 A szerkezet megtervezése

A projektet a **kutatás köré** építettem, nem fordítva. Ez a döntés a projekt egészét
meghatározta:

```
kutatási kérdés  →  kérdőív  →  adatok  →  következtetések  →  weboldal + prezentáció
```

Ez azt jelentette, hogy a weboldal végleges tartalmát nem tudtam az elején megírni:
meg kellett várnom, mit mutatnak az adatok. Ezért az ütemtervben az adatgyűjtés indul
a legkorábban, és közben a weboldal *szerkezetén* és az *ábráin* dolgoztam, amelyek
nem függenek a konkrét számoktól.

### 2.3 Technológiai döntések

| Döntés | Alternatíva | Miért így? |
|---|---|---|
| Python az elemzéshez | Excel | Újrafuttatható: egy parancs frissíti mind a 18 diagramot |
| Bootstrap + saját CSS | Csak Bootstrap | Az alapértelmezett Bootstrap-kinézet felismerhető és jellegtelen |
| Saját SVG ábrák | Letöltött stock fotók | Nincs jogi kérdés, és pontosan azt mutatja, amit el akarok mondani |
| JSON adatréteg | Kézzel beírt számok | A weboldal és a prezi számai egy forrásból jönnek, nem térhetnek el |

Az utolsó pont a projekt legfontosabb szerkezeti döntése. Az elemző szkript egy
`osszesites.json` állományba írja ki az összes számot, és **a weboldal-generátor és a
prezentáció-generátor egyaránt ebből dolgozik**. Így kizárt, hogy a weboldalon más
szám szerepeljen, mint a prezentációban — ami kézi átírásnál szinte biztosan
előfordult volna.

---

## 3. Munkamegosztás

A feladatkiírás 2–3 fős csoportokat ír elő. A csoportbeosztás során nem alakult ki
több fős csapat, ezért **a projekt minden elemét egyedül készítettem el**:
a projekttervezést, az információgyűjtést, a kérdőív összeállítását és elemzését, a
weboldal fejlesztését, a prezentációt és ezt a dokumentációt is.

| Terület | Felelős | Elkészült |
|---|---|---|
| Projekttervezés, ütemterv | Gerecze Ádám | `projektterv/` |
| Információgyűjtés, forráskritika | Gerecze Ádám | `forrasok/` |
| Kérdőív és elemzés | Gerecze Ádám | `produktum/kerdoiv/` |
| Weboldal (HTML, CSS, JS, SVG) | Gerecze Ádám | `produktum/weboldal/` |
| Prezentáció | Gerecze Ádám | `produktum/prezentacio/` |
| Dokumentáció, GitHub | Gerecze Ádám | `dokumentacio/`, `README.md` |

Az önálló munkának volt hátránya és előnye is. Hátránya, hogy nem volt kivel megvitatni
a szakmai döntéseket — így nagyobb a kockázata annak, hogy egy rossz irányt sokáig
viszek tovább. Ez konkrétan meg is történt (lásd az 5.3 pontot). További hátrány, hogy
a kérdőívet egyetlen ismeretségi körben tudtam terjeszteni, ami növelte a minta
torzítását. Előnye viszont, hogy minden részfeladatot végig kellett csinálnom, így a
projekt egészét értem, nem csak egy szeletét.

---

## 4. Az elkészített feladatok

### 4.1 Projektweboldal (kötelező elem)

Hat aloldalból álló, reszponzív weboldal: kezdőlap, táplálkozás, mozgás, alvás és
képernyőidő, kutatásunk, források.

- **Keretrendszer:** Bootstrap 5.3, saját stíluslappal kiegészítve
- **Tipográfia:** Outfit (címek) és Karla (törzsszöveg) a Google Fontsról
- **Illusztrációk:** 5 saját készítésű SVG ábra + 17 saját diagram
- **Interaktív elem:** napi ellenőrzőlista JavaScripttel, haladásjelző sávval
- **Hozzáférhetőség:** billentyűzettel bejárható, látható fókuszjelzés, `alt`
  szövegek minden képnél, `prefers-reduced-motion` figyelembe vétele

Az oldal visszatérő eleme az **adatcsík**: minden témaoldal tetején négy szám áll a
saját felmérésből. Ez köti össze az általános ismereteket a konkrét kutatással.

### 4.2 Online kérdőív és elemzés (választott feladat: D)

- **16 kérdés** öt témakörben: alapadatok, táplálkozás, mozgás, alvás/képernyő,
  attitűd
- **Google Űrlapok**, anonim kitöltés, kb. 3 perc, **22 kitöltő**
- **Feldolgozás:** Python (pandas, matplotlib), 18 diagram
- **Kimenet:** diagramok, `osszesites.json`, írásos elemzés következtetésekkel

Az elemzés két kereszttáblát emel ki: a képernyőidő és a rendszeres nappali fáradtság
kapcsolatát, valamint az alvásmennyiség és az egészség-önértékelés kapcsolatát.

### 4.3 Prezentáció (választott feladat: A)

- **16 dia**, saját diamintával (világos és sötét változat)
- **Natív PowerPoint-diagramok**, nem képek — így szerkeszthetők maradnak
- **Áttűnések** minden diára, **belépő animációk** a tartalmi elemekre
- **Előadói jegyzet** minden diához, a szóbeli bemutatóhoz

---

## 5. Felmerült problémák és megoldásaik

### 5.1 Kevés kitöltő az első napon

**A probléma.** A kérdőív linkjét bedobtam a csoportba, és az első nap alig érkezett
válasz. A feladat legalább 20 kitöltőt ír elő, tehát ez veszélybe sodorta a projekt
gerincét.

**A megoldás.** Áttértem a személyre szóló megkeresésre: egyesével írtam embereknek,
és megírtam, hogy három perc az egész, és mire kell. Így gyűlt össze a 22 kitöltő.
A tanulság az, hogy egy csoportba dobott link mindenki felelőssége, tehát senkié — a
személyes kérés viszont konkrét.

### 5.2 Az elemzés kézzel kezelhetetlen volt

**A probléma.** Elsőre táblázatkezelőben kezdtem összesíteni a válaszokat. Minden új
kitöltő érkezésekor újra kellett számolni a százalékokat, és újra kellett rajzolni a
diagramokat. Ez néhány kör után nyilvánvalóan tarthatatlanná vált.

**A megoldás.** Megírtam az elemzést Python szkriptként. Ez beolvassa a CSV-t,
kiszámol mindent, és legenerálja a diagramokat. Egy futtatás, kb. két másodperc.
Később ezt kiterjesztettem: a szkript egy JSON állományba is kiírja a számokat,
amelyet a weboldal- és a prezentáció-generátor is felhasznál.

### 5.3 Az adat mást mutatott, mint amit vártam

**A probléma.** A kérdőívet azzal a feltételezéssel állítottam össze, hogy a fiatalok
általánosan rosszul élnek: keveset mozognak, sok cukros üdítőt isznak, kevés vizet.
Az első weboldal-vázlatom is erre épült.

Az adat ezt megcáfolta. A 22 válaszadóból 18 mozog legalább heti háromszor, 18 iszik
naponta legalább 5 pohár vizet, 19-en a 21 válaszolóból rendszeresen reggeliznek, és
az átlagos egészség-önértékelés 3,82 az ötös skálán. Ez egy **aktív, tudatos minta**.

**A megoldás.** Nem hagytam figyelmen kívül a nekem nem tetsző adatokat, hanem átírtam
a projekt üzenetét. Az adatokból két olyan terület rajzolódott ki, ahol ez az egyébként
jól teljesítő minta is egyértelműen elmarad:

- **Zöldség és gyümölcs:** 22 emberből 1 közelíti meg a WHO ajánlását.
- **Alvás:** 10 fő (45%) 7 óránál kevesebbet alszik.

Így a produktum végül nem az általános életmódról szól, hanem erről a **két
vakfoltról** — ami sokkal konkrétabb és hasznosabb üzenet.

Ez volt a projekt legfontosabb tanulsága: **az adat felülírta a saját előfeltevésemet**,
és nekem ehhez kellett igazodnom, nem fordítva.

### 5.4 Egy összefüggés egyszerűen nem működött

**A probléma.** Fő összefüggésnek a **sportolás és az egészség-önértékelés**
kapcsolatát terveztem. Az adatok ezt nem tették lehetővé: a 22 válaszadóból 17 ugyanabba
a kategóriába (szinte naponta sportol) esett, a másik három csoportban összesen 1–2
ember van. Ekkora alcsoportokból nem lehet átlagot értelmezni — egyetlen ember válasza
az egész csoportátlagot eltolja.

**A megoldás.** Nem közöltem ezt az összefüggést, hanem helyette az **alvásmennyiség és
az önértékelés** kapcsolatát vizsgáltam, ahol kiegyensúlyozottabbak a csoportméretek.
A ki nem közölt elemzést viszont nem hallgattam el: az elemzésben, a weboldalon és a
prezentációban is leírtam, hogy mit terveztem, miért nem működött, és mit tanultam
belőle.

Ez maga is tanulság: egy homogén minta bizonyos kérdésekre nem tud válaszolni, mert
nincs benne elég változatosság.

### 5.5 Az ok-okozat kísértése

**A probléma.** A képernyőidő és a fáradtság közötti összefüggés élesen jött ki: a
napi 4 óránál kevesebbet képernyőzők közül 30% (3 fő a 10-ből), a 4 óránál többet
képernyőzők közül 92% (11 fő a 12-ből) érzi magát rendszeresen fáradtnak. Nagyon
csábító volt kimondani, hogy a képernyőzés fárasztja el a fiatalokat.

**A megoldás.** Nem mondtam ki, mert nem következik az adatokból. A felmérés
keresztmetszeti: egyetlen időpontban kérdez, tehát az irányt nem tudja megállapítani.
Ugyanúgy lehetséges, hogy a fáradt ember választja a passzív képernyőzést. Ráadásul a
két szélső kategóriában mindössze 1, illetve 2 válaszadó van. Ezt a korlátot külön
dobozban jeleztem a weboldalon, a prezentáció fő diáján és az elemzésben is.

### 5.6 Az adatok és a szövegek szétcsúszása

**A probléma.** Amikor a weboldalon és a prezentációban is kézzel írtam be a
számokat, előfordult, hogy egy javítás után a két helyen más érték szerepelt.

**A megoldás.** Bevezettem a JSON adatréteget. Az elemző szkript kiírja az összes
számot, a weboldal- és a prezentáció-generátor pedig onnan olvassa. A számok így
csak egy helyen léteznek. Új kérdőívadat esetén három parancs frissíti a teljes
projektet:

```bash
python3 produktum/kerdoiv/elemzes.py     # adatok és diagramok
python3 eszkozok/weboldal.py             # weboldal
node eszkozok/prezi.js                   # prezentáció
```

---

## 6. Önértékelés

### Amivel elégedett vagyok

**Saját adatot gyűjtöttem.** A projekt nem internetes cikkek összefoglalása. Minden
állítás mögött vagy egy intézményi forrás (WHO, Harvard, Sleep Foundation, EFSA), vagy
a saját felmérésem áll.

**Az elemzést újrafuttathatóvá tettem.** Ez több munka volt, mint kézzel összeadni a
válaszokat, de sokkal robusztusabb lett tőle a projekt. Ezt tartom a legjobb
informatikai döntésemnek — és konkrétan meg is térült, amikor a beérkező valódi adatok
alapján az egész projektet újra kellett generálni.

**A produktum az adatokhoz igazodott.** A weboldalt és a prezentációt átírtam, amikor
kiderült, hogy a kiinduló feltételezésem téves volt. Könnyebb lett volna ragaszkodni az
eredeti tervhez és kiválogatni a nekem tetsző számokat, de az nem lett volna őszinte.

**Nem közöltem olyan összefüggést, amit a minta nem bír el.** A sport–önértékelés
kapcsolatot kihagytam, mert az alcsoportok 1–2 fősek lettek. Ezt megindokolva
leírtam, ahelyett hogy elhallgattam volna.

**Végig jeleztem a minta korlátait.** Egy 22 fős, nem reprezentatív és feltűnően
sportos mintából csak korlátozott következtetés vonható le. Ezt nem rejtettem el,
hanem mindenhol kiírtam, ahol számot közlök.

### Amit legközelebb máshogy csinálnék

**Nem hagynám ki az akadályokra kérdező tételt.** Ez volt a legkomolyabb hibám. Az
űrlap véglegesítésekor kimaradt az a kérdés, amely a kutatási kérdésem magját adta
volna. Emiatt a projekt eredeti fő kérdésére nem tudok válaszolni. Legközelebb a
kérdéslistát tételesen összevetném az űrlappal, mielőtt megosztom.

**Változatosabb mintát gyűjtenék.** A 22 válaszadóból 17 szinte naponta sportol. Ez
nem a korosztályra jellemző, hanem az én ismeretségi körömre — és emiatt több elemzést
sem tudtam elvégezni. Ha több osztályon keresztül, tanári segítséggel terjeszteném a
kérdőívet, kevésbé lenne torzított.

**Beépítenék nyitott kérdéseket is.** Mind a 16 kérdés zárt volt, ami a feldolgozást
könnyítette, de sok információt elvesztettem. Egyetlen nyitott kérdés — például „mi
lenne az az egy dolog, ami segítene?" — sokat hozzátett volna.

**Több időt hagynék az adatgyűjtésre.** Több válasz mellett a kereszttáblák
alcsoportjai is elemezhető méretűek lennének.

### Amit a projektből tanultam

A legfontosabb, amit megtanultam, nem informatikai, hanem szemléleti: **az adat nem
arra való, hogy alátámassza, amit előre gondoltam.** Amikor a kérdőív szembement a
feltételezésemmel — a minta sokkal egészségesebben élt, mint vártam —, azt
választhattam volna, hogy kihangsúlyozom a nekem tetsző részeket, és úgy állítom be,
mintha a fiatalok rosszul élnének. Ehelyett átírtam a projekt üzenetét.

Ugyanez volt a helyzet két másik ponton. Az ok-okozati következtetés látványosabb lett
volna, ha többet állítok róla, mint amennyit az adat bír. A sport–önértékelés
összefüggést pedig ki lehetett volna tenni egy diagramra úgy, hogy senki nem veszi
észre, hogy 1–2 fős csoportokból származik.

Informatikai oldalról a legfontosabb tanulság az volt, hogy **egy adatot csak egy
helyen érdemes tárolni**. Ez akkor térült meg igazán, amikor a valódi kitöltések
megérkeztek: a diagramok, a weboldal számai és a prezentáció adatai egyetlen
parancssorozattal frissültek.

---

## 7. Mellékletek és a projekt elérhetősége

| Tartalom | Hely a repositoryban |
|---|---|
| Projektterv és Gantt-diagram | `projektterv/` |
| Kérdőív kérdései, űrlap-útmutató | `produktum/kerdoiv/` |
| Nyers válaszok, elemzés, 18 diagram | `produktum/kerdoiv/` |
| Projektweboldal | `produktum/weboldal/` |
| Prezentáció | `produktum/prezentacio/` |
| Forrásjegyzék | `forrasok/` |
| A bemutató forgatókönyve | `bemutato_video/` |
| Generátor szkriptek | `eszkozok/` |
