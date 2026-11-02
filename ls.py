# Nama File: ls.py
# Pembuat: Raka
# Tanggal: 7 September 2026
# Deskripsi: Menghitung jarak antara dua titik pada
#            koordinat kartesian

# Definisi dan Spesifikasi
# ls: 4 real -> real
#     ls(x1,y1,x2,y2) adalah jarak antara dua buah titik
#     (x1,y1) dengan (x2,y2)

# dif2: 2 real -> real
#       dif2(x,y) adalah kuadrat dari selisih antara x dan y

# fx2: real -> real
#      fx2(x) adalah hasil kuadrat dari x

# Realisasi
def fx2(x: float) -> float:
    return x * x

def dif2(x: float, y: float) -> float:
    return fx2(x - y)

def ls(x1: float, y1: float, x2: float, y2: float) -> float:
    return (dif2(y2, y1) + dif2(x2, x1)) ** 0.5

# Aplikasi
print(ls(1, 3, 5, 6))