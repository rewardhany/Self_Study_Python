# ======================================================
# 06 RECURSION
# ======================================================
# RECURSION adalah:
# Fungsi yang memanggil DIRINYA SENDIRI
#
# Digunakan ketika:
# - Masalah bisa dipecah jadi versi lebih kecil dari masalah yang sama
#
# STRUKTUR DASAR:
# def fungsi(n):
#     if kondisi_berhenti:      # BASE CASE - wajib ada!
#         return nilai_dasar
#     return fungsi(versi_lebih_kecil_dari_n)
# ======================================================


# ------------------------------------------------------
# CONTOH 1: FACTORIAL (KASUS KLASIK RECURSION)
# ------------------------------------------------------

def factorial(n):
    if n <= 1:              # BASE CASE: berhenti di sini
        return 1
    return n * factorial(n - 1)   # panggil dirinya sendiri dengan n lebih kecil

print(factorial(5))   # 5 * 4 * 3 * 2 * 1 = 120

# Penjelasan:
# - factorial(5) = 5 * factorial(4)
# - factorial(4) = 4 * factorial(3)
# - ...terus mengecil sampai factorial(1) = 1 (base case), baru hasilnya "naik" lagi
# - Base case WAJIB ada, kalau tidak -> RecursionError (infinite loop)


# ------------------------------------------------------
# CONTOH 2: FIBONACCI
# ------------------------------------------------------

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(8):
    print(fibonacci(i), end=" ")
print()

# Penjelasan:
# - Setiap angka fibonacci = jumlah 2 angka sebelumnya
# - Fungsi ini manggil dirinya sendiri DUA KALI tiap eksekusi
# - Catatan: cara ini gampang dipahami tapi LAMBAT untuk n besar (akan dibahas
#   optimasinya kalau nanti masuk ke topik algoritma lanjutan)


# ------------------------------------------------------
# CONTOH 3: MENJUMLAHKAN LIST SECARA REKURSIF
# ------------------------------------------------------

def jumlah_list(data):
    if len(data) == 0:          # BASE CASE: list kosong = 0
        return 0
    return data[0] + jumlah_list(data[1:])   # ambil elemen pertama + sisanya

angka = [10, 20, 30, 40]
print(jumlah_list(angka))

# Penjelasan:
# - data[0] = elemen pertama, data[1:] = sisa list tanpa elemen pertama
# - Tiap panggilan, list-nya makin pendek, sampai akhirnya kosong (base case)
# - Ini cara "manual" untuk apa yang sebenarnya sum() sudah lakukan otomatis


# ------------------------------------------------------
# CONTOH 4: JEBAKAN RECURSION TANPA BASE CASE YANG BENAR
# ------------------------------------------------------

# SALAH (jangan dijalankan, ini bakal infinite recursion):
# def hitung_mundur_salah(n):
#     print(n)
#     return hitung_mundur_salah(n - 1)   # tidak pernah berhenti!

# BENAR:
def hitung_mundur_benar(n):
    if n < 0:              # base case yang jelas
        return
    print(n)
    hitung_mundur_benar(n - 1)

hitung_mundur_benar(3)

# Penjelasan:
# - Tanpa base case yang BENAR-BENAR tercapai, fungsi manggil dirinya sendiri terus
# - Python akan berhenti sendiri dengan error "RecursionError: maximum recursion depth exceeded"
# - Selalu pastikan: ada base case, DAN nilai yang dikirim makin lama makin dekat ke base case itu


# ------------------------------------------------------
# CATATAN PENTING
# ------------------------------------------------------
# - Recursion selalu bisa diganti jadi loop biasa (while/for), dan sering kali
#   loop lebih efisien -> recursion dipakai kalau bikin kode LEBIH JELAS dibaca
# - Base case adalah bagian PALING PENTING, tulis itu duluan sebelum logika lain
# - Kalau bingung, coba trace manual di kertas untuk n kecil dulu (n=2 atau n=3)