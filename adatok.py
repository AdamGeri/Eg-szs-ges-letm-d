# -*- coding: utf-8 -*-
"""Közös adatbetöltő. Az elemzés kimenetéből (osszesites.json) képez
megjelenítésre kész értékeket, amelyeket a weboldal- és a prezentáció-generátor,
valamint az elemzés szövegének generátora egyaránt használ.
"""
import json
import os

GYOKER = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JSON_UT = os.path.join(GYOKER, "produktum", "kerdoiv", "osszesites.json")


class Adatok(dict):
    """Hiányzó kulcs esetén gondolatjelet ad vissza, nem hibát."""
    def __missing__(self, kulcs):
        return "—"


def tv(x, tizedes=2):
    """Tizedesvessző a magyar helyesírás szerint."""
    return f"{float(x):.{tizedes}f}".replace(".", ",")


def keszit():
    if not os.path.exists(JSON_UT):
        A = Adatok()
        A["van_adat"] = False
        return A

    with open(JSON_UT, encoding="utf-8") as f:
        o = json.load(f)

    A = Adatok()
    A["van_adat"] = True
    A["nyers"] = o
    A["n"] = o["kitoltok_szama"]
    for kulcs, ertek in o["szarmaztatott"].items():
        A[kulcs] = ertek

    A["onertekeles_atlag"] = tv(o["onertekeles_atlag"])
    A["ferfi_fo"] = o["nemek"]["Férfi"]
    A["no_fo"] = o["nemek"]["Nő"]
    A["kepernyo_faradtsag"] = o["kepernyo_faradtsag"]
    A["alvas_onertekeles"] = o["alvas_onertekeles"]
    A["sport_onertekeles"] = o["sport_onertekeles"]
    A["informacioforras"] = o["informacioforras"]
    A["mozgasformak"] = o["mozgasformak"]
    A["alvas"] = o["alvas"]
    A["eletkor"] = o["eletkor"]

    # alvás-önértékelés a legjobb és a legrosszabb alvó csoportban
    ao = o["alvas_onertekeles"]
    A["ao_78"] = tv(ao["7–8 órát"]["atlag"])
    A["ao_alatt6"] = tv(ao["6 óránál kevesebbet"]["atlag"])
    A["ao_alatt6_n"] = ao["6 óránál kevesebbet"]["n"]
    A["ao_78_n"] = ao["7–8 órát"]["n"]
    return A
