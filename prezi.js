/* Egészséges életmód – prezentáció
   IKT Projektmunka I. · Gerecze Ádám · 2026
   Generálás: pptxgenjs */

const pptxgen = require("pptxgenjs");
const fs = require("fs");
const path = require("path");

/* ---- A kérdőív adatainak betöltése ----------------------------------
   Minden szám az elemzés kimenetéből (osszesites.json) származik, így új
   kérdőívadat esetén elég újrafuttatni ezt a szkriptet.                */
const GYOKER = path.join(__dirname, "..");
const JSON_UT = path.join(GYOKER, "produktum", "kerdoiv", "osszesites.json");
if (!fs.existsSync(JSON_UT)) {
  console.error("Előbb futtasd az elemzést: python3 produktum/kerdoiv/elemzes.py");
  process.exit(1);
}
const O = JSON.parse(fs.readFileSync(JSON_UT, "utf-8"));
const D = O.szarmaztatott;
const N = O.kitoltok_szama;

// tizedesvessző a magyar helyesírás szerint
const tv = (x, t = 2) => Number(x).toFixed(t).replace(".", ",");
const kf = O.kepernyo_faradtsag;
const kfCimkek = Object.keys(kf);
const AO = O.alvas_onertekeles;
const aoCimkek = Object.keys(AO);
// magyar határozott névelő a szó kezdőhangja szerint
const nev = (sz) => ("aáeéiíoóöőuúüű".includes(String(sz)[0].toLowerCase()) ? "az" : "a");
const ABRA = path.join(__dirname, "abrak") + path.sep;

const P = new pptxgen();
P.layout = "LAYOUT_WIDE";           // 13.3" x 7.5"
P.author = "Gerecze Ádám";
P.company = "IKT Projektmunka I. – 1/13. Sz.";
P.title = "Egészséges életmód";
P.subject = "Osztályozó vizsga házi dolgozat";

const W = 13.3, H = 7.5;

const C = {
  sotet:  "14503B",
  zold:   "1F7A5C",
  vil:    "7FB89A",
  halv:   "E3F0E9",
  lime:   "A9CF46",
  korall: "D9594C",
  narancs:"E9873F",
  tinta:  "16241F",
  szurke: "5F6F68",
  feher:  "FFFFFF",
  keret:  "DCE6E1"
};

const FEJ = "Cambria";     // címek, nagy számok
const TXT = "Calibri";     // törzsszöveg

/* ============ DIAMINTÁK ============ */

P.defineSlideMaster({
  title: "VILAGOS",
  background: { color: C.feher },
  objects: [
    { rect: { x: 0, y: 7.06, w: W, h: 0.44, fill: { color: C.halv } } },
    { text: {
        text: "Egészséges életmód · IKT Projektmunka I.",
        options: { x: 0.62, y: 7.06, w: 6, h: 0.44, fontSize: 10, fontFace: TXT,
                   color: C.szurke, valign: "middle", isTextBox: true, margin: 0 } } },
    { text: {
        text: "Gerecze Ádám · 2026",
        options: { x: 6.7, y: 7.06, w: 6, h: 0.44, fontSize: 10, fontFace: TXT,
                   color: C.szurke, align: "right", valign: "middle", isTextBox: true, margin: 0 } } }
  ],
  slideNumber: { x: 12.72, y: 7.06, w: 0.5, h: 0.44, fontSize: 10, fontFace: TXT,
                 color: C.zold, align: "right", valign: "middle" }
});

P.defineSlideMaster({
  title: "SOTET",
  background: { color: C.sotet },
  objects: [
    { text: {
        text: "Egészséges életmód · IKT Projektmunka I.",
        options: { x: 0.62, y: 7.06, w: 6, h: 0.44, fontSize: 10, fontFace: TXT,
                   color: "8FB0A1", valign: "middle", isTextBox: true, margin: 0 } } }
  ],
  slideNumber: { x: 12.72, y: 7.06, w: 0.5, h: 0.44, fontSize: 10, fontFace: TXT,
                 color: C.lime, align: "right", valign: "middle" }
});

/* ============ SEGÉDFÜGGVÉNYEK ============ */

function cim(s, szoveg, rovat) {
  if (rovat) {
    s.addText(rovat.toUpperCase(), { x: 0.62, y: 0.42, w: 8, h: 0.28, fontSize: 11,
      fontFace: TXT, bold: true, color: C.zold, charSpacing: 2, isTextBox: true, margin: 0 });
  }
  s.addText(szoveg, { x: 0.62, y: rovat ? 0.74 : 0.55, w: 12.1, h: 0.85, fontSize: 32,
    fontFace: FEJ, bold: true, color: C.sotet, valign: "top", isTextBox: true, margin: 0 });
}

function mintajel(s, x, y) {
  s.addShape(P.ShapeType.roundRect, { x: x, y: y, w: 1.35, h: 0.34,
    fill: { color: C.halv }, rectRadius: 0.17, line: { color: C.halv } });
  s.addText(`saját adat · n=${N}`, { x: x, y: y, w: 1.35, h: 0.34, fontSize: 8.5,
    fontFace: TXT, color: C.zold, bold: true, align: "center", valign: "middle",
    isTextBox: true, margin: 0 });
}

function statKartya(s, x, y, w, szam, leiras, szin) {
  s.addShape(P.ShapeType.roundRect, { x: x, y: y, w: w, h: 2.15,
    fill: { color: C.feher }, line: { color: C.keret, width: 1 }, rectRadius: 0.12 });
  s.addText(szam, { x: x + 0.22, y: y + 0.22, w: w - 0.44, h: 0.95, fontSize: 40,
    fontFace: FEJ, bold: true, color: szin || C.sotet, valign: "middle", isTextBox: true, margin: 0 });
  s.addText(leiras, { x: x + 0.22, y: y + 1.16, w: w - 0.44, h: 0.85, fontSize: 12.5,
    fontFace: TXT, color: C.szurke, valign: "top", isTextBox: true, margin: 0 });
}

function korSzam(s, x, y, n, szin) {
  s.addShape(P.ShapeType.ellipse, { x: x, y: y, w: 0.5, h: 0.5, fill: { color: szin || C.halv } });
  s.addText(String(n), { x: x, y: y, w: 0.5, h: 0.5, fontSize: 16, fontFace: FEJ, bold: true,
    color: szin === C.sotet ? C.lime : C.sotet, align: "center", valign: "middle",
    isTextBox: true, margin: 0 });
}

const DIAGRAM_ALAP = () => ({
  chartColors: [C.zold],
  showLegend: false,
  showValue: true,
  dataLabelPosition: "outEnd",
  dataLabelFontSize: 12,
  dataLabelFontFace: TXT,
  dataLabelColor: C.tinta,
  catAxisLabelColor: C.szurke,
  catAxisLabelFontSize: 11.5,
  catAxisLabelFontFace: TXT,
  valAxisLabelColor: C.szurke,
  valAxisLabelFontSize: 10,
  valAxisLabelFontFace: TXT,
  valGridLine: { color: "EDF2EF", size: 1 },
  catGridLine: { style: "none" },
  valAxisHidden: true,
  barGapWidthPct: 55
});

