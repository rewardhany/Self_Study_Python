# ======================================================
# 06 REQUIREMENTS.TXT (CATATAN, BUKAN RUNNABLE)
# ======================================================
# requirements.txt adalah:
# File teks berisi DAFTAR library yang dipakai project, beserta versinya
#
# Kenapa penting: supaya orang lain (atau kamu sendiri di laptop lain)
# bisa install SEMUA library yang sama persis, cukup 1 perintah
# ======================================================


# ------------------------------------------------------
# CONTOH ISI FILE requirements.txt
# ------------------------------------------------------
#
# requests==2.31.0
# flask==3.0.0
# pandas==2.1.4
#
# Penjelasan:
# - Satu baris = satu library
# - ==versi -> mengunci versi PERSIS, supaya tidak ada masalah "di laptop
#   saya jalan, di laptop lain error" gara-gara beda versi


# ------------------------------------------------------
# MEMBUAT requirements.txt DARI LIBRARY YANG SUDAH TERINSTALL
# ------------------------------------------------------

# Setelah venv aktif dan sudah install semua library yang dibutuhkan:
#   pip freeze > requirements.txt
#
# Penjelasan:
# - pip freeze -> nampilin semua library + versi yang terinstall di venv ini
# - > requirements.txt -> hasilnya DITULIS ke file requirements.txt
#   (bukan ditampilkan di layar)


# ------------------------------------------------------
# INSTALL SEMUA LIBRARY DARI requirements.txt
# ------------------------------------------------------

# Di komputer lain (atau venv baru), cukup jalankan:
#   pip install -r requirements.txt
#
# Penjelasan:
# - -r requirements.txt -> baca daftar dari file itu, install SEMUANYA
#   sekaligus, tidak perlu install satu-satu manual


# ------------------------------------------------------
# ALUR KERJA LENGKAP (RINGKASAN BAB 8)
# ------------------------------------------------------
#
# 1. python -m venv venv              -> bikin virtual environment
# 2. source venv/bin/activate         -> aktifkan (Mac/Linux)
#    atau venv\Scripts\activate       -> aktifkan (Windows)
# 3. pip install requests flask       -> install library yang dibutuhkan
# 4. pip freeze > requirements.txt    -> catat semua library yang dipakai
# 5. git add . && git commit ...      -> push requirements.txt ke GitHub
#    (folder venv/ TIDAK ikut di-push, sudah masuk .gitignore)
#
# Orang lain yang clone repo kamu tinggal:
# 1. python -m venv venv
# 2. aktifkan venv
# 3. pip install -r requirements.txt   -> langsung dapat semua library yang sama


# ------------------------------------------------------
# CATATAN PENTING
# ------------------------------------------------------
# - requirements.txt = "resep" supaya project bisa dijalankan ulang di
#   komputer manapun dengan hasil yang sama persis
# - Selalu update requirements.txt (pip freeze > requirements.txt) setiap
#   kali kamu install library baru ke project
# - Ini file yang WAJIB ada di setiap project yang kamu push ke GitHub
#   mulai sekarang, terutama begitu masuk BAB 9 dan seterusnya