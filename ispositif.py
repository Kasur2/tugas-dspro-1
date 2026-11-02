# Nama File: ispositif.py
# Pembuat: Muhammad Taraka Pramudya
# Tanggal: 7 September 2026
# Deskripsi: Menentukan apakah suatu bilangan positif

# Definisi dan Spesifikasi
# is_positif: integer -> boolean
#     is_positif(x) benar jika x positif

# Realisasi
def is_positif(x: int) -> bool:
    return x >= 0

# Aplikasi
print(is_positif(1))
print(is_positif(0))
print(is_positif(-1))