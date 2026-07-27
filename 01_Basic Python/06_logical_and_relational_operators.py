# ======================================================
# 06_logical_and_relational_operators.py
# ======================================================
# MATERI: OPERATOR PERBANDINGAN & LOGIKA
# ======================================================
#
# Di file ini kita akan belajar:
#
#   1. Operator Perbandingan (Relational)
#   2. JEBAKAN PEMULA: Beda `=` dan `==`
#   3. Operator Logika (Logical: and, or, not)
#   4. Chained Comparisons (Perbandingan Berantai ala Python)
#   5. Operator Keanggotaan (Membership: in, not in)
#   6. Konsep Truthy dan Falsy (Advanced Basic)
#   7. Studi Kasus Nyata
#   8. Latihan
#
# ======================================================


# ======================================================
# 1. OPERATOR PERBANDINGAN (RELATIONAL)
# ======================================================
#
# Operator ini digunakan untuk membandingkan dua buah nilai.
# Hasil dari perbandingan ini SELALU berupa boolean: True atau False.
#
# Macam-macam operator:
#   >   : Lebih besar dari
#   <   : Lebih kecil dari
#   >=  : Lebih besar atau sama dengan
#   <=  : Lebih kecil atau sama dengan
#   !=  : Tidak sama dengan
#   ==  : Sama dengan

print("--- 1. OPERATOR PERBANDINGAN ---")

x = 10
y = 5

print("Apakah x lebih besar dari y?", x > y)    # True
print("Apakah x lebih kecil dari y?", x < y)    # False
print("Apakah x tidak sama dengan y?", x != y)  # True
print("Apakah 10 >= 10?", 10 >= 10)             # True (karena ada "sama dengan")

print()


# ======================================================
# 2. JEBAKAN PEMULA: Beda `=` dan `==`
# ======================================================
#
# Ini adalah kesalahan paling sering terjadi saat baru belajar kode!
#
#   =   (Satu sama dengan) -> ASSIGNMENT (Memasukkan nilai)
#   ==  (Dua sama dengan)  -> COMPARISON (Membandingkan nilai)
#
# Analogi:
#   umur = 20   --> "Tolong masukkan angka 20 ke dalam kotak bernama umur."
#   umur == 20  --> "Apakah angka di dalam kotak umur bernilai 20?"

print("--- 2. PERBEDAAN = DAN == ---")

angka_rahasia = 7               # Memasukkan nilai 7 ke variabel
tebakan_user = 7                # Memasukkan nilai 7 ke variabel

hasil_tebakan = (tebakan_user == angka_rahasia) # Membandingkan keduanya
print("Apakah tebakan benar?", hasil_tebakan)   # Output: True

print()


# ======================================================
# 3. OPERATOR LOGIKA (LOGICAL)
# ======================================================
#
# Operator logika digunakan untuk menggabungkan beberapa kondisi perbandingan.
#
#   and -> True HANYA JIKA kedua kondisi True.
#   or  -> True JIKA SALAH SATU saja kondisi True.
#   not -> Membalik nilai boolean (True jadi False, False jadi True).
#
# Analogi 'and': (Harus bawa KTP DAN Tiket untuk masuk konser)
# Analogi 'or' : (Boleh bayar pakai Cash ATAU Debit)

print("--- 3. OPERATOR LOGIKA ---")

bawa_ktp = True
bawa_tiket = False

print("Bisa masuk konser (and)?", bawa_ktp and bawa_tiket)  # False (karena tiket False)
print("Boleh masuk (or)?", bawa_ktp or bawa_tiket)          # True (karena salah satu True)

# Contoh penggunaan 'not'
hujan = True
print("Apakah sekarang tidak hujan?", not hujan)            # False

print()


# ======================================================
# 4. CHAINED COMPARISONS (PERBANDINGAN BERANTAI)
# ======================================================
#
# Salah satu fitur paling keren di Python!
# Kalau di bahasa pemrograman lain, untuk cek rentang angka harus pakai 'and'.
#
# Contoh bahasa lain: umur >= 13 and umur <= 17
# Di Python, kamu bisa menulisnya seperti rumus matematika biasa!

print("--- 4. PERBANDINGAN BERANTAI ---")

umur = 15

# Cara biasa (Valid, tapi panjang)
cek_remaja_1 = umur >= 13 and umur <= 17
print("Cara biasa:", cek_remaja_1)

# Cara Pythonic (Lebih elegan dan disarankan)
cek_remaja_2 = 13 <= umur <= 17
print("Cara Pythonic:", cek_remaja_2)

print()


