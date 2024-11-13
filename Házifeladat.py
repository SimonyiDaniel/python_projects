def hazi()
    szavak = []

    while True:
        szo = input("Adj meg egy szót (ENTER a befejezéshez): ").strip( )
        
        if szo == "":
            break
        
        if szo[0] == 'a' or szo[0] == 'A':
            szavak.append(szo)


    print("A begyűjtött szavak:", szavak)