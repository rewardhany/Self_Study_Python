# ======================================================
# 04 JSON BASIC
# ======================================================
# JSON (JavaScript Object Notation) adalah:
# Format data yang strukturnya MIRIP BANGET sama dictionary Python
#
# Kenapa penting:
# - Format standar untuk nyimpen data yang punya struktur (bukan cuma teks polos)
# - Format yang dipakai HAMPIR SEMUA API di internet (nyambung ke BAB 9)
# - Firebase/Firestore yang kamu pakai di HelpBlue juga berbasis JSON
#
# STRUKTUR DASAR:
# import json
# json.dump(data, file)     -> simpan dict ke file JSON
# json.load(file)           -> baca file JSON jadi dict
# ======================================================

import json


# ------------------------------------------------------
# CONTOH 1: DICT KE JSON STRING (TANPA FILE DULU)
# ------------------------------------------------------

profil = {
    "nama": "Reffa",
    "divisi": "Keamanan",
    "umur": 20,
    "aktif": True
}

json_string = json.dumps(profil)   # dict -> string berformat JSON
print(json_string)
print(type(json_string))

json_string_rapi = json.dumps(profil, indent=4)   # dengan indentasi biar gampang dibaca
print(json_string_rapi)

# Penjelasan:
# - json.dumps() (dengan "s" = string) ubah dict jadi STRING format JSON
# - indent=4 bikin hasilnya rapi dengan indentasi, enak dibaca manusia
# - Perhatikan: True di Python jadi true di JSON (huruf kecil semua)


# ------------------------------------------------------
# CONTOH 2: MENYIMPAN DICT LANGSUNG KE FILE JSON
# ------------------------------------------------------

data_panitia = {
    "nama": "Reffa",
    "divisi": "Keamanan",
    "tugas": ["Notulensi", "Tata Tertib", "PPT Progress"]
}

with open("panitia.json", "w") as file:
    json.dump(data_panitia, file, indent=4)   # dump() (tanpa "s") -> langsung ke file

print("Data berhasil disimpan ke panitia.json")

# Penjelasan:
# - json.dump(data, file) -> simpan LANGSUNG ke file, tidak perlu file.write() manual
# - Perhatikan bedanya sama CONTOH 1: dumps() -> string, dump() -> file


# ------------------------------------------------------
# CONTOH 3: MEMBACA FILE JSON KEMBALI JADI DICT
# ------------------------------------------------------

with open("panitia.json", "r") as file:
    data_dibaca = json.load(file)   # load() -> baca file JSON jadi dict Python

print(data_dibaca)
print(data_dibaca["nama"])
print(data_dibaca["tugas"][0])

# Penjelasan:
# - json.load(file) mengembalikan dict PYTHON BIASA, bisa diakses seperti dict biasa
# - Inilah yang bikin JSON penting: data yang tersimpan tetap terstruktur
#   (list, dict, nested) begitu dibaca lagi, tidak jadi teks berantakan


# ------------------------------------------------------
# CONTOH 4: json.loads() - DARI STRING JSON (BUKAN FILE)
# ------------------------------------------------------

respon_dari_luar = '{"status": "sukses", "kode": 200, "pesan": "Data diterima"}'

data = json.loads(respon_dari_luar)   # loads() (dengan "s") -> dari STRING, bukan file
print(data["status"])
print(data["kode"])

# Penjelasan:
# - json.loads() dipakai kalau data JSON-nya berupa STRING (bukan file)
# - Ini persis situasi yang akan kamu temui di BAB 9 (Working With APIs):
#   response dari API biasanya string JSON, perlu di-loads() dulu jadi dict


# ------------------------------------------------------
# CATATAN PENTING
# ------------------------------------------------------
# - dump/dumps = MENULIS (dict -> JSON), load/loads = MEMBACA (JSON -> dict)
# - yang ada huruf "s" (dumps/loads) = urusannya STRING
# - yang tanpa "s" (dump/load) = urusannya FILE
# - JSON tidak bisa nyimpen semua tipe data Python (misal: tuple otomatis
#   jadi list, custom object butuh diubah dulu jadi dict)