# ======================================================
# 5. OPERATOR KEANGGOTAAN (MEMBERSHIP)
# ======================================================
#
# Sangat berguna untuk mengecek apakah sebuah nilai ada di dalam
# sekumpulan nilai (seperti teks/string, list, dll).
#
#   in      -> True jika nilai DITEMUKAN
#   not in  -> True jika nilai TIDAK DITEMUKAN

print("--- 5. OPERATOR KEANGGOTAAN ---")

nama_user = "Reffa"
huruf_dicari = "R"

print("Apakah ada huruf 'R' di nama_user?", huruf_dicari in nama_user)      # True
print("Apakah ada huruf 'Z' di nama_user?", "Z" in nama_user)               # False

# Cek kata terlarang (contoh sederhana)
komentar = "Dasar kamu bodoh!"
print("Apakah ada kata kasar?", "bodoh" in komentar)                        # True

print()


# ======================================================
# 6. KONSEP TRUTHY DAN FALSY (PENTING!)
# ======================================================
#
# Di Python, sesuatu yang dievaluasi sebagai logika tidak harus
# berupa tulisan `True` atau `False`.
#
# Segala sesuatu yang KOSONG dianggap False (Falsy).
# Segala sesuatu yang ADA ISINYA dianggap True (Truthy).
#
# Yang dianggap FALSY (False):
#   - Angka 0
#   - String kosong ""
#   - List kosong []
#   - None
#
# Selain di atas, semuanya TRUTHY (True)!

print("--- 6. TRUTHY DAN FALSY ---")

# Memanfaatkan Falsy pada string kosong
username_input = ""  # User tidak mengetik apa-apa

# 'not username_input' artinya 'not False' -> True
if not username_input:
    print("Error: Username tidak boleh kosong!")

print("Nilai boolean dari 0 adalah:", bool(0))          # False
print("Nilai boolean dari 100 adalah:", bool(100))      # True
print("Nilai boolean dari 'Halo' adalah:", bool("Halo"))# True

print()


# ======================================================
# 7. STUDI KASUS NYATA
# ======================================================

print("--- 7. STUDI KASUS ---")

# Sistem pengecekan syarat mendaftar pekerjaan
# Syarat: Umur 18-30 tahun, lulusan S1, dan tidak punya catatan kriminal

umur_pelamar = 24
gelar = "S1"
catatan_kriminal = False

syarat_umur = 18 <= umur_pelamar <= 30
syarat_pendidikan = gelar == "S1"
berkelakuan_baik = not catatan_kriminal  # (not False -> True)

lulus_seleksi = syarat_umur and syarat_pendidikan and berkelakuan_baik

print("Apakah pelamar lulus seleksi administrasi?", lulus_seleksi)
print()


# ======================================================
# 8. LATIHAN
# ======================================================
#
# Kerjakan latihan di bawah ini untuk menguji pemahamanmu!
# Tulis kodemu di bagian yang sudah disediakan.
#
# ------------------------------------------------------
# SOAL 1: Cek Diskon Belanja
#
# Seorang pembeli akan mendapatkan diskon JIKA:
# - Total belanjanya lebih dari 100.000, ATAU
# - Dia adalah member VIP (member_vip = True)
#
# Buatlah logika untuk mengecek apakah pembeli dapat diskon!
# ------------------------------------------------------

# Tulis kodemu di sini:



# ------------------------------------------------------
# SOAL 2: Sistem Login Sederhana
#
# Username yang benar adalah "admin"
# Password yang benar adalah "rahasia123"
#
# Buatlah program yang meminta input() username dan password,
# lalu cetak True jika login berhasil, dan False jika gagal.
# ------------------------------------------------------

# Tulis kodemu di sini:



# ------------------------------------------------------
# SOAL 3: Pengecekan Umur (Gunakan Chained Comparison)
#
# Buat program yang mengecek kategori umur:
# - Anak   : < 13
# - Remaja : 13 - 17
# - Dewasa : >= 18
#
# Coba buat se-efisien mungkin menggunakan cara Pythonic!
# ------------------------------------------------------

# Tulis kodemu di sini:



# ======================================================
# RINGKASAN MATERI
# ======================================================
#
#   > < >= <= !=   -> Operator Perbandingan
#   = vs ==        -> = (isi nilai), == (cek kesamaan)
#   and            -> Dua-duanya wajib True
#   or             -> Salah satu True udah cukup
#   not            -> Membalik fakta (True -> False)
#   in / not in    -> Cek isi di dalam kumpulan teks/data
#   Truthy/Falsy   -> 0 dan "" itu False, selain itu True
#   10 < x < 20    -> Cara elegan Python (Chained Comparison)
#
# ======================================================
# END OF MATERIAL
# ======================================================