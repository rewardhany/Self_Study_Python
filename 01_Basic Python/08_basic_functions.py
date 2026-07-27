# ======================================================
# 08_basic_functions.py
# ======================================================
# MATERI: BASIC FUNCTIONS (FUNGSI DASAR)
# ======================================================
#
# Di file ini kita akan belajar:
#
#   1. Apa itu Function
#   2. Kenapa Function Penting
#   3. Cara Membuat Function
#   4. Cara Memanggil Function
#   5. Parameter dan Argument (bedanya apa?)
#   6. Default Parameter
#   7. Return Value
#   8. Return vs Print (konsep paling sering salah)
#   9. Alur Eksekusi Function Step-by-step
#  10. Function dengan Input dari User
#  11. Docstring (cara dokumentasi function)
#  12. Scope (ruang hidup variabel)
#  13. Studi Kasus Nyata
#  14. Latihan
#
# ======================================================


# ======================================================
# 1. APA ITU FUNCTION?
# ======================================================
#
# Function adalah BLOK KODE yang diberi nama,
# dan bisa dipanggil berkali-kali kapan pun kita mau.
#
# Analogi:
#
#   Bayangkan function seperti RESEP MASAK.
#
#   Kamu tidak memasak ulang dari nol setiap kali mau makan.
#   Kamu punya resep → ikuti → selesai.
#
#   Resep = Function
#   Bahan = Input (Parameter)
#   Masakan = Output (Return Value)
#
#
# Visualisasi sederhana:
#
#   [INPUT] --> ( FUNCTION ) --> [OUTPUT]
#
#
# Contoh di dunia nyata:
#
#   Mesin ATM:
#
#   Input  : Kartu + PIN + Jumlah uang
#   Proses : Verifikasi, potong saldo
#   Output : Uang keluar
#
#   Kita tidak tahu mekanisme dalamnya.
#   Kita hanya peduli: masukkan input → dapat output.
#
#   Inilah konsep function!


# ======================================================
# 2. KENAPA FUNCTION ITU PENTING?
# ======================================================
#
# Masalah tanpa function:
#
#   Misalkan kamu ingin hitung luas persegi untuk 3 data:

panjang1 = 5
luas1 = panjang1 * panjang1
print("Luas 1:", luas1)

panjang2 = 8
luas2 = panjang2 * panjang2
print("Luas 2:", luas2)

panjang3 = 12
luas3 = panjang3 * panjang3
print("Luas 3:", luas3)

#
# Kode di atas berulang terus!
# Kalau ada bug di formula, kamu harus perbaiki di 3 tempat.
# Bayangkan kalau 100 data?
#
#
# Solusinya: FUNCTION
#
# Prinsip DRY = Don't Repeat Yourself
#
# Tulis sekali, pakai berkali-kali.


# ======================================================
# 3. MEMBUAT FUNCTION
# ======================================================
#
# Kata kunci: def
# def = define = mendefinisikan
#
# Struktur dasar:
#
#   def nama_function():
#       isi kode
#
#
# ATURAN NAMA FUNCTION:
#
#   - Huruf kecil semua
#   - Kata dipisah dengan underscore _
#   - Nama harus menjelaskan APA yang dilakukan
#
#   BENAR  : hitung_luas, cek_kelulusan, tampilkan_menu
#   SALAH  : x, fungsi1, f, HITUNGLUAS
#
#
# Contoh paling sederhana:

def tampilkan_salam():
    print("Halo, selamat datang di Python!")

#
# PERHATIKAN INI:
#
#   Saat Python membaca baris "def tampilkan_salam():"
#   Python HANYA MENDAFTARKAN function tersebut.
#   Function BELUM DIJALANKAN.
#
#   Ini seperti kamu menulis resep di buku.
#   Resep belum dimasak. Hanya dicatat.
#


# ======================================================
# 4. MEMANGGIL FUNCTION
# ======================================================
#
# Untuk menjalankan function, kita harus memanggilnya:
#
#   nama_function()
#
# Jangan lupa tanda kurung ()!

tampilkan_salam()
# Output: Halo, selamat datang di Python!

#
# Function bisa dipanggil berkali-kali:

tampilkan_salam()
tampilkan_salam()
tampilkan_salam()

# Output:
# Halo, selamat datang di Python!
# Halo, selamat datang di Python!
# Halo, selamat datang di Python!

#
# Sekarang kita perbaiki masalah luas persegi tadi:

