# ======================================================
# PRACTICE OOP 01
# ======================================================
# Materi yang diuji: 01_class_dan_object, 02_attribute_dan_method,
#                     03_constructor_init
#
# Coba dulu dari ingatan, cocokkan ke materi belakangan.
# ======================================================


# ------------------------------------------------------
# SOAL 1: CLASS SEDERHANA + __init__
# ------------------------------------------------------
# Buat class bernama BukuPerpustakaan dengan __init__ menerima
# judul dan penulis. Buat method info() yang print:
# "{judul} - ditulis oleh {penulis}"
#
# Test: buku1 = BukuPerpustakaan("Laskar Pelangi", "Andrea Hirata")
#       buku1.info()

# TODO: tulis class-nya di sini


# ------------------------------------------------------
# SOAL 2: INSTANCE ATTRIBUTE VS CLASS ATTRIBUTE
# ------------------------------------------------------
# Buat class Perpustakaan dengan:
# - class attribute nama_perpustakaan = "Gramedia" (sama untuk semua object)
# - __init__ menerima parameter jumlah_buku (beda tiap object)
# - method info() yang print "{nama_perpustakaan} - koleksi: {jumlah_buku} buku"
#
# Buat 2 object dengan jumlah_buku berbeda, buktikan nama_perpustakaan-nya sama

# TODO: tulis class-nya di sini


# ------------------------------------------------------
# SOAL 3: METHOD YANG MENGUBAH ATRIBUT OBJECT
# ------------------------------------------------------
# Buat class Antrian dengan:
# - __init__ yang bikin list kosong bernama daftar
# - method tambah(nama) untuk nambah ke daftar
# - method proses_berikutnya() yang HAPUS dan return orang PALING DEPAN di daftar
#   (kalau daftar kosong, print "Antrian kosong" dan return None)
#
# Test dengan tambah 3 nama, lalu proses_berikutnya() 2 kali

# TODO: tulis class-nya di sini


# ------------------------------------------------------
# SOAL 4 (SEDIKIT LEBIH SUSAH): __init__ DENGAN VALIDASI
# ------------------------------------------------------
# Buat class Peserta dengan __init__ menerima nama dan umur.
# Kalau umur < 0, print "Umur tidak valid!" dan set self.umur = 0
# (jangan biarkan umur negatif tersimpan)
#
# Test: Peserta("Reffa", -5) -> umur harus jadi 0, bukan -5

# TODO: tulis class-nya di sini


# ------------------------------------------------------
# KALAU SUDAH SELESAI
# ------------------------------------------------------
# Cek lagi ke 01_class_dan_object.py, 02_attribute_dan_method.py,
# dan 03_constructor_init.py. Perhatikan khususnya soal 2 - itu jebakan
# yang sering bikin bingung soal class attribute vs instance attribute.