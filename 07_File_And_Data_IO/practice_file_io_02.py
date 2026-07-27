# ======================================================
# PRACTICE FILE IO 02 (PROJECT CHALLENGE)
# ======================================================
# Gabungan SEMUA materi BAB 7: read/write, mode, with, JSON, CSV,
# path handling.
#
# Kerjakan bertahap sesuai TODO.
# ======================================================

# ------------------------------------------------------
# KONTEKS PROJECT
# ------------------------------------------------------
# Upgrade "SISTEM PEMINJAMAN BUKU" (dari BAB 2 & BAB 6) supaya datanya
# TIDAK HILANG setiap program ditutup - persis masalah yang disebutkan
# di roadmap awal kamu.

data_awal = [
    {"judul": "Laskar Pelangi", "peminjam": "Reffa", "status": "dipinjam"},
    {"judul": "Bumi Manusia", "peminjam": "Galan", "status": "dipinjam"},
]


# ------------------------------------------------------
# TODO 1: SIAPKAN FOLDER OUTPUT
# ------------------------------------------------------
# Pakai os.path atau pathlib, cek apakah folder "data_perpustakaan" ada.
# Kalau belum, buat foldernya.


# ------------------------------------------------------
# TODO 2: SIMPAN data_awal KE FILE JSON
# ------------------------------------------------------
# Simpan data_awal ke "data_perpustakaan/peminjaman.json" (pakai with +
# json.dump, dengan indent=4 biar rapi)


# ------------------------------------------------------
# TODO 3: FUNGSI baca_data() YANG AMAN
# ------------------------------------------------------
# Buat fungsi baca_data() yang:
# - coba baca "data_perpustakaan/peminjaman.json" pakai json.load
# - kalau file belum ada (FileNotFoundError), return list kosong []
#   (JANGAN crash kalau ini pertama kali program dijalankan)


# ------------------------------------------------------
# TODO 4: FUNGSI tambah_peminjaman(judul, peminjam)
# ------------------------------------------------------
# Buat fungsi yang:
# - baca data lama pakai baca_data()
# - tambahkan entry baru {"judul":..., "peminjam":..., "status": "dipinjam"}
# - simpan LAGI ke file JSON (timpa dengan data yang sudah termasuk entry baru)


# ------------------------------------------------------
# TODO 5: EXPORT KE CSV UNTUK LAPORAN
# ------------------------------------------------------
# Buat fungsi export_ke_csv() yang:
# - baca data dari peminjaman.json
# - tulis ke "data_perpustakaan/laporan_peminjaman.csv" pakai csv.DictWriter
#   (kolom: judul, peminjam, status)


# ------------------------------------------------------
# TODO 6: TES SEMUANYA
# ------------------------------------------------------
# - Panggil tambah_peminjaman("Filosofi Teras", "Bintang")
# - Panggil export_ke_csv()
# - Buka kembali file JSON dan CSV-nya, print isi keduanya untuk
#   membuktikan data baru sudah masuk ke kedua file


# ------------------------------------------------------
# KALAU STUCK
# ------------------------------------------------------
# Urutan TODO 1 -> 5 saling bergantung. Kalau TODO 3 membingungkan,
# lihat lagi 04_json_basic.py CONTOH 3, dan practice_error_handling_01.py
# soal 3 untuk pola try/except yang serupa.