def hitung_luas_persegi(panjang):
    luas = panjang * panjang
    print("Luas:", luas)

hitung_luas_persegi(5)
hitung_luas_persegi(8)
hitung_luas_persegi(12)

# Jauh lebih rapi!
# Kalau formula salah, cukup perbaiki di 1 tempat.


# ======================================================
# 5. PARAMETER vs ARGUMENT
# ======================================================
#
# INI SERING BIKIN BINGUNG. Mari kita luruskan.
#
#
# PARAMETER = variabel yang ditulis saat MEMBUAT function
#
#   def sapa(nama):   <-- "nama" adalah PARAMETER
#       print("Halo,", nama)
#
#
# ARGUMENT = nilai nyata yang dikirim saat MEMANGGIL function
#
#   sapa("Reffa")     <-- "Reffa" adalah ARGUMENT
#
#
# Analogi:
#
#   Parameter = Kolom isian di formulir  (nama: ___)
#   Argument  = Tinta yang kamu isi       (nama: Reffa)
#
#
# Contoh lebih jelas:

def perkenalan(nama, kota):      # nama, kota = PARAMETER
    print("Nama saya", nama)
    print("Saya dari", kota)

perkenalan("Reffa", "Bandung")   # "Reffa", "Bandung" = ARGUMENT

# Output:
# Nama saya Reffa
# Saya dari Bandung

#
# Yang terjadi di balik layar:
#
#   nama = "Reffa"    (argument dikirim ke parameter)
#   kota = "Bandung"
#
#   lalu kode di dalam function dijalankan

perkenalan("Budi", "Jakarta")    # bisa panggil lagi dengan data berbeda

# Output:
# Nama saya Budi
# Saya dari Jakarta


# ======================================================
# 6. DEFAULT PARAMETER
# ======================================================
#
# Kita bisa memberi nilai DEFAULT pada parameter.
# Artinya: kalau argument tidak dikirim, pakai nilai default.
#
# Bentuk:
#
#   def nama_function(parameter=nilai_default):

def sapa(nama, sapaan="Halo"):
    print(sapaan + ",", nama + "!")

sapa("Reffa")              # sapaan pakai default "Halo"
# Output: Halo, Reffa!

sapa("Budi", "Selamat pagi")  # sapaan diganti
# Output: Selamat pagi, Budi!

#
# ATURAN PENTING:
#
#   Parameter dengan default harus ditulis SETELAH
#   parameter tanpa default.
#
#   BENAR  : def fungsi(a, b=10)
#   SALAH  : def fungsi(a=10, b)   <-- error!


# ======================================================
# 7. RETURN VALUE
# ======================================================
#
# Return = mengembalikan nilai dari dalam function
#          ke luar (ke yang memanggilnya)
#
# Analoginya:
#
#   Kamu minta tolong teman beli kopi.
#   Teman pergi → beli kopi → MENGEMBALIKAN kopi ke kamu.
#
#   "mengembalikan" itulah RETURN.
#
#
# Tanpa return (hanya print):

def tambah_tanpa_return(a, b):
    print(a + b)     # hanya tampil di layar

hasil = tambah_tanpa_return(3, 5)
print("Isi variabel hasil:", hasil)

# Output:
# 8                      (dari print di dalam function)
# Isi variabel hasil: None   <-- NONE! Bukan 8!

#
# Kenapa None?
# Karena function tidak mengembalikan nilai apapun.
# Python otomatis mengembalikan None kalau tidak ada return.
#
#
# Dengan return:

def tambah_dengan_return(a, b):
    return a + b     # nilai dikembalikan ke pemanggil

hasil = tambah_dengan_return(3, 5)
print("Isi variabel hasil:", hasil)

# Output:
# Isi variabel hasil: 8   <-- BENAR!

#
# Sekarang nilai 8 tersimpan di variabel hasil.
# Bisa dipakai lagi!

print(hasil * 2)      # 16
print(hasil + 100)    # 108

#
# Alur lengkap dengan return:
#
#   tambah_dengan_return(3, 5)
#          |
#          v
#       a = 3, b = 5
#          |
#          v
#       return 3 + 5
#          |
#          v
#       return 8
#          |
#          v
#   hasil = 8   (nilai 8 "pulang" ke variabel hasil)


