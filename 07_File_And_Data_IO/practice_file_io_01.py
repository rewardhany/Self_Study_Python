# ======================================================
# PRACTICE FILE IO 01
# ======================================================
# Materi yang diuji: 01_read_write_file, 02_mode_file_r_w_a,
#                     03_with_statement
# ======================================================


# ------------------------------------------------------
# SOAL 1: TULIS DAN BACA FILE SEDERHANA
# ------------------------------------------------------
# Pakai with statement, tulis 3 baris tugas kamu hari ini ke file
# "tugas_hari_ini.txt", lalu baca dan print isinya kembali

# TODO: tulis kode di sini


# ------------------------------------------------------
# SOAL 2: APPEND LOG
# ------------------------------------------------------
# Buat fungsi tambah_log(pesan) yang menambahkan (append, BUKAN menimpa)
# pesan ke file "log.txt", tiap pesan di baris baru.
# Panggil fungsinya 3 kali dengan pesan berbeda, lalu buka dan print
# seluruh isi log.txt untuk membuktikan ketiga pesan tersimpan semua

# TODO: tulis kode di sini


# ------------------------------------------------------
# SOAL 3: BACA FILE DENGAN AMAN (try/except + with)
# ------------------------------------------------------
# Buat fungsi baca_file_aman(nama_file) yang:
# - coba baca isi file pakai with
# - kalau file tidak ditemukan, return string "File tidak ditemukan"
#   (JANGAN biarkan program crash)
#
# Test dengan file yang ADA dan file yang TIDAK ADA

# TODO: tulis kode di sini


# ------------------------------------------------------
# SOAL 4: CEK MODE YANG TEPAT
# ------------------------------------------------------
# Diberikan skenario ini, tentukan mode file yang PALING TEPAT
# (jawab dalam komentar, tidak perlu kode):
# a) Menyimpan log aktivitas yang terus bertambah setiap hari -> mode: ...
# b) Membuat file baru, dan HARUS gagal kalau file itu sudah ada -> mode: ...
# c) Menimpa total isi file lama dengan data baru -> mode: ...

# TODO: jawab di sini sebagai komentar


# ------------------------------------------------------
# KALAU SUDAH SELESAI
# ------------------------------------------------------
# Cek ke 01_read_write_file.py, 02_mode_file_r_w_a.py, 03_with_statement.py.
# Soal 3 penting banget - ini pola yang akan sering kepakai ke depannya.