# Útmutató: hogyan hozd létre a kérdőívet Google Űrlapokban

Ez a fájl lépésről lépésre végigvezet a kérdőív elkészítésén. A kérdések szövege
és a válaszlehetőségek másolásra készen szerepelnek a `kerdoiv_kerdesek.md`
fájlban — innen egyszerűen ki tudod másolni őket.

---

## 1. Az űrlap létrehozása

1. Nyisd meg a <https://forms.google.com> oldalt, és jelentkezz be.
2. Kattints az **Üres űrlap** lehetőségre.
3. Az űrlap címe legyen: **Egészséges életmód a középiskolások körében**
4. A leírás mezőbe másold be a `kerdoiv_kerdesek.md` fájl „Bevezető szöveg" részét.

---

## 2. FONTOS: számozd meg a kérdéseket

A kérdés szövegét **mindig a sorszámmal kezdd**, pontosan így:

```
1. Mi a nemed?
2. Hány éves vagy?
3. Reggelizel iskolanapokon?
```

**Miért fontos ez?** Az elemző szkript a sorszám alapján ismeri fel a kérdéseket
az exportált táblázatban. Ha lemarad a szám, a feldolgozás nem fog működni.

---

## 3. A kérdéstípusok beállítása

| Kérdés | Típus Google Űrlapokban |
|---|---|
| 1–8., 10–13., 17. | **Feleletválasztós** (egy válasz) |
| 9., 15., 16. | **Jelölőnégyzetek** (több válasz) |
| 14. | **Lineáris skála**, 1-től 5-ig |

A 14. kérdésnél a skála két végét címkézd fel:
- 1 = *egyáltalán nem*
- 5 = *teljesen*

Minden kérdésnél kapcsold be a **Kötelező** kapcsolót, hogy ne maradjon üres válasz.

---

## 4. Az űrlap beállításai

Kattints a fogaskerék ikonra, és állítsd be:

- **Válaszok** fülön: az „E-mail-címek gyűjtése" legyen **kikapcsolva** (a kérdőív anonim)
- **Válaszadási korlát**: legyen kikapcsolva (ne kelljen bejelentkezni)
- **Bemutató** fülön: a visszaigazoló üzenet legyen pl. „Köszönöm, hogy segítettél!"

---

## 5. Megosztás

1. Kattints a **Küldés** gombra, majd a link ikonra.
2. Kapcsold be a **Rövid URL** lehetőséget.
3. Oszd meg a linket.

**Tipp a kitöltők számához:** a feladat legalább 20 kitöltőt ír elő. Tapasztalat
szerint a csoportba bedobott link kevesebb kitöltést hoz, mint a személyre szóló
üzenet. Érdemes egyesével megkérni embereket, és megírni, hogy 3 perc az egész.

---

## 6. Az adatok letöltése

Ha összegyűlt legalább 20 kitöltés:

1. Az űrlap **Válaszok** fülén kattints a zöld táblázat ikonra → **Táblázat létrehozása**.
2. A megnyíló Google Táblázatban: **Fájl → Letöltés → Vesszővel elválasztott értékek (.csv)**.
3. A letöltött fájlt nevezd át erre: **`valaszok.csv`**
4. Másold be ebbe a mappába: `produktum/kerdoiv/valaszok.csv`

---

## 7. Az elemzés futtatása

A projekt gyökérkönyvtárában add ki ezt a parancsot:

```bash
python3 produktum/kerdoiv/elemzes.py
```

A szkript ekkor:
- beolvassa a valódi válaszokat,
- legenerálja mind a 18 diagramot a `diagramok/` mappába,
- kiírja az `osszesites.json` fájlt a számokkal,
- elkészíti az `elemzes.md` szöveges elemzést.

Ezután futtasd ezt is, hogy a weboldal és a prezentáció is a valódi számokat mutassa:

```bash
python3 eszkozok/weboldal.py
node eszkozok/prezi.js
```

---

## A kérdőív véglegesített formája

Az elkészült űrlap **16 kérdést** tartalmaz: az eredetileg tervezett, az akadályokra
vonatkozó 15. kérdés a véglegesítéskor kimaradt. Az elemző szkript ezért 16 kérdéssel
számol. Ha a kérdőívet később kiegészíted, a `KERDESEK` szótárt kell frissíteni az
`elemzes.py` fájl elején.

**Kérdések száma:** 16 · **Kitöltők:** 22 fő
