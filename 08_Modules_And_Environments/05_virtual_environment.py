# ======================================================
# 05 VIRTUAL ENVIRONMENT (CATATAN, BUKAN RUNNABLE)
# ======================================================
# Sama seperti file 04, ini PERINTAH TERMINAL, bukan kode Python.
#
# VIRTUAL ENVIRONMENT (venv) adalah:
# "Kotak terpisah" untuk tiap project, supaya library yang diinstall
# untuk project A TIDAK bentrok sama library project B
# ======================================================


# ------------------------------------------------------
# KENAPA BUTUH VIRTUAL ENVIRONMENT
# ------------------------------------------------------
# Bayangkan:
# - Project HelpBlue butuh library versi X
# - Project belajar Python (BAB 11 nanti) butuh library versi Y (beda)
#
# Kalau semua diinstall LANGSUNG ke Python utama komputer (global),
# kedua versi itu akan BENTROK, cuma bisa ada 1 versi terinstall.
#
# Virtual environment = tiap project punya "Python-nya sendiri" secara
# terpisah, jadi versi library bisa beda-beda tanpa masalah.


# ------------------------------------------------------
# MEMBUAT VIRTUAL ENVIRONMENT
# ------------------------------------------------------

# Di folder project kamu, jalankan:
#   python -m venv venv
#
# Penjelasan: ini bikin FOLDER baru bernama "venv" (nama boleh apa saja)
# yang isinya instalasi Python terpisah, khusus untuk project ini


# ------------------------------------------------------
# MENGAKTIFKAN VIRTUAL ENVIRONMENT
# ------------------------------------------------------

# Windows (Command Prompt):
#   venv\Scripts\activate

# Windows (PowerShell):
#   venv\Scripts\Activate.ps1

# Mac / Linux:
#   source venv/bin/activate

# Setelah aktif, biasanya muncul tanda (venv) di depan baris terminal,
# menandakan kamu sedang "di dalam" virtual environment ini


# ------------------------------------------------------
# INSTALL LIBRARY SETELAH VENV AKTIF
# ------------------------------------------------------

# Setelah venv aktif, pip install akan masuk ke venv INI SAJA,
# tidak mempengaruhi Python utama di komputer:
#   pip install requests


# ------------------------------------------------------
# MENONAKTIFKAN VIRTUAL ENVIRONMENT
# ------------------------------------------------------

#   deactivate
#
# Setelah ini, terminal kembali pakai Python global, bukan venv lagi


# ------------------------------------------------------
# ATURAN PRAKTIS
# ------------------------------------------------------
# - SETIAP project baru sebaiknya punya venv sendiri-sendiri
# - Folder venv/ TIDAK PERLU (dan SEBAIKNYA TIDAK) di-push ke GitHub -
#   masukkan ke .gitignore (ingat dari dokumen Programmer Essentials)
# - Yang di-push ke GitHub bukan folder venv-nya, tapi DAFTAR library-nya
#   (requirements.txt - lihat file berikutnya)


# ------------------------------------------------------
# CATATAN PENTING
# ------------------------------------------------------
# - venv = "kotak terpisah" per project, mencegah bentrok versi library
# - Alur standar: bikin venv -> aktifkan -> pip install -> kerja -> deactivate
# - Mulai BAB 9 (butuh library requests) adalah waktu yang pas untuk
#   mulai membiasakan diri pakai venv, bukan install langsung ke global