# ======================================================
# 07_assignment_and_ternary.py
# ======================================================
# Di file ini kita akan belajar:
# 1. Assignment (penugasan nilai)
# 2. Assignment operator (+=, -=, dll)
# 3. Ternary operator (if satu baris)
# ======================================================


# ------------------------------------------------------
# ASSIGNMENT DASAR
# ------------------------------------------------------
# Assignment artinya memberi nilai ke sebuah variabel
# Tanda "=" digunakan untuk menyimpan nilai

x = 10
print("Nilai awal x:", x)


# ------------------------------------------------------
# ASSIGNMENT OPERATOR
# ------------------------------------------------------
# Assignment operator digunakan untuk mempersingkat penulisan

# x = x + 5
x += 5      # Sama dengan x = x + 5
print("Setelah x += 5:", x)

# x = x - 3
x -= 3
print("Setelah x -= 3:", x)

# x = x * 2
x *= 2
print("Setelah x *= 2:", x)

# x = x / 4
x /= 4
print("Setelah x /= 4:", x)


# ------------------------------------------------------
# CONTOH PENGGUNAAN DI PROGRAM
# ------------------------------------------------------
saldo = 100000

# Menambah saldo
saldo += 50000
print("Saldo sekarang:", saldo)

# Mengurangi saldo
saldo -= 20000
print("Saldo sekarang:", saldo)

# ======================================================
# TERNARY OPERATOR (PYTHON)
# ======================================================

# ------------------------------------------------------
# 1. PENGERTIAN
# ------------------------------------------------------
# Ternary operator adalah cara singkat untuk menulis
# percabangan (if-else) dalam satu baris.
#
# Digunakan ketika kondisi sederhana dan hanya
# menghasilkan dua kemungkinan nilai.

# Format dasar:
# nilai_jika_true if kondisi else nilai_jika_false


# ------------------------------------------------------
# 2. CONTOH DASAR
# ------------------------------------------------------
umur = 20

status = "Dewasa" if umur >= 18 else "Belum Dewasa"
print("Status:", status)
# Output: Status: Dewasa


# ------------------------------------------------------
# 3. PERBANDINGAN DENGAN IF BIASA
# ------------------------------------------------------

# IF BIASA:
umur = 16

if umur >= 18:
    status = "Dewasa"
else:
    status = "Belum Dewasa"

print("IF BIASA:", status)


# TERNARY:
umur = 16

status = "Dewasa" if umur >= 18 else "Belum Dewasa"
print("TERNARY:", status)
12
# ------------------------------------------------------
# 4. MENGGUNAKAN INPUT USER
# ------------------------------------------------------
umur = int(input("Masukkan umur: "))

status = "Dewasa" if umur >= 18 else "Belum Dewasa"
print("Status kamu:", status)


# ------------------------------------------------------
# 5. CONTOH LAIN (GENAP / GANJIL)
# ------------------------------------------------------
angka = 7

hasil = "Genap" if angka % 2 == 0 else "Ganjil"
print("Angka tersebut:", hasil)


# ------------------------------------------------------
# 6. TERNARY DENGAN OPERASI MATEMATIKA
# ------------------------------------------------------
nilai = 80

bonus = 10 if nilai >= 75 else 0
total = nilai + bonus

print("Total nilai:", total)


# ------------------------------------------------------
# 7. TERNARY BERTINGKAT (NESTED TERNARY)
# ------------------------------------------------------
# Bisa digunakan untuk lebih dari 2 kondisi,
# tapi harus hati-hati karena bisa membingungkan.

nilai = 85

hasil = (
    "A" if nilai >= 90 else
    "B" if nilai >= 80 else
    "C" if nilai >= 70 else
    "D"
)

print("Grade:", hasil)


# ------------------------------------------------------
# 8. TERNARY DENGAN TIPE DATA BERBEDA
# ------------------------------------------------------
# Bisa mengembalikan tipe data berbeda

umur = 17

info = "Boleh buat KTP" if umur >= 17 else None
print("Info:", info)


# ------------------------------------------------------
# 9. TERNARY DALAM LIST
# ------------------------------------------------------
# Bisa digunakan dalam list comprehension

angka_list = [1, 2, 3, 4, 5]

hasil = ["Genap" if x % 2 == 0 else "Ganjil" for x in angka_list]
print("Hasil list:", hasil)


# ------------------------------------------------------
# 10. KAPAN SEBAIKNYA MENGGUNAKAN TERNARY?
# ------------------------------------------------------
# Gunakan ternary jika:
# - Kondisi sederhana
# - Hanya ada 2 kemungkinan hasil
#
# Jangan gunakan jika:
# - Logika kompleks
# - Banyak kondisi (lebih baik pakai if biasa)


# ------------------------------------------------------
# 11. LATIHAN DASAR
# ------------------------------------------------------

# 1. Buat variabel nilai = 70
nilai = 70

# Tambahkan 10 menggunakan assignment operator
nilai += 10

# 2. Gunakan ternary operator
status = "LULUS" if nilai >= 75 else "TIDAK LULUS"

print("Nilai akhir:", nilai)
print("Status:", status)


# ------------------------------------------------------
# 12. LATIHAN TAMBAHAN
# ------------------------------------------------------

# A. Cek bilangan positif / negatif
angka = -5
hasil = "Positif" if angka >= 0 else "Negatif"
print("Bilangan:", hasil)

# B. Diskon belanja
total_belanja = 120000

diskon = 0.1 if total_belanja >= 100000 else 0
print("Diskon:", diskon)

# C. Password sederhana
password = "admin123"

akses = "Login Berhasil" if password == "admin123" else "Login Gagal"
print(akses)


# ------------------------------------------------------
# 13. RANGKUMAN
# ------------------------------------------------------
# - Ternary operator = versi singkat if-else
# - Cocok untuk kondisi sederhana
# - Membuat kode lebih ringkas
# - Hindari jika terlalu kompleks
#
# Format utama:
# hasil = nilai_true if kondisi else nilai_false
# ======================================================