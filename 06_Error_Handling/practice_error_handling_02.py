# ======================================================
# PRACTICE ERROR HANDLING 02 (PROJECT CHALLENGE)
# ======================================================
# Gabungan SEMUA materi BAB 6: try/except, multiple exceptions,
# finally/else, raise, custom exception class.
#
# Kerjakan bertahap sesuai TODO.
# ======================================================

# ------------------------------------------------------
# KONTEKS PROJECT
# ------------------------------------------------------
# Bikin ulang "SISTEM PEMINJAMAN BUKU" (dari test2_08_func.py yang sudah
# ada) tapi sekarang dengan validasi error yang benar-benar aman, tidak
# akan pernah crash walau inputnya berantakan.

daftar_buku = {
    "Laskar Pelangi": 3,
    "Bumi Manusia": 2,
    "Filosofi Teras": 0
}


# ------------------------------------------------------
# TODO 1: CUSTOM EXCEPTION
# ------------------------------------------------------
# Buat 2 custom exception:
# - BukuTidakDitemukanError (kalau judul tidak ada di daftar_buku)
# - StokTidakCukupError (kalau stok buku 0 atau kurang dari jumlah yang diminta)


# ------------------------------------------------------
# TODO 2: FUNGSI VALIDASI + raise
# ------------------------------------------------------
# Buat fungsi pinjam_buku(judul, jumlah) yang:
# - raise BukuTidakDitemukanError kalau judul tidak ada di daftar_buku
# - raise StokTidakCukupError kalau stok tidak cukup untuk jumlah yang diminta
# - kalau semua valid: kurangi stok di daftar_buku, return True


# ------------------------------------------------------
# TODO 3: LOOP INPUT DENGAN VALIDASI LENGKAP
# ------------------------------------------------------
# Buat loop yang:
# - minta user input judul buku dan jumlah yang mau dipinjam
# - jumlah HARUS di-convert ke int (tangani ValueError kalau bukan angka)
# - panggil pinjam_buku(), tangani BukuTidakDitemukanError dan
#   StokTidakCukupError dengan pesan yang BEDA untuk masing-masing
# - kalau berhasil, print "Peminjaman berhasil!" pakai else
# - finally selalu print "--- Percobaan peminjaman selesai ---"
# - loop berhenti kalau user ketik "selesai" di input judul


# ------------------------------------------------------
# TODO 4 (BONUS): CUSTOM EXCEPTION DENGAN DATA TAMBAHAN
# ------------------------------------------------------
# Upgrade StokTidakCukupError supaya __init__-nya nyimpen stok_tersedia
# dan jumlah_diminta, lalu di except-nya print selisih kekurangannya:
# "Kurang {selisih} buku dari stok yang tersedia"


# ------------------------------------------------------
# KALAU STUCK
# ------------------------------------------------------
# Urutan TODO 1 -> 2 -> 3 saling bergantung. Kalau TODO 3 kerasa berat,
# coba pecah dulu: bikin loop yang cuma nangkep ValueError-nya dulu,
# baru tambahin custom exception setelah itu jalan.