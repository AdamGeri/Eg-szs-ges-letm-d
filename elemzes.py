# -*- coding: utf-8 -*-
"""
Az online kérdőív válaszainak feldolgozása.
Projekt: Egészséges életmód – IKT Projektmunka I.
Készítette: Gerecze Ádám, 2026.

Használat a projekt gyökérkönyvtárából:
    python3 produktum/kerdoiv/elemzes.py

Bemenet:  valaszok.csv – a Google Űrlapok exportja (16 kérdés)
Kimenet:  diagramok/*.png    – 18 diagram
          osszesites.json    – a számok gépi formában, ebből dolgozik
                               a weboldal- és a prezentáció-generátor is
"""

import os
import re
import sys
import json
from collections import Counter

import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------- beállítások

ITT = os.path.dirname(os.path.abspath(__file__))
DIAGRAMOK = os.path.join(ITT, "diagramok")
CSV = os.path.join(ITT, "valaszok.csv")

ZOLD, VILAGOS, HALVANY = "#2E7D5B", "#7FB89A", "#BFDCCB"
NARANCS, PIROS, SZURKE = "#E9873F", "#D9594C", "#8FA39A"

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "axes.edgecolor": "#CFD8D3", "axes.labelcolor": "#33413B",
    "text.color": "#33413B", "xtick.color": "#5A6B63", "ytick.color": "#5A6B63",
})

# A Google Űrlapok a teljes kérdésszöveget írja fejlécbe, ezért a kérdés elején
# álló sorszám alapján azonosítjuk az oszlopokat.
KERDESEK = {
    1: "Nem", 2: "Eletkor", 3: "Reggeli", 4: "ZoldsegGyumolcs", 5: "CukrosUdito",
    6: "VizPohar", 7: "Gyorsetterem", 8: "SportGyakorisag", 9: "Mozgasformak",
    10: "AlvasOra", 11: "KepernyoIdo", 12: "Faradtsag", 13: "Energiaital",
    14: "OnertekelesSkala", 15: "Informacioforras", 16: "Valtoztatas",
}

# A kitöltők által beírt/kiválasztott válaszok egységes alakra hozása.
# (Az űrlapon néhány válasz kisbetűvel vagy hosszabb formában szerepelt.)
EGYSEGESITES = {
    "havonta 1–2 alkalommal": "Havonta 1–2 alkalommal",
    "havonta néhányszor": "Havonta néhányszor",
    "konditerem, erősítés": "Konditerem, erősítés",
    "kerékpározás": "Kerékpározás",
    "Más sport tevékenység ( itt nem felsorolt)": "Egyéb sporttevékenység",
    "Közösségi média ( TikTok, Instagram, Youtube, X stb.)": "Közösségi média",
    "Iskolában tanároktól": "Iskola, tanárok",
    "Szakmai weboldalak, cikkek": "Szakmai weboldalak",
}


def egyseges(szoveg):
    """Egységesíti a válaszcímkéket: nagykötőjel, kezdő nagybetű, ismert alakok."""
    s = str(szoveg).strip()
    s = re.sub(r"(?<=\d)\s*-\s*(?=\d)", "–", s)      # 6-7 → 6–7
    s = re.sub(r"\s+", " ", s)
    if s in EGYSEGESITES:
        return EGYSEGESITES[s]
    s2 = s[0].upper() + s[1:] if s else s
    return EGYSEGESITES.get(s2, s2)


# ---------------------------------------------------------------- beolvasás

