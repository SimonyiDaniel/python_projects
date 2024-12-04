#Generáljunk le 50 db, -60 és 100 közötti véletlen számot (az input txt-hez hasonlóan, de természetesen listába rakva),
#majd a következő feladatokat oldjuk meg.
#Minden feladat előtt a program írja ki a feladat sorszámát!
#1. Mennyi a sorozatban található számok szorzata?
#2. Írjuk ki az utolsó 5-tel vagy 7-tel osztható szám indexét!
#3. Írjuk ki az első 3-mal és 7-tel osztható szám indexét!
#4. Igaz-e, hogy minden szám negatív?
#5. Van-e a sorozatban olyan szám, amelyik 1 és 10 közé esik?
#6. Hány 18-cal osztható szám található a sorozatban?
#7. Mennyi a sorozatban található egyik legkisebb szám indexe?
#8. Írjuk ki a sorozatban található 17-tel vagy 18-cal osztható számok négyzetét!
#9. Van-e a sorozatban olyan negatív szám, amelynek az összes szomszédja pozitív?
#10. Igaz-e, hogy a sorozat szigorúan monoton növekvő?
#11. Válogassuk ki két listába a páros és a páratlan számokat!

import random

def feladat():
#szamok megvannak
    szamok = [random.randint(-60, 100) for i in range(50)]
    print(szamok)
#1.ossze szorzas
    szorzat = 1
    for szam in szamok:
        szorzat *= szam
    print(f'a sorozatban talalhato szamok szorzata:\n {szorzat}')
#2.utolso 5 v 7tel oszthato szam
    utolso_index = None
    for i in range(len(szamok)-1, -1, -1):
        if szamok[i] % 5 == 0 or szamok[i] % 7 == 0:
            utolso_index = i
            break
    print(utolso_index)
#3.elso 3 v 7tel oszthato
    utolso_index = None
    for i in range(len(szamok)):
        if szamok[i] % 3 == 0 and szamok[i] % 7 == 0:
            utolso_index = i
            break
    print(utolso_index)
#4.
    minden_negativ = all(szam < 0 for szam in szamok)

    if minden_negativ:
        print("Minden szám negatív.")
    else:
        print("Nem minden szám negatív.")
#5
    egy_es_tiz = all(1 <= szam <= 10 for szam in szamok)

    if egy_es_tiz:
        print("Van olyan ami 1 és 10 kozé esik.")
    else:
        print("Nincs olyan ami 1 és 10 kozé esik.")
#6
    oszthatok_18_cal = sum(1 for szam in szamok if szam % 18 == 0)
    print(f"A listában {oszthatok_18_cal} darab 18-cal osztható szám található.")
#7
    legkis = min(szamok)
    print(legkis)
#8
    for szam in szamok:
        if szam % 17 == 0 or szam % 18 == 0:
            print(f"A szám: {szam}, négyzete: {szam ** 2}")
#9
    for i in range(1, len(szamok) - 1):
        if szamok[i] < 0 and szamok[i - 1] > 0 and szamok[i + 1] > 0:
            print(f"A negatív szám: {szamok[i]}, szomszédjai: {szamok[i - 1]} és {szamok[i + 1]}")
            break
else:
    print("Nincs olyan negatív szám, amelynek minden szomszédja pozitív.")
# 10. Ellenőrzés, hogy a lista szigorúan monoton növekvő-e
    monoton_novekvo = all(szamok[i] < szamok[i+1] for i in range(len(szamok)-1))
    print("A lista szigorúan monoton növekvő:", monoton_novekvo)
# 11. Kiválogatás páros és páratlan számokra
    paros_szamok = [szam for szam in szamok if szam % 2 == 0]
    paratlan_szamok = [szam for szam in szamok if szam % 2 != 0]

# Eredmények kiíratása
    print("Páros számok:", paros_szamok)
    print("Páratlan számok:", paratlan_szamok)

feladat()