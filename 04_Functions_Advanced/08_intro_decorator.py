# ======================================================
# 08 INTRO DECORATOR
# ======================================================
# DECORATOR adalah:
# Fungsi yang "membungkus" fungsi lain, untuk menambah perilaku baru
# TANPA mengubah kode asli fungsi tersebut
#
# STRUKTUR DASAR:
# @nama_decorator
# def fungsi_asli():
#     kode
# ======================================================


# ------------------------------------------------------
# CONTOH 1: FUNGSI SEBAGAI "OBJEK BIASA" (FIRST-CLASS FUNCTION)
# ------------------------------------------------------

def sapa():
    print("Halo!")

fungsi_lain = sapa   # fungsi bisa disimpan ke variabel lain, TANPA tanda kurung
fungsi_lain()          # baru dipanggil di sini

# Penjelasan:
# - Di Python, function itu "objek biasa" -> bisa disimpan, dikirim, di-return
# - sapa (tanpa kurung) = merujuk ke fungsinya
# - sapa()  (dengan kurung) = MEMANGGIL/menjalankan fungsinya
# - Konsep ini yang bikin decorator bisa ada


# ------------------------------------------------------
# CONTOH 2: FUNGSI YANG RETURN FUNGSI LAIN (CLOSURE)
# ------------------------------------------------------

def buat_pengali(angka):
    def pengali(x):
        return x * angka
    return pengali   # return FUNGSI, bukan hasil akhir

kali_tiga = buat_pengali(3)
print(kali_tiga(10))   # 10 * 3 = 30

# Penjelasan:
# - buat_pengali(3) mengembalikan FUNGSI BARU yang "ingat" angka=3
# - Ini disebut closure: fungsi dalam yang tetap ingat variabel dari fungsi luar
# - Closure adalah dasar mekanisme di balik decorator


# ------------------------------------------------------
# CONTOH 3: DECORATOR SEDERHANA DENGAN @ SYNTAX
# ------------------------------------------------------

def decorator_log(fungsi_asli):
    def pembungkus():
        print(f"[LOG] Menjalankan fungsi: {fungsi_asli.__name__}")
        fungsi_asli()
        print(f"[LOG] Selesai menjalankan: {fungsi_asli.__name__}")
    return pembungkus

@decorator_log
def proses_peminjaman():
    print("Memproses peminjaman buku...")

proses_peminjaman()

# Penjelasan:
# - @decorator_log di atas def sama saja dengan:
#   proses_peminjaman = decorator_log(proses_peminjaman)
# - fungsi_asli() tetap dijalankan, tapi sekarang "dibungkus" log di sekelilingnya
# - Fungsi asli TIDAK diubah kodenya sama sekali


# ------------------------------------------------------
# CONTOH 4: DECORATOR UNTUK FUNGSI YANG PUNYA PARAMETER
# ------------------------------------------------------

def decorator_timer(fungsi_asli):
    def pembungkus(*args, **kwargs):     # *args/**kwargs biar fleksibel untuk parameter apapun
        print(f"[TIMER] Mulai: {fungsi_asli.__name__}")
        hasil = fungsi_asli(*args, **kwargs)
        print(f"[TIMER] Selesai: {fungsi_asli.__name__}")
        return hasil
    return pembungkus

@decorator_timer
def hitung_denda(hari_telat):
    return hari_telat * 5000

total = hitung_denda(3)
print(f"Denda: {total}")

# Penjelasan:
# - *args, **kwargs (ingat BAB 4 file 03) dipakai supaya decorator ini bisa
#   membungkus fungsi APAPUN, tidak peduli berapa banyak parameternya
# - Ini pola standar kalau bikin decorator yang dipakai ulang di banyak fungsi


# ------------------------------------------------------
# CATATAN PENTING
# ------------------------------------------------------
# - Decorator sering dipakai untuk: logging, mengukur waktu eksekusi,
#   autentikasi/permission (nanti relevan banget di BAB 14 Auth_And_Sessions)
# - Kamu tidak perlu jago BIKIN decorator dulu -> yang penting paham cara BACA-nya,
#   karena banyak framework (Flask nanti) pakai @app.route(...) yang konsepnya sama persis
# - Kalau masih bingung, cukup ingat: @decorator di atas fungsi = fungsi itu "dibungkus"
#   sebelum benar-benar dijalankan