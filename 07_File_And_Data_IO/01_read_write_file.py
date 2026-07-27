# ======================================================
# 01 READ WRITE FILE
# ======================================================
# FILE HANDLING adalah:
# Cara Python menyimpan data ke file di disk, dan membacanya kembali
#
# Kenapa penting: semua project kamu selama ini datanya HILANG tiap
# program ditutup (list, dict cuma hidup di memori). File I/O adalah
# langkah pertama supaya data bisa PERSISTEN (tersimpan permanen).
#
# STRUKTUR DASAR:
# file = open("nama_file.txt", "mode")
# file.write("isi")   /   file.read()
# file.close()
# ======================================================


# ------------------------------------------------------
# CONTOH 1: MENULIS FILE BARU
# ------------------------------------------------------

file = open("catatan.txt", "w")   # "w" = write, bikin file baru (atau timpa yang lama)
file.write("Catatan ODWH 2026\n")
file.write("Divisi Keamanan sudah selesai notulensi.\n")
file.close()   # WAJIB ditutup setelah selesai

print("File berhasil ditulis.")

# Penjelasan:
# - open("nama_file.txt", "w") -> buka file untuk DITULIS, bikin baru kalau belum ada
# - write() bisa dipanggil berkali-kali, tulisan menumpuk sampai close()
# - \n = pindah baris baru di dalam file
# - close() WAJIB, kalau lupa datanya bisa saja tidak benar-benar tersimpan


# ------------------------------------------------------
# CONTOH 2: MEMBACA SELURUH ISI FILE
# ------------------------------------------------------

file = open("catatan.txt", "r")   # "r" = read, default mode
isi = file.read()
file.close()

print(isi)

# Penjelasan:
# - read() ambil SEMUA isi file jadi satu string panjang
# - Kalau file-nya besar, ini bisa boros memori -> lihat CONTOH 3 buat baca per baris


# ------------------------------------------------------
# CONTOH 3: MEMBACA PER BARIS
# ------------------------------------------------------

file = open("catatan.txt", "r")
for baris in file:              # bisa langsung di-loop, per baris
    print(f"-> {baris.strip()}")   # .strip() buang \n di akhir tiap baris
file.close()

# cara lain: readlines() -> hasilnya LIST of string, satu per baris
file = open("catatan.txt", "r")
semua_baris = file.readlines()
file.close()
print(semua_baris)

# Penjelasan:
# - for baris in file -> cara paling hemat memori, baca satu-satu
# - readlines() -> ambil semua baris sekaligus jadi list, lebih gampang diolah
#   tapi lebih boros memori untuk file besar


# ------------------------------------------------------
# CONTOH 4: MASALAH KALAU LUPA close()
# ------------------------------------------------------

def tulis_data_ceroboh():
    file = open("data_sementara.txt", "w")
    file.write("Data penting")
    # lupa file.close() !
    # kalau program crash SEBELUM baris close() sempat jalan,
    # data bisa TIDAK tersimpan dengan benar, atau file "terkunci"

# Penjelasan:
# - Ini masalah nyata: manual open()...close() gampang lupa, apalagi kalau
#   ada error di tengah jalan (close() jadi tidak pernah kepanggil)
# - Solusinya ada di file berikutnya: with statement, yang otomatis
#   nutup file walau terjadi error


# ------------------------------------------------------
# CATATAN PENTING
# ------------------------------------------------------
# - "w" menulis file BARU (menimpa kalau sudah ada), "r" membaca file
# - SELALU close() setelah selesai -> tapi mulai file berikutnya, pakai
#   with statement supaya tidak perlu ingat manual
# - File yang dibuat (catatan.txt) akan muncul di folder yang sama
#   dengan file .py ini dijalankan