# ======================================================
# 04_data_types_and_casting.py
# ======================================================
# Di file ini kita akan belajar:
# 1. Tipe data dasar di Python (lebih dalam)
# 2. Perbedaan tipe data
# 3. Type Casting (konversi tipe data)
# 4. Masalah umum saat casting
# ======================================================


# ------------------------------------------------------
# TIPE DATA DASAR DI PYTHON
# ------------------------------------------------------
# Beberapa tipe data yang sering digunakan:
# - int    : angka bulat
# - float  : angka desimal
# - str    : teks
# - bool   : True / False

angka_int = 10
angka_float = 3.14
teks = "100"
status = True


# ------------------------------------------------------
# MENGECEK TIPE DATA
# ------------------------------------------------------
print(type(angka_int))     # < class 'int'>
print(type(angka_float))   # < class 'float'>
print(type(teks))          # < class 'str'>
print(type(status))        # < class 'bool'>


# ------------------------------------------------------
# TYPE CASTING (KONVERSI TIPE DATA)
# ------------------------------------------------------
# Type casting adalah proses mengubah satu tipe data ke tipe lain
# Python menyediakan fungsi:
# - int()
# - float()
# - str()
# - bool()

# String ke Integer
teks_angka = "200"
angka = int(teks_angka)
print(angka, type(angka))

# Integer ke String
umur = 20
umur_str = str(umur)
print(umur_str, type(umur_str))

# Integer ke Float
nilai = 90
nilai_float = float(nilai)
print(nilai_float, type(nilai_float))


# ------------------------------------------------------
# PERHATIAN SAAT TYPE CASTING
# ------------------------------------------------------
# Tidak semua string bisa diubah jadi angka

# Contoh SALAH:
# teks_salah = "halo"
# int(teks_salah)  -> ERROR!


# ------------------------------------------------------
# CASTING DARI INPUT
# ------------------------------------------------------
# Ingat: input() SELALU menghasilkan STRING

umur_input = input("Masukkan umur kamu: ")
umur_int = int(umur_input)

print("Umur kamu tahun depan:", umur_int + 1)
print()


# ------------------------------------------------------
# LATIHAN
# ------------------------------------------------------
# 1. Minta input:
#    - berat badan (kg)
#    - tinggi badan (cm)
#
# 2. Ubah input menjadi float
# 3. Tampilkan hasilnya

# YOUR CODE STARTS HERE !
# NO 1
print("=== EXERCISE ===")
body_weight = input("Enter your weight: ")
weight = float(body_weight)

print("Your weight is: ", weight)
print()

body_height = input("Enter your height: ")
height = float(body_height)

print("Your height is: ", height)
print()

book = input("What is the title of your book: ")
book_page = input("How many pages are your book: ")
pages = int(book_page)

print(f"Your book title is {book}, there are {pages} pages inside its book")
print()

panjang = float(input("Masukkan panjang: "))
lebar = float(input("Masukkan lebar: "))
luas = panjang * lebar
print(f"Luas persegi panjang adalah: {luas}cm²")
print()

contoh_teks = "1500"
angkaBulat = int(contoh_teks)
print(contoh_teks, type(angkaBulat))