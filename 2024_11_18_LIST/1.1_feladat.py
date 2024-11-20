nevek =[]
folytat = true
wihle folytat:
    nev = input("kérlek adj meg egy keresztnevet: ")
    if nev == "":
        break
    nevek.append(nev)
    
print(nevek)