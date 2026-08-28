# -*- coding: utf-8 -*-
"""A kérdőív írásos elemzésének (elemzes.md) generálása az osszesites.json-ból.

Futtatás a projekt gyökeréből:
    python3 eszkozok/elemzes_szoveg.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import adatok  # noqa: E402

GYOKER = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KIMENET = os.path.join(GYOKER, "produktum", "kerdoiv", "elemzes.md")

A = adatok.keszit()
if not A["van_adat"]:
    sys.exit("Előbb futtasd az elemzést: python3 produktum/kerdoiv/elemzes.py")

o, N = A["nyers"], A["n"]
tv = adatok.tv

kf_sorok = ""
for cimke, e in A["kepernyo_faradtsag"].items():
    ossz, far = e["osszes"], e["faradt"]
    arany = f"{round(far / ossz * 100)}%" if ossz else "–"
    kf_sorok += f"| {cimke} | {ossz} fő | {far} fő | {arany} |\n"

ao_sorok = ""
for k, e in A["alvas_onertekeles"].items():
    ao_sorok += f"| {k} | {e['n']} fő | {tv(e['atlag'])} |\n"

sp_sorok = ""
for k, e in A["sport_onertekeles"].items():
    ao = tv(e["atlag"]) if e["n"] else "–"
    sp_sorok += f"| {k} | {e['n']} fő | {ao} |\n"

inf_lista = "".join(f"- **{k}** – {v} fő\n" for k, v in A["informacioforras"].items())
mf_lista = "".join(f"- **{k}** – {v} fő\n" for k, v in A["mozgasformak"].items())

szoveg = f"""# A kérdőív eredményeinek elemzése

**Projekt:** Egészséges életmód – digitális projektmunka
**Készítette:** Gerecze Ádám
**Minta:** {N} fő, 14–19 éves fiatalok
**Eszközök:** Google Űrlapok (adatgyűjtés) · Python – pandas, matplotlib (feldolgozás)

---

## 0. A legfontosabb megállapítás egy mondatban

A megkérdezett fiatalok **lényegesen aktívabbak és tudatosabbak**, mint amire a
kérdőív összeállításakor számítottam — mégis van két terület, ahol szinte mindenki
elmarad az ajánlástól: a **zöldség- és gyümölcsfogyasztás** és az **alvás**.

---

## 1. A minta összetétele

A kérdőívet **{N} fő** töltötte ki: {A['ferfi_fo']} férfi és {A['no_fo']} nő.
A legnépesebb korcsoport a **{A['kor_top']} évesek** köre ({A['kor_top_fo']} fő), tehát
a minta a felső középiskolás korosztály felé tolódik.

> ⚠️ **A minta korlátai — ezt fontos elöljáróban tisztázni.**
> A felmérés **nem reprezentatív**. Kényelmi mintavétellel készült: a válaszadók a
> saját iskolai és ismeretségi körömből származnak. Ez különösen fontos itt, mert a
> minta feltűnően sportos ({A['sport_gyakori_fo']} fő mozog legalább heti háromszor),
> ami valószínűleg nem a korosztály egészére, hanem az én környezetemre jellemző.
> Az eredmények tehát **erről a {N} emberről** szólnak, nem a magyar fiatalokról.

![Nemek megoszlása](diagramok/01_nemek.png)
![Életkori megoszlás](diagramok/02_eletkor.png)

---

## 2. Táplálkozási szokások

### Reggeli — jobb, mint vártam

A válaszadók közül **{A['reggeli_rendszeres_fo']} fő a {A['reggeli_valaszolt']}-ből
({A['reggeli_rendszeres_sz']}%) mindig vagy gyakran reggelizik** iskolanapokon, és
egyetlen ember sem jelölte azt, hogy soha. Ez lényegesen jobb arány, mint amire
a szakirodalom alapján számítottam.

*(Egy válaszadó ezt a kérdést üresen hagyta, ezért itt {A['reggeli_valaszolt']} a
viszonyítási alap.)*

![Reggeli](diagramok/03_reggeli.png)

