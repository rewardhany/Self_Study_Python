# ======================================================
# 04 PIP INSTALL BASIC (CATATAN, BUKAN RUNNABLE)
# ======================================================
# File ini BUKAN kode Python yang dijalankan dengan `python file.py`.
# Semua di bawah adalah PERINTAH TERMINAL - ketik di terminal/CMD,
# bukan di dalam script Python.
#
# PIP adalah:
# Package manager Python - cara install library yang dibuat orang lain
# (misal: requests, pandas, flask - yang akan kamu pakai mulai BAB 9)
# ======================================================


# ------------------------------------------------------
# PERINTAH DASAR
# ------------------------------------------------------

# Install 1 package:
#   pip install requests

# Install versi TERTENTU (bukan versi terbaru):
#   pip install requests==2.31.0

# Install BEBERAPA package sekaligus:
#   pip install requests pandas flask

# Uninstall package:
#   pip uninstall requests


# ------------------------------------------------------
# MELIHAT PACKAGE YANG SUDAH TERINSTALL
# ------------------------------------------------------

# Lihat SEMUA package yang terinstall:
#   pip list

# Lihat detail 1 package (versi, lokasi, dependencies):
#   pip show requests

# Cek apakah ada package yang perlu di-update:
#   pip list --outdated


# ------------------------------------------------------
# UPDATE PACKAGE
# ------------------------------------------------------

# Update ke versi terbaru:
#   pip install --upgrade requests

# Update pip itu sendiri:
#   pip install --upgrade pip


# ------------------------------------------------------
# KENAPA INI PENTING SEBELUM BAB 9
# ------------------------------------------------------
# BAB 9 (Working With APIs) butuh library "requests" yang TIDAK bawaan
# Python -> WAJIB install dulu sebelum file-file BAB 9 bisa dijalankan:
#
#   pip install requests
#
# Kalau lupa install dan langsung "import requests", akan muncul:
#   ModuleNotFoundError: No module named 'requests'


# ------------------------------------------------------
# CATATAN PENTING
# ------------------------------------------------------
# - pip install nama_package -> perintah paling sering dipakai
# - Selalu jalankan pip DI DALAM virtual environment (lihat file 05),
#   supaya tidak "mengotori" instalasi Python utama di komputermu
# - pip show nama_package berguna buat cek versi yang lagi kepakai,
#   sering dibutuhkan pas troubleshooting error compatibility