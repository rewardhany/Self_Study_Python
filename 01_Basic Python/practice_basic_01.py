# ======================================================
# PRACTICE BASIC 01
# ======================================================
# Fokus latihan:
# - input()
# - type casting
# - operator aritmatika
# - output dengan kalimat rapi
# ======================================================


# ------------------------------------------------------
# SOAL 1: UMUR 5 TAHUN LAGI
# ------------------------------------------------------
# Buat program yang:
# 1. Meminta input nama
# 2. Meminta input umur (dalam tahun)
# 3. Hitung umur pengguna 5 tahun lagi
# 4. Tampilkan hasilnya dalam 1 kalimat
#
# CONTOH INPUT:
# Nama  : Reffa
# Umur  : 20
#
# OUTPUT YANG DIHARAPKAN:
# Halo Reffa, umur kamu 5 tahun lagi adalah 25 tahun


# ------------------------------------------------------
# SOAL 2: UMUR DALAM BULAN
# ------------------------------------------------------
# Buat program yang:
# 1. Meminta input umur (dalam tahun)
# 2. Hitung umur dalam bulan
#
# PETUNJUK:
# - 1 tahun = 12 bulan
#
# CONTOH INPUT:
# Umur: 20
#
# OUTPUT YANG DIHARAPKAN:
# Umur kamu dalam bulan adalah 240 bulan


# ------------------------------------------------------
# SOAL 3: TAHUN KELAHIRAN
# ------------------------------------------------------
# Buat program yang:
# 1. Meminta input nama
# 2. Meminta input umur
# 3. Hitung tahun kelahiran
#
# PETUNJUK:
# - Gunakan tahun sekarang (hardcode, misalnya 2026)
#
# CONTOH INPUT:
# Nama: Reffa
# Umur: 20
#
# OUTPUT YANG DIHARAPKAN:
# Halo Reffa, kamu lahir pada tahun 2006


# ------------------------------------------------------
# SOAL 4: HITUNG TOTAL BELANJA
# ------------------------------------------------------
# Buat program yang:
# 1. Meminta input harga barang pertama
# 2. Meminta input harga barang kedua
# 3. Hitung total harga
#
# CONTOH INPUT:
# Harga 1: 15000
# Harga 2: 25000
#
# OUTPUT YANG DIHARAPKAN:
# Total belanja kamu adalah Rp40000


# ------------------------------------------------------
# SOAL 5: BAGI RATA
# ------------------------------------------------------
# Buat program yang:
# 1. Meminta input total uang
# 2. Meminta input jumlah orang
# 3. Hitung berapa uang yang diterima tiap orang
#
# CATATAN:
# - Gunakan pembagian
#
# CONTOH INPUT:
# Total uang : 100000
# Jumlah orang: 4
#
# OUTPUT YANG DIHARAPKAN:
# Setiap orang mendapatkan Rp25000


# ------------------------------------------------------
# SOAL 6 (BONUS): KONVERSI SUHU
# ------------------------------------------------------
# Buat program yang:
# 1. Meminta input suhu dalam Celcius
# 2. Konversi ke Fahrenheit
#
# RUMUS:
# Fahrenheit = (Celcius * 9 / 5) + 32
#
# CONTOH INPUT:
# Celcius: 30
#
# OUTPUT YANG DIHARAPKAN:
# Suhu dalam Fahrenheit adalah 86

# YOUR CODE STARTS HERE !

# ==== QUESTION NO 1 ====
print("== QUESTION NO 1 ==")
name = input("Enter your name: ")
age = int(input("Enter your age: "))

age = age + 5
print(f"Hello {name}, your age in 5 years later will be {age} years old!")
print()

# ==== QUESTION NO 2 ====
print("== QUESTION NO 2 ==")
age_months = int(input("Enter your age here: "))
age_months = age_months * 12

print(f"Your age in months is {age_months} months !")
print()

# ==== QUESTION NO 3 ====
print("== QUESTION NO 3 ==")
nama = input("Enter your name here: ")
umur = int(input("Enter your age here: "))
year = 2026
umur = year - umur

print(f"Hello {nama}, you were born in {umur}")
print()

# === QUESTION NO 4 ===
print("== QUESTION NO 4 ==")

barang_pertama = int(input("Harga barang pertama: "))
barang_kedua = int(input("Harga barang kedua: "))

print(barang_pertama + barang_kedua)
print()

# == QUESTION NO 5 ==
print("== QUESTION NO 5 ==")

money_total = int(input("Total uang: "))
person_total = int(input("Jumlah orang: "))
money_received = money_total / person_total

print("Setiap orang mendapatkan: Rp", money_received)
print()

# == QUESTION NO 6 ==
print("== QUESTION NO 6 BONUS ==")

suhu = int(input("Masukkan suhu: "))
hasil = (suhu * 9 / 5) + 32

print(f"Suhu dalam fahrenheit adalah: {hasil}")