/* =========================================================
   1. CÍMDIA
   ========================================================= */
let s = P.addSlide({ masterName: "SOTET" });
s.addShape(P.ShapeType.ellipse, { x: 9.6, y: -1.5, w: 6.2, h: 6.2,
  fill: { color: C.zold, transparency: 55 }, line: { color: C.zold, transparency: 100 } });
s.addShape(P.ShapeType.ellipse, { x: 11.1, y: 3.2, w: 3.4, h: 3.4,
  fill: { color: C.lime, transparency: 82 }, line: { color: C.lime, transparency: 100 } });

s.addText("OSZTÁLYOZÓ VIZSGA HÁZI DOLGOZAT", { x: 0.9, y: 1.55, w: 8, h: 0.3, fontSize: 12,
  fontFace: TXT, bold: true, color: C.lime, charSpacing: 2.5, isTextBox: true, margin: 0 });
s.addText("Egészséges életmód", { x: 0.9, y: 2.0, w: 9.2, h: 1.25, fontSize: 54,
  fontFace: FEJ, bold: true, color: C.feher, isTextBox: true, margin: 0 });
s.addText(`Mit mutat ${N} fiatal válasza arról, hogyan élnek?`, { x: 0.9, y: 3.25, w: 8.4, h: 0.55,
  fontSize: 19, fontFace: TXT, italic: true, color: "C6DDD2", isTextBox: true, margin: 0 });
s.addShape(P.ShapeType.rect, { x: 0.9, y: 4.15, w: 1.4, h: 0.05, fill: { color: C.lime } });
s.addText([
  { text: "Gerecze Ádám\n", options: { bold: true, fontSize: 17, color: C.feher } },
  { text: "IKT Projektmunka I. · 1/13. Sz. évfolyam\n", options: { fontSize: 13, color: "9DBBAE" } },
  { text: "2026. augusztus 28.", options: { fontSize: 13, color: "9DBBAE" } }
], { x: 0.9, y: 4.5, w: 7, h: 1.3, fontFace: TXT, isTextBox: true, margin: 0 });
s.addNotes(`Köszöntés. Bemutatkozás. A projekt témája az egészséges életmód. A fő kérdés az volt: mennyire élnek egészségesen a körülöttem lévő fiatalok, és hol maradnak el az ajánlásoktól. ${N} ember töltötte ki a kérdőívemet. A prezentáció kb. 8 perc lesz.`);

/* =========================================================
   2. A PROJEKTRŐL
   ========================================================= */
s = P.addSlide({ masterName: "VILAGOS" });
cim(s, "A projekt kerete", "Bevezetés");
const projInfo = [
  ["Cél", "Felmérni a 14–19 évesek életmódbeli szokásait, és a saját adatokra épülő, gyakorlati útmutatót adni azoknak, akik változtatnának."],
  ["Célközönség", "14–19 éves középiskolások, valamint az őket tanító pedagógusok és a szülők."],
  ["Kutatási kérdés", "Mennyire élnek egészségesen a körülöttem lévő fiatalok, és melyek azok a területek, ahol elmaradnak az ajánlásoktól?"],
  ["Munkaforma", "Önálló munka. A csoportbeosztás során nem alakult ki több fős csapat, ezért a projekt minden elemét egyedül készítettem el."]
];
let yy = 1.95;
projInfo.forEach(function (sor, i) {
  korSzam(s, 0.62, yy - 0.06, i + 1, i === 3 ? C.sotet : C.halv);
  s.addText(sor[0], { x: 1.3, y: yy - 0.08, w: 2.4, h: 0.35, fontSize: 15, fontFace: FEJ,
    bold: true, color: C.sotet, isTextBox: true, margin: 0 });
  s.addText(sor[1], { x: 3.75, y: yy - 0.1, w: 8.9, h: 0.95, fontSize: 13.5, fontFace: TXT,
    color: C.szurke, isTextBox: true, margin: 0 });
  yy += 1.22;
});
s.addNotes("A projekt célja nem az volt, hogy általánosságban beszéljek az egészségről, hanem hogy saját adatot gyűjtsek. A negyedik pont fontos: önállóan dolgoztam, mert a csoportbeosztásnál nem alakult ki csapat — így a tervezés, a kérdőív, a weboldal, az elemzés és a prezentáció is a saját munkám.");

/* =========================================================
   3. MIÉRT EZ A TÉMA?
   ========================================================= */
s = P.addSlide({ masterName: "VILAGOS" });
cim(s, "Négy szám, ami átírta a projektet", "Az eredmény");
s.addText(`Ezek a saját felmérésem adatai: ${N} konkrét ember válaszai a környezetemből. Nem azt mutatták, amire számítottam.`,
  { x: 0.62, y: 1.68, w: 11.6, h: 0.5, fontSize: 13.5, fontFace: TXT, color: C.szurke,
    isTextBox: true, margin: 0 });
statKartya(s, 0.62, 2.4, 2.9, D.sport_gyakori_sz + "%", "mozog legalább heti három alkalommal", C.zold);
statKartya(s, 3.72, 2.4, 2.9, D.viz_sok_sz + "%", "iszik naponta legalább 5 pohár vizet", C.zold);
statKartya(s, 6.82, 2.4, 2.9, D.zoldseg_sok_fo + " fő", `eszik napi 4-szer zöldséget – a ${N}-ből`, C.korall);
statKartya(s, 9.92, 2.4, 2.9, D.alvas_keves_sz + "%", "alszik 7 óránál kevesebbet", C.korall);
s.addShape(P.ShapeType.roundRect, { x: 0.62, y: 5.0, w: 12.2, h: 1.5,
  fill: { color: C.halv }, line: { color: C.halv }, rectRadius: 0.12 });
s.addText([
  { text: "Az első kettő zöld, a másik kettő piros.  ", options: { bold: true, color: C.sotet, fontSize: 15 } },
  { text: `Ez a minta sportol, vizet iszik és reggelizik — sokkal jobban, mint amire számítottam. Mégis van két terület, ahol majdnem mindenki elmarad: a zöldségfogyasztás és az alvás. Ez a két vakfolt lett a projekt fő témája.`,
    options: { color: C.tinta, fontSize: 14 } }
], { x: 0.95, y: 5.15, w: 11.5, h: 1.2, fontFace: TXT, isTextBox: true, margin: 0, valign: "middle" });
s.addNotes(`Ez a dia a projekt fordulópontja. Azzal a feltételezéssel indultam, hogy a fiatalok általánosan rosszul élnek. Az adat ezt megcáfolta: ${D.sport_gyakori_sz} százalék mozog rendszeresen, ${D.viz_sok_sz} százalék iszik elég vizet. Két területen viszont majdnem mindenki elmarad: a zöldségfogyasztásban — ${N} emberből ${D.zoldseg_sok_fo} éri el az ajánlást — és az alvásban. Ezért írtam át az egész produktumot erre a két vakfoltra.`);

/* =========================================================
   4. MÓDSZERTAN
   ========================================================= */