# ======================================================
# 8. RETURN vs PRINT — PERBEDAAN PALING PENTING
# ======================================================
#
# Ini konsep yang paling sering salah dipahami pemula.
#
# +------------------+---------------------------+
# |      PRINT       |          RETURN           |
# +------------------+---------------------------+
# | Tampilkan ke     | Kirim nilai ke            |
# | layar (manusia)  | pemanggil function        |
# +------------------+---------------------------+
# | Nilai hilang     | Nilai bisa disimpan       |
# | setelah tampil   | di variabel               |
# +------------------+---------------------------+
# | Untuk debugging  | Untuk dipakai lagi        |
# | atau info user   | di bagian kode lain       |
# +------------------+---------------------------+
#
#
# Contoh kasus nyata:
#
# Misalkan kamu ingin hitung luas dan keliling persegi,
# lalu jumlahkan keduanya.
#
# Dengan PRINT (tidak bisa dijumlahkan):

def luas_print(sisi):
    print(sisi * sisi)       # tampil ke layar, tapi hilang

def keliling_print(sisi):
    print(4 * sisi)          # sama, tampil tapi hilang

# Tidak bisa dijumlahkan!
# luas_print(5) + keliling_print(5) --> ERROR!
#
#
# Dengan RETURN (bisa dijumlahkan):

def luas_return(sisi):
    return sisi * sisi

def keliling_return(sisi):
    return 4 * sisi

l = luas_return(5)       # l = 25
k = keliling_return(5)   # k = 20
total = l + k
print("Total:", total)   # Total: 45

#
# KESIMPULAN:
#
#   Gunakan PRINT  : kalau hanya ingin tampilkan info ke layar
#   Gunakan RETURN : kalau nilai akan dipakai lagi di kode lain


# ======================================================
# 9. ALUR EKSEKUSI FUNCTION STEP-BY-STEP
# ======================================================
#
# Penting untuk paham URUTAN Python menjalankan kode.
#
# Contoh:

def kuadrat(x):
    hasil = x * x
    return hasil

print("Sebelum memanggil function")

nilai = kuadrat(7)

print("Sesudah memanggil function")
print("Hasilnya:", nilai)

#
# Alur eksekusinya:
#
#   1. Python baca "def kuadrat(x):" → function didaftarkan, tidak jalan
#
#   2. Python jalankan: print("Sebelum memanggil function")
#      Output: Sebelum memanggil function
#
#   3. Python baca: nilai = kuadrat(7)
#      → Python MASUK ke function kuadrat
#      → x = 7
#      → hasil = 7 * 7 = 49
#      → return 49
#      → Python KELUAR dari function
#      → nilai = 49
#
#   4. Python jalankan: print("Sesudah memanggil function")
#      Output: Sesudah memanggil function
#
#   5. Python jalankan: print("Hasilnya:", nilai)
#      Output: Hasilnya: 49
#
#
# Bayangkan seperti pergi ke minimarket:
#
#   Kamu lagi jalan (program utama)
#   → Mampir ke minimarket (masuk function)
#   → Beli sesuatu (proses di dalam function)
#   → Balik ke jalan (return, keluar function)
#   → Lanjut perjalanan (program utama lanjut)


# ======================================================
# 10. FUNCTION DENGAN INPUT DARI USER
# ======================================================
#
# Input dari user sebaiknya diambil DI LUAR function.
# Kenapa?
#
#   Supaya function bisa dipakai ulang dengan data apapun,
#   tidak hanya dari keyboard.
#
# KURANG BAIK (input di dalam function):

def luas_kurang_baik():
    sisi = int(input("Masukkan sisi: "))   # terlalu spesifik
    return sisi * sisi

# Function ini HANYA bisa dipakai kalau ada keyboard.
# Tidak bisa dipakai kalau data dari file atau database.

#
# LEBIH BAIK (input di luar function):

def hitung_luas(sisi):                     # function murni
    return sisi * sisi

# Ambil input di luar
sisi_input = int(input("Masukkan panjang sisi: "))

# Kirim ke function
luas = hitung_luas(sisi_input)

print("Luas persegi:", luas)

#
# Dengan cara ini, function hitung_luas bisa dipakai untuk:
#   - Data dari keyboard  : hitung_luas(int(input(...)))
#   - Data dari list      : hitung_luas(data[0])
#   - Data langsung       : hitung_luas(10)


# ======================================================
# 11. DOCSTRING — DOKUMENTASI FUNCTION
# ======================================================
#
# Docstring adalah teks penjelasan di dalam function.
# Ditulis pakai tiga tanda kutip """ di baris pertama function.
#
# Tujuannya: supaya orang lain (atau kamu sendiri 6 bulan lagi)
# bisa langsung paham apa yang dilakukan function ini.

