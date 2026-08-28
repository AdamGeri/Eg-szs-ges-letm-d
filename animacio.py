# -*- coding: utf-8 -*-
"""Diaáttűnések és belépő animációk hozzáadása a kész .pptx-hez.

A pptxgenjs nem tud animációt írni, ezért a becsomagolt OOXML-t módosítjuk:
 - minden diára <p:transition> (áttűnés) kerül,
 - minden diára <p:timing> blokk kerül, amely a tartalmi elemeket
   kattintásra, kaszkádszerűen úsztatja be (Fade / Áttűnés belépő effekt).
"""
import re, os, shutil, zipfile, sys

GYOKER = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

FORRAS = os.path.join(GYOKER, "produktum", "prezentacio", "egeszseges_eletmod.pptx")
MUNKA = os.path.join(GYOKER, "eszkozok", "_kicsomag")

# dia sorszám -> áttűnés típusa (a sötét, hangsúlyos diák másikat kapnak)
ATTUNES = {
    1: '<p:fade/>',
    7: '<p:push dir="u"/>',
    16: '<p:push dir="u"/>',
}
ALAP_ATTUNES = '<p:fade/>'


def effekt(par_id, spid, node_tipus, delay):
    """Egy elem "Fade in" belépő animációja."""
    return (
        f'<p:par><p:cTn id="{par_id}" presetID="10" presetClass="entr" presetSubtype="0" '
        f'fill="hold" grpId="0" nodeType="{node_tipus}">'
        f'<p:stCondLst><p:cond delay="{delay}"/></p:stCondLst>'
        f'<p:childTnLst>'
        f'<p:set><p:cBhvr><p:cTn id="{par_id+1}" dur="1" fill="hold">'
        f'<p:stCondLst><p:cond delay="0"/></p:stCondLst></p:cTn>'
        f'<p:tgtEl><p:spTgt spid="{spid}"/></p:tgtEl>'
        f'<p:attrNameLst><p:attrName>style.visibility</p:attrName></p:attrNameLst>'
        f'</p:cBhvr><p:to><p:strVal val="visible"/></p:to></p:set>'
        f'<p:animEffect transition="in" filter="fade">'
        f'<p:cBhvr><p:cTn id="{par_id+2}" dur="500"/>'
        f'<p:tgtEl><p:spTgt spid="{spid}"/></p:tgtEl></p:cBhvr></p:animEffect>'
        f'</p:childTnLst></p:cTn></p:par>'
    )


def timing_blokk(spidek):
    if not spidek:
        return ""
    effektek, azon = "", 5
    for i, sp in enumerate(spidek):
        effektek += effekt(azon, sp, "clickEffect" if i == 0 else "withEffect",
                           0 if i == 0 else 120 * i)
        azon += 3
    return (
        '<p:timing><p:tnLst><p:par>'
        '<p:cTn id="1" dur="indefinite" restart="never" nodeType="tmRoot"><p:childTnLst>'
        '<p:seq concurrent="1" nextAc="seek">'
        '<p:cTn id="2" dur="indefinite" nodeType="mainSeq"><p:childTnLst>'
        '<p:par><p:cTn id="3" fill="hold">'
        '<p:stCondLst><p:cond delay="indefinite"/></p:stCondLst><p:childTnLst>'
        '<p:par><p:cTn id="4" fill="hold">'
        '<p:stCondLst><p:cond delay="0"/></p:stCondLst><p:childTnLst>'
        + effektek +
        '</p:childTnLst></p:cTn></p:par>'
        '</p:childTnLst></p:cTn>'
        '<p:prevCondLst><p:cond evt="onPrev" delay="0"><p:tgtEl><p:sldTgt/></p:tgtEl></p:cond></p:prevCondLst>'
        '<p:nextCondLst><p:cond evt="onNext" delay="0"><p:tgtEl><p:sldTgt/></p:tgtEl></p:cond></p:nextCondLst>'
        '</p:par>'
        '</p:childTnLst></p:cTn>'
        '<p:prevCondLst><p:cond evt="onPrev" delay="0"><p:tgtEl><p:sldTgt/></p:tgtEl></p:cond></p:prevCondLst>'
        '<p:nextCondLst><p:cond evt="onNext" delay="0"><p:tgtEl><p:sldTgt/></p:tgtEl></p:cond></p:nextCondLst>'
        '</p:seq></p:childTnLst></p:cTn></p:par></p:tnLst></p:timing>'
    )


# --- kicsomagolás ---
if os.path.exists(MUNKA):
    shutil.rmtree(MUNKA)
with zipfile.ZipFile(FORRAS) as z:
    z.extractall(MUNKA)

sd = os.path.join(MUNKA, "ppt", "slides")
fajlok = sorted([f for f in os.listdir(sd) if f.endswith(".xml")],
                key=lambda n: int(re.search(r"\d+", n).group()))

for f in fajlok:
    n = int(re.search(r"\d+", f).group())
    ut = os.path.join(sd, f)
    xml = open(ut, encoding="utf-8").read()

    if "<p:timing>" in xml:
        continue

    # a spTree elemeinek azonosítói, dokumentumsorrendben
    tree = re.search(r"<p:spTree>(.*)</p:spTree>", xml, re.S).group(1)
    idk = [m.group(1) for m in re.finditer(r'<p:cNvPr id="(\d+)"', tree)]
    idk = idk[1:]              # az első a spTree saját azonosítója
    idk = idk[2:]              # a rovat és a főcím végig látszik
    idk = idk[:8]              # legfeljebb 8 elem animálódik

    beszuras = f'<p:transition spd="med">{ATTUNES.get(n, ALAP_ATTUNES)}</p:transition>' \
               + timing_blokk(idk)

    if "</p:clrMapOvr>" in xml:
        xml = xml.replace("</p:clrMapOvr>", "</p:clrMapOvr>" + beszuras, 1)
    else:
        xml = xml.replace("</p:cSld>", "</p:cSld>" + beszuras, 1)

    open(ut, "w", encoding="utf-8").write(xml)
    print(f"  {f}: áttűnés + {len(idk)} animált elem")

# --- visszacsomagolás ---
KI = FORRAS
if os.path.exists(KI):
    os.remove(KI)
zf = zipfile.ZipFile(KI, "w", zipfile.ZIP_DEFLATED)
for gyoker, _, files in os.walk(MUNKA):
    for name in files:
        teljes = os.path.join(gyoker, name)
        zf.write(teljes, os.path.relpath(teljes, MUNKA))
zf.close()
shutil.rmtree(MUNKA)
print("\nKész:", KI)