s = P.addSlide({ masterName: "VILAGOS" });
cim(s, "Hogyan készült a felmérés?", "Módszertan");
const lepesek = [
  ["Kérdőív összeállítása", "16 kérdés öt témakörben, Google Űrlapokban"],
  ["Megosztás", "anonim online link, osztálycsoport és ismerősök"],
  ["Adatgyűjtés", `2026. augusztus, összesen ${N} kitöltő`],
  ["Feldolgozás", "CSV export, majd Python (pandas, matplotlib)"],
  ["Megjelenítés", "18 diagram, weboldal és prezentáció"]
];
let ly = 1.95;
lepesek.forEach(function (l, i) {
  korSzam(s, 0.62, ly, i + 1);
  s.addText(l[0], { x: 1.3, y: ly - 0.04, w: 3.6, h: 0.32, fontSize: 14.5, fontFace: FEJ,
    bold: true, color: C.sotet, isTextBox: true, margin: 0 });
  s.addText(l[1], { x: 1.3, y: ly + 0.27, w: 5.6, h: 0.32, fontSize: 12.5, fontFace: TXT,
    color: C.szurke, isTextBox: true, margin: 0 });
  ly += 0.92;
});
s.addShape(P.ShapeType.roundRect, { x: 7.5, y: 1.95, w: 5.2, h: 2.35,
  fill: { color: "FCEEEC" }, line: { color: "FCEEEC" }, rectRadius: 0.12 });
s.addText("A minta korlátai", { x: 7.85, y: 2.15, w: 4.5, h: 0.35, fontSize: 15, fontFace: FEJ,
  bold: true, color: "A8382B", isTextBox: true, margin: 0 });
s.addText(`A felmérés nem reprezentatív. Kényelmi mintavétellel készült, ${N} fővel, a saját ismeretségi körömből. Ez itt különösen fontos: a minta feltűnően sportos (${D.sport_gyakori_fo} fő mozog legalább heti háromszor), ami valószínűleg az én környezetemre jellemző, nem a korosztályra.`,
  { x: 7.85, y: 2.55, w: 4.5, h: 1.6, fontSize: 12.5, fontFace: TXT, color: "7A2B22",
    isTextBox: true, margin: 0 });
s.addShape(P.ShapeType.roundRect, { x: 7.5, y: 4.5, w: 5.2, h: 2.0,
  fill: { color: C.halv }, line: { color: C.halv }, rectRadius: 0.12 });
s.addText("Miért Python és nem Excel?", { x: 7.85, y: 4.7, w: 4.5, h: 0.35, fontSize: 15,
  fontFace: FEJ, bold: true, color: C.sotet, isTextBox: true, margin: 0 });
s.addText("Az elemzést szkriptbe írtam, így egyetlen futtatással frissül mind a 18 diagram. A számokat egy JSON állomány köti össze, amelyből a weboldal és ez a prezentáció is dolgozik — így nem tudnak eltérni egymástól.",
  { x: 7.85, y: 5.1, w: 4.5, h: 1.3, fontSize: 12.5, fontFace: TXT, color: C.tinta,
    isTextBox: true, margin: 0 });
s.addNotes("A kérdőívet Google Űrlapokban készítettem, az elemzést viszont nem Excelben, hanem Python szkripttel. Ennek az az előnye, hogy újrafuttatható. Fontos kiemelni: a minta nem reprezentatív, 24 fő a saját környezetemből — ezt minden eredménynél hangsúlyozom.");

/* =========================================================
   5. TÁPLÁLKOZÁS
   ========================================================= */
s = P.addSlide({ masterName: "VILAGOS" });
cim(s, "Táplálkozás: egyetlen gyenge pont", "Eredmények · 1");
s.addChart(P.ChartType.bar, [{
  name: "Fő", labels: ["Egyszer sem", "1×", "2–3×", "4× vagy több"],
  values: [O.zoldseg_gyumolcs["Egyszer sem"], O.zoldseg_gyumolcs["1 alkalommal"],
           O.zoldseg_gyumolcs["2–3 alkalommal"], O.zoldseg_gyumolcs["4 vagy több alkalommal"]]
}], Object.assign(DIAGRAM_ALAP(), {
  x: 0.62, y: 1.9, w: 6.6, h: 3.6,
  chartColors: [C.korall, C.narancs, C.vil, C.zold],
  varyColors: true,
  showTitle: true, title: "Napi zöldség- és gyümölcsfogyasztás (fő)",
  titleFontSize: 14, titleFontFace: TXT, titleColor: C.sotet
}));
mintajel(s, 0.62, 5.62);
s.addImage({ path: ABRA + "tanyer.png", x: 7.55, y: 1.95, w: 3.05, h: 2.46 });
s.addText("A tányérmodell: a tányér fele zöldség és gyümölcs. A WHO ajánlása napi 400 g, kb. 5 adag.",
  { x: 10.75, y: 2.05, w: 2.1, h: 2.2, fontSize: 12, fontFace: TXT, color: C.szurke,
    isTextBox: true, margin: 0 });
s.addShape(P.ShapeType.roundRect, { x: 7.55, y: 4.6, w: 5.25, h: 1.9,
  fill: { color: C.halv }, line: { color: C.halv }, rectRadius: 0.12 });
s.addText([
  { text: `${N} emberből ${D.zoldseg_sok_fo}.\n`, options: { bold: true, fontSize: 17, color: C.sotet, breakLine: true } },
  { text: `Ennyien közelítik meg az ajánlott zöldség-gyümölcs mennyiséget. Közben ${D.viz_sok_fo}-en isznak elég vizet, ${D.udito_ritkan_fo}-en ritkán vagy soha nem üdítőznek, és ${D.reggeli_rendszeres_fo}-en rendszeresen reggeliznek. A zöldség önálló vakfolt.`,
    options: { fontSize: 12.5, color: C.tinta } }
], { x: 7.9, y: 4.78, w: 4.6, h: 1.6, fontFace: TXT, isTextBox: true, margin: 0 });
s.addNotes(`A táplálkozásnál egyetlen gyenge pont van. A víz, az üdítő és a reggeli mind rendben: ${D.viz_sok_fo} ember iszik elég vizet, ${D.udito_ritkan_fo} ritkán vagy soha nem üdítőzik, ${D.reggeli_rendszeres_fo} rendszeresen reggelizik. A zöldségnél viszont ${N} emberből ${D.zoldseg_sok_fo} éri el az ajánlott mennyiséget. Ez azért érdekes, mert ugyanezek az emberek minden más kérdésben jól teljesítenek — vagyis nem általános igénytelenségről van szó, hanem egy konkrét vakfoltról.`);

/* =========================================================
   6. MOZGÁS
   ========================================================= */
