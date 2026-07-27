# ======================================================
# 03 *ARGS & **KWARGS
# ======================================================
# *ARGS adalah:
# Cara menerima JUMLAH ARGUMEN TAK TERBATAS (tanpa keyword) ke dalam 1 tuple
#
# **KWARGS adalah:
# Cara menerima JUMLAH KEYWORD ARGUMENT TAK TERBATAS ke dalam 1 dictionary
#
# Digunakan ketika:
# - Kamu tidak tahu pasti berapa banyak data yang akan dikirim ke fungsi
#
# STRUKTUR DASAR:
# def nama_fungsi(*args, **kwargs):
#     kode
# ======================================================


# ------------------------------------------------------
# CONTOH 1: *ARGS - JUMLAH ARGUMEN TAK TERBATAS
# ------------------------------------------------------

def total_belanja(*harga):
    print(f"Tipe args: {type(harga)}")   # selalu tuple
    return sum(harga)

print(total_belanja(15000, 20000))
print(total_belanja(15000, 20000, 5000, 8000))

# Penjelasan:
# - *harga menampung SEMUA argumen yang dikirim jadi 1 tuple
# - Bisa dipanggil dengan 2 argumen, 5 argumen, atau 0 argumen - semua valid


# ------------------------------------------------------
# CONTOH 2: **KWARGS - KEYWORD ARGUMENT TAK TERBATAS
# ------------------------------------------------------

def buat_profil(**data):
    print(f"Tipe kwargs: {type(data)}")   # selalu dict
    for key, value in data.items():
        print(f"{key}: {value}")

buat_profil(nama="Reffa", jurusan="Teknik Komputer", divisi="Keamanan")

# Penjelasan:
# - **data menampung SEMUA keyword argument jadi 1 dictionary
# - Cocok kalau field data-nya bisa beda-beda tiap pemanggilan


# ------------------------------------------------------
# CONTOH 3: KOMBINASI PARAMETER NORMAL + *ARGS + **KWARGS
# ------------------------------------------------------

def catat_transaksi(nama_pembeli, *item, **detail):
    print(f"Pembeli: {nama_pembeli}")
    print(f"Item dibeli: {item}")
    print(f"Detail tambahan: {detail}")

catat_transaksi("Reffa", "Kabel HDMI", "Extension", metode_bayar="QRIS", diskon=10)

# Penjelasan:
# - Urutan WAJIB: parameter normal -> *args -> **kwargs
# - nama_pembeli = wajib diisi urutan pertama
# - item = menampung semua argumen tanpa nama (jadi tuple)
# - detail = menampung semua argumen dengan nama (jadi dict)


# ------------------------------------------------------
# CONTOH 4: UNPACKING SAAT MEMANGGIL FUNGSI
# ------------------------------------------------------

def hitung_volume_balok(panjang, lebar, tinggi):
    return panjang * lebar * tinggi

ukuran = [5, 3, 2]
print(hitung_volume_balok(*ukuran))          # unpacking list jadi positional argument

data_profil = {"nama": "Reffa", "divisi": "Keamanan"}
def tampilkan_profil(nama, divisi):
    print(f"{nama} - {divisi}")

tampilkan_profil(**data_profil)               # unpacking dict jadi keyword argument

# Penjelasan:
# - *ukuran saat MEMANGGIL fungsi = "bongkar" list jadi argumen terpisah
# - **data_profil saat MEMANGGIL fungsi = "bongkar" dict jadi keyword argument
# - Ini kebalikan dari CONTOH 1 & 2 (di sana *args/**kwargs itu MENGUMPULKAN, di sini MEMBONGKAR)


# ------------------------------------------------------
# CATATAN PENTING
# ------------------------------------------------------
# - args dan kwargs cuma NAMA VARIABEL, yang penting simbol * dan **-nya
# - Urutan parameter: normal -> *args -> parameter dengan default -> **kwargs
# - Jangan overuse *args/**kwargs kalau parameternya sebenarnya sudah pasti jumlahnya -
#   itu bikin fungsi susah dibaca karena tidak jelas apa isinya tanpa buka dokumentasi