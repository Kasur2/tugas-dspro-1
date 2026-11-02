# Nama File: isvalid.py
# Pembuat: Raka
# Tanggal: 7 September 2026
# Deskripsi: Menentukan apakah suatu bilangan valid

# Definisi dan Spesifikasi
# is_valid: integer -> boolean
#     is_valid(x) benar jika x lebih kecil dari 5
#     atau lebih besar dari 500

# Realisasi
def is_valid(x: int) -> bool:
    return x < 5 or x > 500

# Aplikasi
print(is_valid(5))
print(is_valid(0))
print(is_valid(500))
print(is_valid(6000))