# ======================================================
# 01 IMPORT MODULE BAWAAN
# ======================================================
# MODULE adalah:
# File Python berisi kode (fungsi, class, variabel) yang bisa dipakai
# ulang di file lain lewat import
#
# Python punya BANYAK module bawaan (built-in) yang siap pakai,
# tidak perlu install apapun
#
# STRUKTUR DASAR:
# import nama_module
# from nama_module import sesuatu_spesifik
# ======================================================

import math


# ------------------------------------------------------
# CONTOH 1: import MODULE PENUH
# ------------------------------------------------------

print(math.sqrt(16))     # akar kuadrat
print(math.pi)            # konstanta pi
print(math.ceil(4.2))     # pembulatan ke atas

# Penjelasan:
# - import math -> ambil SELURUH isi module math
# - Cara pakainya: math.nama_fungsi() atau math.nama_konstanta
# - Titik (.) di sini sama konsepnya dengan self.atribut di OOP (BAB 5)


# ------------------------------------------------------
# CONTOH 2: from ... import ... (AMBIL SEBAGIAN SAJA)
# ------------------------------------------------------

from math import sqrt, pi

print(sqrt(25))    # tidak perlu tulis math.sqrt() lagi
print(pi)

# Penjelasan:
# - from math import sqrt, pi -> cuma ambil 2 hal spesifik itu saja
# - Setelah ini, langsung pakai sqrt() dan pi tanpa awalan math.
# - Cocok kalau cuma butuh 1-2 fungsi dari module yang besar


# ------------------------------------------------------
# CONTOH 3: import DENGAN ALIAS (NAMA LEBIH PENDEK)
# ------------------------------------------------------

import random as rd
import datetime as dt

angka_acak = rd.randint(1, 10)
print(f"Angka acak: {angka_acak}")

sekarang = dt.datetime.now()
print(f"Waktu sekarang: {sekarang}")

# Penjelasan:
# - "as rd" bikin nama panggilan lebih pendek, berguna kalau nama module panjang
# - Ini juga konvensi umum di library luar nanti (import pandas as pd,
#   import numpy as np -> akan sering ketemu ini di BAB 11)


# ------------------------------------------------------
# CONTOH 4: MODULE BAWAAN YANG SERING DIPAKAI
# ------------------------------------------------------

import os
import random
import datetime

print(os.getcwd())                        # folder kerja saat ini
print(random.choice(["A", "B", "C"]))       # pilih random dari list
print(datetime.date.today())                # tanggal hari ini

# Penjelasan modul bawaan yang paling sering kepakai:
# - math      -> operasi matematika (sqrt, pi, ceil, floor)
# - random    -> angka acak, pilihan acak
# - datetime  -> tanggal & waktu
# - os        -> interaksi dengan sistem operasi (folder, path - lihat BAB 7 file 06)
# - json      -> sudah dipakai di BAB 7 file 04


# ------------------------------------------------------
# CATATAN PENTING
# ------------------------------------------------------
# - import module (built-in) TIDAK perlu install apapun, sudah ada di Python
# - import X vs from X import Y -> pilih sesuai kebutuhan, "from" kalau
#   cuma butuh sedikit, "import" biasa kalau butuh banyak fungsi dari situ
# - Import selalu ditulis di PALING ATAS file, sebelum kode lain