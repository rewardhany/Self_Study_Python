# ======================================================
# 03_variables_and_data_types.py
# ======================================================
# Di file ini kita akan belajar:
# 1. Apa itu variabel
# 2. Jenis-jenis tipe data dasar
# 3. Cara mengecek tipe data
# ======================================================


# ------------------------------------------------------
# VARIABEL
# ------------------------------------------------------
# Variabel adalah "wadah" untuk menyimpan data
# Di Python, kita TIDAK perlu menyebutkan tipe data di awal
# Ini disebut Dynamic Typing
# Variabel posisi nya di sebelah kiri tanda sama dengan "=" dan tipe data itu di bagian kanan sebelah tanda sama dengan "=". Tipe data bisa berupa string, int, float, maupun bool. Di variabel ini kita bebas mau menamai nya, sesuai apa yang kita mau dan mudah kita kenali untuk panggil di fungsi.

nama = "Reffa"        # String (teks)
umur = 20             # Integer (angka bulat)
tinggi = 170.5        # Float (angka desimal)
is_coding = True      # Boolean (True / False)


# ------------------------------------------------------
# TIPE DATA1
# ------------------------------------------------------
# String  -> str  -> teks
# Integer -> int  -> angka bulat
# Float   -> float-> angka desimal
# Boolean -> bool -> True / False


# ------------------------------------------------------
# MENGECEK TIPE DATA
# ------------------------------------------------------
# Gunakan fungsi type()

print(type(nama))
print(type(umur))
print(type(tinggi))
print(type(is_coding))
print()


# ------------------------------------------------------
# LATIHAN
# ------------------------------------------------------
# 1. Buat variabel:
#    - nama_sekolah
#    - kelas
#    - nilai
#
# 2. Cetak tipe data masing-masing

# YOUR CODE STARTS HERE!
print("Ini adalah program latihan saya!")
namaSekolah = "SMA PGRI 3 BANDUNG"
kelas = 12
nilai = 92.5
adalah_siswa = False

print(type(namaSekolah))
print(type(kelas))
print(type(nilai))
print(type(adalah_siswa))

name_input = input("Enter customer name: ")

