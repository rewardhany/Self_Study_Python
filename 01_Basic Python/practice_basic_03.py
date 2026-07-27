# ======================================================
# PRACTICE BASIC 03
# ======================================================
# Fokus latihan:
# - input()
# - type casting
# - operator perbandingan
# - operator logika
# - ternary operator
# ======================================================


# ------------------------------------------------------
# SOAL 1: KATEGORI USIA
# ------------------------------------------------------
# Buat program yang:
# 1. Meminta input umur
# 2. Gunakan TERNARY OPERATOR untuk menentukan kategori usia
#
# KETENTUAN:
# - Umur < 13        -> "Anak-anak"
# - Umur 13 - 17    -> "Remaja"
# - Umur >= 18      -> "Dewasa"
#
# CATATAN:
# - Minimal gunakan 1 ternary operator
#
# CONTOH INPUT:
# Umur: 16
#
# OUTPUT YANG DIHARAPKAN:
# Kategori usia: Remaja


# ------------------------------------------------------
# SOAL 2: STATUS AKSES
# ------------------------------------------------------
# Buat program yang:
# 1. Meminta input umur
# 2. Tentukan apakah pengguna BOLEH atau TIDAK BOLEH mengakses
#
# KETENTUAN:
# - Umur >= 18 -> "Akses diizinkan"
# - Umur < 18  -> "Akses ditolak"
#
# CATATAN:
# - Gunakan ternary operator
#
# CONTOH INPUT:
# Umur: 20
#
# OUTPUT YANG DIHARAPKAN:
# Status akses: Akses diizinkan


# ------------------------------------------------------
# SOAL 3: GANJIL ATAU GENAP
# ------------------------------------------------------
# Buat program yang:
# 1. Meminta input sebuah angka
# 2. Tentukan apakah angka GANJIL atau GENAP
#
# PETUNJUK:
# - Gunakan operator modulus (%)
# - Gunakan ternary operator
#
# CONTOH INPUT:
# Angka: 7
#
# OUTPUT YANG DIHARAPKAN:
# Angka tersebut adalah GANJIL


# ------------------------------------------------------
# SOAL 4: STATUS NILAI (TERNARY BERTINGKAT)
# ------------------------------------------------------
# Buat program yang:
# 1. Meminta input nilai ujian
# 2. Tentukan status nilai menggunakan TERNARY OPERATOR
#
# KETENTUAN:
# - Nilai >= 85 -> "Sangat Baik"
# - Nilai >= 75 -> "Baik"
# - Nilai < 75  -> "Perlu Perbaikan"
#
# CATATAN:
# - Gunakan ternary bertingkat (nested ternary)
#
# CONTOH INPUT:
# Nilai: 80
#
# OUTPUT YANG DIHARAPKAN:
# Status nilai: Baik


# ------------------------------------------------------
# SOAL 5 (BONUS): CEK USIA PRODUKTIF
# ------------------------------------------------------
# Buat program yang:
# 1. Meminta input umur
# 2. Tentukan apakah usia termasuk usia produktif
#
# KETENTUAN:
# - Usia produktif: 15 sampai 64 tahun
#
# PETUNJUK:
# - Gunakan operator logika AND
# - Gunakan ternary operator
#
# CONTOH INPUT:
# Umur: 30
#
# OUTPUT YANG DIHARAPKAN:
# Status: Usia produktif


# === QUESTION NO 1 ===
print("== QUESTION NO 1")

umur = int(input("Masukkan umur anda: "))
kategori = "Anak-anak" if umur < 13 else "Remaja" if umur <= 17 else "Dewasa"
print("Kategori usia: ", kategori)
print()

# === QUESTION NO 2 ===
print("== QUESTION NO 2==")

age = int(input("Masukkan umur: "))
permission = "Akses diizinkan" if age >= 18 else "Akses ditolak"
print("Status Akses: ", permission)
print()

# === QUESTION NO 3 ===
print("== QUESTION 3==")

num = float(input("Masukkan angka: "))
result = "GENAP" if num % 2 == 0 else "GANJIL"
print("Angka tersebut adalah: ", result)
print()

# === QUESTION NO 4 ===