s = P.addSlide({ masterName: "VILAGOS" });
cim(s, "Mozgás: a minta legerősebb területe", "Eredmények · 2");
s.addChart(P.ChartType.bar, [{
  name: "Fő",
  labels: ["Szinte naponta", "Heti 3–4×", "Heti 1–2×", "Szinte soha"],
  values: [O.sport["Szinte naponta"], O.sport["Hetente 3–4 alkalommal"],
           O.sport["Hetente 1–2 alkalommal"], O.sport["Szinte soha"]]
}], Object.assign(DIAGRAM_ALAP(), {
  x: 0.62, y: 1.9, w: 7.0, h: 3.7,
  chartColors: [C.zold, C.vil, C.narancs, C.korall],
  varyColors: true,
  showTitle: true, title: "Testmozgás gyakorisága a testnevelési órán kívül (fő)",
  titleFontSize: 14, titleFontFace: TXT, titleColor: C.sotet
}));
mintajel(s, 0.62, 5.7);
s.addImage({ path: ABRA + "mozgas-piramis.png", x: 8.0, y: 1.9, w: 2.55, h: 1.89 });
s.addText("A piramis alja a hétköznapi mozgás: séta, lépcső, bicikli. Ehhez nem kell terem és nem kell tagdíj.",
  { x: 10.7, y: 2.0, w: 2.15, h: 1.8, fontSize: 12, fontFace: TXT, color: C.szurke,
    isTextBox: true, margin: 0 });
s.addShape(P.ShapeType.roundRect, { x: 8.0, y: 4.05, w: 4.85, h: 2.4,
  fill: { color: C.sotet }, line: { color: C.sotet }, rectRadius: 0.12 });
s.addText([
  { text: `De ez nem véd meg mindentől\n`, options: { bold: true, fontSize: 16, color: C.lime, breakLine: true } },
  { text: `A válaszadók ${D.sport_gyakori_sz}%-a mozog legalább heti háromszor — mégis ${D.faradt_rendszeres_fo} ember (${D.faradt_rendszeres_sz}%) érzi magát legalább hetente többször fáradtnak. A sport önmagában nem pótolja az alvást.\n\n`,
    options: { fontSize: 12.5, color: "D6EDE2" } },
  { text: `A legnépszerűbb mozgásforma a ${D.mozgas_elso.toLowerCase()} volt (${D.mozgas_elso_fo} fő).`,
    options: { fontSize: 12, italic: true, color: "9DBBAE" } }
], { x: 8.35, y: 4.22, w: 4.2, h: 2.1, fontFace: TXT, isTextBox: true, margin: 0 });
s.addNotes(`Ez a minta legerősebb területe: ${D.sport_gyakori_fo} ember mozog legalább heti háromszor, ${D.sport_naponta_fo} szinte naponta. Ez viszont egyben a minta torzítását is mutatja — valószínűleg az én ismeretségi köröm sportosabb az átlagnál. A jobb oldali doboz a lényeg: hiába mozognak ennyien, ${D.faradt_rendszeres_fo} ember rendszeresen fáradt. A sport önmagában nem pótolja az alvást.`);

/* =========================================================
   7. FŐ EREDMÉNY – KÉPERNYŐ ÉS FÁRADTSÁG (sötét)
   ========================================================= */
s = P.addSlide({ masterName: "SOTET" });
s.addText("A FELMÉRÉS FŐ EREDMÉNYE", { x: 0.62, y: 0.42, w: 8, h: 0.28, fontSize: 11,
  fontFace: TXT, bold: true, color: C.lime, charSpacing: 2.5, isTextBox: true, margin: 0 });
s.addText("Képernyőidő és rendszeres fáradtság", { x: 0.62, y: 0.74, w: 12.1, h: 0.8, fontSize: 32,
  fontFace: FEJ, bold: true, color: C.feher, isTextBox: true, margin: 0 });
s.addChart(P.ChartType.bar, [
  { name: "Összes válaszadó", labels: kfCimkek, values: kfCimkek.map((k) => kf[k].osszes) },
  { name: "Ebből: legalább hetente többször fáradt", labels: kfCimkek, values: kfCimkek.map((k) => kf[k].faradt) }
], {
  x: 0.62, y: 1.85, w: 7.4, h: 4.35,
  chartColors: ["5C8F79", C.narancs],
  showLegend: true, legendPos: "t", legendFontSize: 12, legendColor: "C6DDD2", legendFontFace: TXT,
  showValue: true, dataLabelPosition: "outEnd", dataLabelFontSize: 12,
  dataLabelFontFace: TXT, dataLabelColor: C.feher,
  catAxisLabelColor: "C6DDD2", catAxisLabelFontSize: 12, catAxisLabelFontFace: TXT,
  valAxisHidden: true, valGridLine: { style: "none" }, catGridLine: { style: "none" },
  barGapWidthPct: 45
});
s.addShape(P.ShapeType.roundRect, { x: 8.4, y: 1.85, w: 4.4, h: 2.15,
  fill: { color: C.korall }, line: { color: C.korall }, rectRadius: 0.12 });
s.addText(`${D.kep_also_faradt_sz}%  →  ${D.kep_felso_faradt_sz}%`,
  { x: 8.72, y: 2.02, w: 3.8, h: 0.72, fontSize: 32, bold: true,
    color: C.feher, fontFace: FEJ, valign: "middle", isTextBox: true, margin: 0 });
s.addText(`A napi 4 óránál kevesebbet képernyőzők közül ${D.kep_also_faradt_fo} fő a ${D.kep_also_fo}-ből fáradt rendszeresen. A 4 óránál többet képernyőzők közül ${D.kep_felso_faradt_fo} a ${D.kep_felso_fo}-ből.`,
  { x: 8.72, y: 2.8, w: 3.8, h: 1.05, fontSize: 12.5, color: "FDE7E4", fontFace: TXT,
    isTextBox: true, margin: 0 });
s.addShape(P.ShapeType.roundRect, { x: 8.4, y: 4.25, w: 4.4, h: 1.95,
  fill: { color: "1C6449" }, line: { color: "1C6449" }, rectRadius: 0.12 });
s.addText([
  { text: "Amit ebből NEM állítok\n", options: { fontSize: 14, bold: true, color: C.lime, fontFace: FEJ, breakLine: true } },
  { text: `Ez együttjárás, nem bizonyított ok-okozat. Lehet, hogy a képernyőzés fáraszt — de az is, hogy a fáradt ember választja a passzív képernyőzést. A két szélső kategóriában ráadásul csak 1, illetve 2 válaszadó van.`,
    options: { fontSize: 12, color: "C6DDD2", fontFace: TXT } }
], { x: 8.72, y: 4.4, w: 3.8, h: 1.7, isTextBox: true, margin: 0 });
s.addNotes(`Ez a felmérés legmarkánsabb eredménye, ezért kapott külön diát. A napi négy óránál kevesebbet képernyőzők közül ${D.kep_also_faradt_sz} százalék fáradt rendszeresen, a négy óránál többet képernyőzők közül ${D.kep_felso_faradt_sz} százalék. A trend monoton emelkedő. A jobb alsó doboz szándékosan van itt: nagyon fontos, hogy ezt együttjárásként és ne ok-okozatként mutassam be. A két szélső kategóriában ráadásul csak egy-két ember van, tehát a középső két oszlop összehasonlítása a megbízhatóbb.`);

/* =========================================================
   8. ALVÁS
   ========================================================= */
