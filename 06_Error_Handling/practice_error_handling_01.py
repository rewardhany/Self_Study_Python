# ======================================================
# PRACTICE ERROR HANDLING 01
# ======================================================
# Materi yang diuji: 01_try_except_basic, 02_multiple_exceptions,
#                     03_finally_dan_else
# ======================================================


# ------------------------------------------------------
# SOAL 1: TRY-EXCEPT DASAR
# ------------------------------------------------------
# Minta user input 2 angka, lalu print hasil pembagiannya.
# Tangani KEDUA kemungkinan error ini secara terpisah:
# - Input bukan angka (ValueError)
# - Pembagi = 0 (ZeroDivisionError)

# TODO: tulis kode di sini


# ------------------------------------------------------
# SOAL 2: LOOP VALIDASI SAMPAI BENAR
# ------------------------------------------------------
# Minta user input angka index (0-4) untuk akses list berikut:
data = ["A", "B", "C", "D", "E"]
# Program HARUS terus minta input sampai user kasih index yang valid
# (tangani ValueError kalau bukan angka, dan IndexError kalau di luar jangkauan)

# TODO: tulis kode di sini


# ------------------------------------------------------
# SOAL 3: finally UNTUK LOGGING
# ------------------------------------------------------
# Buat fungsi proses_transaksi(jumlah) yang:
# - raise ValueError kalau jumlah <= 0
# - kalau valid, print "Transaksi Rp{jumlah} berhasil"
# - APAPUN hasilnya (berhasil/gagal), finally harus print "Log: percobaan transaksi dicatat"
#
# Test dengan proses_transaksi(50000) dan proses_transaksi(-1000)

# TODO: tulis kode di sini


# ------------------------------------------------------
# SOAL 4: else UNTUK MEMISAHKAN LOGIKA SUKSES
# ------------------------------------------------------
# Minta user input umur. Kalau berhasil di-convert ke int DAN umur >= 17,
# pakai else buat print "Boleh mendaftar SIM"
# Kalau input bukan angka, except ValueError print "Input tidak valid"
# Kalau umur < 17 (tapi valid angka), print "Umur belum cukup" di dalam else juga

# TODO: tulis kode di sini


# ------------------------------------------------------
# KALAU SUDAH SELESAI
# ------------------------------------------------------
# Cek ke 01_try_except_basic.py, 02_multiple_exceptions.py,
# 03_finally_dan_else.py. Soal 2 sengaja mirip pola yang sudah
# dicontohkan - coba kerjakan dari nol dulu sebelum diintip.