# Nama File: isorigin.py
# Pembuat: Raka
# Tanggal: 7 September 2026
# Deskripsi: Menentukan apakah dua bilangan x dan y
#            merupakan titik origin (0,0)

# Definisi dan Spesifikasi
# is_origin: 2 real -> boolean
#     is_origin(x,y) benar jika (x,y) merupakan titik origin (0,0)

# Realisasi
def is_origin(x: float, y: float) -> bool:
    return x == 0 and y == 0

# Aplikasi
print(is_origin(1, 0))
print(is_origin(1, 1))
print(is_origin(0, 0))