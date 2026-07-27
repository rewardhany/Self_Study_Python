# ======================================================
# PRACTICE API 01
# ======================================================
# Materi yang diuji: 01-05 (GET, POST, parsing, headers/params, error handling)
# Semua soal pakai https://jsonplaceholder.typicode.com (API latihan, gratis)
# ======================================================


# ------------------------------------------------------
# SOAL 1: GET SEDERHANA
# ------------------------------------------------------
# Ambil data dari https://jsonplaceholder.typicode.com/todos/1
# Print title dan apakah sudah "completed" atau belum

# TODO: tulis kode di sini


# ------------------------------------------------------
# SOAL 2: GET DENGAN PARAMS
# ------------------------------------------------------
# Ambil SEMUA todos milik userId=1 dari endpoint /todos
# (pakai params, bukan looping manual)
# Print berapa banyak yang statusnya completed=True

# TODO: tulis kode di sini


# ------------------------------------------------------
# SOAL 3: POST SEDERHANA
# ------------------------------------------------------
# Kirim data baru ke endpoint /todos berupa:
# {"title": "Belajar API", "completed": False, "userId": 1}
# Print status_code dan id yang dikasih server sebagai konfirmasi

# TODO: tulis kode di sini


# ------------------------------------------------------
# SOAL 4: ERROR HANDLING
# ------------------------------------------------------
# Buat fungsi ambil_todo(id_todo) yang:
# - GET ke /todos/{id_todo}
# - kalau id_todo tidak ditemukan (404), return None dan print pesan yang jelas
# - kalau berhasil, return dict data-nya
# - WAJIB pakai timeout dan try/except (bukan cuma cek if status_code == 200)
#
# Test dengan id yang ADA (misal 1) dan id yang TIDAK ADA (misal 99999)

# TODO: tulis kode di sini


# ------------------------------------------------------
# KALAU SUDAH SELESAI
# ------------------------------------------------------
# Cek ke file 01-05. Soal 4 harus benar-benar tahan banting - coba
# putuskan internet sebentar dan jalankan lagi, programnya harus tetap
# tidak crash (harusnya masuk ke except ConnectionError/Timeout).