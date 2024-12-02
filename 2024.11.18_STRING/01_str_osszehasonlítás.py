
sztring = 'Ismered ezt a számot?'

# Index-szel hivatkozhatunk egy elemükre
print(sztring[0])      # I
print(sztring[-1])     # ?

# Szeletelhetjük ezeket is 
print(sztring[2:11])
print(sztring[:9])
print(sztring[7:])

# Meghatározhatjuk a hosszukat
print(len(sztring))

# for-ciklussal is bejárhatóak
for betu in sztring:
    if betu == 'e' or betu == 'E':
        szamlalo += 1
print(f'A sztringben {szamlalo} db e/E betű van.')

# Ezeknél is használható az in operátor
if 'e' in sztring:
    print('Van benne e betű.')
else:
    print('Nincs benne e betű.') 
