# ======================================================
# 03 PACKAGE & __init__.py
# ======================================================
# PACKAGE adalah:
# FOLDER berisi banyak module (file .py), dikelompokkan jadi satu
#
# Kalau module = 1 file .py, package = 1 FOLDER berisi banyak module
#
# STRUKTUR DASAR:
# nama_package/
# ├── __init__.py      <- WAJIB ada, menandakan folder ini adalah package
# ├── module_a.py
# └── module_b.py
# ======================================================


# ------------------------------------------------------
# CONTOH 1: STRUKTUR PACKAGE SEDERHANA
# ------------------------------------------------------

# Bayangkan struktur folder seperti ini:
#
# project_odwh/
# ├── main.py
# └── utils/                    <- ini PACKAGE (folder)
#     ├── __init__.py           <- file kosong, tapi WAJIB ada
#     ├── denda.py               <- module di dalam package
#     └── laporan.py             <- module lain di dalam package

# Penjelasan:
# - utils/ jadi package KARENA ada file __init__.py di dalamnya
# - Tanpa __init__.py, Python (versi lama) tidak menganggap folder itu package
# - denda.py dan laporan.py adalah module BIASA, cuma sekarang dikelompokkan


# ------------------------------------------------------
# CONTOH 2: CARA IMPORT DARI PACKAGE
# ------------------------------------------------------

# ---- isi utils/denda.py ----
# def hitung_denda(hari_telat):
#     return hari_telat * 5000
# --------------------------------

# ---- cara pakainya di main.py ----
# from utils import denda
#
# total = denda.hitung_denda(3)
# --------------------------------

# ATAU langsung ambil fungsinya:
# from utils.denda import hitung_denda
#
# total = hitung_denda(3)
# --------------------------------

# Penjelasan:
# - from utils import denda -> ambil MODULE denda dari PACKAGE utils
# - from utils.denda import hitung_denda -> langsung ambil FUNGSI-nya
# - Titik (utils.denda) dipakai buat "masuk" ke dalam folder package


# ------------------------------------------------------
# CONTOH 3: __init__.py KOSONG VS __init__.py YANG "MEMBUKA JALAN"
# ------------------------------------------------------

# __init__.py boleh KOSONG total, package tetap jalan normal.
# Tapi __init__.py juga bisa diisi supaya import-nya lebih pendek:

# ---- isi utils/__init__.py ----
# from .denda import hitung_denda
# from .laporan import buat_laporan
# --------------------------------

# ---- sekarang di main.py bisa langsung: ----
# from utils import hitung_denda, buat_laporan
# (tidak perlu from utils.denda import ... lagi)
# --------------------------------

# Penjelasan:
# - Tanda titik di depan (.denda) artinya "dari folder yang sama dengan
#   __init__.py ini" -> disebut relative import
# - Ini cuma buat kenyamanan, package tetap berfungsi walau __init__.py kosong


# ------------------------------------------------------
# CONTOH 4: KAPAN BUTUH PACKAGE (BUKAN CUMA MODULE BIASA)
# ------------------------------------------------------

# Module biasa (1 file) cukup kalau:
# - project masih kecil, cuma butuh beberapa fungsi helper

# Package (folder) lebih pas kalau:
# - project makin besar, module-nya banyak dan perlu dikelompokkan
# - contoh nyata: BAB 11 nanti pakai library seperti pandas -> pandas
#   SEBENARNYA adalah package raksasa, isinya ratusan module di dalamnya

# Penjelasan:
# - Semua library luar yang kamu install lewat pip (BAB 8 file 04) itu
#   pada dasarnya adalah PACKAGE -> sekarang kamu paham struktur di baliknya


# ------------------------------------------------------
# CATATAN PENTING
# ------------------------------------------------------
# - Package = folder + __init__.py, isinya banyak module
# - __init__.py boleh kosong, atau diisi buat mempersingkat cara import
# - Untuk project belajar kamu sekarang (BAB 1-10), module biasa saja
#   sudah cukup -> package baru relevan kalau project sudah lumayan besar