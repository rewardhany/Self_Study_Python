# ======================================================
# 02 IF ELSE STATEMENT
# ======================================================
# IF ELSE digunakan ketika kita ingin:
# - Menjalankan 1 kode jika kondisi True
# - Menjalankan kode LAIN jika kondisi False
#
# STRUKTUR DASAR:
# if kondisi:
#     kode_jika_true
# else:
#     kode_jika_false
# ======================================================


# ------------------------------------------------------
# CONTOH 1: IF ELSE SEDERHANA
# ------------------------------------------------------

umur = int(input("Masukkan umur kamu: "))

if umur >= 18:
    print("Status: Dewasa")
else:
    print("Status: Belum dewasa")

# Penjelasan:
# - Jika umur >= 18 → if dijalankan
# - Jika umur < 18  → else dijalankan
# - PASTI salah satu dijalankan


# ------------------------------------------------------
# CONTOH 2: CEK KELULUSAN
# ------------------------------------------------------

nilai = int(input("Masukkan nilai ujian: "))

if nilai >= 75:
    print("LULUS")
else:
    print("TIDAK LULUS")

# Berbeda dengan if saja,
# di sini kita MENANGANI SEMUA KONDISI


# ------------------------------------------------------
# CONTOH 3: IF ELSE DENGAN STRING
# ------------------------------------------------------

username = input("Masukkan username: ")

if username == "admin":
    print("Selamat datang, Admin")
else:
    print("Kamu bukan admin")


# ------------------------------------------------------
# CONTOH 4: IF ELSE DENGAN OPERATOR LOGIKA
# ------------------------------------------------------

umur = int(input("Masukkan umur: "))

if umur >= 13 and umur <= 17:
    print("Kategori: Remaja")
else:
    print("Bukan remaja")

# Penjelasan:
# - and → kedua kondisi harus True
# - Jika salah satu False → else dijalankan


# ------------------------------------------------------
# CATATAN PENTING
# ------------------------------------------------------
# - if else cocok untuk 2 kemungkinan
# - Jika kondisi lebih dari 2,
#   kita akan pakai elif (materi berikutnya)