s = P.addSlide({ masterName: "VILAGOS" });
cim(s, "Alvás: a második vakfolt", "Eredmények · 3");
s.addChart(P.ChartType.doughnut, [{
  name: "Fő", labels: ["8 óránál többet", "7–8 órát", "6–7 órát", "6 óránál kevesebbet"],
  values: [O.alvas["8 óránál többet"], O.alvas["7–8 órát"],
           O.alvas["6–7 órát"], O.alvas["6 óránál kevesebbet"]]
}], {
  x: 0.4, y: 1.85, w: 5.6, h: 4.3, holeSize: 52,
  chartColors: [C.zold, C.vil, C.narancs, C.korall],
  showLegend: true, legendPos: "b", legendFontSize: 12, legendFontFace: TXT, legendColor: C.tinta,
  showValue: false, showPercent: true, dataLabelFontSize: 12, dataLabelColor: C.feher,
  dataLabelFontFace: TXT, dataLabelFontBold: true,
  showTitle: true, title: "Alvásidő iskolai éjszakán (fő)",
  titleFontSize: 14, titleFontFace: TXT, titleColor: C.sotet
});
s.addImage({ path: ABRA + "alvasciklus.png", x: 6.25, y: 1.95, w: 4.3, h: 2.44 });
s.addText(`Az ajánlott 8 órát ${N} emberből ${D.alvas_ajanlott_fo} éri el. A mély alvás az éjszaka első felére esik, ezért nem pótolható hétvégi hosszú alvással.`,
  { x: 10.7, y: 2.1, w: 2.15, h: 2.4, fontSize: 12, fontFace: TXT, color: C.szurke,
    isTextBox: true, margin: 0 });
s.addShape(P.ShapeType.roundRect, { x: 6.25, y: 4.75, w: 3.1, h: 1.7,
  fill: { color: C.feher }, line: { color: C.keret }, rectRadius: 0.12 });
s.addText(D.alvas_keves_fo + " fő", { x: 6.55, y: 4.92, w: 2.6, h: 0.5, fontSize: 26, bold: true,
  color: C.korall, fontFace: FEJ, valign: "middle", isTextBox: true, margin: 0 });
s.addText(`alszik 7 óránál kevesebbet — a minta ${D.alvas_keves_sz}%-a`, { x: 6.55, y: 5.46, w: 2.6, h: 0.85,
  fontSize: 12, color: C.szurke, fontFace: TXT, isTextBox: true, margin: 0 });
s.addShape(P.ShapeType.roundRect, { x: 9.55, y: 4.75, w: 3.25, h: 1.7,
  fill: { color: C.feher }, line: { color: C.keret }, rectRadius: 0.12 });
s.addText(D.energiaital_soha_fo + " fő", { x: 9.85, y: 4.92, w: 2.7, h: 0.5, fontSize: 26, bold: true,
  color: C.zold, fontFace: FEJ, valign: "middle", isTextBox: true, margin: 0 });
s.addText("soha nem iszik energiaitalt, és napi fogyasztó nincs a mintában",
  { x: 9.85, y: 5.46, w: 2.7, h: 0.85, fontSize: 12, color: C.szurke, fontFace: TXT,
    isTextBox: true, margin: 0 });
mintajel(s, 0.62, 6.5);
s.addNotes(`A korosztálynak nyolc-tíz óra alvás lenne az ajánlott. Ezt ${N} emberből ${D.alvas_ajanlott_fo} érte el, és ${D.alvas_keves_fo} ember hét óránál is kevesebbet alszik. Ez a második vakfolt. Az energiaitalnál viszont jó hírem van: ${D.energiaital_soha_fo} ember soha nem iszik ilyet, és napi fogyasztó egyáltalán nincs a mintában. Vagyis a fáradtság oka nem a koffein, hanem valószínűleg az alvás és a képernyőidő.`);

/* =========================================================
   9. AKADÁLYOK
   ========================================================= */
s = P.addSlide({ masterName: "VILAGOS" });
cim(s, "Alvás és önértékelés", "Eredmények · 4");
s.addChart(P.ChartType.bar, [{
  name: "Átlagos önértékelés",
  labels: aoCimkek.map((k) => `${k} (n=${AO[k].n})`),
  values: aoCimkek.map((k) => AO[k].atlag)
}], Object.assign(DIAGRAM_ALAP(), {
  x: 0.62, y: 1.9, w: 7.5, h: 4.3,
  chartColors: [C.zold, C.vil, C.narancs, C.korall],
  varyColors: true,
  dataLabelFormatCode: "0.00",
  catAxisLabelFontSize: 11,
  showTitle: true, title: "Egészség-önértékelés (1–5) az alvásmennyiség szerint",
  titleFontSize: 14, titleFontFace: TXT, titleColor: C.sotet
}));
mintajel(s, 0.62, 6.3);
s.addShape(P.ShapeType.roundRect, { x: 8.5, y: 1.9, w: 4.3, h: 2.5,
  fill: { color: C.halv }, line: { color: C.halv }, rectRadius: 0.12 });
s.addText([
  { text: "A tendencia jó irányba mutat\n", options: { fontSize: 15, bold: true, color: C.sotet, fontFace: FEJ, breakLine: true } },
  { text: `Aki többet alszik, magasabbra értékeli a saját egészségét. A különbség azonban kicsi, és az alcsoportok nagyon kis elemszámúak — a legkevesebbet alvók között mindössze ${AO["6 óránál kevesebbet"].n} ember van.`,
    options: { fontSize: 12.5, color: C.tinta, fontFace: TXT } }
], { x: 8.82, y: 2.08, w: 3.7, h: 2.2, isTextBox: true, margin: 0 });
s.addShape(P.ShapeType.roundRect, { x: 8.5, y: 4.6, w: 4.3, h: 1.7,
  fill: { color: C.feher }, line: { color: C.keret }, rectRadius: 0.12 });
s.addText([
  { text: "Amit nem tudtam megvizsgálni\n", options: { fontSize: 14, bold: true, color: C.sotet, fontFace: FEJ, breakLine: true } },
  { text: `A sportolás és az önértékelés kapcsolatát terveztem fő összefüggésnek. Nem lehetett: ${D.sport_naponta_fo} ember egyetlen kategóriába esett, a többiben 1–2 fő van.`,
    options: { fontSize: 12.5, color: C.szurke, fontFace: TXT } }
], { x: 8.82, y: 4.78, w: 3.7, h: 1.4, isTextBox: true, margin: 0 });
s.addNotes(`Itt két dolgot mutatok. Egyrészt az alvás és az önértékelés kapcsolatát: aki többet alszik, magasabbra értékeli az egészségét — de a különbség kicsi, és az alcsoportok nagyon kicsik, ezért csak tendenciaként közlöm. Másrészt a jobb alsó dobozban azt, amit nem tudtam megvizsgálni. Eredetileg a sportolás és az önértékelés kapcsolatát terveztem fő összefüggésnek, de ${D.sport_naponta_fo} ember egyetlen kategóriába esett. Ekkora alcsoportokból nem lehet átlagot értelmezni, ezért inkább kihagytam.`);

/* =========================================================
   10. TÁJÉKOZÓDÁS
   ========================================================= */
