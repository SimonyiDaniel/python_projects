import random 
def otos_lotto():
 
    nyero_szamok = random.sample(range(1, 91), 5)
    talalatok = 0
    megadott_szamok = []
    while True:
            if len(megadott_szamok) == 5:
                break
            szam = int(input("\nAdj meg egy számot!(1-90): "))
            
            if szam < 1 or szam > 90:
                print("Ez a szám nem megfelelő vagy már megadtad.")
            
            elif szam in megadott_szamok:
                print("Ez a szám nem megfelelő vagy már megadtad.")
            
            else:
                megadott_szamok.append(szam)

            if szam in nyero_szamok:
                talalatok += 1
    print(f"A választott számaid:  {megadott_szamok}")
    
    print(f"A nyerő számok: {nyero_szamok}")
    print(f"Ennyi számot találtál el: {talalatok} ennyi pénz jár érte:{talalatok * "💵💵💵💵💵💵"}")

def hatos_lotto():
 
    nyero_szamok = random.sample(range(1, 45), 6)
    talalatok = 0
    megadott_szamok = []
    while True:
            if len(megadott_szamok) == 6:
                break
            szam = int(input("\nAdj meg egy számot!(1-45): "))
            
            if szam < 1 or szam > 46:
                print("Ez a szám nem megfelelő vagy már megadtad.")
            
            elif szam in megadott_szamok:
                print("Ez a szám nem megfelelő vagy már megadtad.")
            
            else:
                megadott_szamok.append(szam)

            if szam in nyero_szamok:
                talalatok += 1
    print(f"A választott számaid:  {megadott_szamok}")
    
    print(f"A nyerő számok: {nyero_szamok}")
    print(f"Ennyi számot találtál el: {talalatok} ennyi pénz jár érte:{talalatok * "💵💵💵"}")



def jatek_valasztasa():
    
    jatek_valasztas = int(input("\nVálassz egy játékot: 1 (ötös lottó) vagy 2 (hatos lottó): "))  
    
    if jatek_valasztas == 1:
        otos_lotto()

    elif jatek_valasztas == 2:
        hatos_lotto()

    else:
        print("Kérlek az rendelkezésre álló 2 játék módból válassz!")
        jatek_valasztasa()

menet = input("Mehet a lottó? (igen vagy nem): ")
if menet == "igen":
    jatek_valasztasa()
elif menet == "nem":
    print("ok👍")
else:
    print("Nem értelek!")