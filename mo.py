# Nama File: mo.py
# Pembuat: Raka
# Tanggal: 7 September 2026
# Deskripsi: Menghitung Mean Olympique dari 4 bilangan

# Definisi dan Spesifikasi
# mo: 4 integer > 0 -> real
#     mo(u,v,w,x) menghitung rata-rata dari dua buah bilangan
#     integer, yang bukan maksimum dan bukan minimum
#     dari 4 buah integer.

# max2: 2 integer > 0 -> integer
#        max2(a,b) menentukan maksimum dari 2 bilangan integer

# min2: 2 integer > 0 -> integer
#        min2(a,b) menentukan minimum dari 2 bilangan integer

# max4: 4 integer > 0 -> integer
#        max4(i,j,k,l) menentukan maksimum dari 4 bilangan integer

# min4: 4 integer > 0 -> integer
#        min4(i,j,k,l) menentukan minimum dari 4 bilangan integer

# Realisasi
def max2(a: int, b: int) -> int:
    return (a + b + abs(a - b)) / 2

def min2(a: int, b: int) -> int:
    return (a + b - abs(a - b)) / 2

def max4(i: int, j: int, k: int, l: int) -> int:
    return max2(max2(i, j), max2(k, l))

def min4(i: int, j: int, k: int, l: int) -> int:
    return min2(min2(i, j), min2(k, l))

def mo(u: int, v: int, w: int, x: int) -> float:
    return (u + v + w + x - min4(u, v, w, x) - max4(u, v, w, x)) / 2

# Aplikasi
print(mo(8, 12, 10, 20))