s = P.addSlide({ masterName: "VILAGOS" });
const infCimkek = Object.keys(O.informacioforras).reverse();
cim(s, "Honnan tájékozódnak?", "Eredmények · 5");
s.addChart(P.ChartType.bar, [{
  name: "Fő",
  labels: infCimkek, values: infCimkek.map((k) => O.informacioforras[k])
}], Object.assign(DIAGRAM_ALAP(), {
  x: 0.62, y: 1.9, w: 7.5, h: 4.3,
  barDir: "bar",
  chartColors: infCimkek.map((k, i) =>
    i === infCimkek.length - 1 ? C.narancs : (k === "Sehonnan" ? C.vil : C.zold)),
  varyColors: true,
  catAxisLabelFontSize: 12,
  showTitle: true, title: "Információforrások egészségügyi kérdésekben (többválaszos)",
  titleFontSize: 14, titleFontFace: TXT, titleColor: C.sotet
}));
mintajel(s, 0.62, 6.3);
s.addShape(P.ShapeType.roundRect, { x: 8.5, y: 1.9, w: 4.3, h: 2.35,
  fill: { color: C.sotet }, line: { color: C.sotet }, rectRadius: 0.12 });
s.addText("Jobb a vártnál", { x: 8.82, y: 2.1, w: 3.7, h: 0.6, fontSize: 26, bold: true,
  color: C.lime, fontFace: FEJ, valign: "middle", isTextBox: true, margin: 0 });
s.addText(`${nev(D.info_elso)[0].toUpperCase() + nev(D.info_elso).slice(1)} ${D.info_elso.toLowerCase()} vezet (${D.info_elso_fo} fő), de orvostól is ${D.info_orvos_fo} ember tájékozódik, és senki nem jelölte, hogy sehonnan. A többség több forrásból is tájékozódik.`,
  { x: 8.82, y: 2.78, w: 3.7, h: 1.3, fontSize: 12.5, color: "C6DDD2", fontFace: TXT,
    isTextBox: true, margin: 0 });
s.addShape(P.ShapeType.roundRect, { x: 8.5, y: 4.45, w: 4.3, h: 1.85,
  fill: { color: "FCEEEC" }, line: { color: "FCEEEC" }, rectRadius: 0.12 });
s.addText([
  { text: "A kockázat azért megmarad\n", options: { fontSize: 14, bold: true, color: "A8382B", fontFace: FEJ, breakLine: true } },
  { text: "A platformokon terjedő étrend- és edzéstanácsok jelentős része ellenőrizetlen, gyakran valamit el akar adni. Három kérdés segít: ki mondja, mire hivatkozik, mit akar eladni?",
    options: { fontSize: 12, color: "7A2B22", fontFace: TXT } }
], { x: 8.82, y: 4.62, w: 3.7, h: 1.55, isTextBox: true, margin: 0 });
s.addNotes(`Itt is jobb a kép, mint amire számítottam. A közösségi média valóban vezet ${D.info_elso_fo} fővel, de orvostól is ${D.info_orvos_fo} ember tájékozódik, és senki nem jelölte, hogy sehonnan. A többség több forrásból tájékozódik. A kockázat azért megmarad, ezért került a weboldal forrásoldalára az a három kérdés: ki mondja, mire hivatkozik, mit akar eladni.`);

/* =========================================================
   11. KÖVETKEZTETÉSEK
   ========================================================= */
s = P.addSlide({ masterName: "VILAGOS" });
cim(s, "Hat következtetés", "Összegzés");
const kov = [
  ["Jobb a vártnál", `${D.sport_gyakori_sz}% mozog rendszeresen, ${D.viz_sok_sz}% iszik elég vizet. A kiinduló feltételezésem nem igazolódott.`, C.zold],
  ["Zöldség: vakfolt", `${N} emberből ${D.zoldseg_sok_fo} közelíti meg az ajánlott mennyiséget — miközben minden más táplálkozási kérdésben jól teljesítenek.`, C.korall],
  ["Alvás: vakfolt", `A minta ${D.alvas_keves_sz}%-a 7 óránál kevesebbet alszik. A jó szokások ezt nem kompenzálják.`, C.korall],
  ["Képernyő és fáradtság", `4 óra alatt ${D.kep_also_faradt_sz}%, 4 óra felett ${D.kep_felso_faradt_sz}% a rendszeresen fáradtak aránya.`, C.narancs],
  ["Kiegyensúlyozott tájékozódás", `A közösségi média vezet, de orvostól is ${D.info_orvos_fo} ember tájékozódik, és senki nem jelölte, hogy sehonnan.`, C.zold],
  ["Kétféle üzenet kell", `${D.valtoztat_fo} fő változtatna, ${D.valtoztat_elegedett_fo} viszont elégedett — nekik a két vakfoltot kell megmutatni.`, C.narancs]
];
kov.forEach(function (k, i) {
  const x = 0.62 + (i % 3) * 4.13;
  const y = 1.95 + Math.floor(i / 3) * 2.35;
  s.addShape(P.ShapeType.roundRect, { x: x, y: y, w: 3.85, h: 2.05,
    fill: { color: C.feher }, line: { color: C.keret, width: 1 }, rectRadius: 0.12 });
  s.addShape(P.ShapeType.ellipse, { x: x + 0.28, y: y + 0.26, w: 0.42, h: 0.42, fill: { color: k[2] } });
  s.addText(String(i + 1), { x: x + 0.28, y: y + 0.26, w: 0.42, h: 0.42, fontSize: 13,
    fontFace: FEJ, bold: true, color: C.feher, align: "center", valign: "middle",
    isTextBox: true, margin: 0 });
  s.addText(k[0], { x: x + 0.85, y: y + 0.26, w: 2.8, h: 0.42, fontSize: 15, fontFace: FEJ,
    bold: true, color: C.sotet, valign: "middle", isTextBox: true, margin: 0 });
  s.addText(k[1], { x: x + 0.28, y: y + 0.82, w: 3.3, h: 1.05, fontSize: 12.5, fontFace: TXT,
    color: C.szurke, isTextBox: true, margin: 0 });
});
s.addNotes("Összefoglalva hat pont. Az első a fő meglepetés: a minta jobban él, mint vártam. A második és a harmadik a két vakfolt. A negyedik a legmarkánsabb összefüggés. Az ötödik egy újabb jó hír. A hatodik pedig azt mondja meg, hogy nem egyetlen üzenet kell, hanem kettő.");

/* =========================================================
   12. JAVASLATOK
   ========================================================= */
s = P.addSlide({ masterName: "VILAGOS" });
cim(s, "Öt lépés, ami ma elkezdhető", "Javaslatok");
s.addText("A megkérdezettek nagy része már sportol, vizet iszik és reggelizik. Ezért nem életmódváltást javaslok, hanem öt apróságot — pont a két hiányzó területre.",
  { x: 0.62, y: 1.7, w: 11.8, h: 0.5, fontSize: 14, fontFace: TXT, color: C.szurke,
    isTextBox: true, margin: 0 });
s.addImage({ path: ABRA + "lepesek.png", x: 0.62, y: 3.0, w: 8.6, h: 3.11 });
s.addShape(P.ShapeType.roundRect, { x: 9.5, y: 2.55, w: 3.3, h: 3.55,
  fill: { color: C.halv }, line: { color: C.halv }, rectRadius: 0.12 });
