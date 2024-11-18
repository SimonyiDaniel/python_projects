nyelvek = ['Python', 'C', 'C++', 'Java']

# eltávolítja a legutolsó elemet, és azzal tér vissza
# itt például a törölt értéket a 'torolt_nyelv' fogja tartalmazni
nyelvek.pop()
torolt_nyelv = nyelvek.pop()
print(f"torolt nyev{torolt_nyelv}")

# eltávolítja a megadott indexű elemet,  és azzal tér vissza
nyelvek.pop(1)
print(nyelvek)

# eltávolítja a megadott elemet az elsőként megtalált pozícióból
nyelvek.remove('Python')
print(nyelvek)

# törli a listát
nyelvek.clear()
print(nyelvek)
