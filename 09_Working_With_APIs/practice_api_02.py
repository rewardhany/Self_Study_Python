# ======================================================
# PRACTICE API 02 (PROJECT CHALLENGE)
# ======================================================
# Gabungan SEMUA materi BAB 9, pakai API musik NYATA: iTunes Search API
# (gratis, TANPA perlu API key/token) - cocok sama minat kamu di musik.
#
# Endpoint dasarnya: https://itunes.apple.com/search?term=NAMA_LAGU&limit=5
#
# Kerjakan bertahap sesuai TODO.
# ======================================================

# ------------------------------------------------------
# KONTEKS PROJECT
# ------------------------------------------------------
# Bikin "MUSIC SEARCH TOOL" sederhana: user ketik nama lagu/artis,
# program cari lewat iTunes API dan tampilkan hasilnya rapi.


# ------------------------------------------------------
# TODO 1: FUNGSI PENCARIAN DASAR
# ------------------------------------------------------
# Buat fungsi cari_lagu(kata_kunci, jumlah=5) yang:
# - GET ke "https://itunes.apple.com/search"
# - pakai params: {"term": kata_kunci, "limit": jumlah, "media": "music"}
# - pakai timeout dan try/except (ConnectionError, Timeout, RequestException)
# - return list hasil pencarian (field "results" dari response JSON),
#   atau list kosong [] kalau terjadi error


# ------------------------------------------------------
# TODO 2: PARSING HASIL PENCARIAN
# ------------------------------------------------------
# Buat fungsi tampilkan_hasil(daftar_lagu) yang loop hasil dari TODO 1,
# dan print untuk tiap lagu:
# "{trackName} - {artistName} ({collectionName})"
#
# Gunakan .get() untuk field yang mungkin tidak selalu ada
# (misal collectionName kadang kosong untuk single)


# ------------------------------------------------------
# TODO 3: FILTER HASIL BERDASARKAN DURASI
# ------------------------------------------------------
# iTunes API ngasih field "trackTimeMillis" (durasi dalam milidetik).
# Buat fungsi filter_durasi_pendek(daftar_lagu, maks_menit=4) yang
# cuma return lagu dengan durasi KURANG DARI maks_menit menit
# (ingat: 1 menit = 60000 milidetik)
#
# Petunjuk: pakai list comprehension (BAB 3) + .get() buat handle field
# yang mungkin tidak ada


# ------------------------------------------------------
# TODO 4: PROGRAM UTAMA (GABUNGKAN SEMUA)
# ------------------------------------------------------
# Buat loop utama program:
# - minta user input kata kunci pencarian (atau ketik "keluar" untuk berhenti)
# - panggil cari_lagu()
# - kalau hasil kosong, print "Tidak ditemukan"
# - kalau ada hasil, tanya user: mau lihat SEMUA hasil, atau HANYA yang
#   durasinya pendek (pakai filter_durasi_pendek dari TODO 3)
# - tampilkan_hasil() sesuai pilihan user


# ------------------------------------------------------
# BONUS (OPSIONAL)
# ------------------------------------------------------
# Simpan hasil pencarian terakhir ke file JSON (ingat BAB 7), supaya
# bisa dibuka lagi tanpa perlu request ulang ke API


# ------------------------------------------------------
# KALAU STUCK
# ------------------------------------------------------
# Coba dulu TODO 1 SENDIRIAN, print(response.json()) mentahnya dulu
# buat lihat struktur data aslinya sebelum lanjut ke TODO 2 - jangan
# nebak-nebak nama field-nya.