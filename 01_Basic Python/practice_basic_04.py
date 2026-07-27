# ======================================================
# PRACTICE BASIC 04
# ======================================================
# Fokus latihan:
# - Membuat fungsi (def)
# - Parameter
# - Return value
# - Memanggil fungsi
# - Input & output
# ======================================================


# ------------------------------------------------------
# SOAL 1: LUAS PERSEGI PANJANG
# ------------------------------------------------------
# Buat sebuah fungsi bernama:
#   hitung_luas_persegi_panjang
#
# FUNGSI TERSEBUT:
# - Menerima 2 parameter: panjang dan lebar
# - Mengembalikan (return) nilai luas
#
# PROGRAM UTAMA:
# 1. Minta input panjang dan lebar
# 2. Panggil fungsi
# 3. Tampilkan hasil luas
#
# CONTOH INPUT:
# Panjang: 10
# Lebar  : 5
#
# OUTPUT YANG DIHARAPKAN:
# Luas persegi panjang adalah: 50


# ------------------------------------------------------
# SOAL 2: LUAS PERSEGI
# ------------------------------------------------------
# Buat sebuah fungsi bernama:
#   hitung_luas_persegi
#
# FUNGSI TERSEBUT:
# - Menerima 1 parameter: sisi
# - Mengembalikan nilai luas
#
# PROGRAM UTAMA:
# 1. Minta input sisi
# 2. Panggil fungsi
# 3. Tampilkan hasilnya
#
# CONTOH INPUT:
# Sisi: 6
#
# OUTPUT YANG DIHARAPKAN:
# Luas persegi adalah: 36


# ------------------------------------------------------
# SOAL 3: KELILING PERSEGI PANJANG
# ------------------------------------------------------
# Buat sebuah fungsi bernama:
#   hitung_keliling_persegi_panjang
#
# FUNGSI TERSEBUT:
# - Menerima 2 parameter: panjang dan lebar
# - Mengembalikan nilai keliling
#
# RUMUS:
# Keliling = 2 * (panjang + lebar)
#
# CONTOH INPUT:
# Panjang: 8
# Lebar  : 4
#
# OUTPUT YANG DIHARAPKAN:
# Keliling persegi panjang adalah: 24


# ------------------------------------------------------
# SOAL 4: KONVERSI CELCIUS KE FAHRENHEIT
# ------------------------------------------------------
# Buat sebuah fungsi bernama:
#   celcius_ke_fahrenheit
#
# FUNGSI TERSEBUT:
# - Menerima 1 parameter: suhu_celcius
# - Mengembalikan suhu dalam fahrenheit
#
# RUMUS:
# Fahrenheit = (Celcius * 9 / 5) + 32
#
# CONTOH INPUT:
# Celcius: 30
#
# OUTPUT YANG DIHARAPKAN:
# Suhu dalam Fahrenheit adalah: 86


# ------------------------------------------------------
# SOAL 5 (BONUS): HITUNG TOTAL & RATA-RATA
# ------------------------------------------------------
# Buat dua fungsi:
#
# 1. hitung_total
#    - Menerima 3 parameter angka
#    - Mengembalikan totalnya
#
# 2. hitung_rata_rata
#    - Menerima total dan jumlah data
#    - Mengembalikan nilai rata-rata
#
# PROGRAM UTAMA:
# 1. Minta input 3 angka
# 2. Panggil fungsi hitung_total
# 3. Panggil fungsi hitung_rata_rata
# 4. Tampilkan hasil total dan rata-rata
#
# CONTOH INPUT:
# Angka 1: 10
# Angka 2: 20
# Angka 3: 30
#
# OUTPUT YANG DIHARAPKAN:
# Total: 60
# Rata-rata: 20

# === QUESTION NO 1 ===
# A = l x w
print("== QUESTION NO 1 ==")

length = float(input("Enter length: "))
width = float(input("Enter width: "))
result = length * width
print("Area is: ", result)

print("===========")

def menyapa():
    print("welcome to hyperOS!")
menyapa()

print("======")

def tambah(a, b):
    hasil = a + b
    print(hasil)
    return hasil

x = tambah(5, 5)

print("Isi x =", x)

print("=======")
def luas_persegi_panjang(length, width):
    return length * width

length = float(input("Enter length: "))
width = float(input("Enter width: "))

print("Rectangle Area: ", luas_persegi_panjang(length, width))

