# ======================================================
# 06 LATIHAN DENGAN PUBLIC API NYATA (GITHUB)
# ======================================================
# Ini contoh LENGKAP menggabungkan semua materi BAB 9, pakai API
# GitHub yang BENERAN (bukan API latihan seperti file sebelumnya)
# dan tidak butuh API key untuk fitur dasar.
#
# Sekaligus nyambung ke Programmer Essentials yang sudah dibahas -
# kamu bisa cek profil GitHub siapa saja lewat API ini.
# ======================================================

import requests


# ------------------------------------------------------
# CONTOH 1: AMBIL DATA PROFIL GITHUB
# ------------------------------------------------------

def cek_profil_github(username):
    url = f"https://api.github.com/users/{username}"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
    except requests.exceptions.HTTPError:
        print(f"User '{username}' tidak ditemukan di GitHub")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Terjadi masalah koneksi: {e}")
        return None

    return response.json()

data = cek_profil_github("torvalds")   # pembuat Linux & Git, contoh acak
if data:
    print(f"Nama       : {data.get('name', 'Tidak diisi')}")
    print(f"Bio        : {data.get('bio', 'Tidak ada bio')}")
    print(f"Repo publik: {data['public_repos']}")
    print(f"Followers  : {data['followers']}")

# Penjelasan:
# - Menggabungkan: GET request, timeout, raise_for_status, try/except
#   BEBERAPA jenis error, dan parsing JSON dengan .get() untuk field
#   yang mungkin kosong (name/bio bisa saja null di GitHub)


# ------------------------------------------------------
# CONTOH 2: MENGAMBIL LIST REPOSITORY PUBLIK
# ------------------------------------------------------

def daftar_repo_github(username, jumlah=5):
    url = f"https://api.github.com/users/{username}/repos"
    params = {"sort": "updated", "per_page": jumlah}   # params dari file 04

    try:
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Gagal mengambil data repo: {e}")
        return []

    return response.json()

repos = daftar_repo_github("torvalds", jumlah=3)
for repo in repos:
    print(f"- {repo['name']} ({repo['stargazers_count']} stars)")

# Penjelasan:
# - params={"sort": "updated", "per_page": jumlah} -> filter langsung dari API,
#   tidak perlu ambil semua data lalu difilter manual pakai Python
# - Ini pola nyata yang sering dipakai: API sudah sediakan cara filter,
#   manfaatkan itu daripada olah data mentah sendiri


# ------------------------------------------------------
# CONTOH 3: GABUNGKAN JADI 1 LAPORAN
# ------------------------------------------------------

def laporan_github(username):
    profil = cek_profil_github(username)
    if not profil:
        return

    print(f"\n=== LAPORAN GITHUB: {username} ===")
    print(f"Nama  : {profil.get('name', '-')}")
    print(f"Repo  : {profil['public_repos']} repository publik")

    repos = daftar_repo_github(username, jumlah=3)
    print("Repo terbaru:")
    for repo in repos:
        print(f"  - {repo['name']}")

laporan_github("torvalds")

# Penjelasan:
# - Fungsi laporan_github() MEMANGGIL fungsi lain (CONTOH 1 & 2) yang sudah dibuat
# - Ini pola "compose" fungsi kecil jadi laporan besar, sama seperti
#   project-project gabungan BAB sebelumnya


# ------------------------------------------------------
# CATATAN PENTING
# ------------------------------------------------------
# - API GitHub publik ini TIDAK butuh API key untuk fitur dasar (baca profil,
#   baca repo) -> tapi PUNYA rate limit (batas jumlah request per jam) untuk
#   yang tanpa key, jangan spam terlalu banyak request sekaligus
# - .get('field', default) dipakai kalau field-nya BISA jadi kosong/null,
#   beda dari data['field'] yang akan error kalau field-nya tidak ada sama sekali