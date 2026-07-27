# ======================================================
# 05 CSV BASIC
# ======================================================
# CSV (Comma-Separated Values) adalah:
# Format data berbentuk TABEL (baris & kolom), dipisah pakai koma
# Bisa dibuka juga di Excel/Google Sheets
#
# STRUKTUR DASAR:
# import csv
# csv.writer(file)   -> menulis data berbentuk baris/kolom
# csv.reader(file)   -> membaca data CSV per baris
# ======================================================

import csv


# ------------------------------------------------------
# CONTOH 1: MENULIS CSV SEDERHANA
# ------------------------------------------------------

data_inventaris = [
    ["Nama Barang", "Sumber", "Jumlah"],   # baris header
    ["Proyektor", "Lembaga", 2],
    ["Banner", "Hima", 4],
    ["Laptop", "Panitia", 3]
]

with open("inventaris.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data_inventaris)   # tulis semua baris sekaligus

print("Data berhasil ditulis ke inventaris.csv")

# Penjelasan:
# - newline="" WAJIB ditulis di open() untuk CSV, supaya tidak ada baris kosong ganda
# - csv.writer(file) bikin "penulis" yang paham format CSV
# - writerows() -> tulis BANYAK baris sekaligus (list of list)
# - writerow() (tanpa "s") -> tulis SATU baris saja


# ------------------------------------------------------
# CONTOH 2: MEMBACA CSV
# ------------------------------------------------------

with open("inventaris.csv", "r") as file:
    reader = csv.reader(file)
    for baris in reader:
        print(baris)

# Penjelasan:
# - csv.reader(file) bisa langsung di-loop, tiap baris jadi LIST of string
# - Perhatikan: angka (Jumlah) ikut jadi STRING "2", bukan integer 2 -> perlu
#   di-convert manual pakai int() kalau mau dihitung


# ------------------------------------------------------
# CONTOH 3: DictWriter - MENULIS DARI LIST OF DICT
# ------------------------------------------------------

data_panitia = [
    {"nama": "Reffa", "divisi": "Keamanan"},
    {"nama": "Galan", "divisi": "Logistik"},
    {"nama": "Bintang", "divisi": "Acara"}
]

with open("panitia.csv", "w", newline="") as file:
    kolom = ["nama", "divisi"]   # nama kolom HARUS sesuai key di dictionary
    writer = csv.DictWriter(file, fieldnames=kolom)
    writer.writeheader()          # tulis baris header otomatis dari fieldnames
    writer.writerows(data_panitia)

print("Data panitia berhasil ditulis ke panitia.csv")

# Penjelasan:
# - DictWriter cocok kalau data-mu SUDAH berbentuk list of dict (pola BAB 3!)
# - fieldnames = urutan & nama kolom yang mau ditulis
# - writeheader() nulis baris judul kolom, writerows() nulis isinya


# ------------------------------------------------------
# CONTOH 4: DictReader - MEMBACA LANGSUNG JADI DICT
# ------------------------------------------------------

with open("panitia.csv", "r") as file:
    reader = csv.DictReader(file)
    for baris in reader:
        print(f"{baris['nama']} - {baris['divisi']}")

# Penjelasan:
# - DictReader baca CSV dan langsung ubah tiap baris jadi DICTIONARY
# - Aksesnya pakai nama kolom (baris['nama']), bukan index angka (baris[0])
# - Jauh lebih enak dibaca dibanding csv.reader biasa


# ------------------------------------------------------
# CATATAN PENTING
# ------------------------------------------------------
# - newline="" WAJIB ada di open() saat menulis CSV, supaya formatnya benar
# - csv.reader/writer -> hasilnya list biasa (index angka)
# - csv.DictReader/DictWriter -> hasilnya dictionary (key nama kolom), lebih rapi
# - Semua data yang dibaca dari CSV berbentuk STRING, convert manual kalau
#   butuh angka (int()/float())