# ======================================================
# 09_string_and_manipulation.py
# ======================================================
# Di file ini kita akan belajar:
# 1. Apa itu String
# 2. Cara membuat String
# 3. Mengakses karakter String
# 4. Panjang String
# 5. Operasi pada String
# 6. Method (fungsi) bawaan String
# 7. String Formatting
# ======================================================


# ------------------------------------------------------
# 1. APA ITU STRING?
# ------------------------------------------------------
# String adalah kumpulan karakter (teks)
# String di Python diapit oleh:
# - tanda petik satu (' ')
# - tanda petik dua (" ")

nama = "Reffa"
kalimat = 'Saya sedang belajar Python'

print(nama)
print(kalimat)


# ------------------------------------------------------
# 2. MEMBUAT STRING
# ------------------------------------------------------
# String bisa berisi huruf, angka, simbol, dan spasi

alamat = "Jakarta Timur"
kode_pos = "13450"   # meskipun angka, ini STRING

print(type(kode_pos))   # <class 'str'>


# ------------------------------------------------------
# 3. MENGAKSES KARAKTER STRING (INDEXING)
# ------------------------------------------------------
# Setiap karakter dalam string punya index
# Index dimulai dari 0

kata = "Python"

print(kata[0])   # P
print(kata[1])   # y
print(kata[-1])  # n (index dari belakang)


# ------------------------------------------------------
# 4. PANJANG STRING
# ------------------------------------------------------
# Gunakan fungsi len()

print(len(kata))   # 6


# ------------------------------------------------------
# 5. OPERASI PADA STRING
# ------------------------------------------------------

# Menggabungkan string (concatenation)
nama_depan = "Reffa"
nama_belakang = "Wardany"

nama_lengkap = nama_depan + " " + nama_belakang
print(nama_lengkap)

# Mengulang string
print("Ha" * 3)   # HaHaHa


# ------------------------------------------------------
# 6. METHOD STRING (FUNGSI BAWAAN STRING)
# ------------------------------------------------------
# String di Python memiliki BANYAK method bawaan
# Method adalah fungsi yang "menempel" pada sebuah string
# Cara pakai:
#   nama_string.method()

teks = "belajar python itu menyenangkan"


# -------------------------------
# UBAH BENTUK HURUF
# -------------------------------

print(teks.upper())
# Mengubah SEMUA huruf menjadi HURUF BESAR

print(teks.lower())
# Mengubah SEMUA huruf menjadi huruf kecil

print(teks.title())
# Mengubah huruf AWAL SETIAP KATA menjadi huruf besar

print(teks.capitalize())
# Mengubah HURUF PERTAMA saja menjadi huruf besar


# -------------------------------
# CEK & HITUNG
# -------------------------------

print(len(teks))
# Menghitung jumlah karakter (termasuk spasi)

print(teks.count("a"))
# Menghitung berapa kali huruf / kata muncul

print(teks.find("python"))
# Mencari posisi index awal kata "python"
# Jika tidak ditemukan -> hasilnya -1

print("python" in teks)
# Mengecek apakah kata "python" ADA di dalam string
# Hasilnya True atau False (Boolean)


# -------------------------------
# MANIPULASI ISI STRING
# -------------------------------

print(teks.replace("python", "coding"))
# Mengganti kata "python" menjadi "coding"

print(teks.split())
# Memecah string menjadi list berdasarkan spasi

print(teks.split("python"))
# Memecah string berdasarkan kata tertentu


# -------------------------------
# MENGHILANGKAN SPASI (WHITESPACE)
# -------------------------------

teks_spasi = "   halo python   "

print(teks_spasi.strip())
# Menghapus spasi di KIRI dan KANAN

print(teks_spasi.lstrip())
# Menghapus spasi di KIRI saja

print(teks_spasi.rstrip())
# Menghapus spasi di KANAN saja


# ------------------------------------------------------
# 7. MENGGANTI & MEMECAH STRING
# ------------------------------------------------------

kalimat = "Saya suka Python"

# Mengganti kata
kalimat_baru = kalimat.replace("Python", "Coding")
print(kalimat_baru)

# Memecah string menjadi list
data = "apel,jeruk,mangga"
hasil = data.split(",")
print(hasil)


# ------------------------------------------------------
# 8. MENGHAPUS SPASI (WHITESPACE)
# ------------------------------------------------------

teks_spasi = "   Halo Python   "

print(teks_spasi.strip())   # hapus kiri & kanan
print(teks_spasi.lstrip())  # hapus kiri
print(teks_spasi.rstrip())  # hapus kanan


# ------------------------------------------------------
# 9. STRING FORMATTING
# ------------------------------------------------------
# Cara rapi memasukkan variabel ke dalam string

nama = "Reffa"
umur = 20

# Cara lama
print("Nama saya " + nama + " umur saya " + str(umur))

# Cara format()
print("Nama saya {} umur saya {}".format(nama, umur))

# Cara f-string (PALING DIREKOMENDASIKAN)
print(f"Nama saya {nama} umur saya {umur}")


# ------------------------------------------------------
# 10. STRING DARI INPUT
# ------------------------------------------------------

nama = input("Masukkan nama: ")
hobi = input("Masukkan hobi: ")

print(f"Halo {nama}, hobi kamu adalah {hobi}")

# ------------------------------------------------------
# 11. STRING SLICING
# ------------------------------------------------------
# Mengambil sebagian string menggunakan slicing
# CONTOH: 
# kata = "PythonProgramming"
# Index:
#  P  y  t  h  o  n  P  r  o  g  r  a  m  m  i  n  g
#  0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16

kata = "PythonProgramming"

