"""Szimuláljuk egy 20 oldalú D&D kocka 100 db dobását! A dobásokat egy listában tároljuk! Majd oldjuk meg a következő feladatokat!
Minden feladat előtt a program írja ki a feladat sorszámát!

1. Volt-e 6-os a dobások között?
2. Hányadikra sikerült először 18-nál nagyobbat dobni?
3. Hány darab 1-est dobtak?
4. Melyik volt a legnagyobb dobás a 10-nél kisebbek közül, és hányadik dobás volt?
5. Mennyi a 4-es dobások szorzata?
"""

import random

dobasok = [random.randint(1, 20) for i in range(100)]
print(dobasok)


def elso_feladat():
    if 6 in dobasok:
        print('Volt hatos a dobások között')
    else:
        print('A dobásokk között nem volt hatos')

def masodik_feladat():
    tizennyolc = None
    for i in range(len(dobasok)):
        if dobasok[i] >= 18:
            tizennyolc = i+1
            break
    print(f'{tizennyolc}. szám az nagyobb vagy egyenlő mint 18')

def harmadik_feladat():
    darab_egyes = 0
    for i in range(len(dobasok)):
        if dobasok[i] == 1:
            darab_egyes += 1

    print(f'{darab_egyes} darab 1es van a dobások között')

#. Melyik volt a legnagyobb dobás a 10-nél kisebbek közül, és hányadik dobás volt?
def negyedik_feladat():
    tiznel_kisebb = 0
    for i in dobasok:
        if 10 > i and i > tiznel_kisebb:
            tiznel_kisebb = i
    print(f'{dobasok.index(tiznel_kisebb) + 1}. szam az és az a ->{tiznel_kisebb}')

def otodik_feladat():
    darab_negyes_szorzat = 1
    for i in dobasok:
        if i == 4:
            darab_negyes_szorzat *= 4
    print(f'{darab_negyes_szorzat}a 4-es szamok szorzata')

elso_feladat()
masodik_feladat()
harmadik_feladat()
negyedik_feladat()
otodik_feladat()