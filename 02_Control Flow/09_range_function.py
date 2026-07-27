# ======================================================
# 09_range_function.py
# MATERI: RANGE FUNCTION
# ======================================================
#
# range() adalah function bawaan Python yang
# menghasilkan urutan angka.
#
# Sangat sering dipakai bersama for loop.
#
# Ada 3 cara pakai range():
#
#   range(stop)
#   range(start, stop)
#   range(start, stop, step)
#
# ======================================================


# ------------------------------------------------------
# 1. range(stop) — MULAI DARI 0
# ------------------------------------------------------
#
# Menghasilkan angka dari 0 sampai (stop - 1)

for i in range(5):
    print(i, end=" ")
# Output: 0 1 2 3 4
# INGAT: angka 5 tidak termasuk!

# Bayangkan seperti:
# range(5) → [0, 1, 2, 3, 4]


# ------------------------------------------------------
# 2. range(start, stop) — TENTUKAN TITIK AWAL
# ------------------------------------------------------
#
# Mulai dari start, sampai (stop - 1)

print()
for i in range(1, 6):
    print(i, end=" ")
# Output: 1 2 3 4 5

print()
for i in range(3, 8):
    print(i, end=" ")
# Output: 3 4 5 6 7


# ------------------------------------------------------
# 3. range(start, stop, step) — TENTUKAN LANGKAH
# ------------------------------------------------------
#
# Naik/turun sesuai nilai step

# Loncat 2
print()
for i in range(0, 11, 2):
    print(i, end=" ")
# Output: 0 2 4 6 8 10

# Loncat 5
print()
for i in range(0, 51, 5):
    print(i, end=" ")
# Output: 0 5 10 15 20 25 30 35 40 45 50

# HITUNG MUNDUR (step negatif)
print()
for i in range(10, 0, -1):
    print(i, end=" ")
# Output: 10 9 8 7 6 5 4 3 2 1

# Hitung mundur dari 10 ke 0
print()
for i in range(10, -1, -1):
    print(i, end=" ")
# Output: 10 9 8 7 6 5 4 3 2 1 0


# ------------------------------------------------------
# 4. LIHAT ISI RANGE DENGAN list()
# ------------------------------------------------------
#
# range() tidak langsung berisi list.
# Bisa konversi ke list untuk melihat isinya.

print()
print(list(range(5)))          # [0, 1, 2, 3, 4]
print(list(range(1, 6)))       # [1, 2, 3, 4, 5]
print(list(range(0, 10, 3)))   # [0, 3, 6, 9]


# ------------------------------------------------------
# 5. PAKAI INDEX DENGAN RANGE
# ------------------------------------------------------
#
# Cara pakai range untuk akses elemen list dengan index

nama = ["Andi", "Budi", "Cika", "Dani"]

for i in range(len(nama)):
    print(f"No. {i+1} → {nama[i]}")

# Output:
# No. 1 → Andi
# No. 2 → Budi
# No. 3 → Cika
# No. 4 → Dani

# len(nama) = 4
# range(4)  = 0, 1, 2, 3
# Cocok untuk akses nama[0], nama[1], nama[2], nama[3]


# ------------------------------------------------------
# 6. RANGE UNTUK PERULANGAN N KALI
# ------------------------------------------------------
#
# Kalau tidak butuh nilai i-nya, pakai _ (underscore)
# Konvensi Python untuk "variabel yang tidak dipakai"

print()
for _ in range(3):
    print("Selamat datang!")

# Output:
# Selamat datang!
# Selamat datang!
# Selamat datang!


# ======================================================
# LATIHAN
# ======================================================
#
# 1. Tampilkan bilangan ganjil dari 1 sampai 19
#    menggunakan range() dengan step
#
# 2. Hitung jumlah total dari 1 sampai 100
#    (jawaban yang benar: 5050)
#    Gunakan range() dan akumulasi
#
# 3. Tampilkan tabel pangkat dua dari 1 sampai 10:
#    1² = 1
#    2² = 4
#    3² = 9
#    ... dst
#
# Tulis jawaban di sini: