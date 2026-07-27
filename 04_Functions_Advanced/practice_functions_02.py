# ======================================================
# PRACTICE FUNCTIONS 02
# ======================================================
# Materi yang diuji: 03_args_dan_kwargs, 04_lambda_function,
#                     05_scope_dan_global, 06_recursion
#
# CARA PAKAI: sama seperti practice_functions_01.py -
# coba dulu dari ingatan, cocokkan belakangan.
# ======================================================


# ------------------------------------------------------
# SOAL 1: *args
# ------------------------------------------------------
# Buat fungsi bernama total_belanja(*harga) yang menerima SEBERAPA PUN
# jumlah argumen harga, lalu return jumlah totalnya.
#
# Test: total_belanja(15000, 20000, 8000) -> harus hasilnya 43000
# Test: total_belanja(5000) -> harus hasilnya 5000

# TODO: tulis fungsimu di sini


# ------------------------------------------------------
# SOAL 2: **kwargs
# ------------------------------------------------------
# Buat fungsi bernama cetak_profil(**data) yang menerima jumlah keyword
# argument BEBAS, lalu print setiap key & value-nya dalam format:
# "nama: Reffa"
# "divisi: Keamanan"
#
# Test: cetak_profil(nama="Reffa", divisi="Keamanan", umur=20)

# TODO: tulis fungsimu di sini


# ------------------------------------------------------
# SOAL 3: LAMBDA + sorted()
# ------------------------------------------------------
# Diberikan list berikut:
panitia = [
    {"nama": "Reffa", "divisi": "Keamanan"},
    {"nama": "Galan", "divisi": "Logistik"},
    {"nama": "Alya", "divisi": "Acara"}
]
# Urutkan list ini berdasarkan "nama" secara alfabetis, pakai sorted() + lambda.
# JANGAN pakai fungsi def biasa untuk soal ini, harus pakai lambda.

# TODO: tulis kode urutannya di sini, lalu print hasilnya


# ------------------------------------------------------
# SOAL 4: SCOPE & GLOBAL
# ------------------------------------------------------
# Diberikan variabel global berikut:
saldo = 100000
# Buat fungsi bernama tarik_saldo(jumlah) yang MENGURANGI variabel
# global saldo di atas (bukan bikin variabel local baru).
# Panggil fungsinya 2 kali dengan jumlah berbeda, lalu print saldo akhir.

# TODO: tulis fungsimu di sini


# ------------------------------------------------------
# SOAL 5: RECURSION
# ------------------------------------------------------
# Buat fungsi rekursif bernama hitung_pangkat(basis, eksponen) yang
# menghitung basis pangkat eksponen TANPA memakai operator ** atau pow().
# Contoh: hitung_pangkat(2, 4) -> harus hasilnya 16 (2*2*2*2)
#
# Petunjuk: base case-nya adalah saat eksponen == 0 (hasilnya 1)

# TODO: tulis fungsimu di sini


# ------------------------------------------------------
# KALAU SUDAH SELESAI SEMUA
# ------------------------------------------------------
# Cocokkan ke file materi terkait. Kalau soal 5 masih bingung,
# coba trace manual di kertas dulu untuk hitung_pangkat(2, 3) sebelum ngoding.