def hitung_rata_rata(angka1, angka2, angka3):
    """
    Menghitung rata-rata dari tiga angka.

    Parameter:
        angka1 : angka pertama
        angka2 : angka kedua
        angka3 : angka ketiga

    Return:
        rata-rata dari ketiga angka (float)
    """
    total = angka1 + angka2 + angka3
    return total / 3

hasil = hitung_rata_rata(80, 90, 70)
print("Rata-rata:", hasil)

# Output: Rata-rata: 80.0

#
# Kamu bisa lihat docstring dengan:
# help(hitung_rata_rata)
# atau
# print(hitung_rata_rata.__doc__)


# ======================================================
# 12. SCOPE — RUANG HIDUP VARIABEL
# ======================================================
#
# Scope = area di mana sebuah variabel bisa diakses.
#
# Ada dua jenis:
#
#   LOCAL  = variabel yang hidup DI DALAM function
#   GLOBAL = variabel yang hidup DI LUAR function
#
#
# Contoh LOCAL scope:

def hitung():
    angka = 100        # angka adalah variabel LOCAL
    print(angka)       # bisa diakses di dalam function

hitung()

# print(angka)       # ERROR! angka tidak dikenal di luar function

#
# Kenapa?
# Variabel lokal "mati" begitu function selesai dijalankan.
# Seperti catatan di papan tulis yang dihapus setelah kelas selesai.
#
#
# Contoh GLOBAL scope:

nama_program = "Kalkulator Sederhana"   # variabel GLOBAL

def tampilkan_judul():
    print("Program:", nama_program)     # bisa akses variabel global

tampilkan_judul()
# Output: Program: Kalkulator Sederhana

#
#
# ATURAN PENTING:
#
#   Variabel dengan nama yang sama di dalam dan luar function
#   adalah DUA VARIABEL BERBEDA!

x = 10          # x global

def ubah():
    x = 99      # ini x LOCAL (berbeda dengan x global!)
    print("x di dalam function:", x)

ubah()
print("x di luar function:", x)

# Output:
# x di dalam function: 99
# x di luar function: 10
#
# x global tidak berubah!


# ======================================================
# 13. STUDI KASUS NYATA
# ======================================================
#
# Mari kita buat program sederhana yang menggunakan
# beberapa function sekaligus.
#
# Kasus: Sistem Nilai Mahasiswa

def hitung_rata_rata_nilai(tugas, uts, uas):
    """
    Hitung rata-rata nilai dengan bobot:
    Tugas 30%, UTS 30%, UAS 40%
    """
    return (tugas * 0.3) + (uts * 0.3) + (uas * 0.4)

def tentukan_grade(rata_rata):
    """
    Tentukan grade berdasarkan nilai rata-rata.
    """
    if rata_rata >= 85:
        return "A"
    elif rata_rata >= 75:
        return "B"
    elif rata_rata >= 65:
        return "C"
    elif rata_rata >= 55:
        return "D"
    else:
        return "E"

def cek_kelulusan(grade):
    """
    Cek apakah mahasiswa lulus berdasarkan grade.
    Lulus jika grade A, B, atau C.
    """
    if grade in ["A", "B", "C"]:
        return "LULUS"
    else:
        return "TIDAK LULUS"

def tampilkan_hasil(nama, rata_rata, grade, status):
    """
    Tampilkan laporan nilai mahasiswa.
    """
    print("=" * 30)
    print("LAPORAN NILAI MAHASISWA")
    print("=" * 30)
    print("Nama    :", nama)
    print("Rata-rata:", round(rata_rata, 2))
    print("Grade   :", grade)
    print("Status  :", status)
    print("=" * 30)

# Program utama
nama_mhs   = "Rewardany"
nilai_tugas = 85
nilai_uts   = 78
nilai_uas   = 90

rata   = hitung_rata_rata_nilai(nilai_tugas, nilai_uts, nilai_uas)
grade  = tentukan_grade(rata)
status = cek_kelulusan(grade)

tampilkan_hasil(nama_mhs, rata, grade, status)

# Output:
# ==============================
# LAPORAN NILAI MAHASISWA
# ==============================
# Nama    : Rewardany
# Rata-rata: 85.4
# Grade   : A
# Status  : LULUS
# ==============================