def beolvas():
    if not os.path.exists(CSV):
        sys.exit("HIBA: a valaszok.csv nem található. Lásd: urlap_utmutato.md")
    df = pd.read_csv(CSV)

    uj, talalt = {}, set()
    for oszlop in df.columns:
        m = re.match(r"\s*(\d+)\s*[.)]", str(oszlop))
        if m and int(m.group(1)) in KERDESEK:
            uj[oszlop] = KERDESEK[int(m.group(1))]
            talalt.add(int(m.group(1)))
        elif str(oszlop).strip().lower().startswith(("időbélyeg", "timestamp")):
            uj[oszlop] = "Idobelyeg"
    df = df.rename(columns=uj)

    hianyzo = sorted(set(KERDESEK) - talalt)
    if hianyzo:
        print("HIBA: az alábbi kérdések nem találhatók a táblázatban:", hianyzo)
        print("      Minden kérdésnek sorszámmal kell kezdődnie, pl. '3. Reggelizel...'")
        sys.exit(1)

    for oszlop in KERDESEK.values():
        if oszlop != "OnertekelesSkala":
            df[oszlop] = df[oszlop].apply(lambda x: egyseges(x) if pd.notna(x) else x)
    df["OnertekelesSkala"] = pd.to_numeric(df["OnertekelesSkala"], errors="coerce")
    return df


# ---------------------------------------------------------------- rajzolás

