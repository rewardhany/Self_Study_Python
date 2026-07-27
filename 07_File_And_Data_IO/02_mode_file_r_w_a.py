# ======================================================
# 02 MODE FILE (r, w, a, dan lainnya)
# ======================================================
# Mode menentukan APA yang boleh dilakukan ke file saat dibuka
#
# - "r"  -> read (default), ERROR kalau file tidak ada
# - "w"  -> write, BIKIN BARU atau TIMPA HABIS isi lama
# - "a"  -> append, TAMBAH di akhir file, isi lama tetap ada
# - "x"  -> exclusive create, ERROR kalau file SUDAH ADA
# - "r+" -> baca DAN tulis sekaligus
# ======================================================


# ------------------------------------------------------
# CONTOH 1: "w" MENIMPA HABIS ISI LAMA
# ------------------------------------------------------

file = open("log_kegiatan.txt", "w")
file.write("Baris pertama\n")
file.close()

file = open("log_kegiatan.txt", "w")   # dibuka lagi dengan "w"
file.write("Baris ini MENIMPA baris pertama\n")
file.close()

file = open("log_kegiatan.txt", "r")
print(file.read())   # "Baris pertama" SUDAH HILANG
file.close()

# Penjelasan:
# - Setiap kali file dibuka dengan "w", isi LAMA LANGSUNG HILANG
# - Hati-hati: ini kesalahan umum kalau maksudnya mau NAMBAH data, bukan menimpa


# ------------------------------------------------------
# CONTOH 2: "a" MENAMBAH TANPA MENGHAPUS ISI LAMA
# ------------------------------------------------------

file = open("log_kegiatan.txt", "w")
file.write("Log 1: Rapat divisi Keamanan\n")
file.close()

file = open("log_kegiatan.txt", "a")   # mode APPEND
file.write("Log 2: Cek logistik selesai\n")
file.close()

file = open("log_kegiatan.txt", "r")
print(file.read())   # KEDUA baris muncul, tidak ada yang hilang
file.close()

# Penjelasan:
# - "a" selalu nulis di AKHIR file, isi sebelumnya tetap utuh
# - Cocok buat file log yang datanya terus bertambah dari waktu ke waktu


# ------------------------------------------------------
# CONTOH 3: "r" ERROR KALAU FILE TIDAK ADA (SEGUE KE BAB 6)
# ------------------------------------------------------

try:
    file = open("file_yang_tidak_ada.txt", "r")
    print(file.read())
    file.close()
except FileNotFoundError:
    print("File tidak ditemukan!")

# Penjelasan:
# - "r" (dan default kalau mode tidak ditulis) BUTUH file-nya sudah ADA
# - Kalau tidak ada -> FileNotFoundError, ini kenapa BAB 6 (Error Handling)
#   penting banget buat file I/O -> banyak hal bisa gagal (file hilang,
#   tidak ada izin akses, dst)


# ------------------------------------------------------
# CONTOH 4: "x" - BIKIN FILE BARU, TAPI ERROR KALAU SUDAH ADA
# ------------------------------------------------------

try:
    file = open("catatan.txt", "x")   # dari file 01, catatan.txt sudah ada
    file.write("Ini tidak akan pernah tertulis")
    file.close()
except FileExistsError:
    print("File sudah ada, tidak jadi ditimpa (mode 'x' melindungi dari overwrite)")

# Penjelasan:
# - "x" kebalikan dari "w" -> "w" bikin baru ATAU timpa, "x" CUMA bikin baru
# - Berguna kalau kamu mau PASTIKAN tidak sengaja menimpa file yang sudah ada


# ------------------------------------------------------
# CATATAN PENTING
# ------------------------------------------------------
# - "w" = timpa habis, "a" = tambah di akhir, "r" = baca saja (file harus ada)
# - "x" = bikin baru, tapi menolak kalau file sudah ada
# - Salah pilih mode ("w" padahal maksudnya "a") adalah kesalahan paling
#   umum pemula -> data yang harusnya bertambah malah hilang semua