#
# Perhatikan:
#
#   Program dipecah menjadi 4 function kecil.
#   Masing-masing punya 1 tugas spesifik.
#
#   Ini disebut prinsip Single Responsibility:
#   "Satu function, satu tanggung jawab."


# ======================================================
# 14. CARA BERPIKIR SAAT MEMBUAT FUNCTION
# ======================================================
#
# Sebelum menulis kode, jawab 4 pertanyaan ini:
#
#   1. Apa NAMA function?    → harus deskriptif
#   2. Apa INPUT-nya?        → parameter apa saja?
#   3. Apa PROSES-nya?       → logika di dalam
#   4. Apa OUTPUT-nya?       → apa yang di-return?
#
#
# Contoh:
#
#   Tugas: hitung luas segitiga
#
#   1. Nama  : hitung_luas_segitiga
#   2. Input : alas, tinggi
#   3. Proses: (alas * tinggi) / 2
#   4. Output: nilai luas (float)
#
#   Hasilnya:

def hitung_luas_segitiga(alas, tinggi):
    """Menghitung luas segitiga."""
    return (alas * tinggi) / 2

print(hitung_luas_segitiga(10, 5))   # Output: 25.0

#
# Kalau kamu bingung bikin function,
# jawab 4 pertanyaan itu dulu.
# Kodenya biasanya jadi mudah setelah itu.


# ======================================================
# 15. LATIHAN
# ======================================================
#
# Kerjakan semua latihan di bawah ini.
# Tulis kode kamu tepat di bawah masing-masing soal.
#
# -------------------------------------------------------
# LATIHAN 1
#
# Buat function: hitung_luas_persegi_panjang(panjang, lebar)
# - Gunakan return
# - Panggil dengan beberapa data berbeda
# -------------------------------------------------------

# Tulis kodemu di sini:


# -------------------------------------------------------
# LATIHAN 2
#
# Buat function: cek_kelulusan(nilai)
# - Jika nilai >= 70, return "LULUS"
# - Jika nilai < 70,  return "TIDAK LULUS"
# - Cetak hasilnya saat memanggil function
# -------------------------------------------------------

# Tulis kodemu di sini:


# -------------------------------------------------------
# LATIHAN 3
#
# Buat function: konversi_suhu(celsius)
# - Konversi celsius ke fahrenheit
# - Rumus: (celsius * 9/5) + 32
# - Gunakan return
# - Panggil dan cetak hasilnya
# -------------------------------------------------------

# Tulis kodemu di sini:


# -------------------------------------------------------
# LATIHAN 4 (TANTANGAN)
#
# Buat 3 function:
#
#   1. hitung_keliling_lingkaran(jari_jari)
#      Rumus: 2 * 3.14 * jari_jari
#
#   2. hitung_luas_lingkaran(jari_jari)
#      Rumus: 3.14 * jari_jari * jari_jari
#
#   3. tampilkan_info_lingkaran(jari_jari)
#      - Panggil function 1 dan 2 di sini
#      - Tampilkan keliling dan luas
#
# Panggil tampilkan_info_lingkaran dengan beberapa nilai.
# -------------------------------------------------------

# Tulis kodemu di sini:


# -------------------------------------------------------
# LATIHAN 5 (TANTANGAN EKSTRA)
#
# Buat program kalkulator sederhana dengan function:
#
#   tambah(a, b)    → return a + b
#   kurang(a, b)    → return a - b
#   kali(a, b)      → return a * b
#   bagi(a, b)      → return a / b (jika b != 0)
#                                    return "Tidak bisa dibagi 0" (jika b = 0)
#
# Ambil dua angka dari user dengan input().
# Jalankan semua operasi dan tampilkan hasilnya.
# -------------------------------------------------------

# Tulis kodemu di sini:


# ======================================================
# RINGKASAN MATERI
# ======================================================
#
#   def nama():          → membuat function
#   nama()               → memanggil function
#   def f(x):            → parameter
#   f(10)                → argument
#   return nilai         → mengembalikan nilai
#   """docstring"""      → dokumentasi function
#
#   LOCAL  scope: variabel hidup di dalam function
#   GLOBAL scope: variabel hidup di luar function
#
#   PRINT  → tampilkan ke layar, nilai hilang
#   RETURN → nilai bisa disimpan dan dipakai lagi
#
#   DRY = Don't Repeat Yourself
#   Satu function = Satu tanggung jawab
#
# ======================================================
# END OF MATERIAL
# ======================================================