print(kata[0:6])    # Python -> artinya dia mengambil indek dari 0, 1, 2, 3, 4, 5
print(kata[6:])     # Programming -> dari index 6 sampai akhir
print(kata[:6])     # Python -> dari awal sampai index 5
print(kata[:])      # seluruh string "PythonProgramming"
print(kata[::-1])   
# [::-1] Artinya:
# - Tidak ditentukan index awal  -> mulai dari akhir string
# - Tidak ditentukan index akhir -> sampai awal string
# - Step = -1 berarti:
#   ambil karakter MUNDUR satu per satu
# - Digunakan untuk membalik string
# Hasil: "gnimmargorPnohty"


# ------------------------------------------------------
# 12. ESCAPE CHARACTERS
# ------------------------------------------------------
# Escape character digunakan untuk:
# - Menulis karakter khusus di dalam string
# - Menghindari konflik dengan tanda petik
# - Membuat baris baru, tab, dll
#
# Escape character diawali dengan tanda backslash (\)

# -------------------------------
# PETIK DI DALAM STRING
# -------------------------------

print("Dia berkata: \"Python itu keren\"")
# \" digunakan untuk menampilkan tanda petik ganda di dalam string

print('Dia berkata: \'Belajar Python\'')
# \' digunakan untuk menampilkan tanda petik satu di dalam string


# -------------------------------
# BARIS BARU (NEW LINE)
# -------------------------------

print("Baris pertama\nBaris kedua\nBaris ketiga")
# \n membuat baris baru


# -------------------------------
# TAB (SPASI HORIZONTAL)
# -------------------------------

print("Nama:\tReffa")
print("Umur:\t20")
# \t membuat jarak seperti tombol TAB


# -------------------------------
# BACKSLASH ITU SENDIRI
# -------------------------------

print("Lokasi file: C:\\Users\\Reffa\\Documents")
# \\ digunakan untuk menampilkan satu karakter backslash (\)


# -------------------------------
# MULTI-LINE STRING
# -------------------------------
# Untuk teks panjang atau paragraf, bisa gunakan triple quote

teks_panjang = """Ini adalah contoh
string dengan banyak baris
tanpa perlu escape \\n secara manual"""

print(teks_panjang)


# -------------------------------
# RAW STRING
# -------------------------------
# Raw string (r"") membuat Python TIDAK memproses escape character
# Sangat berguna untuk path file atau regex

path = r"C:\Users\Reffa\Documents\python"
print(path)

# ------------------------------------------------------
# 13. STRING INTERPOLATION
# ------------------------------------------------------
# String interpolation adalah teknik menyisipkan
# nilai variabel ke dalam string dengan rapi dan mudah
#
# Tujuannya:
# - Membuat output lebih bersih
# - Menghindari penggabungan string yang ribet
# - Membuat kode lebih mudah dibaca


nama = "Reffa"
umur = 20
tinggi = 170.5


# ------------------------------------------------------
# CARA 1: CONCATENATION (CARA LAMA & TIDAK DISARANKAN)
# ------------------------------------------------------
# Menggabungkan string dengan tanda +

print("Nama saya " + nama + ", umur saya " + str(umur))
# Kekurangan:
# - Harus casting manual (str(umur))
# - Sulit dibaca
# - Mudah error


# ------------------------------------------------------
# CARA 2: STRING FORMAT (.format())
# ------------------------------------------------------
# Menggunakan method format()

print("Nama saya {}, umur saya {}".format(nama, umur))

print("Nama: {0}, Umur: {1}, Tinggi: {2}".format(nama, umur, tinggi))
# Angka 0,1,2 menunjukkan urutan variabel

print("Nama: {n}, Umur: {u}".format(n=nama, u=umur))
# Bisa juga pakai nama variabel


# ------------------------------------------------------
# CARA 3: F-STRING (PALING DIREKOMENDASIKAN)
# ------------------------------------------------------
# F-string diperkenalkan di Python 3.6+
# Cara ini:
# - Paling rapi
# - Paling mudah dibaca
# - Paling sering dipakai di dunia nyata

print(f"Nama saya {nama}, umur saya {umur}, tinggi saya {tinggi} cm")


# ------------------------------------------------------
# F-STRING DENGAN EKSPRESI
# ------------------------------------------------------
# Kita bisa langsung menulis ekspresi di dalam {}

print(f"Umur saya tahun depan adalah {umur + 1}")
print(f"Tinggi saya dalam meter adalah {tinggi / 100}")


# ------------------------------------------------------
# F-STRING DENGAN FUNCTION
# ------------------------------------------------------

def kuadrat(x):
    return x * x

print(f"Hasil kuadrat dari 5 adalah {kuadrat(5)}")


# ------------------------------------------------------
# F-STRING DENGAN FORMAT ANGKA
# ------------------------------------------------------
# Mengatur jumlah angka desimal

nilai = 3.14159265

print(f"Nilai pi: {nilai:.2f}")
# .2f artinya tampilkan 2 angka di belakang koma


# ------------------------------------------------------
# F-STRING MULTI-LINE
# ------------------------------------------------------

laporan = f"""
===== BIODATA =====
Nama   : {nama}
Umur   : {umur}
Tinggi : {tinggi} cm
===================
"""

print(laporan)


# ------------------------------------------------------
# LATIHAN
# ------------------------------------------------------
# 1. Minta input nama lengkap
#    - Tampilkan versi HURUF BESAR
#
# 2. Minta input kalimat
#    - Hitung jumlah karakternya
#
# 3. Minta input kata
#    - Tampilkan huruf pertama & terakhir
#
# 4. Buat program biodata rapi pakai f-string
