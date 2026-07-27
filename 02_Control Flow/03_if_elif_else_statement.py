# ======================================================
# 03 IF ELIF ELSE STATEMENT
# ======================================================
# IF ELIF ELSE digunakan ketika kita memiliki
# LEBIH DARI DUA kemungkinan kondisi.
#
# Dibanding if else:
# - if else → hanya 2 kemungkinan
# - if elif else → banyak kemungkinan
#
# STRUKTUR DASAR:
# if kondisi_1:
#     kode_jika_kondisi_1_true
# elif kondisi_2:
#     kode_jika_kondisi_2_true
# elif kondisi_3:
#     kode_jika_kondisi_3_true
# else:
#     kode_jika_semua_kondisi_false
#
# CATATAN PENTING:
# - Python mengecek kondisi dari ATAS ke BAWAH
# - Jika satu kondisi True, maka:
#   kondisi di bawahnya TIDAK DICEK lagi
# ======================================================


# ------------------------------------------------------
# CONTOH 1: PENILAIAN SEDERHANA
# ------------------------------------------------------

nilai = int(input("Masukkan nilai ujian: "))

if nilai >= 85:
    print("Grade: A")
elif nilai >= 75:
    print("Grade: B")
elif nilai >= 65:
    print("Grade: C")
else:
    print("Grade: D")

# Penjelasan:
# - Jika nilai >= 85 → langsung Grade A
# - Jika tidak, cek nilai >= 75 → Grade B
# - Jika tidak, cek nilai >= 65 → Grade C
# - Jika SEMUA kondisi di atas False → else


# ------------------------------------------------------
# CONTOH 2: KATEGORI UMUR
# ------------------------------------------------------

umur = int(input("Masukkan umur: "))

if umur < 5:
    print("Balita")
elif umur < 12:
    print("Anak-anak")
elif umur < 18:
    print("Remaja")
elif umur < 60:
    print("Dewasa")
else:
    print("Lansia")

# Penjelasan:
# - Tidak perlu menulis umur >= 5, >= 12, dst
# - Karena kondisi dicek berurutan
# - Jika umur < 12, otomatis umur >= 5 sudah terlewati


# ------------------------------------------------------
# CONTOH 3: LOGIN SEDERHANA
# ------------------------------------------------------

username = input("Username: ")

if username == "admin":
    print("Selamat datang Admin")
elif username == "user":
    print("Selamat datang User")
elif username == "guest":
    print("Selamat datang Tamu")
else:
    print("Username tidak dikenali")

# Penjelasan:
# - Setiap elif adalah alternatif kondisi
# - else menangani semua kemungkinan lain


# ------------------------------------------------------
# CONTOH 4: DISKON BELANJA
# ------------------------------------------------------

total_belanja = int(input("Masukkan total belanja: "))

if total_belanja >= 500000:
    print("Diskon 20%")
elif total_belanja >= 300000:
    print("Diskon 10%")
elif total_belanja >= 100000:
    print("Diskon 5%")
else:
    print("Tidak dapat diskon")

# Penjelasan:
# - Urutan kondisi SANGAT PENTING
# - Jika dibalik, hasil bisa salah


# ------------------------------------------------------
# CATATAN PENTING IF ELIF ELSE
# ------------------------------------------------------
# - Gunakan if elif else jika:
#   • Banyak pilihan kondisi
# - else bersifat OPSIONAL
# - elif bisa lebih dari satu
# - HANYA SATU BLOK yang dijalankan
