# ======================================================
# PRACTICE OOP 02
# ======================================================
# Materi yang diuji: 04_inheritance, 05_encapsulation, 06_polymorphism
# ======================================================


# ------------------------------------------------------
# SOAL 1: INHERITANCE + super()
# ------------------------------------------------------
# Buat class Kendaraan dengan __init__ menerima merk, dan method
# info() yang print "Kendaraan merk {merk}"
#
# Buat class Motor(Kendaraan) dengan __init__ menerima merk DAN cc,
# panggil __init__ induknya pakai super(), lalu override info() supaya
# print "Motor merk {merk}, {cc}cc" (tetap manggil super().info() dulu
# baru tambahin info cc-nya)

# TODO: tulis class Kendaraan dan Motor di sini


# ------------------------------------------------------
# SOAL 2: ENCAPSULATION - REKENING SEDERHANA
# ------------------------------------------------------
# Buat class Rekening dengan:
# - __saldo (private) di-set lewat __init__
# - method setor(jumlah) yang nolak kalau jumlah <= 0
# - method tarik(jumlah) yang nolak kalau jumlah > saldo
# - method cek_saldo() untuk lihat saldo
#
# Pastikan __saldo TIDAK bisa diakses/diubah langsung dari luar class

# TODO: tulis class-nya di sini


# ------------------------------------------------------
# SOAL 3: POLYMORPHISM - BENTUK BANGUN DATAR
# ------------------------------------------------------
# Buat class BangunDatar dengan method luas() yang return 0 (default)
# Buat class Persegi(BangunDatar) dan Lingkaran(BangunDatar), masing-masing
# override luas() sesuai rumusnya sendiri:
# - Persegi: __init__ terima sisi, luas = sisi * sisi
# - Lingkaran: __init__ terima jari_jari, luas = 3.14 * jari_jari * jari_jari
#
# Buat list berisi beberapa object Persegi dan Lingkaran, loop dan print
# luas masing-masing TANPA if/elif cek tipe object-nya

# TODO: tulis class-nya di sini


# ------------------------------------------------------
# SOAL 4 (GABUNGAN): SISTEM PANITIA DENGAN ROLE BERBEDA
# ------------------------------------------------------
# Buat class Panitia (induk) dengan __init__(nama, divisi) dan method
# tugas() yang return "Belum ada tugas spesifik"
#
# Buat 2 class turunan: Sekretaris(Panitia) dan Bendahara(Panitia),
# masing-masing override tugas() sesuai perannya (bebas isinya, yang
# penting beda satu sama lain)
#
# Buat list campuran Sekretaris dan Bendahara, loop dan print tugas()
# masing-masing

# TODO: tulis class-nya di sini


# ------------------------------------------------------
# KALAU SUDAH SELESAI
# ------------------------------------------------------
# Cek ke 04_inheritance.py, 05_encapsulation.py, 06_polymorphism.py.
# Soal 3 dan 4 sengaja mirip - itu untuk latihan pola yang sama diulang
# dengan konteks beda, ini bagian dari interleaving yang sudah dibahas.