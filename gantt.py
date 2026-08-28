# -*- coding: utf-8 -*-
"""A projekt ütemtervének (Gantt-diagram) rajzolása.

Futtatás a projekt gyökeréből:
    python3 eszkozok/gantt.py
"""
import os
from datetime import date

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

GYOKER = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KIMENET = os.path.join(GYOKER, "projektterv", "gantt.png")

plt.rcParams["font.family"] = "DejaVu Sans"

ZOLD, VILAGOS, NARANCS, SOTET = "#2E7D5B", "#7FB89A", "#E9873F", "#14503B"

KEZDET = date(2026, 8, 23)   # vasárnap
VEGE = date(2026, 8, 28)
NAPOK = (VEGE - KEZDET).days + 1     # 6 nap

# (feladat, kezdőnap indexe, hossz napokban, szín, szakasz)
FELADATOK = [
    ("Témaválasztás, projektterv készítése",        0, 1, SOTET,   "Tervezés"),
    ("Információgyűjtés, források feldolgozása",    0, 2, SOTET,   "Tervezés"),
    ("A kérdőív kérdéseinek összeállítása",         1, 1, ZOLD,    "Kutatás"),
    ("Google Űrlap létrehozása, megosztás",         1, 1, ZOLD,    "Kutatás"),
    ("Adatgyűjtés (kitöltési időszak)",             2, 3, VILAGOS, "Kutatás"),
    ("Weboldal szerkezete, arculat, CSS",           2, 2, NARANCS, "Fejlesztés"),
    ("Saját SVG ábrák elkészítése",                 2, 1, NARANCS, "Fejlesztés"),
    ("Weboldal tartalmi oldalainak megírása",       3, 2, NARANCS, "Fejlesztés"),
    ("Adatok feldolgozása, diagramok (Python)",     4, 1, ZOLD,    "Kutatás"),
    ("Az elemzés és a következtetések megírása",    4, 1, ZOLD,    "Kutatás"),
    ("Prezentáció készítése (diaminta, animációk)", 4, 2, NARANCS, "Fejlesztés"),
    ("Dokumentáció, projektbeszámoló",              4, 2, SOTET,   "Lezárás"),
    ("GitHub feltöltés, README",                    5, 1, SOTET,   "Lezárás"),
    ("Bemutató próbája, véglegesítés",              5, 1, SOTET,   "Lezárás"),
]

fig, ax = plt.subplots(figsize=(11.5, 6.4), dpi=150)

napnevek = ["vas.", "hétfő", "kedd", "szerda", "csüt.", "péntek"]
for i in range(NAPOK):
    if i % 2 == 0:
        ax.axvspan(i, i + 1, color="#F2F7F4", zorder=0)

for sor, (nev, kezd, hossz, szin, _) in enumerate(FELADATOK):
    y = len(FELADATOK) - sor - 1
    doboz = FancyBboxPatch((kezd + 0.06, y + 0.18), hossz - 0.12, 0.64,
                           boxstyle="round,pad=0,rounding_size=0.09",
                           facecolor=szin, edgecolor="none", zorder=3)
    ax.add_patch(doboz)
    ax.text(kezd + hossz / 2, y + 0.5, f"{hossz} nap", ha="center", va="center",
            color="white", fontsize=9, fontweight="bold", zorder=4)

ax.set_xlim(0, NAPOK)
ax.set_ylim(0, len(FELADATOK))
ax.set_yticks([len(FELADATOK) - i - 0.5 for i in range(len(FELADATOK))])
ax.set_yticklabels([f"{i + 1}. {nev}" for i, (nev, *_) in enumerate(FELADATOK)], fontsize=10)
ax.set_xticks([i + 0.5 for i in range(NAPOK)])
ax.set_xticklabels([f"08.{23 + i:02d}.\n{napnevek[i]}" for i in range(NAPOK)], fontsize=10)
ax.xaxis.set_ticks_position("top")
ax.xaxis.set_label_position("top")

for i in range(NAPOK + 1):
    ax.axvline(i, color="#DCE6E1", lw=1, zorder=1)
ax.set_axisbelow(True)
for s in ("top", "right", "left", "bottom"):
    ax.spines[s].set_visible(False)
ax.tick_params(length=0)

ax.set_title("Egészséges életmód – projekt ütemterve (2026. 08. 23. – 08. 28.)",
             fontsize=14, fontweight="bold", color=SOTET, pad=42, loc="left")

jelmagyarazat = [(SOTET, "Tervezés és lezárás"), (ZOLD, "Kutatás"),
                 (VILAGOS, "Adatgyűjtés (passzív)"), (NARANCS, "Fejlesztés")]
for i, (szin, cimke) in enumerate(jelmagyarazat):
    ax.add_patch(FancyBboxPatch((0.08 + i * 1.45, -1.05), 0.22, 0.34,
                                boxstyle="round,pad=0,rounding_size=0.06",
                                facecolor=szin, edgecolor="none",
                                clip_on=False, zorder=5))
    ax.text(0.38 + i * 1.45, -0.88, cimke, fontsize=9.5, va="center",
            color="#33413B", clip_on=False)

fig.tight_layout()
fig.savefig(KIMENET, bbox_inches="tight", facecolor="white")
print("Elkészült:", os.path.relpath(KIMENET, GYOKER))