### Zöldség és gyümölcs — a felmérés leggyengébb pontja

Itt viszont éles a kép: a WHO ajánlása napi legalább 400 gramm, azaz körülbelül
5 adag zöldség és gyümölcs. Ezt **{N} emberből mindössze {A['zoldseg_sok_fo']}
közelíti meg**, miközben **{A['zoldseg_keves_fo']} fő legfeljebb napi egyszer** eszik
ilyet.

Ez azért különösen érdekes, mert ugyanez a minta minden más táplálkozási kérdésben jól
teljesít. A zöldségfogyasztás tehát nem általános igénytelenségből marad el, hanem
önmagában, konkrét vakfoltként.

![Zöldség-gyümölcs](diagramok/04_zoldseg_gyumolcs.png)

### Folyadék és cukor — meglepően jó eredmények

- **{A['viz_sok_fo']} fő ({A['viz_sok_sz']}%) iszik naponta legalább 5 pohár vizet**,
  és senki nem jelölte a legalacsonyabb kategóriát.
- **{A['udito_ritkan_fo']} fő ({A['udito_ritkan_sz']}%) ritkán vagy soha nem iszik
  cukros üdítőt.** Ugyanakkor {A['udito_naponta_fo']} ember naponta fogyaszt ilyet —
  ők egy kicsi, de jól elkülönülő csoport.
- **{A['gyors_ritkan_fo']} fő ({A['gyors_ritkan_sz']}%)** legfeljebb havonta 1–2
  alkalommal eszik gyorséttermi vagy rendelt ételt.

![Cukros üdítő](diagramok/05_cukros_udito.png)
![Vízfogyasztás](diagramok/06_vizfogyasztas.png)
![Gyorsétterem](diagramok/07_gyorsetterem.png)

---

## 3. Testmozgás

Ez a minta legerősebb területe: **{A['sport_gyakori_fo']} fő ({A['sport_gyakori_sz']}%)
mozog legalább heti három alkalommal** a testnevelési órán kívül, közülük
{A['sport_naponta_fo']} szinte naponta. Mindössze {A['sport_soha_fo']} ember jelölte,
hogy szinte soha nem sportol.

A választott mozgásformák:

{mf_lista}
A legnépszerűbb a **{A['mozgas_elso'].lower()}** ({A['mozgas_elso_fo']} fő). Figyelemre
méltó, hogy a válaszadók többsége több mozgásformát is megjelölt, tehát nem egyetlen
sportághoz kötődnek.

![Sportolási gyakoriság](diagramok/08_sport_gyakorisag.png)
![Mozgásformák](diagramok/09_mozgasformak.png)

---

## 4. Alvás, képernyőidő, közérzet

### Alvás — a másik vakfolt

A 14–19 éves korosztály számára ajánlott alvásmennyiség 8–10 óra. Ezt
**{A['alvas_ajanlott_fo']} ember éri el** a {N}-ből. Ennél is beszédesebb, hogy
**{A['alvas_keves_fo']} fő ({A['alvas_keves_sz']}%) 7 óránál kevesebbet alszik** egy
átlagos iskolai éjszakán, közülük {A['alvas_nagyon_keves_fo']} hat óránál is kevesebbet.

Vagyis miközben ez a minta sportol, vizet iszik és reggelizik, az alvás területén
majdnem a fele elmarad a minimumtól is.

![Alvás](diagramok/10_alvas.png)

### Képernyőidő

**{A['kepernyo_sok_fo']} fő ({A['kepernyo_sok_sz']}%) tölt naponta több mint 4 órát
képernyő előtt** szabadidőben — ez az iskolai és tanulási képernyőidőn felül értendő.

![Képernyőidő](diagramok/11_kepernyoido.png)

### Fáradtság

**{A['faradt_rendszeres_fo']} fő ({A['faradt_rendszeres_sz']}%) érzi magát legalább
hetente többször fáradtnak** napközben, {A['faradt_naponta_fo']} ember pedig szinte
minden nap. Ez az arány feltűnően magas egy ilyen aktív mintában — és éppen ez teszi
érdekessé a következő fejezetet.

