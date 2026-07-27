# ======================================================
# 06 PATH HANDLING (os.path & pathlib)
# ======================================================
# PATH HANDLING adalah:
# Cara menangani lokasi/alamat file & folder dengan BENAR,
# supaya kodenya tetap jalan di Windows, Mac, ATAU Linux
#
# Kenapa penting: Windows pakai "\", Mac/Linux pakai "/" untuk pemisah
# folder -- kalau ditulis manual, kode bisa error di OS yang beda
# ======================================================

import os
from pathlib import Path


# ------------------------------------------------------
# CONTOH 1: os.path.join() - GABUNG PATH LINTAS OS
# ------------------------------------------------------

# Cara SALAH (hardcode pemisah folder):
path_salah = "data" + "/" + "panitia.json"   # cuma benar di Mac/Linux

# Cara BENAR:
path_benar = os.path.join("data", "panitia.json")
print(path_benar)

# Penjelasan:
# - os.path.join() otomatis pakai pemisah folder yang SESUAI dengan OS
#   yang menjalankan kode ini (Windows pakai \, Mac/Linux pakai /)
# - Selalu pakai ini daripada nulis manual "folder/file.txt"


# ------------------------------------------------------
# CONTOH 2: os.path.exists() - CEK FILE/FOLDER ADA ATAU TIDAK
# ------------------------------------------------------

if os.path.exists("catatan.txt"):
    print("File catatan.txt ditemukan")
else:
    print("File catatan.txt tidak ada")

if os.path.exists("folder_belum_ada"):
    print("Folder ada")
else:
    print("Folder belum ada, perlu dibuat dulu")

# Penjelasan:
# - os.path.exists() cek APAKAH path itu ada, entah file atau folder
# - Berguna banget SEBELUM baca file (hindari FileNotFoundError) atau
#   sebelum bikin folder baru (hindari error "folder sudah ada")


# ------------------------------------------------------
# CONTOH 3: os.makedirs() - BIKIN FOLDER OTOMATIS
# ------------------------------------------------------

folder_output = "data_odwh"

if not os.path.exists(folder_output):
    os.makedirs(folder_output)
    print(f"Folder '{folder_output}' berhasil dibuat")
else:
    print(f"Folder '{folder_output}' sudah ada")

path_file = os.path.join(folder_output, "rekap.txt")
with open(path_file, "w") as file:
    file.write("Rekap kegiatan ODWH 2026")

# Penjelasan:
# - os.makedirs() bikin folder baru (bisa sekaligus beberapa level: "a/b/c")
# - Selalu cek exists() dulu sebelum makedirs(), supaya tidak error kalau
#   folder-nya sudah pernah dibuat sebelumnya


# ------------------------------------------------------
# CONTOH 4: pathlib.Path - CARA MODERN (ALTERNATIF os.path)
# ------------------------------------------------------

folder = Path("data_odwh")
file_path = folder / "rekap.txt"   # operator / dipakai buat gabung path!

print(file_path)
print(file_path.exists())
print(file_path.name)      # nama file-nya saja: rekap.txt
print(file_path.suffix)    # ekstensinya saja: .txt

# Penjelasan:
# - pathlib.Path adalah cara yang lebih modern dan lebih "Python-ic"
# - Operator / dipakai buat gabung path, MENGGANTIKAN os.path.join()
# - Punya banyak method siap pakai (.exists(), .name, .suffix, dll)
# - os.path masih sangat umum dipakai di kode lama, tapi Path lebih
#   disarankan untuk project baru


# ------------------------------------------------------
# CATATAN PENTING
# ------------------------------------------------------
# - JANGAN PERNAH hardcode "/" atau "\" manual di path -> pakai
#   os.path.join() atau pathlib.Path
# - Cek exists() dulu sebelum baca file atau bikin folder baru
# - os.path = cara klasik (masih banyak dipakai), pathlib.Path = cara modern
#   -> pilih salah satu, konsisten dalam 1 project