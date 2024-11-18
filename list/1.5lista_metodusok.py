nyelvek = ['Python', 'C', 'C++', 'Java']
def a():

    nyelvek2 = sorted(nyelvek)
    print(nyelvek)
    print(nyelvek2)

    nyelvek.sort()
    print(nyelvek2)

    nyelvek.reverse()
    print(nyelvek)


    print(nyelvek.index('C'))
    print(nyelvek.count('Python'))
    print('C++' in nyelvek)
def bfeladat():
    
    nyelvek.append('Python')
    print(nyelvek)
   
    # a listát másolja
    nyelvek_masolat = nyelvek.copy()
    print(nyelvek)
    
    # a lista végére hozzáfűz egy másik gyűjteményt (pl. listát)
    nyelvek_honlapkesziteshez = ['HTML', 'CSS', 'JavaScript']
    nyelvek.extend(nyelvek_honlapkesziteshez)
    print(nyelvek)
   
    # adott indexű helyre beszúrja a megadott elemet
    nyelvek.insert(1, 'Go')     
    print(nyelvek)
g
bfeladat