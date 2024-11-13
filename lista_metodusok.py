nyelvek = ['Python', 'C', 'C++', 'Java']
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