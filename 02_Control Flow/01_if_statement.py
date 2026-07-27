# ======================================================
# 01 IF STATEMENT
# ======================================================
# IF STATEMENT digunakan untuk menjalankan kode
# HANYA JIKA suatu kondisi bernilai True
#
# Jika kondisi False, maka kode di dalam if
# TIDAK akan dijalankan
#
# STRUKTUR DASAR:
# if kondisi:
#     kode_yang_dijalankan
#
# CATATAN PENTING:
# - Kondisi HARUS menghasilkan True atau False
# - Python SANGAT memperhatikan indentasi (spasi)
# ======================================================


# ------------------------------------------------------
# CONTOH 1: IF SEDERHANA
# ------------------------------------------------------

umur = 20

if umur >= 18:
    print("Kamu sudah dewasa")

# Penjelasan:
# - Kondisi: umur >= 18
# - Jika True → print dijalankan
# - Jika False → tidak terjadi apa-apa


# ------------------------------------------------------
# CONTOH 2: IF DENGAN INPUT
# ------------------------------------------------------

umur = int(input("Masukkan umur kamu: "))

if umur >= 18:
    print("Status: Dewasa")

# Jika umur < 18
# Program TIDAK error, hanya tidak mencetak apa pun


# ------------------------------------------------------
# CONTOH 3: IF DENGAN PERBANDINGAN ANGKA
# ------------------------------------------------------

nilai = int(input("Masukkan nilai ujian: "))

if nilai >= 75:
    print("Selamat, kamu LULUS!")

# Di sini:
# - Jika nilai >= 75 → LULUS
# - Jika nilai < 75 → tidak ada output


# ------------------------------------------------------
# CONTOH 4: IF DENGAN STRING
# ------------------------------------------------------

nama = input("Masukkan nama kamu: ")

if nama == "Reffa":
    print("Halo Reffa, selamat datang!")

# Perbandingan string bersifat CASE-SENSITIVE
# "reffa" != "Reffa"


# ------------------------------------------------------
# KESALAHAN UMUM PEMULA
# ------------------------------------------------------
# ❌ SALAH:
# if umur >= 18
#     print("Dewasa")
#
# ❌ SALAH:
# if umur = 18:
#
# ✅ BENAR:
# if umur >= 18:
#     print("Dewasa")