s.addText([
  { text: "Miért ez az öt?\n\n", options: { fontSize: 15, bold: true, color: C.sotet, fontFace: FEJ, breakLine: true } },
  { text: "Kettő a zöldségre és az alvásra irányul — ez a két vakfolt. Egy a képernyőidőre, ami a fáradtsággal jár együtt.\n\n", options: { fontSize: 12.5, color: C.tinta, fontFace: TXT } },
  { text: "A „hétfőtől teljesen új életet kezdek” típusú tervek jellemzően a második héten elhalnak — és utána nehezebb újrakezdeni, mint el sem kezdeni.\n\n",
    options: { fontSize: 12.5, color: C.tinta, fontFace: TXT } },
  { text: "Egy kihagyott nap nem bukás. Két kihagyott hét már az.",
    options: { fontSize: 12.5, italic: true, color: C.zold, fontFace: TXT } }
], { x: 9.82, y: 2.75, w: 2.7, h: 3.2, isTextBox: true, margin: 0 });
s.addNotes("Mivel a megkérdezettek nagy része már sportol és vizet iszik, nem életmódváltást javaslok. Az öt lépésből kettő a zöldségre és az alvásra irányul — ez a két vakfolt —, egy pedig a képernyőidőre, ami a fáradtsággal jár együtt. Mindegyik egy döntés, nem egy program.");

/* =========================================================
   13. A PRODUKTUMOK
   ========================================================= */
s = P.addSlide({ masterName: "VILAGOS" });
cim(s, "Mi készült el a projektben?", "Produktum");
const prod = [
  ["Projektweboldal", "6 aloldal, Bootstrap 5.3, saját CSS és JavaScript, reszponzív, billentyűzettel is használható. Saját készítésű SVG ábrák.", "🌐"],
  ["Online kérdőív + elemzés", `16 kérdés, ${N} kitöltő, Google Űrlapok. Python (pandas, matplotlib) feldolgozás, 18 diagram, írásos elemzés.`, "📊"],
  ["Prezentáció", "18 dia, saját diaminta, egységes arculat, natív diagramok, animációk és áttűnések.", "🖥️"]
];
prod.forEach(function (p, i) {
  const x = 0.62 + i * 4.13;
  s.addShape(P.ShapeType.roundRect, { x: x, y: 1.95, w: 3.85, h: 3.0,
    fill: { color: C.feher }, line: { color: C.keret, width: 1 }, rectRadius: 0.12 });
  s.addShape(P.ShapeType.roundRect, { x: x + 0.3, y: 2.25, w: 0.7, h: 0.7,
    fill: { color: C.halv }, line: { color: C.halv }, rectRadius: 0.14 });
  s.addText(p[2], { x: x + 0.3, y: 2.25, w: 0.7, h: 0.7, fontSize: 20, align: "center",
    valign: "middle", isTextBox: true, margin: 0 });
  s.addText(p[0], { x: x + 0.3, y: 3.12, w: 3.3, h: 0.4, fontSize: 16, fontFace: FEJ,
    bold: true, color: C.sotet, isTextBox: true, margin: 0 });
  s.addText(p[1], { x: x + 0.3, y: 3.58, w: 3.3, h: 1.25, fontSize: 12.5, fontFace: TXT,
    color: C.szurke, isTextBox: true, margin: 0 });
});
s.addShape(P.ShapeType.roundRect, { x: 0.62, y: 5.2, w: 12.2, h: 1.3,
  fill: { color: C.sotet }, line: { color: C.sotet }, rectRadius: 0.12 });
s.addText([
  { text: "Mindez GitHub repositoryban:  ", options: { fontSize: 14, bold: true, color: C.feher, fontFace: FEJ } },
  { text: "README.md · projektterv/ · produktum/ · dokumentacio/ · bemutato_video/ · forrasok/",
    options: { fontSize: 13, color: C.lime, fontFace: "Consolas" } }
], { x: 0.95, y: 5.35, w: 11.6, h: 1.0, isTextBox: true, margin: 0, valign: "middle" });
s.addNotes("Három produktum készült el. A weboldal a kötelező elem, emellett a kérdőívet és a prezentációt választottam a négy opció közül. Minden a GitHub repositoryban van, a feladatkiírás szerinti mappastruktúrában. Érdemes kiemelni, hogy a weboldal és ez a prezentáció ugyanabból a JSON állományból veszi a számokat, tehát nem tudnak eltérni egymástól.");

/* =========================================================
   14. TAPASZTALATOK
   ========================================================= */
s = P.addSlide({ masterName: "VILAGOS" });
cim(s, "Nehézségek és amit megtanultam", "Tapasztalatok");
const tap = [
  ["Kevés kitöltő az első napon", "Az első nap alig érkezett válasz.", `Személyre szóló üzenetben kértem meg embereket a link általános megosztása helyett — így lett ${N}.`],
  ["Az elemzés Excelben lassú volt", "Minden új válasznál kézzel kellett újraszámolni.", "Áttértem Python szkriptre: egy futtatás frissíti mind a 18 diagramot."],
  ["Az adat mást mutatott, mint vártam", "A minta sokkal aktívabb, mint feltételeztem.", "Átírtam a produktumot: nem az általános életmódról szól, hanem két konkrét vakfoltról."],
  ["Ok-okozat kísértése", "Kézenfekvő lett volna kimondani, hogy a képernyő fáraszt.", `${N} fős mintán ez nem állítható. Végig együttjárásként fogalmaztam.`],
  ["Egy összefüggés nem működött", "A sport–önértékelés kapcsolatot terveztem fő eredménynek.", "Az alcsoportok 1–2 fősek lettek. Nem erőltettem: kihagytam, és jeleztem, miért."]
];
let ty = 1.9;
tap.forEach(function (t, i) {
  s.addShape(P.ShapeType.roundRect, { x: 0.62, y: ty, w: 12.2, h: 0.92,
    fill: { color: i % 2 === 0 ? C.feher : "FAFCFB" }, line: { color: C.keret, width: 1 }, rectRadius: 0.1 });
  s.addText(t[0], { x: 0.92, y: ty + 0.06, w: 3.2, h: 0.8, fontSize: 13, fontFace: FEJ,
    bold: true, color: C.sotet, valign: "middle", isTextBox: true, margin: 0 });
  s.addText(t[1], { x: 4.25, y: ty + 0.06, w: 3.7, h: 0.8, fontSize: 11.5, fontFace: TXT,
    color: C.szurke, valign: "middle", isTextBox: true, margin: 0 });
  s.addText(t[2], { x: 8.1, y: ty + 0.06, w: 4.45, h: 0.8, fontSize: 11.5, fontFace: TXT,
    color: C.zold, valign: "middle", isTextBox: true, margin: 0 });
  ty += 1.02;
});
s.addText("Probléma", { x: 0.92, y: 1.55, w: 3, h: 0.3, fontSize: 10.5, fontFace: TXT,
  bold: true, color: C.szurke, charSpacing: 1.5, isTextBox: true, margin: 0 });
