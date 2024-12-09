import random 

def otos_lotto():
    megadott_szamok = []
    while True:
            if len(megadott_szamok) == 5:
                break
            szam = int(input("\nAdj meg egy számot!"))
            
            if szam < 1 or szam > 91:
                print("Ez a szám nem megfelelő vagy már megadtad.")
            
            elif szam in megadott_szamok:
                print("Ez a szám nem megfelelő vagy már megadtad.")
            
            else:
                megadott_szamok.append(szam)
    print(f"A választott számaid:  {megadott_szamok}")



otos_lotto()