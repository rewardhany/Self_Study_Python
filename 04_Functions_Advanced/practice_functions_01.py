# ======================================================
# PRACTICE FUNCTIONS 01
# ======================================================
# Materi yang diuji: 01_function_review, 02_parameter_dan_default_value
#
# CARA PAKAI FILE INI:
# - JANGAN buka file materinya dulu
# - Coba tulis kode di bawah TODO masing-masing, dari ingatan
# - Baru cocokkan ke materi kalau sudah selesai / benar-benar stuck
# ======================================================


# ------------------------------------------------------
# SOAL 1: FUNGSI HITUNG KELILING
# ------------------------------------------------------
# Buat fungsi bernama hitung_keliling_persegi_panjang(panjang, lebar)
# yang MENGEMBALIKAN (return) nilai kelilingnya.
# Rumus keliling = 2 * (panjang + lebar)
#
# Test dengan: hitung_keliling_persegi_panjang(5, 3) -> harus hasilnya 16

# TODO: tulis fungsimu di sini


# ------------------------------------------------------
# SOAL 2: FUNGSI DENGAN DEFAULT VALUE
# ------------------------------------------------------
# Buat fungsi bernama daftar_hadir(nama, status="Hadir")
# yang print "{nama} - {status}"
#
# Panggil 3 kali:
# 1. Dengan status default (jangan diisi parameter status-nya)
# 2. Dengan status="Izin"
# 3. Dengan status="Sakit", tapi panggil pakai keyword argument

# TODO: tulis fungsi + 3 pemanggilannya di sini


# ------------------------------------------------------
# SOAL 3: MULTIPLE RETURN VALUE
# ------------------------------------------------------
# Buat fungsi bernama analisis_denda(list_hari_telat) yang menerima
# LIST berisi jumlah hari telat beberapa orang, lalu return:
# - total seluruh denda (setiap hari telat = Rp5000)
# - orang dengan denda TERBESAR (hari telat terbanyak)
#
# Contoh: analisis_denda([2, 5, 1, 3]) -> total=55000, hari_terbanyak=5

# TODO: tulis fungsimu di sini, lalu panggil dan print hasilnya


# ------------------------------------------------------
# SOAL 4 (SEDIKIT LEBIH SUSAH): VALIDASI PARAMETER
# ------------------------------------------------------
# Buat fungsi bernama daftar_peserta(nama, umur, kontak="Belum diisi")
# yang PRINT "Nama tidak valid!" kalau nama-nya string kosong ("")
# atau PRINT profil lengkapnya kalau nama valid
#
# Test dengan: daftar_peserta("", 20) dan daftar_peserta("Reffa", 20)

# TODO: tulis fungsimu di sini


# ------------------------------------------------------
# KALAU SUDAH SELESAI SEMUA
# ------------------------------------------------------
# - Cek balik ke 01_function_review.py dan 02_parameter_dan_default_value.py
# - Bandingkan gaya penulisanmu, bukan cuma hasil akhirnya
# - Ada bagian yang kamu skip/lupa? Itu tandanya perlu diulang, bukan tanda gagal