s.addText("Mit jelentett", { x: 4.25, y: 1.55, w: 3, h: 0.3, fontSize: 10.5, fontFace: TXT,
  bold: true, color: C.szurke, charSpacing: 1.5, isTextBox: true, margin: 0 });
s.addText("Megoldás", { x: 8.1, y: 1.55, w: 3, h: 0.3, fontSize: 10.5, fontFace: TXT,
  bold: true, color: C.zold, charSpacing: 1.5, isTextBox: true, margin: 0 });
s.addNotes("Öt konkrét nehézség volt. A legfontosabb tanulság a harmadik és az ötödik. A harmadik: az adat mást mutatott, mint amire számítottam, és ehhez nekem kellett igazodnom, nem fordítva. Az ötödik: egy összefüggés egyszerűen nem működött, mert a minta túl homogén volt. Ezt nem szépítettem, hanem kihagytam és megindokoltam.");

/* =========================================================
   15. ÖNÉRTÉKELÉS
   ========================================================= */
s = P.addSlide({ masterName: "VILAGOS" });
cim(s, "Önértékelés", "Zárás előtt");
s.addShape(P.ShapeType.roundRect, { x: 0.62, y: 1.95, w: 5.95, h: 2.2,
  fill: { color: C.halv }, line: { color: C.halv }, rectRadius: 0.12 });
s.addText("Amivel elégedett vagyok", { x: 0.95, y: 2.15, w: 5.3, h: 0.35, fontSize: 15,
  fontFace: FEJ, bold: true, color: C.sotet, isTextBox: true, margin: 0 });
s.addText([
  { text: "Saját adatot gyűjtöttem, nem csak internetes cikkeket idéztem.", options: { bullet: true, breakLine: true } },
  { text: "Az elemzést újrafuttatható szkriptbe írtam.", options: { bullet: true, breakLine: true } },
  { text: "A produktumot átírtam, amikor az adat mást mutatott.", options: { bullet: true, breakLine: true } },
  { text: "Nem közöltem olyan összefüggést, amit a minta nem bír el.", options: { bullet: true } }
], { x: 0.95, y: 2.55, w: 5.3, h: 1.5, fontSize: 12.5, fontFace: TXT, color: C.tinta,
     paraSpaceAfter: 4, isTextBox: true, margin: 0 });

s.addShape(P.ShapeType.roundRect, { x: 6.87, y: 1.95, w: 5.95, h: 2.2,
  fill: { color: "FCEEEC" }, line: { color: "FCEEEC" }, rectRadius: 0.12 });
s.addText("Amit legközelebb máshogy csinálnék", { x: 7.2, y: 2.15, w: 5.3, h: 0.35, fontSize: 15,
  fontFace: FEJ, bold: true, color: "A8382B", isTextBox: true, margin: 0 });
s.addText([
  { text: "Nem hagynám ki az akadályokra kérdező tételt.", options: { bullet: true, breakLine: true } },
  { text: "Változatosabb mintát gyűjtenék — ez túl sportos lett.", options: { bullet: true, breakLine: true } },
  { text: "Beépítenék néhány nyitott kérdést is a zártak mellé.", options: { bullet: true, breakLine: true } },
  { text: "Több időt hagynék az adatgyűjtésre.", options: { bullet: true } }
], { x: 7.2, y: 2.55, w: 5.3, h: 1.5, fontSize: 12.5, fontFace: TXT, color: "7A2B22",
     paraSpaceAfter: 4, isTextBox: true, margin: 0 });

s.addShape(P.ShapeType.roundRect, { x: 0.62, y: 4.35, w: 12.2, h: 2.05,
  fill: { color: C.feher }, line: { color: C.keret, width: 1 }, rectRadius: 0.12 });
s.addText("Az önálló munkáról", { x: 0.95, y: 4.55, w: 6, h: 0.35, fontSize: 15, fontFace: FEJ,
  bold: true, color: C.sotet, isTextBox: true, margin: 0 });
s.addText("A csoportbeosztás során nem alakult ki több fős csapat, ezért a projekt minden elemét egyedül készítettem el: a tervezést, az információgyűjtést, a kérdőív összeállítását és elemzését, a weboldal fejlesztését, a prezentációt és a dokumentációt. Ennek egyértelmű hátránya volt, hogy nem volt kivel megvitatni a döntéseket, és a kérdőívet is egyetlen ismeretségi körben tudtam terjeszteni. Előnye viszont, hogy minden részfeladatot végig kellett csinálnom — így a projekt egészét értem, nem csak a rám eső szeletet.",
  { x: 0.95, y: 4.95, w: 11.6, h: 1.35, fontSize: 12.5, fontFace: TXT, color: C.szurke,
    isTextBox: true, margin: 0 });
s.addNotes("Az önálló munka indoklása. A hátránya konkrétan meg is látszik az adatokon: a kérdőívet csak egy ismeretségi körben tudtam terjeszteni, és ez a kör feltűnően sportos. Ez a minta legnagyobb torzítása. Előny viszont, hogy a projekt minden részét át kellett látnom. Emellett egy kérdés kimaradt az űrlapról, ami az akadályokra kérdezett — emiatt egy tervezett elemzést nem tudtam elvégezni.");

/* =========================================================
   16. ZÁRÓ DIA
   ========================================================= */
s = P.addSlide({ masterName: "SOTET" });
s.addShape(P.ShapeType.ellipse, { x: -1.8, y: 3.8, w: 5.6, h: 5.6,
  fill: { color: C.zold, transparency: 60 }, line: { color: C.zold, transparency: 100 } });
s.addText("KÖSZÖNÖM A FIGYELMET", { x: 1.1, y: 2.15, w: 9, h: 0.32, fontSize: 12, fontFace: TXT,
  bold: true, color: C.lime, charSpacing: 2.5, isTextBox: true, margin: 0 });
s.addText("Jól élnek.\nKét dolog mégis kimarad.", { x: 1.1, y: 2.6, w: 9.6, h: 1.7,
  fontSize: 40, fontFace: FEJ, bold: true, color: C.feher, lineSpacingMultiple: 1.12,
  isTextBox: true, margin: 0 });
s.addShape(P.ShapeType.rect, { x: 1.1, y: 4.5, w: 1.4, h: 0.05, fill: { color: C.lime } });
s.addText([
  { text: "Gerecze Ádám  ·  IKT Projektmunka I.  ·  1/13. Sz. évfolyam\n", options: { fontSize: 14, color: "C6DDD2" } },
  { text: "A projekt teljes anyaga: GitHub repository", options: { fontSize: 13, color: "9DBBAE", italic: true } }
], { x: 1.1, y: 4.85, w: 9, h: 1.0, fontFace: TXT, isTextBox: true, margin: 0 });
s.addNotes("Zárás. Köszönöm a figyelmet — szívesen válaszolok kérdésekre. A teljes anyag, beleértve a nyers adatokat és az elemző szkriptet is, elérhető a GitHub repositoryban.");

/* ============ MENTÉS ============ */
P.writeFile({ fileName: path.join(GYOKER, "produktum", "prezentacio", "egeszseges_eletmod.pptx") })
  .then(function (f) { console.log("Elkészült:", f); });
