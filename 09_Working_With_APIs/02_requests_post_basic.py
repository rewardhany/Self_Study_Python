# ======================================================
# 02 REQUESTS - POST BASIC
# ======================================================
# POST REQUEST adalah:
# Cara MENGIRIM data BARU ke server (beda dengan GET yang cuma ambil data)
#
# STRUKTUR DASAR:
# response = requests.post("url", json=data_yang_dikirim)
# ======================================================

import requests


# ------------------------------------------------------
# CONTOH 1: POST REQUEST SEDERHANA
# ------------------------------------------------------

data_baru = {
    "title": "Laporan ODWH 2026",
    "body": "Divisi Keamanan sudah menyelesaikan tata tertib",
    "userId": 1
}

response = requests.post("https://jsonplaceholder.typicode.com/posts", json=data_baru)

print(response.status_code)   # 201 = berhasil DIBUAT (bukan 200)
print(response.json())

# Penjelasan:
# - json=data_baru -> otomatis convert dict jadi JSON dan kirim ke server
# - Server (versi latihan ini) akan "pura-pura" nyimpen dan mengembalikan
#   data yang sama plus id baru
# - status_code 201 = "Created", beda dari GET yang biasanya 200


# ------------------------------------------------------
# CONTOH 2: MEMERIKSA HASIL SETELAH POST
# ------------------------------------------------------

response = requests.post("https://jsonplaceholder.typicode.com/posts", json=data_baru)
hasil = response.json()

print(f"Data tersimpan dengan ID: {hasil['id']}")
print(f"Judul: {hasil['title']}")

# Penjelasan:
# - Response dari POST biasanya berisi data yang BARU DIBUAT, termasuk
#   id baru yang dikasih server
# - Ini pola umum: kirim data -> server balikin konfirmasi + id-nya


# ------------------------------------------------------
# CONTOH 3: POST DENGAN DATA NESTED (LEBIH KOMPLEKS)
# ------------------------------------------------------

data_peserta = {
    "nama": "Reffa",
    "kontak": {
        "email": "reffa@example.com",
        "whatsapp": "08123456789"
    },
    "divisi": ["Keamanan"]
}

response = requests.post("https://jsonplaceholder.typicode.com/posts", json=data_peserta)
print(response.status_code)

# Penjelasan:
# - json= bisa terima dict yang isinya nested (dict di dalam dict, list
#   di dalam dict) - persis pola BAB 3 (nested dictionary)
# - requests otomatis handle convert struktur kompleks ini jadi JSON valid


# ------------------------------------------------------
# CONTOH 4: GET VS POST - KAPAN PAKAI YANG MANA
# ------------------------------------------------------

# GET: MENGAMBIL data yang sudah ada
response_get = requests.get("https://jsonplaceholder.typicode.com/posts/1")

# POST: MENGIRIM data baru untuk DIBUAT di server
response_post = requests.post("https://jsonplaceholder.typicode.com/posts", json={"title": "Baru"})

print(f"GET status : {response_get.status_code}")   # 200
print(f"POST status: {response_post.status_code}")  # 201

# Penjelasan:
# - GET = "tolong kasih saya data" -> tidak mengubah apapun di server
# - POST = "tolong simpan data baru ini" -> menciptakan data baru
# - Nanti di BAB 13 (REST API) akan ketemu juga PUT (update) dan DELETE (hapus)


# ------------------------------------------------------
# CATATAN PENTING
# ------------------------------------------------------
# - json=dict_python -> cara paling gampang kirim data lewat POST
# - status_code 201 = berhasil dibuat, beda dari GET yang biasanya 200
# - jsonplaceholder ini API latihan -> data yang dikirim TIDAK BENERAN
#   tersimpan permanen, cuma buat latihan syntax dengan aman