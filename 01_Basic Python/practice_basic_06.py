# ======================================================
# PRACTICE BASIC 06 - STRING
# ======================================================
# Fokus latihan:
# - String manipulation
# - String slicing
# - String method
# - String interpolation (f-string)
# - Escape characters
# ======================================================


# ------------------------------------------------------
# SOAL 1: UBAH FORMAT NAMA
# ------------------------------------------------------
# Buat program yang:
# 1. Meminta input nama lengkap (contoh: "reffa kusumah wardany")
# 2. Ubah nama menjadi:
#    - Huruf besar semua
#    - Format Title Case
# 3. Tampilkan hasilnya menggunakan f-string
#
# CONTOH INPUT:
# Nama lengkap: reffa kusumah wardany
#
# OUTPUT YANG DIHARAPKAN:
# Nama (UPPER) : REFFA KUSUMAH WARDANY
# Nama (TITLE) : Reffa Kusumah Wardany


# ------------------------------------------------------
# SOAL 2: HITUNG KARAKTER & KATA
# ------------------------------------------------------
# Buat program yang:
# 1. Meminta input sebuah kalimat
# 2. Hitung:
#    - Jumlah karakter (termasuk spasi)
#    - Jumlah kata
#
# PETUNJUK:
# - Gunakan len()
# - Gunakan split()
#
# CONTOH INPUT:
# Kalimat: belajar python itu menyenangkan
#
# OUTPUT YANG DIHARAPKAN:
# Jumlah karakter: 33
# Jumlah kata    : 4


# ------------------------------------------------------
# SOAL 3: CEK KATA DALAM KALIMAT
# ------------------------------------------------------
# Buat program yang:
# 1. Meminta input sebuah kalimat
# 2. Meminta input sebuah kata
# 3. Cek apakah kata tersebut ADA di dalam kalimat
#
# PETUNJUK:
# - Gunakan operator "in"
#
# CONTOH INPUT:
# Kalimat: saya suka belajar python
# Kata   : python
#
# OUTPUT YANG DIHARAPKAN:
# Kata "python" ditemukan dalam kalimat


# ------------------------------------------------------
# SOAL 4: POTONG & BALIK KATA
# ------------------------------------------------------
# Buat program yang:
# 1. Meminta input sebuah kata
# 2. Tampilkan:
#    - 3 huruf pertama
#    - 3 huruf terakhir
#    - Versi terbalik dari kata tersebut
#
# PETUNJUK:
# - Gunakan slicing
#
# CONTOH INPUT:
# Kata: Programming
#
# OUTPUT YANG DIHARAPKAN:
# 3 huruf pertama : Pro
# 3 huruf terakhir: ing
# Kata terbalik   : gnimmargorP


# ------------------------------------------------------
# SOAL 5: SENSOR KATA (CENSOR)
# ------------------------------------------------------
# Buat program yang:
# 1. Meminta input sebuah kalimat
# 2. Meminta input kata terlarang
# 3. Ganti semua kata terlarang dengan tanda bintang (*)
#
# PETUNJUK:
# - Gunakan replace()
# - Panjang bintang harus sama dengan panjang kata terlarang
#
# CONTOH INPUT:
# Kalimat      : python itu jelek
# Kata terlarang: jelek
#
# OUTPUT YANG DIHARAPKAN:
# python itu *****


# ------------------------------------------------------
# SOAL 6: FORMAT BIODATA RAPI
# ------------------------------------------------------
# Buat program yang:
# 1. Meminta input:
#    - Nama
#    - Umur
#    - Kota
# 2. Tampilkan biodata dengan format rapi menggunakan:
#    - f-string
#    - escape character (\n dan \t)
#
# OUTPUT YANG DIHARAPKAN:
# ===== BIODATA =====
# Nama : Reffa
# Umur : 20
# Kota : Jakarta
# ===================


# ------------------------------------------------------
# SOAL 7: VALIDASI FORMAT EMAIL (SIMPLE)
# ------------------------------------------------------
# Buat program yang:
# 1. Meminta input em
