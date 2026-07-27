# ======================================================
# 02_input_output.py
# ======================================================
# Di file ini kita akan belajar:
# 1. Apa itu input
# 2. Cara menerima data dari user
# 3. Perbedaan input dan print
# ======================================================


# ------------------------------------------------------
# OUTPUT (print)
# ------------------------------------------------------
# print() digunakan untuk menampilkan teks ke layar

print("Selamat datang di program Python!")


# ------------------------------------------------------
# INPUT (input)
# ------------------------------------------------------
# input() digunakan untuk MENGAMBIL data dari user
# Data dari input() SELALU bertipe STRING (str)

# Menampilkan hasil input
# print("Halo,", nama)


# ------------------------------------------------------
# LATIHAN
# ------------------------------------------------------
# 1. Minta input:
#    - Umur
#    - Hobi
#
# 2. Tampilkan hasilnya dalam satu kalimat
#
# Contoh output:
# Halo Reffa, umur kamu 20 tahun dan hobi kamu coding

# YOUR CODE STARTS HERE!
print("Ini adalah program saya!")
nama = input("Masukkan nama kamu: ")
umur = input("Masukkan umur kamu: ")
hobi = input("Masukkan hobi kamu: ")

print(f"Halo {nama}, umur kamu {umur} dan hobi kamu {hobi}")
# ini menggunakan f-string, F-string (singkatan dari formatted string literal) di Python memiliki kegunaan utama untuk menyisipkan nilai variabel atau ekspresi secara langsung ke dalam string dengan cara yang sangat ringkas dan mudah dibaca.

# contoh cara lama:
# print("Halo " + nama + ", umur kamu " + str(umur) + " dan hobi kamu " + hobi)

# contoh f-string (lebih efisien):
# print(f"Halo {nama}, umur kamu {umur} dan hobi kamu {hobi}")
