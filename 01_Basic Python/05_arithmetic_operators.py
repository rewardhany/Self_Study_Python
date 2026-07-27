# ======================================================
# 05_arithmetic_operators.py
# ======================================================
# Di file ini kita akan belajar:
# 1. Operator aritmatika di Python (angka)
# 2. Operator aritmatika pada string
# 3. Operator membership pada string (in, not in)
# 4. Shortcut operator (assignment)
# 5. Operasi dengan input
# 6. Urutan operasi (operator precedence)
# 7. Fungsi matematika dasar
# ======================================================


# ------------------------------------------------------
# OPERATOR ARITMATIKA (ANGKA)
# ------------------------------------------------------
# +  -> penjumlahan
# -  -> pengurangan
# *  -> perkalian
# /  -> pembagian (hasil float)
# // -> pembagian bulat
# %  -> modulus (sisa bagi)
# ** -> pangkat

a = 10
b = 3


# ------------------------------------------------------
# CONTOH OPERASI ARITMATIKA
# ------------------------------------------------------
print("Penjumlahan:", a + b)
print("Pengurangan:", a - b)
print("Perkalian:", a * b)
print("Pembagian:", a / b)
print("Pembagian bulat:", a // b)
print("Sisa bagi:", a % b)
print("Pangkat:", a ** b)


# ------------------------------------------------------
# OPERATOR ARITMATIKA DENGAN NEGATIF & UNARY
# ------------------------------------------------------
# Unary minus (-) digunakan untuk membalik tanda

x = 5
print("Nilai x:", x)
print("Nilai -x:", -x)


# ------------------------------------------------------
# OPERATOR ARITMATIKA PADA STRING
# ------------------------------------------------------
# Catatan penting:
# - String TIDAK bisa dikurang, dibagi, atau dipangkatkan
# - String hanya mendukung:
#   1. + (penggabungan / concatenation)
#   2. * (pengulangan / repetition)

nama_depan = "Reffa"
nama_belakang = "Wardany"

# Penggabungan string
nama_lengkap = nama_depan + " " + nama_belakang
print("Nama lengkap:", nama_lengkap)

# Pengulangan string
print("Halo! " * 3)


# ------------------------------------------------------
# PERBEDAAN OPERATOR + PADA ANGKA DAN STRING
# ------------------------------------------------------
print(10 + 5)        # penjumlahan angka
print("10" + "5")    # penggabungan string

# print("10" + 5)    # ERROR: string tidak bisa digabung dengan angka


# ------------------------------------------------------
# OPERATOR STRING: MEMBERSHIP (in & not in)
# ------------------------------------------------------
# Digunakan untuk mengecek apakah suatu teks
# ADA atau TIDAK ADA di dalam string lain

kalimat = "saya sedang belajar python"

print("python" in kalimat)     # True
print("java" in kalimat)       # False
print("java" not in kalimat)   # True


# ------------------------------------------------------
# CONTOH PENGGUNAAN OPERATOR in
# ------------------------------------------------------
kata = input("Masukkan sebuah kata: ")

if "python" in kata:
    print("Kata mengandung 'python'")
else:
    print("Kata tidak mengandung 'python'")


# ------------------------------------------------------
# OPERATOR ASSIGNMENT (SHORTCUT)
# ------------------------------------------------------
# Operator ini mempersingkat operasi matematika

nilai = 10

nilai += 5    # nilai = nilai + 5
print("+= :", nilai)

nilai -= 3    # nilai = nilai - 3
print("-= :", nilai)

nilai *= 2    # nilai = nilai * 2
print("*= :", nilai)

nilai //= 4   # nilai = nilai // 4
print("//= :", nilai)


# ------------------------------------------------------
# OPERASI MATEMATIKA DENGAN INPUT
# ------------------------------------------------------
# input() selalu menghasilkan STRING
# maka harus dikonversi ke int atau float

angka1 = int(input("Masukkan angka pertama: "))
angka2 = int(input("Masukkan angka kedua: "))

hasil = angka1 + angka2
print("Hasil penjumlahan:", hasil)


# ------------------------------------------------------
# URUTAN OPERASI (OPERATOR PRECEDENCE)
# ------------------------------------------------------
# Python memiliki aturan prioritas operasi.
# Operasi dengan prioritas lebih tinggi
# akan dikerjakan TERLEBIH DAHULU.
#
# Urutan prioritas dari yang tertinggi:
# 1. ()        -> tanda kurung (dipaksa duluan)
# 2. **        -> pangkat
# 3. * / // %  -> perkalian, pembagian, sisa bagi
# 4. + -       -> penjumlahan, pengurangan
#
# Jika ragu, SELALU gunakan tanda kurung ()
# agar hasil perhitungan jelas dan aman.

# Tanpa tanda kurung
hasil1 = 2 + 3 * 4
# Python hitung: 3 * 4 = 12, lalu 2 + 12 = 14

# Dengan tanda kurung
hasil2 = (2 + 3) * 4
# Python hitung: 2 + 3 = 5, lalu 5 * 4 = 20

print("Tanpa kurung:", hasil1)
print("Pakai kurung:", hasil2)


# ------------------------------------------------------
# FUNGSI MATEMATIKA DASAR BAWAAN
# ------------------------------------------------------
# abs()    -> nilai absolut
# pow()    -> pangkat
# round()  -> pembulatan

print("Abs(-10):", abs(-10))
print("Pow(2, 3):", pow(2, 3))
print("Round(3.6):", round(3.6))

# ------------------------------------------------------
# PEMAHAMAN MODULUS: APA ITU MODULUS (%) ?
# ------------------------------------------------------
# Modulus (%) adalah operator untuk mengambil
# SISA dari hasil pembagian.

# Contoh:
print(10 % 3)  # Output: 1
# Penjelasan:
# 10 dibagi 3 = 3 (sisa 1)

print(8 % 2)   # Output: 0
# 8 dibagi 2 = 4 (sisa 0)


# ------------------------------------------------------
# A. ILUSTRASI SEDERHANA
# ------------------------------------------------------
# Bayangkan kamu punya 10 permen dan mau dibagi ke 3 orang
# masing-masing dapat 3, sisa 1 → itulah modulus

# 10 % 3 = 1


# ------------------------------------------------------
# B. KENAPA SERING PAKAI % 2 ?
# ------------------------------------------------------
# Karena 2 adalah pembagi untuk menentukan GENAP / GANJIL

# ATURANNYA:
# - Jika sisa bagi = 0 → GENAP
# - Jika sisa bagi = 1 → GANJIL


# ------------------------------------------------------
# C. MAKSUD DARI: angka % 2 == 0
# ------------------------------------------------------
# Artinya:
# "Apakah angka ini habis dibagi 2 tanpa sisa?"

angka = 6

print(angka % 2)        # Output: 0
print(angka % 2 == 0)   # Output: True


# Penjelasan step-by-step:
# 6 % 2 = 0  (tidak ada sisa)
# 0 == 0 → True
# Jadi 6 adalah bilangan GENAP


# ------------------------------------------------------
# D. CONTOH GENAP / GANJIL
# ------------------------------------------------------
angka = 7

if angka % 2 == 0:
    print("Genap")
else:
    print("Ganjil")

# Output: Ganjil


# ------------------------------------------------------
# E. CONTOH LAIN MODULUS
# ------------------------------------------------------

# A. Mengecek kelipatan
angka = 15

if angka % 5 == 0:
    print("Kelipatan 5")

# B. Cek kelipatan 3
if angka % 3 == 0:
    print("Kelipatan 3")


# ------------------------------------------------------
# F. MODULUS DENGAN ANGKA NEGATIF
# ------------------------------------------------------
print(-7 % 3)  
# Output: 2
# Python tetap menghasilkan sisa positif


# ------------------------------------------------------
# G. MODULUS DALAM TERNARY
# ------------------------------------------------------
angka = 10

hasil = "Genap" if angka % 2 == 0 else "Ganjil"
print(hasil)


# ------------------------------------------------------
# H. LATIHAN
# ------------------------------------------------------

# 1. Tentukan apakah angka 12 genap atau ganjil
angka = 12
print("Genap" if angka % 2 == 0 else "Ganjil")

# 2. Cek apakah 20 kelipatan 4
angka = 20
print("Kelipatan 4" if angka % 4 == 0 else "Bukan kelipatan 4")

# 3. Cek apakah 17 habis dibagi 5
angka = 17
print("Habis dibagi 5" if angka % 5 == 0 else "Tidak habis dibagi 5")


# ------------------------------------------------------
# 11. RANGKUMAN
# ------------------------------------------------------
# - % = modulus (sisa pembagian)
# - angka % 2 == 0 → GENAP
# - angka % 2 == 1 → GANJIL
# - Digunakan untuk:
#   ✔ cek genap/ganjil
#   ✔ cek kelipatan
#   ✔ logika kondisi
# ======================================================

# ------------------------------------------------------
# CATATAN PENTING
# ------------------------------------------------------
# - Operator in & not in BUKAN arithmetic operator
# - Tapi masih termasuk OPERATOR di Python
# - Sangat sering dipakai saat:
#   - validasi input
#   - pencarian teks
#   - filtering data


# ------------------------------------------------------
# LATIHAN
# ------------------------------------------------------
# 1. Buat program kalkulator sederhana:
#    - penjumlahan
#    - pengurangan
#    - perkalian
#    - pembagian
#
# 2. Buat program menghitung:
#    - luas persegi
#    - luas persegi panjang
#
# 3. Buat program:
#    - input nama
#    - tampilkan nama tersebut 5 kali
#
# 4. Coba tebak hasil dari operasi berikut:
#    10 + 2 * 3 ** 2
