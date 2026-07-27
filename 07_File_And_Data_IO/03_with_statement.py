# ======================================================
# 03 WITH STATEMENT
# ======================================================
# WITH STATEMENT adalah:
# Cara membuka file yang OTOMATIS menutupnya sendiri,
# walau terjadi error di tengah jalan
#
# STRUKTUR DASAR:
# with open("file.txt", "mode") as file:
#     kode
# # file otomatis tertutup di sini, walau ada error di dalam blok with
# ======================================================


# ------------------------------------------------------
# CONTOH 1: MANUAL close() VS with (PERBANDINGAN)
# ------------------------------------------------------

# Cara manual (dari file 01):
file = open("catatan.txt", "w")
file.write("Ditulis cara manual\n")
file.close()

# Cara with (lebih aman):
with open("catatan.txt", "w") as file:
    file.write("Ditulis pakai with statement\n")
# tidak perlu file.close() -> otomatis tertutup begitu keluar blok with

# Penjelasan:
# - "as file" -> file yang dibuka disimpan ke variabel file, sama seperti biasa
# - Begitu baris di dalam with selesai (atau kalau ada error), file OTOMATIS ditutup
# - Ini alasan kenapa with jadi CARA STANDAR untuk file I/O di Python


# ------------------------------------------------------
# CONTOH 2: with UNTUK MEMBACA FILE
# ------------------------------------------------------

with open("catatan.txt", "r") as file:
    isi = file.read()
    print(isi)

# file sudah tertutup otomatis di titik ini, walau tidak ada file.close()

# Penjelasan:
# - Sama seperti open() biasa, tinggal tambah with ... as di depannya
# - Variabel isi tetap bisa dipakai SETELAH blok with selesai (isinya sudah
#   ke-copy ke variabel), yang tertutup cuma KONEKSI ke file-nya


# ------------------------------------------------------
# CONTOH 3: with UNTUK MENULIS BEBERAPA BARIS SEKALIGUS
# ------------------------------------------------------

daftar_tugas = ["Notulensi rapat", "Cek logistik", "Update tata tertib"]

with open("tugas_odwh.txt", "w") as file:
    for tugas in daftar_tugas:
        file.write(f"- {tugas}\n")

with open("tugas_odwh.txt", "r") as file:
    print(file.read())

# Penjelasan:
# - Bisa nulis file dalam loop, selama masih di dalam 1 blok with yang sama
# - Ini pola umum: siapkan data di list/dict dulu, baru tulis semuanya ke file


# ------------------------------------------------------
# CONTOH 4: with + try/except (KOMBINASI DENGAN BAB 6)
# ------------------------------------------------------

try:
    with open("file_tidak_ada.txt", "r") as file:
        isi = file.read()
except FileNotFoundError:
    print("File tidak ditemukan, tidak bisa dibaca.")
else:
    print(isi)
finally:
    print("Percobaan baca file selesai.")

# Penjelasan:
# - with TIDAK menggantikan try/except -> keduanya dipakai BARENGAN
# - with urus soal "pastikan file tertutup dengan benar"
# - try/except urus soal "apa yang terjadi kalau file-nya bermasalah"
# - Ini kombinasi yang akan kamu pakai HAMPIR SELALU untuk file I/O ke depannya


# ------------------------------------------------------
# CATATAN PENTING
# ------------------------------------------------------
# - Mulai sekarang, SELALU pakai with untuk buka file, bukan open()...close() manual
# - with menjamin file tertutup walau ada error, open manual tidak menjamin itu
# - with + try/except adalah kombinasi standar untuk file I/O yang aman