![Fáradtság](diagramok/12_faradtsag.png)

### Energiaital

**{A['energiaital_soha_fo']} fő ({A['energiaital_soha_sz']}%) soha nem fogyaszt
energiaitalt**, {A['energiaital_fo']} ember pedig legalább alkalmanként. Napi
fogyasztót a mintában nem találtam. Ez lényegesen kedvezőbb kép, mint amit a téma
médiavisszhangja alapján vártam.

![Energiaital](diagramok/13_energiaital.png)

### Egészség-önértékelés

A válaszadók **átlagosan {A['onertekeles_atlag']}-re** értékelték saját életmódjuk
egészségességét az 1–5-ös skálán. Ez magas érték, és összhangban van azzal, amit a
mozgásra és a folyadékfogyasztásra vonatkozó válaszok mutatnak.

![Önértékelés](diagramok/14_onertekeles.png)

---

## 5. Két összefüggés

### A) Képernyőidő és a rendszeres fáradtság — a felmérés fő eredménye

| Napi képernyőidő | Válaszadó | Legalább hetente többször fáradt | Arány |
|---|---|---|---|
{kf_sorok}
Két csoportra összevonva a kép még élesebb:

- **Napi 4 óránál kevesebb képernyőidő:** {A['kep_also_fo']} főből
  {A['kep_also_faradt_fo']} fáradt rendszeresen — **{A['kep_also_faradt_sz']}%**
- **Napi 4 óránál több képernyőidő:** {A['kep_felso_fo']} főből
  {A['kep_felso_faradt_fo']} fáradt rendszeresen — **{A['kep_felso_faradt_sz']}%**

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
{ao_sorok}
A tendencia iránya megfelel a várakozásnak: aki többet alszik, magasabbra értékeli a
saját egészségét. **A különbség azonban kicsi, és az alcsoportok nagyon kis
elemszámúak** (a legkevesebbet alvók csoportjában mindössze {A['ao_alatt6_n']} ember
van). Ebből komoly következtetést nem vonok le — tendenciaként érdemes kezelni.

![Alvás és önértékelés](diagramok/18_alvas_onertekeles.png)

### Amit meg akartam nézni, de nem lehetett

Eredetileg a **sportolás és az önértékelés** kapcsolatát terveztem központi
összefüggésnek. Az adatok ezt nem tették lehetővé:

| Sportolási gyakoriság | Válaszadó | Átlagos önértékelés |
|---|---|---|
{sp_sorok}
A válaszadók {A['sport_naponta_fo']}-en egyetlen kategóriába (szinte naponta) estek,
a többi három csoportban összesen 1–2 ember van. **Ekkora alcsoportokból nem lehet
átlagot értelmezni**: egyetlen ember válasza az egész csoportátlagot eltolja. Ezért
ezt az összefüggést nem ábrázoltam diagramon, és nem is építettem rá következtetést.

Ez maga is tanulság: egy homogén minta bizonyos kérdésekre egyszerűen nem tud
válaszolni, mert nincs benne elég változatosság.

---

## 6. Tájékozódás

{inf_lista}
A **{A['info_elso'].lower()}** vezet ({A['info_elso_fo']} fő), de a kép kiegyensúlyozottabb,
mint amire számítottam: **orvostól vagy szakembertől {A['info_orvos_fo']} ember**
tájékozódik, és senki nem jelölte, hogy sehonnan.

Ez fontos árnyalat. A közösségi média valóban a leggyakoribb forrás, de nem kizárólagos:
a válaszadók többsége több forrásból is tájékozódik, és a szakmai források is jelen
vannak. A forráskritika tehát továbbra is fontos, de a helyzet nem olyan rossz, mint a
téma szokásos beállítása sugallja.

![Információforrás](diagramok/15_informacioforras.png)

---

## 7. Változtatási hajlandóság

