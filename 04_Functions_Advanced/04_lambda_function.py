# ======================================================
# 04 LAMBDA FUNCTION
# ======================================================
# LAMBDA adalah:
# Fungsi tanpa nama (anonymous function), ditulis dalam SATU baris
#
# Digunakan ketika:
# - Butuh fungsi kecil, sekali pakai, biasanya sebagai argumen fungsi lain
#
# STRUKTUR DASAR:
# lambda parameter: ekspresi
# ======================================================


# ------------------------------------------------------
# CONTOH 1: LAMBDA VS DEF (PERBANDINGAN LANGSUNG)
# ------------------------------------------------------

def kuadrat_def(x):
    return x ** 2

kuadrat_lambda = lambda x: x ** 2

print(kuadrat_def(5))
print(kuadrat_lambda(5))

# Penjelasan:
# - Keduanya menghasilkan hasil yang SAMA PERSIS
# - lambda tidak butuh kata `return` -> hasil ekspresi otomatis di-return
# - lambda cocok kalau logikanya SANGAT PENDEK, tidak untuk logika panjang


# ------------------------------------------------------
# CONTOH 2: LAMBDA SEBAGAI KEY DI sorted()
# ------------------------------------------------------

panitia = [
    {"nama": "Reffa", "umur": 20},
    {"nama": "Galan", "umur": 22},
    {"nama": "Bintang", "umur": 19}
]

urut_by_umur = sorted(panitia, key=lambda p: p["umur"])
print(urut_by_umur)

# Penjelasan:
# - key=lambda p: p["umur"] artinya: "urutkan berdasarkan nilai umur tiap item"
# - Ini penggunaan lambda paling umum -> dipakai buat nentuin ATURAN urutan
# - Tanpa lambda, kamu harus bikin fungsi terpisah cuma buat ini


# ------------------------------------------------------
# CONTOH 3: LAMBDA DENGAN BEBERAPA PARAMETER
# ------------------------------------------------------

hitung_total = lambda harga, jumlah: harga * jumlah

print(hitung_total(15000, 3))

# Penjelasan:
# - Lambda bisa punya lebih dari 1 parameter, dipisah koma seperti fungsi biasa
# - Tetap harus 1 ekspresi saja, tidak bisa ada banyak baris logika di dalamnya


# ------------------------------------------------------
# CONTOH 4: KAPAN SEBAIKNYA TIDAK PAKAI LAMBDA
# ------------------------------------------------------

# Kurang baik (lambda dipaksa buat logika kompleks, susah dibaca):
cek_kelulusan_lambda = lambda nilai: "Lulus" if nilai >= 75 else ("Remedial" if nilai >= 60 else "Tidak Lulus")

# Lebih baik (logika kompleks -> pakai def biasa):
def cek_kelulusan(nilai):
    if nilai >= 75:
        return "Lulus"
    elif nilai >= 60:
        return "Remedial"
    else:
        return "Tidak Lulus"

print(cek_kelulusan_lambda(70))
print(cek_kelulusan(70))

# Penjelasan:
# - Lambda yang dipaksa jadi panjang malah bikin susah dibaca, tujuannya kebalik
# - Aturan gampang: kalau lambda-nya sampai butuh dibaca 2x buat ngerti, pakai def


# ------------------------------------------------------
# CATATAN PENTING
# ------------------------------------------------------
# - lambda TIDAK punya nama, makanya biasa dipakai langsung di tempat
#   (misalnya di dalam sorted(), tidak disimpan ke variabel)
# - lambda hanya boleh 1 ekspresi, tidak bisa ada banyak baris statement
# - Kalau logika lebih dari 1 baris atau butuh nama yang jelas -> pakai def