# ======================================================
# PRACTICE OOP 03 (PROJECT CHALLENGE)
# ======================================================
# Gabungan SEMUA materi BAB 5: class/object, attribute/method,
# __init__, inheritance, encapsulation, polymorphism, dunder methods,
# classmethod/staticmethod.
#
# Kerjakan bertahap sesuai TODO, jangan loncat.
# ======================================================

# ------------------------------------------------------
# KONTEKS PROJECT
# ------------------------------------------------------
# Refactor "MUSIC QUEUE SERVICE" dari BAB 2 (yang dulu masih pakai
# while-loop + list biasa) jadi versi OOP penuh.


# ------------------------------------------------------
# TODO 1: CLASS Lagu (data sederhana + dunder method)
# ------------------------------------------------------
# Buat class Lagu dengan __init__(judul, durasi_detik)
# Tambahkan __str__ supaya print(lagu) hasilnya: "{judul} ({durasi_detik}s)"


# ------------------------------------------------------
# TODO 2: CLASS MusicPlayer (encapsulation)
# ------------------------------------------------------
# Buat class MusicPlayer dengan:
# - __init__ yang bikin __antrian (private) = list kosong
# - method tambah_lagu(lagu) -> terima OBJECT Lagu, masukkan ke __antrian
# - method putar_selanjutnya() -> hapus & return lagu PALING DEPAN,
#   kalau kosong print "Antrian kosong" dan return None
# - method lihat_antrian() -> print semua lagu di antrian (pakai __str__ dari Lagu)


# ------------------------------------------------------
# TODO 3: __len__ UNTUK MusicPlayer
# ------------------------------------------------------
# Tambahkan __len__ ke MusicPlayer supaya len(player) langsung ngasih
# jumlah lagu di antrian, tanpa perlu method terpisah


# ------------------------------------------------------
# TODO 4: INHERITANCE - PremiumMusicPlayer
# ------------------------------------------------------
# Buat class PremiumMusicPlayer(MusicPlayer) yang override
# putar_selanjutnya() supaya SEBELUM manggil versi induknya (super()),
# print "[PREMIUM] Memutar tanpa iklan..." dulu


# ------------------------------------------------------
# TODO 5: STATIC METHOD - VALIDASI DURASI
# ------------------------------------------------------
# Tambahkan @staticmethod bernama durasi_valid(detik) ke class Lagu,
# yang return True kalau detik > 0, False kalau tidak.
# Panggil validasi ini di __init__ Lagu - kalau tidak valid, print
# "Durasi tidak valid!" dan set durasi jadi 0


# ------------------------------------------------------
# TODO 6: CLASSMETHOD - BIKIN LAGU DARI STRING
# ------------------------------------------------------
# Tambahkan @classmethod bernama dari_string(cls, data) ke class Lagu,
# yang menerima string format "judul,durasi" (contoh: "Blinding Lights,200")
# dan return object Lagu baru dari situ


# ------------------------------------------------------
# TODO 7: TES SEMUANYA
# ------------------------------------------------------
# - Buat player = PremiumMusicPlayer()
# - Tambahkan 3 lagu (campur cara biasa Lagu(...) dan Lagu.dari_string(...))
# - print(len(player))
# - Panggil putar_selanjutnya() 2 kali
# - lihat_antrian() di akhir


# ------------------------------------------------------
# KALAU STUCK
# ------------------------------------------------------
# Urutan TODO 1 -> 6 saling bergantung, jangan loncat ke TODO 4 sebelum
# TODO 2 selesai. Kalau TODO 4 bingung soal override + super(), buka lagi
# 04_inheritance.py CONTOH 3.