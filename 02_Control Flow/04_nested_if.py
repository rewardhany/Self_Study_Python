# ======================================================
# 04 NESTED IF
# ======================================================
# NESTED IF adalah:
# IF di dalam IF
#
# Digunakan ketika:
# - Sebuah keputusan BERGANTUNG pada keputusan sebelumnya
# - Kondisi harus dicek bertahap
#
# STRUKTUR DASAR:
# if kondisi_luar:
#     if kondisi_dalam:
#         kode
# ======================================================


# ------------------------------------------------------
# CONTOH 1: CEK UMUR DAN STATUS
# ------------------------------------------------------

umur = int(input("Masukkan umur: "))

if umur >= 18:
    print("Umur mencukupi")
    
    status = input("Apakah kamu punya KTP? (ya/tidak): ")
    
    if status == "ya":
        print("Kamu boleh mendaftar")
    else:
        print("Kamu belum boleh mendaftar")
else:
    print("Umur belum mencukupi")

# Penjelasan:
# - if luar mengecek umur
# - if dalam mengecek status KTP
# - if dalam HANYA dicek jika if luar True


# ------------------------------------------------------
# CONTOH 2: LOGIN DENGAN ROLE
# ------------------------------------------------------

username = input("Username: ")
password = input("Password: ")

if username == "admin":
    if password == "12345":
        print("Login admin berhasil")
    else:
        print("Password admin salah")
else:
    print("Username tidak terdaftar")

# Penjelasan:
# - Cek username dulu
# - Jika username benar, BARU cek password
# - Ini lebih aman dan logis


# ------------------------------------------------------
# CONTOH 3: CEK NILAI DAN KELULUSAN
# ------------------------------------------------------

nilai = int(input("Masukkan nilai: "))

if nilai >= 75:
    print("Lulus")
    
    if nilai >= 90:
        print("Predikat: Sangat Baik")
    else:
        print("Predikat: Baik")
else:
    print("Tidak lulus")

# Penjelasan:
# - Lulus dulu baru dapat predikat
# - Tidak mungkin dapat predikat kalau tidak lulus


# ------------------------------------------------------
# CONTOH 4: NESTED IF DENGAN OPERATOR LOGIKA
# ------------------------------------------------------

umur = int(input("Masukkan umur: "))
izin = input("Ada izin orang tua? (ya/tidak): ")

if umur < 18:
    if izin == "ya":
        print("Boleh masuk dengan izin")
    else:
        print("Tidak boleh masuk")
else:
    print("Boleh masuk tanpa izin")

# Penjelasan:
# - Anak di bawah 18 tahun perlu izin
# - Dewasa tidak perlu izin


# ------------------------------------------------------
# CATATAN PENTING NESTED IF
# ------------------------------------------------------
# - Nested if bisa membuat kode panjang
# - Jika terlalu banyak nested:
#   • Pertimbangkan elif
# - Perhatikan INDENTASI (spasi)
# - Salah indent → program ERROR
