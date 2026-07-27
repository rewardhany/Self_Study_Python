# ======================================================
# 05 ERROR HANDLING UNTUK API
# ======================================================
# API bisa GAGAL karena banyak alasan: internet mati, server down,
# URL salah, data tidak ditemukan, dst. Selalu asumsikan API BISA gagal.
# ======================================================

import requests


# ------------------------------------------------------
# CONTOH 1: CEK status_code MANUAL
# ------------------------------------------------------

response = requests.get("https://jsonplaceholder.typicode.com/posts/9999")   # id tidak ada

if response.status_code == 200:
    print("Berhasil!")
    print(response.json())
elif response.status_code == 404:
    print("Data tidak ditemukan (404)")
else:
    print(f"Terjadi masalah, status code: {response.status_code}")

# Penjelasan status code yang paling sering ditemui:
# - 200 -> OK, berhasil
# - 201 -> Created, berhasil dibuat (dari POST)
# - 400 -> Bad Request, permintaan yang dikirim salah format
# - 401 -> Unauthorized, butuh autentikasi (API key/token)
# - 404 -> Not Found, data/endpoint tidak ditemukan
# - 500 -> Internal Server Error, masalah dari SISI SERVER, bukan kodemu


# ------------------------------------------------------
# CONTOH 2: raise_for_status() - CARA LEBIH SINGKAT
# ------------------------------------------------------

try:
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    response.raise_for_status()   # otomatis raise error kalau status BUKAN 2xx
    print(response.json())
except requests.exceptions.HTTPError as e:
    print(f"Terjadi HTTP error: {e}")

# Penjelasan:
# - raise_for_status() otomatis MEMUNCULKAN error (raise, ingat BAB 6)
#   kalau status_code menunjukkan masalah (400-an atau 500-an)
# - Kalau status_code 200/201 (sukses), tidak terjadi apa-apa, lanjut normal
# - Ini cara yang lebih singkat daripada if/elif manual di CONTOH 1


# ------------------------------------------------------
# CONTOH 3: TIMEOUT - KALAU SERVER TERLALU LAMA MERESPONS
# ------------------------------------------------------

try:
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1", timeout=5)
    print(response.json())
except requests.exceptions.Timeout:
    print("Request terlalu lama, server tidak merespons dalam 5 detik")

# Penjelasan:
# - timeout=5 -> kalau server tidak jawab dalam 5 detik, request DIBATALKAN
# - Tanpa timeout, program bisa "menggantung" tanpa batas kalau server bermasalah
# - SELALU tambahkan timeout di kode yang akan dipakai sungguhan (bukan cuma latihan)


# ------------------------------------------------------
# CONTOH 4: CONNECTION ERROR - INTERNET BERMASALAH
# ------------------------------------------------------

try:
    response = requests.get("https://url-yang-tidak-akan-pernah-ada-xyz123.com", timeout=5)
except requests.exceptions.ConnectionError:
    print("Tidak bisa terhubung - cek koneksi internet atau URL-nya")
except requests.exceptions.Timeout:
    print("Request terlalu lama")
except requests.exceptions.RequestException as e:
    print(f"Terjadi error lain: {e}")

# Penjelasan:
# - ConnectionError -> URL salah, domain tidak ada, atau internet mati
# - RequestException = "induk" dari SEMUA error yang berhubungan dengan
#   requests, dipakai sebagai fallback paling akhir (sama seperti Exception di BAB 6)
# - Urutan except: dari yang PALING SPESIFIK ke yang PALING UMUM


# ------------------------------------------------------
# CATATAN PENTING
# ------------------------------------------------------
# - SELALU pakai timeout= di setiap requests.get()/post() untuk kode yang
#   benar-benar dipakai (bukan cuma latihan sekali jalan)
# - raise_for_status() + try/except adalah kombinasi paling praktis untuk
#   handle error API dengan rapi
# - Anggap SEMUA pemanggilan API sebagai sesuatu yang BISA GAGAL -
#   inilah kenapa BAB 6 (Error Handling) jadi prasyarat penting BAB 9