**{A['valtoztat_fo']} fő ({A['valtoztat_sz']}%) szeretne változtatni** az életmódján,
közülük {A['valtoztat_nem_tudja_fo']} nem tudja, hol kezdje.
**{A['valtoztat_elegedett_fo']} fő ({A['valtoztat_elegedett_sz']}%) elégedett** a
jelenlegi életmódjával — ami ebben az aktív mintában nem meglepő.

![Változtatás](diagramok/16_valtoztatas.png)

---

## 8. Következtetések

1. **A minta lényegesen egészségesebben él, mint vártam.**
   {A['sport_gyakori_sz']}% mozog legalább heti háromszor, {A['viz_sok_sz']}% iszik
   elég vizet, majdnem mindenki rendszeresen reggelizik, és az átlagos önértékelés
   {A['onertekeles_atlag']}. A kiinduló feltételezésem, hogy a fiatalok általánosan
   rosszul élnek, ebben a körben **nem igazolódott**.

2. **A zöldség- és gyümölcsfogyasztás önálló vakfolt.** {N} emberből
   {A['zoldseg_sok_fo']} közelíti meg az ajánlott mennyiséget. Ez azért figyelemre
   méltó, mert ugyanezek az emberek minden más táplálkozási kérdésben jól teljesítenek.

3. **Az alvás a másik vakfolt.** A minta {A['alvas_keves_sz']}%-a 7 óránál kevesebbet
   alszik. A jó szokások — sport, víz, reggeli — **nem kompenzálják** az alváshiányt.

4. **A képernyőidő és a rendszeres fáradtság szorosan együtt jár.** 4 óra alatt
   {A['kep_also_faradt_sz']}%, 4 óra felett {A['kep_felso_faradt_sz']}% a rendszeresen
   fáradtak aránya. Ez a felmérés legmarkánsabb eredménye — de együttjárás, nem
   bizonyított okozat.

5. **A tájékozódás kiegyensúlyozottabb a vártnál.** A közösségi média vezet, de a
   szakmai források is jelen vannak, és senki nem tájékozódik sehonnan.

6. **A többség változtatna**, ugyanakkor {A['valtoztat_elegedett_fo']} ember elégedett.
   Vagyis nem egyetlen üzenet kell, hanem kettő: az elégedetteknek a két vakfolt
   (alvás, zöldség) megmutatása, a változtatni akaróknak konkrét első lépés.

---

## 9. Javaslatok

A felmérés eredményeiből következően a javaslataim **nem az egész életmód
átalakítására** irányulnak — erre ebben a körben nincs is szükség —, hanem a két
azonosított vakfoltra és a képernyőidőre:

| Terület | Miért ez? | Javasolt első lépés |
|---|---|---|
| **Zöldség, gyümölcs** | {N} emberből csak {A['zoldseg_sok_fo']} éri el az ajánlást | Napi 1 gyümölcs a táskába; a menzán a saláta elsőként |
| **Alvás** | a minta {A['alvas_keves_sz']}%-a 7 óra alatt alszik | Fix lefekvési idő hétvégén is; koffeinstop délután 4 után |
| **Képernyőidő** | 4 óra felett {A['kep_felso_faradt_sz']}% a rendszeres fáradtság | Lefekvés előtt 30 perccel a telefon félretétele |
| **Cukros üdítő** | {A['udito_naponta_fo']} ember naponta iszik | A nap első felében víz az üdítő helyett |
| **Tájékozódás** | a közösségi média a leggyakoribb forrás | Három kérdés minden tanács előtt: ki mondja, mire hivatkozik, mit akar eladni? |

Ezek a javaslatok kerültek be a projekt weboldalának almenüibe és a prezentáció
záró szakaszába.

---

*Ez a dokumentum az `eszkozok/elemzes_szoveg.py` szkripttel, az `osszesites.json`
adataiból automatikusan generálódott. Kézzel szerkeszteni nem érdemes: új adat esetén
felülíródik.*
"""

with open(KIMENET, "w", encoding="utf-8") as f:
    f.write(szoveg)
print("Elkészült:", os.path.relpath(KIMENET, GYOKER))
