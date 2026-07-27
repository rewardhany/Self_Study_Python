# ======================================================
# 02 MEMBUAT MODULE SENDIRI
# ======================================================
# Kamu bisa bikin FILE PYTHON SENDIRI, lalu di-import ke file lain
# persis seperti module bawaan (math, random, dst)
#
# Kenapa penting: daripada copy-paste fungsi yang sama ke banyak
# project (kayak fungsi hitung_denda yang muncul di beberapa file-mu),
# taruh di 1 module, tinggal import di mana pun butuh
# ======================================================


# ------------------------------------------------------
# CONTOH 1: BAYANGKAN ADA FILE TERPISAH BERNAMA helper_denda.py
# ------------------------------------------------------

# ---- isi file helper_denda.py (file TERPISAH, bukan file ini) ----
# def hitung_denda(hari_telat, tarif=5000):
#     return hari_telat * tarif
#
# def format_rupiah(angka):
#     return f"Rp{angka:,}"
# --------------------------------------------------------------

# ---- cara pakainya di file LAIN (misal main.py, satu folder sama helper_denda.py) ----
# import helper_denda
#
# total = helper_denda.hitung_denda(3)
# print(helper_denda.format_rupiah(total))
# --------------------------------------------------------------

# Penjelasan:
# - Nama file (tanpa .py) JADI nama module -> helper_denda.py diimport
#   sebagai "helper_denda"
# - Syarat: kedua file harus ada di folder yang sama (atau diatur pakai
#   package, lihat file berikutnya)


# ------------------------------------------------------
# CONTOH 2: from ... import ... UNTUK MODULE BUATAN SENDIRI
# ------------------------------------------------------

# ---- masih dengan helper_denda.py yang sama ----
# from helper_denda import hitung_denda
#
# total = hitung_denda(3)   # tidak perlu tulis helper_denda.hitung_denda lagi
# --------------------------------------------------------------

# Penjelasan:
# - Sama seperti import module bawaan (BAB 8 file 01), bisa ambil
#   fungsi tertentu saja pakai from ... import ...


# ------------------------------------------------------
# CONTOH 3: if __name__ == "__main__" (POLA PENTING)
# ------------------------------------------------------

# ---- isi file helper_denda.py, DENGAN kode tes di dalamnya ----
# def hitung_denda(hari_telat, tarif=5000):
#     return hari_telat * tarif
#
# if __name__ == "__main__":
#     # kode di bawah ini HANYA jalan kalau helper_denda.py dijalankan
#     # LANGSUNG (python helper_denda.py), TIDAK jalan kalau di-import
#     print("Testing hitung_denda:")
#     print(hitung_denda(5))
# --------------------------------------------------------------

# Penjelasan:
# - __name__ otomatis berisi "__main__" HANYA kalau file itu dijalankan
#   langsung, bukan saat di-import dari file lain
# - Ini bikin kamu bisa nyimpen kode "tes cepat" di dalam module, tanpa
#   kode tes itu ikut jalan tiap kali module-nya di-import di tempat lain


# ------------------------------------------------------
# CONTOH 4: KENAPA MODULARISASI PENTING (KASUS NYATA)
# ------------------------------------------------------

# Bayangkan kamu punya fungsi hitung_denda() yang copy-paste di:
# - test2_08_func.py (project perpustakaan)
# - project logistik ODWH
# - project baru lain nanti
#
# Kalau tarif dendanya berubah dari 5000 jadi 7000, tanpa module:
# -> harus edit fungsi yang SAMA di 3 tempat berbeda, gampang lupa salah satu
#
# Dengan module (helper_denda.py):
# -> edit SATU tempat saja, semua file yang import otomatis ikut ter-update

# Penjelasan:
# - Ini prinsip "DRY" (Don't Repeat Yourself) yang sudah kamu sentuh di
#   BAB 4 (kenapa function itu berguna) -> module adalah level yang
#   lebih besar dari prinsip yang sama


# ------------------------------------------------------
# CATATAN PENTING
# ------------------------------------------------------
# - Module buatan sendiri = file .py biasa, cukup di-import pakai namanya
# - if __name__ == "__main__": dipakai supaya kode tes tidak ikut jalan
#   saat file di-import ke tempat lain
# - Modularisasi = kunci supaya project makin besar tetap gampang dirawat