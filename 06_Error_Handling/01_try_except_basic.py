# ======================================================
# 01 TRY EXCEPT BASIC
# ======================================================
# TRY EXCEPT adalah:
# Cara "menangkap" error supaya program TIDAK CRASH,
# dan bisa kasih respons yang lebih baik ke user
#
# STRUKTUR DASAR:
# try:
#     kode yang MUNGKIN error
# except:
#     kode yang jalan KALAU error terjadi
# ======================================================


# ------------------------------------------------------
# CONTOH 1: TANPA TRY-EXCEPT VS DENGAN TRY-EXCEPT
# ------------------------------------------------------

# Tanpa try-except (program CRASH kalau user input huruf):
# umur = int(input("Masukkan umur: "))   # kalau user ketik "abc" -> ValueError, program berhenti

# Dengan try-except:
try:
    umur = int(input("Masukkan umur: "))
    print(f"Umur kamu: {umur}")
except ValueError:
    print("Input harus berupa angka!")

# Penjelasan:
# - Kode di dalam try dijalankan seperti biasa
# - Kalau terjadi error JENIS ValueError, program TIDAK crash, malah lompat ke except
# - Program lanjut jalan setelah blok try-except, bukan berhenti total


# ------------------------------------------------------
# CONTOH 2: MENANGKAP DAN MELIHAT ISI ERROR (as e)
# ------------------------------------------------------

 try:
    hasil = 10 / 0
 except ZeroDivisionError as e:
    print(f"Terjadi error: {e}")

# Penjelasan:
# - `as e` nyimpen object error-nya ke variabel e
# - print(e) nampilin PESAN error aslinya dari Python, berguna buat debugging
# - ZeroDivisionError = error spesifik saat bagi dengan angka 0


# ------------------------------------------------------
# CONTOH 3: BARE EXCEPT (BOLEH TAPI TIDAK DISARANKAN)
# ------------------------------------------------------

try:
    angka = int("bukan angka")
except:                      # menangkap SEMUA jenis error, apapun itu
    print("Terjadi kesalahan!")

# Penjelasan:
# - except: tanpa nama error menangkap SEGALA jenis error
# - MASALAHNYA: kamu jadi tidak tahu error APA yang sebenarnya terjadi
# - Sebaiknya selalu sebutkan jenis error-nya spesifik (ValueError, dst),
#   lebih detail di 02_multiple_exceptions.py


# ------------------------------------------------------
# CONTOH 4: TRY-EXCEPT DI DALAM LOOP (ULANG SAMPAI VALID)
# ------------------------------------------------------

while True:
    try:
        umur = int(input("Masukkan umur (angka): "))
        break   # kalau berhasil, keluar dari loop
    except ValueError:
        print("Input tidak valid, coba lagi.")

print(f"Umur yang tersimpan: {umur}")

# Penjelasan:
# - Pola ini SANGAT umum: minta input terus sampai valid, tidak langsung crash
# - break di dalam try hanya jalan kalau TIDAK ada error (baris int() berhasil)
# - Ini upgrade penting dari validasi input yang masih sederhana di project-project lama


# ------------------------------------------------------
# CATATAN PENTING
# ------------------------------------------------------
# - try-except MELINDUNGI program dari crash, bukan "menghilangkan" errornya
# - Selalu sebutkan jenis error spesifik, hindari except: kosong
# - Pola while True + try + break sangat berguna untuk validasi input berulang