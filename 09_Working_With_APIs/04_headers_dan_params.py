# ======================================================
# 04 HEADERS & PARAMS
# ======================================================
# PARAMS adalah:
# Data tambahan yang dikirim LEWAT URL (setelah tanda ?)
#
# HEADERS adalah:
# Data tambahan yang dikirim TERPISAH dari URL, biasanya untuk
# identitas/autentikasi (misal: API key, token)
# ======================================================

import requests


# ------------------------------------------------------
# CONTOH 1: QUERY PARAMS LEWAT params=
# ------------------------------------------------------

response = requests.get(
    "https://jsonplaceholder.typicode.com/posts",
    params={"userId": 1}
)

print(response.url)     # lihat URL asli yang terbentuk
data = response.json()
print(f"Jumlah post userId=1: {len(data)}")

# Penjelasan:
# - params={"userId": 1} otomatis diubah jadi ?userId=1 di URL
# - Cara ini LEBIH AMAN & RAPI daripada nulis manual:
#   requests.get("https://.../posts?userId=1")
# - print(response.url) berguna buat cek URL final yang sebenarnya dikirim


# ------------------------------------------------------
# CONTOH 2: PARAMS DENGAN BEBERAPA FILTER SEKALIGUS
# ------------------------------------------------------

response = requests.get(
    "https://jsonplaceholder.typicode.com/comments",
    params={"postId": 1, "_limit": 3}   # ambil 3 komentar dari postId=1
)

data = response.json()
for komentar in data:
    print(f"{komentar['name']}: {komentar['email']}")

# Penjelasan:
# - params bisa punya lebih dari 1 key, semua digabung otomatis ke URL
# - _limit adalah contoh param umum di banyak API untuk BATASI jumlah hasil


# ------------------------------------------------------
# CONTOH 3: HEADERS CUSTOM (SIMULASI, TANPA API KEY BENERAN)
# ------------------------------------------------------

headers_custom = {
    "User-Agent": "BelajarPython/1.0",
    "Accept": "application/json"
}

response = requests.get(
    "https://jsonplaceholder.typicode.com/posts/1",
    headers=headers_custom
)

print(response.status_code)
print(response.request.headers)   # lihat headers yang benar-benar terkirim

# Penjelasan:
# - headers=dict dikirim TERPISAH dari URL, tidak kelihatan di response.url
# - User-Agent = identitas aplikasi yang mengirim request
# - Banyak API BUTUH header khusus (misal Authorization) supaya mau merespons


# ------------------------------------------------------
# CONTOH 4: KOMBINASI HEADERS + PARAMS + CATATAN TENTANG API KEY
# ------------------------------------------------------

# Simulasi API yang butuh API key (bukan API asli, cuma contoh pola):
API_KEY = "contoh_api_key_12345"   # <- JANGAN PERNAH hardcode API key asli seperti ini!

headers_dengan_auth = {
    "Authorization": f"Bearer {API_KEY}"
}

params_pencarian = {
    "query": "python programming",
    "limit": 5
}

# response = requests.get("https://contoh-api.com/search", headers=headers_dengan_auth, params=params_pencarian)
# (baris di atas sengaja dikomentari, karena contoh-api.com bukan API asli)

print("Contoh struktur request dengan headers + params sekaligus")

# Penjelasan:
# - Authorization: Bearer {token} adalah pola PALING UMUM untuk API yang butuh login
# - PENTING: API key/token TIDAK BOLEH ditulis langsung di kode (hardcode) -
#   kalau ter-push ke GitHub, siapa saja bisa lihat dan pakai API key-mu
# - Cara amannya: simpan di file .env terpisah, baru dipakai lewat environment
#   variable (dibahas lebih lanjut di BAB 15 - Deployment_Basics)


# ------------------------------------------------------
# CATATAN PENTING
# ------------------------------------------------------
# - params -> data yang nempel di URL (biasanya buat filter/limit hasil)
# - headers -> data terpisah dari URL (biasanya buat identitas/autentikasi)
# - JANGAN PERNAH hardcode API key langsung di kode, apalagi kalau
#   project-nya akan di-push ke GitHub