def oszlop_diagram(fajl, cimkek, ertekek, cim, N,
                   szinek=None, vizszintes=False, xcim="", tizedes=False, alap=None):
    fig, ax = plt.subplots(figsize=(7.6, 4.4), dpi=150)
    szinek = szinek or [ZOLD] * len(cimkek)
    maxi = max(ertekek) if max(ertekek) else 1
    alap = alap or [N] * len(cimkek)

    def felirat(v, alapszam):
        if tizedes:
            return f"{v:.2f}".replace(".", ",")
        sz = f"{v / alapszam * 100:.0f}%" if alapszam else "–"
        return f"{v} fő ({sz})" if vizszintes else f"{v}\n({sz})"

    if vizszintes:
        y = range(len(cimkek))
        ax.barh(y, ertekek, color=szinek, height=0.62)
        ax.set_yticks(list(y))
        ax.set_yticklabels(cimkek, fontsize=10)
        ax.invert_yaxis()
        for i, v in enumerate(ertekek):
            ax.text(v + maxi * 0.02, i, felirat(v, alap[i]),
                    va="center", fontsize=9.5, color="#33413B")
        ax.set_xlim(0, maxi * 1.32)
        ax.xaxis.grid(True, color="#E8EEEA")
    else:
        x = range(len(cimkek))
        ax.bar(x, ertekek, color=szinek, width=0.6)
        ax.set_xticks(list(x))
        ax.set_xticklabels(cimkek, fontsize=10)
        for i, v in enumerate(ertekek):
            ax.text(i, v + maxi * 0.03, felirat(v, alap[i]),
                    ha="center", fontsize=9.5, color="#33413B")
        ax.set_ylim(0, maxi * 1.34)
        ax.yaxis.grid(True, color="#E8EEEA")

    ax.set_axisbelow(True)
    ax.set_title(cim, fontsize=13, fontweight="bold", pad=14, loc="left")
    if xcim:
        ax.set_xlabel(xcim, fontsize=10)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    fig.tight_layout()
    fig.savefig(os.path.join(DIAGRAMOK, fajl), bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("  ✔", fajl)


def fank_diagram(fajl, cimkek, ertekek, cim, szinek):
    parok = [(c, e, s) for c, e, s in zip(cimkek, ertekek, szinek) if e > 0]
    if not parok:
        return
    cimkek, ertekek, szinek = zip(*parok)
    fig, ax = plt.subplots(figsize=(7.0, 4.4), dpi=150)
    wedges, _, _ = ax.pie(
        ertekek, colors=szinek, autopct=lambda p: f"{p:.0f}%", startangle=90,
        pctdistance=0.78, wedgeprops=dict(width=0.42, edgecolor="white", linewidth=2),
        textprops=dict(fontsize=10.5, fontweight="bold", color="white"))
    ax.legend(wedges, [f"{c} – {e} fő" for c, e in zip(cimkek, ertekek)],
              loc="center left", bbox_to_anchor=(1.0, 0.5), frameon=False, fontsize=10)
    ax.set_title(cim, fontsize=13, fontweight="bold", pad=14, loc="left")
    fig.tight_layout()
    fig.savefig(os.path.join(DIAGRAMOK, fajl), bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("  ✔", fajl)


# ---------------------------------------------------------------- főprogram

def main():
    os.makedirs(DIAGRAMOK, exist_ok=True)
    df = beolvas()
    N = len(df)
    print(f"Beolvasva: {N} kitöltő\n")
    if N < 20:
        print(f"FIGYELEM: a feladat legalább 20 kitöltőt ír elő, jelenleg {N} van.\n")

    O = {"kitoltok_szama": int(N)}

    def szamlal(oszlop, sorrend):
        c = df[oszlop].value_counts()
        return [int(c.get(k, 0)) for k in sorrend]

    def tobbvalaszos(oszlop):
        db = Counter()
        for cella in df[oszlop].dropna():
            for elem in str(cella).split(";"):
                if elem.strip():
                    db[egyseges(elem)] += 1
        return db.most_common()

    print("Diagramok készítése:")

    # 1. Nemek
    s = ["Férfi", "Nő", "Nem szeretnék válaszolni"]
    v = szamlal("Nem", s)
    fank_diagram("01_nemek.png", s, v, f"1. A kitöltők nemek szerinti megoszlása (n={N})",
                 [ZOLD, VILAGOS, SZURKE])
    O["nemek"] = dict(zip(s, v))

    # 2. Életkor
    s = ["14–15", "16–17", "18–19", "20 vagy több"]
    v = szamlal("Eletkor", s)
    oszlop_diagram("02_eletkor.png", s, v, "2. Életkori megoszlás", N,
                   [HALVANY, VILAGOS, ZOLD, SZURKE])
    O["eletkor"] = dict(zip(s, v))

    # 3. Reggeli
    s = ["Mindig", "Gyakran", "Ritkán", "Soha"]
    v = szamlal("Reggeli", s)
    fank_diagram("03_reggeli.png", s, v, "3. Reggelizel iskolanapokon?",
                 [ZOLD, VILAGOS, NARANCS, PIROS])
    O["reggeli"] = dict(zip(s, v))
    O["reggeli_valaszolt"] = int(df["Reggeli"].notna().sum())

    # 4. Zöldség-gyümölcs
    s = ["Egyszer sem", "1 alkalommal", "2–3 alkalommal", "4 vagy több alkalommal"]
    v = szamlal("ZoldsegGyumolcs", s)
    oszlop_diagram("04_zoldseg_gyumolcs.png", ["Egyszer\nsem", "1×", "2–3×", "4× vagy\ntöbb"],
                   v, "4. Napi zöldség- és gyümölcsfogyasztás", N,
                   [PIROS, NARANCS, VILAGOS, ZOLD])
    O["zoldseg_gyumolcs"] = dict(zip(s, v))

    # 5. Cukros üdítő
    s = ["Naponta", "Hetente többször", "Hetente egyszer", "Ritkán vagy soha"]
    v = szamlal("CukrosUdito", s)
    oszlop_diagram("05_cukros_udito.png",
                   ["Naponta", "Hetente\ntöbbször", "Hetente\negyszer", "Ritkán\nvagy soha"],
                   v, "5. Cukros üdítő fogyasztásának gyakorisága", N,
                   [PIROS, NARANCS, VILAGOS, ZOLD])
    O["cukros_udito"] = dict(zip(s, v))

    # 6. Vízfogyasztás
    s = ["0–2", "3–4", "5–7", "8 vagy több"]
    v = szamlal("VizPohar", s)
    oszlop_diagram("06_vizfogyasztas.png", ["0–2 pohár", "3–4 pohár", "5–7 pohár", "8+ pohár"],
                   v, "6. Napi vízfogyasztás (1 pohár ≈ 2 dl)", N,
                   [PIROS, NARANCS, VILAGOS, ZOLD])
    O["viz"] = dict(zip(s, v))

    # 7. Gyorsétterem
    s = ["Hetente többször", "Hetente egyszer", "Havonta 1–2 alkalommal", "Ritkán vagy soha"]
    v = szamlal("Gyorsetterem", s)
    oszlop_diagram("07_gyorsetterem.png",
                   ["Hetente\ntöbbször", "Hetente\negyszer", "Havonta\n1–2×", "Ritkán\nvagy soha"],
                   v, "7. Gyorséttermi vagy rendelt étel fogyasztása", N,
                   [PIROS, NARANCS, VILAGOS, ZOLD])
    O["gyorsetterem"] = dict(zip(s, v))

    # 8. Sportolási gyakoriság
    s = ["Szinte naponta", "Hetente 3–4 alkalommal", "Hetente 1–2 alkalommal", "Szinte soha"]
    v = szamlal("SportGyakorisag", s)
    oszlop_diagram("08_sport_gyakorisag.png",
                   ["Szinte\nnaponta", "Heti\n3–4×", "Heti\n1–2×", "Szinte\nsoha"],
                   v, "8. Testmozgás gyakorisága a testnevelési órán kívül", N,
                   [ZOLD, VILAGOS, NARANCS, PIROS])
    O["sport"] = dict(zip(s, v))

    # 9. Mozgásformák
    mf = tobbvalaszos("Mozgasformak")
    oszlop_diagram("09_mozgasformak.png", [k for k, _ in mf], [x for _, x in mf],
                   "9. Választott mozgásformák (több válasz is megjelölhető)", N,
                   [PIROS if k == "Nem sportolok" else ZOLD for k, _ in mf], vizszintes=True)
    O["mozgasformak"] = dict(mf)

    # 10. Alvás
    s = ["8 óránál többet", "7–8 órát", "6–7 órát", "6 óránál kevesebbet"]
    v = szamlal("AlvasOra", s)
    fank_diagram("10_alvas.png", s, v, "10. Alvásidő egy átlagos iskolai éjszakán",
                 [ZOLD, VILAGOS, NARANCS, PIROS])
    O["alvas"] = dict(zip(s, v))

    # 11. Képernyőidő
    s = ["2 óránál kevesebbet", "2–4 órát", "4–6 órát", "6 óránál többet"]
    v = szamlal("KepernyoIdo", s)
    oszlop_diagram("11_kepernyoido.png", ["< 2 óra", "2–4 óra", "4–6 óra", "6+ óra"], v,
                   "11. Napi szabadidős képernyőidő", N,
                   [ZOLD, VILAGOS, NARANCS, PIROS])
    O["kepernyo"] = dict(zip(s, v))

    # 12. Fáradtság
    s = ["Szinte minden nap", "Hetente többször", "Ritkán", "Szinte soha"]
    v = szamlal("Faradtsag", s)
    oszlop_diagram("12_faradtsag.png",
                   ["Szinte\nminden nap", "Hetente\ntöbbször", "Ritkán", "Szinte\nsoha"], v,
                   "12. Milyen gyakran érzed magad fáradtnak napközben?", N,
                   [PIROS, NARANCS, VILAGOS, ZOLD])
    O["faradtsag"] = dict(zip(s, v))

    # 13. Energiaital
    s = ["Szinte naponta", "Hetente", "Havonta néhányszor", "Soha"]
    v = szamlal("Energiaital", s)
    fank_diagram("13_energiaital.png", s, v, "13. Energiaital-fogyasztás",
                 [PIROS, NARANCS, VILAGOS, ZOLD])
    O["energiaital"] = dict(zip(s, v))

    # 14. Önértékelés
    s = [1, 2, 3, 4, 5]
    v = [int((df["OnertekelesSkala"] == k).sum()) for k in s]
    atlag = float(df["OnertekelesSkala"].mean())
    oszlop_diagram("14_onertekeles.png", ["1", "2", "3", "4", "5"], v,
                   f"14. Egészség-önértékelés – átlag: {atlag:.2f}".replace(".", ","), N,
                   [PIROS, NARANCS, SZURKE, VILAGOS, ZOLD],
                   xcim="1 = egyáltalán nem  ·  5 = teljesen")
    O["onertekeles"] = dict(zip([str(x) for x in s], v))
    O["onertekeles_atlag"] = round(atlag, 2)

    # 15. Információforrások
    inf = tobbvalaszos("Informacioforras")
    oszlop_diagram("15_informacioforras.png", [k for k, _ in inf], [x for _, x in inf],
                   "15. Honnan tájékozódnak egészségügyi kérdésekben?", N,
                   [PIROS if k == "Sehonnan" else ZOLD for k, _ in inf], vizszintes=True)
    O["informacioforras"] = dict(inf)

    # 16. Változtatási szándék
    s = ["Igen, és konkrét terveim is vannak", "Igen, de nem tudom, hol kezdjem",
         "Nem, elégedett vagyok a jelenlegivel", "Nem foglalkoztat a kérdés"]
    v = szamlal("Valtoztatas", s)
    fank_diagram("16_valtoztatas.png",
                 ["Igen, van terve", "Igen, de nem tudja, hogyan",
                  "Nem, elégedett", "Nem foglalkoztatja"], v,
                 "16. Szeretnél változtatni az életmódodon?",
                 [ZOLD, NARANCS, VILAGOS, SZURKE])
    O["valtoztatas"] = dict(zip(s, v))

    # ---------------------------------------------------- 17. összefüggés:
    # képernyőidő és a rendszeres (legalább heti többszöri) fáradtság
    kep_sorrend = ["< 2 óra", "2–4 óra", "4–6 óra", "6+ óra"]
    kep_map = {"2 óránál kevesebbet": "< 2 óra", "2–4 órát": "2–4 óra",
               "4–6 órát": "4–6 óra", "6 óránál többet": "6+ óra"}
    df["_kep"] = df["KepernyoIdo"].map(kep_map)
    df["_faradt"] = df["Faradtsag"].isin(["Szinte minden nap", "Hetente többször"])
    adat = [(int((df["_kep"] == k).sum()), int(df[df["_kep"] == k]["_faradt"].sum()))
            for k in kep_sorrend]

    fig, ax = plt.subplots(figsize=(7.6, 4.4), dpi=150)
    x = range(len(kep_sorrend))
    ossz = [a for a, _ in adat]
    far = [b for _, b in adat]
    ax.bar([i - 0.19 for i in x], ossz, width=0.36, color=HALVANY, label="Összes válaszadó")
    ax.bar([i + 0.19 for i in x], far, width=0.36, color=NARANCS,
           label="Ebből: legalább hetente többször fáradt")
    for i, (a, b) in enumerate(adat):
        ax.text(i - 0.19, a + 0.15, str(a), ha="center", fontsize=10)
        sz = f"{b}\n({b / a * 100:.0f}%)" if a else str(b)
        ax.text(i + 0.19, b + 0.15, sz, ha="center", fontsize=9.5,
                color=NARANCS, fontweight="bold")
    ax.set_xticks(list(x))
    ax.set_xticklabels(kep_sorrend, fontsize=10)
    ax.set_ylim(0, (max(ossz) if max(ossz) else 1) * 1.42)
    ax.set_title("17. Képernyőidő és a rendszeres nappali fáradtság",
                 fontsize=13, fontweight="bold", pad=14, loc="left")
    ax.set_xlabel("Napi szabadidős képernyőidő", fontsize=10)
    ax.set_ylabel("Válaszadók száma (fő)", fontsize=10)
    ax.legend(frameon=False, fontsize=9.5)
    ax.yaxis.grid(True, color="#E8EEEA")
    ax.set_axisbelow(True)
    for sp in ("top", "right"):
        ax.spines[sp].set_visible(False)
    fig.tight_layout()
    fig.savefig(os.path.join(DIAGRAMOK, "17_kepernyo_faradtsag.png"),
                bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("  ✔ 17_kepernyo_faradtsag.png")
    O["kepernyo_faradtsag"] = {k: {"osszes": a, "faradt": b}
                               for k, (a, b) in zip(kep_sorrend, adat)}

    # ---------------------------------------------------- 18. összefüggés:
    # alvásmennyiség és egészség-önértékelés
    al_sorrend = ["8 óránál többet", "7–8 órát", "6–7 órát", "6 óránál kevesebbet"]
    al_atlag, al_n = [], []
    for k in al_sorrend:
        resz = df[df["AlvasOra"] == k]["OnertekelesSkala"]
        al_atlag.append(round(float(resz.mean()), 2) if len(resz) else 0.0)
        al_n.append(len(resz))
    oszlop_diagram("18_alvas_onertekeles.png",
                   [f"{k}\n(n={n})" for k, n in zip(
                       ["8+ órát", "7–8 órát", "6–7 órát", "< 6 órát"], al_n)],
                   al_atlag, "18. Alvásmennyiség és egészség-önértékelés (átlag, 1–5)", N,
                   [ZOLD, VILAGOS, NARANCS, PIROS], tizedes=True)
    O["alvas_onertekeles"] = {k: {"atlag": a, "n": n}
                              for k, a, n in zip(al_sorrend, al_atlag, al_n)}

    # sportolás és önértékelés (diagram nélkül – az alcsoportok túl kicsik)
    sp = ["Szinte naponta", "Hetente 3–4 alkalommal", "Hetente 1–2 alkalommal", "Szinte soha"]
    O["sport_onertekeles"] = {}
    for k in sp:
        resz = df[df["SportGyakorisag"] == k]["OnertekelesSkala"]
        O["sport_onertekeles"][k] = {
            "atlag": round(float(resz.mean()), 2) if len(resz) else 0.0,
            "n": len(resz)}

    # --------------------------------------------------- származtatott számok
    def sz(x, alap=None):
        alap = alap or N
        return round(x / alap * 100) if alap else 0

    a, kep, mf_d = O["alvas"], O["kepernyo"], O["mozgasformak"]
    NR = O["reggeli_valaszolt"]
    d = {
        "alvas_keves_fo": a["6–7 órát"] + a["6 óránál kevesebbet"],
        "alvas_nagyon_keves_fo": a["6 óránál kevesebbet"],
        "alvas_eleg_fo": a["8 óránál többet"] + a["7–8 órát"],
        "alvas_ajanlott_fo": a["8 óránál többet"],
        "kepernyo_sok_fo": kep["4–6 órát"] + kep["6 óránál többet"],
        "zoldseg_sok_fo": O["zoldseg_gyumolcs"]["4 vagy több alkalommal"],
        "zoldseg_keves_fo": (O["zoldseg_gyumolcs"]["Egyszer sem"]
                             + O["zoldseg_gyumolcs"]["1 alkalommal"]),
        "reggeli_mindig_fo": O["reggeli"]["Mindig"],
        "reggeli_rendszeres_fo": O["reggeli"]["Mindig"] + O["reggeli"]["Gyakran"],
        "reggeli_ritkan_fo": O["reggeli"]["Ritkán"] + O["reggeli"]["Soha"],
        "reggeli_valaszolt": NR,
        "udito_ritkan_fo": O["cukros_udito"]["Ritkán vagy soha"],
        "udito_naponta_fo": O["cukros_udito"]["Naponta"],
        "viz_sok_fo": O["viz"]["5–7"] + O["viz"]["8 vagy több"],
        "viz_keves_fo": O["viz"]["0–2"],
        "gyors_ritkan_fo": (O["gyorsetterem"]["Ritkán vagy soha"]
                            + O["gyorsetterem"]["Havonta 1–2 alkalommal"]),
        "sport_gyakori_fo": O["sport"]["Szinte naponta"] + O["sport"]["Hetente 3–4 alkalommal"],
        "sport_naponta_fo": O["sport"]["Szinte naponta"],
        "sport_soha_fo": O["sport"]["Szinte soha"],
        "energiaital_fo": N - O["energiaital"]["Soha"],
        "energiaital_soha_fo": O["energiaital"]["Soha"],
        "faradt_rendszeres_fo": int(df["_faradt"].sum()),
        "faradt_naponta_fo": O["faradtsag"]["Szinte minden nap"],
        "valtoztat_fo": (O["valtoztatas"]["Igen, és konkrét terveim is vannak"]
                         + O["valtoztatas"]["Igen, de nem tudom, hol kezdjem"]),
        "valtoztat_nem_tudja_fo": O["valtoztatas"]["Igen, de nem tudom, hol kezdjem"],
        "valtoztat_elegedett_fo": O["valtoztatas"]["Nem, elégedett vagyok a jelenlegivel"],
        "info_elso": inf[0][0] if inf else "—",
        "info_elso_fo": inf[0][1] if inf else 0,
        "info_orvos_fo": O["informacioforras"].get("Orvos, szakember", 0),
        "info_szakmai_fo": (O["informacioforras"].get("Orvos, szakember", 0)
                            + O["informacioforras"].get("Szakmai weboldalak", 0)),
        "mozgas_elso": mf[0][0] if mf else "—",
        "mozgas_elso_fo": mf[0][1] if mf else 0,
        "kor_top": max(O["eletkor"], key=O["eletkor"].get),
        "kor_top_fo": max(O["eletkor"].values()),
    }
    # az alacsony és a magas képernyőidejű csoport fáradtsági aránya
    kf = O["kepernyo_faradtsag"]
    also = kf["< 2 óra"]["osszes"] + kf["2–4 óra"]["osszes"]
    also_f = kf["< 2 óra"]["faradt"] + kf["2–4 óra"]["faradt"]
    felso = kf["4–6 óra"]["osszes"] + kf["6+ óra"]["osszes"]
    felso_f = kf["4–6 óra"]["faradt"] + kf["6+ óra"]["faradt"]
    d.update({
        "kep_also_fo": also, "kep_also_faradt_fo": also_f, "kep_also_faradt_sz": sz(also_f, also),
        "kep_felso_fo": felso, "kep_felso_faradt_fo": felso_f, "kep_felso_faradt_sz": sz(felso_f, felso),
    })

    for kulcs in ["alvas_keves", "alvas_eleg", "kepernyo_sok", "zoldseg_sok", "zoldseg_keves",
                  "udito_ritkan", "viz_sok", "gyors_ritkan", "sport_gyakori", "sport_naponta",
                  "energiaital_soha", "faradt_rendszeres", "valtoztat", "valtoztat_elegedett"]:
        d[kulcs + "_sz"] = sz(d[kulcs + "_fo"])
    d["reggeli_rendszeres_sz"] = sz(d["reggeli_rendszeres_fo"], NR)
    O["szarmaztatott"] = d

    with open(os.path.join(ITT, "osszesites.json"), "w", encoding="utf-8") as f:
        json.dump(O, f, ensure_ascii=False, indent=2, default=int)

    print("\n=== FŐBB SZÁMOK ===")
    print(f"Kitöltők:                    {N} fő")
    print(f"Legalább heti 3× sportol:    {d['sport_gyakori_fo']} fő ({d['sport_gyakori_sz']}%)")
    print(f"Legalább 5 pohár vizet iszik:{d['viz_sok_fo']:3} fő ({d['viz_sok_sz']}%)")
    print(f"Rendszeresen reggelizik:     {d['reggeli_rendszeres_fo']} / {NR} fő")
    print(f"Napi 4× zöldséget eszik:     {d['zoldseg_sok_fo']} fő")
    print(f"7 óránál kevesebbet alszik:  {d['alvas_keves_fo']} fő ({d['alvas_keves_sz']}%)")
    print(f"Napi 4+ óra képernyő:        {d['kepernyo_sok_fo']} fő ({d['kepernyo_sok_sz']}%)")
    print(f"Rendszeresen fáradt:         {d['faradt_rendszeres_fo']} fő ({d['faradt_rendszeres_sz']}%)")
    print(f"Önértékelés átlaga:          {O['onertekeles_atlag']}")
    print(f"Változtatna:                 {d['valtoztat_fo']} fő ({d['valtoztat_sz']}%)")
    print(f"\nKépernyő–fáradtság: 4 óra alatt {also_f}/{also} ({d['kep_also_faradt_sz']}%), "
          f"4 óra felett {felso_f}/{felso} ({d['kep_felso_faradt_sz']}%)")


if __name__ == "__main__":
    main()
