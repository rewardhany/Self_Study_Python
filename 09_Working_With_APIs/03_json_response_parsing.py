# ======================================================
# 03 JSON RESPONSE PARSING
# ======================================================
# PARSING adalah:
# Proses "membongkar" data JSON yang kompleks untuk ambil bagian
# yang kamu butuhkan
#
# Kebanyakan response API TIDAK sesederhana CONTOH di file sebelumnya -
# biasanya nested (dict di dalam dict, list di dalam dict)
# ======================================================

import requests


# ------------------------------------------------------
# CONTOH 1: AKSES FIELD SEDERHANA
# ------------------------------------------------------

response = requests.get("https://jsonplaceholder.typicode.com/users/1")
data = response.json()

print(data["name"])
print(data["email"])

# Penjelasan:
# - Akses field langsung pakai [] sama seperti dict biasa, ingat BAB 3


# ------------------------------------------------------
# CONTOH 2: RESPONSE BERUPA LIST OF DICT
# ------------------------------------------------------

response = requests.get("https://jsonplaceholder.typicode.com/users")
data = response.json()   # ini LIST, bukan dict tunggal

print(type(data))
print(f"Jumlah user: {len(data)}")

for user in data[:3]:   # ambil 3 user pertama saja
    print(f"{user['name']} - {user['email']}")

# Penjelasan:
# - Beberapa endpoint API balikin LIST of dict, bukan 1 dict tunggal
# - Cek type(data) dulu kalau bingung -> menentukan cara akses selanjutnya
# - data[:3] pakai slicing (BAB 3) buat ambil sebagian saja


# ------------------------------------------------------
# CONTOH 3: NESTED JSON - DATA DI DALAM DATA
# ------------------------------------------------------

response = requests.get("https://jsonplaceholder.typicode.com/users/1")
data = response.json()

print(data["address"]["city"])            # dict di dalam dict
print(data["address"]["geo"]["lat"])       # dict di dalam dict di dalam dict
print(data["company"]["name"])

# Penjelasan:
# - Semakin dalam nested-nya, semakin banyak "rantai" [] yang ditulis
# - Ini persis pola nested dictionary di BAB 3 file 03, cuma sekarang
#   datanya dari internet, bukan kamu buat manual


# ------------------------------------------------------
# CONTOH 4: PARSING DENGAN try/except UNTUK FIELD YANG MUNGKIN TIDAK ADA
# ------------------------------------------------------

def ambil_kota(data_user):
    try:
        return data_user["address"]["city"]
    except KeyError:
        return "Kota tidak tersedia"

response = requests.get("https://jsonplaceholder.typicode.com/users/1")
data = response.json()

print(ambil_kota(data))

data_rusak = {"name": "Test"}   # simulasi data tanpa field address
print(ambil_kota(data_rusak))

# Penjelasan:
# - Response API tidak selalu punya SEMUA field yang kamu harapkan
# - KeyError terjadi kalau field-nya tidak ada -> tangkap dengan try/except (BAB 6)
# - Ini kebiasaan PENTING: jangan asumsikan field API selalu lengkap


# ------------------------------------------------------
# CATATAN PENTING
# ------------------------------------------------------
# - Selalu print(type(data)) dulu kalau bingung struktur response-nya
# - Nested JSON diakses dengan merantai [] satu per satu
# - Selalu siapkan try/except untuk field yang mungkin tidak ada -
#   API dunia nyata sering tidak konsisten formatnya