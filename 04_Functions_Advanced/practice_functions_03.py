# ======================================================
# PRACTICE FUNCTIONS 03 (PROJECT CHALLENGE)
# ======================================================
# Ini gabungan SEMUA materi BAB 4: parameter/default, *args/**kwargs,
# lambda, scope/global, recursion, map/filter/reduce, decorator.
#
# Beda dari 2 file practice sebelumnya: ini 1 project utuh, bukan
# soal-soal terpisah. Kerjakan bertahap sesuai TODO, jangan loncat.
# ======================================================

# ------------------------------------------------------
# KONTEKS PROJECT
# ------------------------------------------------------
# Kamu diminta bikin "SISTEM REKAP LOGISTIK ACARA" sederhana,
# mirip kerjaan divisi logistik kamu di hima event.
#
# Data barang (sudah disiapkan, jangan diubah):

data_barang = [
    {"nama": "Proyektor", "sumber": "Lembaga", "harga": 5000000, "jumlah": 2},
    {"nama": "Banner", "sumber": "Hima", "harga": 150000, "jumlah": 4},
    {"nama": "Sound System", "sumber": "Hima", "harga": 2000000, "jumlah": 1},
    {"nama": "Laptop", "sumber": "Panitia", "harga": 8000000, "jumlah": 3},
    {"nama": "Kabel HDMI", "sumber": "Panitia", "harga": 50000, "jumlah": 5},
]


# ------------------------------------------------------
# TODO 1: FUNGSI TOTAL NILAI PER BARANG (pakai *args atau parameter biasa)
# ------------------------------------------------------
# Buat fungsi hitung_total_nilai(harga, jumlah) yang return harga * jumlah


# ------------------------------------------------------
# TODO 2: DECORATOR LOGGING
# ------------------------------------------------------
# Buat decorator bernama log_proses yang print "[PROSES] Menjalankan {nama fungsi}..."
# SEBELUM fungsi dijalankan, dan pasang decorator ini ke fungsi TODO 3 di bawah


# ------------------------------------------------------
# TODO 3: FILTER + MAP -> REKAP PER SUMBER
# ------------------------------------------------------
# Buat fungsi rekap_per_sumber(data, nama_sumber) yang:
# - pakai filter() + lambda buat ambil barang dengan sumber == nama_sumber
# - pakai map() + lambda (atau fungsi TODO 1) buat hitung total nilai tiap barang
# - return LIST total nilai barang-barang tersebut
#
# Test: rekap_per_sumber(data_barang, "Hima") -> harus dapat total nilai
# Banner dan Sound System


# ------------------------------------------------------
# TODO 4: REDUCE -> GRAND TOTAL SEMUA BARANG
# ------------------------------------------------------
# Buat fungsi grand_total(data) yang pakai reduce() buat menjumlahkan
# SEMUA total nilai barang (harga * jumlah) dari seluruh data_barang,
# tidak peduli sumbernya


# ------------------------------------------------------
# TODO 5: LAPORAN AKHIR (GABUNGKAN SEMUA)
# ------------------------------------------------------
# Buat fungsi cetak_laporan(**kwargs) yang menerima keyword argument bebas
# (misal: nama_acara="ODWH 2026", penanggung_jawab="Reffa") dan PRINT:
# - Judul laporan dari kwargs
# - Rekap total nilai per sumber (Lembaga, Hima, Panitia) - pakai TODO 3
# - Grand total keseluruhan - pakai TODO 4
#
# Panggil di akhir: cetak_laporan(nama_acara="ODWH 2026", penanggung_jawab="Reffa")


# ------------------------------------------------------
# BONUS (OPSIONAL, KALAU MASIH SEMANGAT)
# ------------------------------------------------------
# Ubah cetak_laporan supaya barang dengan total nilai TERBESAR
# ditampilkan terpisah sebagai "Barang paling mahal" - pakai sorted() + lambda


# ------------------------------------------------------
# KALAU STUCK
# ------------------------------------------------------
# Urutan ngerjain TODO 1 -> 4 penting, jangan loncat ke TODO 5 dulu.
# Kalau TODO 3 bingung, buka lagi 07_map_filter_reduce.py CONTOH 4 -
# polanya mirip persis.