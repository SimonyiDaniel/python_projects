'''A program tároljon egy listában színeket. Kérjen be a felhasználótól egy színt, és állapítsa meg, hogy a megadott szín már szerepel-e az adott listában. A vizsgálat eredményéről tájékoztassa a program a felhasználót, és írja ki egymás mellé vesszővel elválasztva a lista által tartalmazott színeket!'''

szinek = ()

megadott_szín = input('Adj meg egy színt')
if megadott_szín in szinek:
    print (f'A megadott szín, {megadott_szín} szerepel a listában')
else:
    print(f'A megadott szín, {megadott_szín} NEM sterepel a listában')