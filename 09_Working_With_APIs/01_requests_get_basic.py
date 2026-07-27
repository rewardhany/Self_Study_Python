# ======================================================
# 01 REQUESTS - GET BASIC
# ======================================================
# CATATAN: perlu install dulu (lihat BAB 8 file 04):
#   pip install requests
#
# GET REQUEST adalah:
# Cara MENGAMBIL data dari server/API lewat internet
#
# STRUKTUR DASAR:
# import requests
# response = requests.get("url")
# ======================================================

import requests


# ------------------------------------------------------
# CONTOH 1: GET REQUEST SEDERHANA
# ------------------------------------------------------

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

print(response)             # objek Response, bukan data mentah
print(response.status_code)  # 200 = sukses

# Penjelasan:
# - requests.get(url) mengirim permintaan ke server, hasilnya objek Response
# - status_code = 200 artinya berhasil (kode status ini dibahas detail
#   di 05_error_handling_api.py)


# ------------------------------------------------------
# CONTOH 2: MELIHAT ISI RESPONSE
# ------------------------------------------------------

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

print(response.text)   # isi response sebagai STRING mentah
print(response.json())  # isi response sudah diubah jadi DICT Python

# Penjelasan:
# - .text -> hasilnya string mentah (mirip json.loads() dari BAB 7 file 04)
# - .json() -> otomatis convert JSON string jadi dict Python, LEBIH sering dipakai
# - .json() sebenarnya = json.loads(response.text), cuma dipersingkat


# ------------------------------------------------------
# CONTOH 3: MENGAKSES FIELD TERTENTU DARI RESPONSE
# ------------------------------------------------------

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
data = response.json()

print(data["title"])
print(data["userId"])

# Penjelasan:
# - Begitu jadi dict (lewat .json()), aksesnya SAMA PERSIS seperti dict biasa
# - Ini kenapa BAB 3 (dictionary) dan BAB 7 (JSON) penting banget sebelum BAB 9


# ------------------------------------------------------
# CONTOH 4: GET BEBERAPA DATA SEKALIGUS (LOOP)
# ------------------------------------------------------

for id_post in range(1, 4):
    response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{id_post}")
    data = response.json()
    print(f"Post {id_post}: {data['title']}")

# Penjelasan:
# - URL bisa dibikin dinamis pakai f-string, sama seperti string biasa
# - Loop di atas manggil API 3 kali, satu-satu, ambil data yang beda tiap kali
# - Ini pola umum kalau butuh banyak data dari API yang sama


# ------------------------------------------------------
# CATATAN PENTING
# ------------------------------------------------------
# - GET dipakai untuk MENGAMBIL data, bukan mengirim data baru (itu POST,
#   file berikutnya)
# - .json() jauh lebih sering dipakai daripada .text untuk API modern
# - jsonplaceholder.typicode.com adalah API publik gratis khusus buat latihan,
#   datanya palsu tapi formatnya sama seperti API sungguhan