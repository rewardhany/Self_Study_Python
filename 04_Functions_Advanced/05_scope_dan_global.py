# ======================================================
# 05 SCOPE & GLOBAL
# ======================================================
# SCOPE adalah:
# "Wilayah" di mana sebuah variabel bisa diakses
#
# Ada 2 jenis utama:
# - LOCAL scope: variabel yang dibuat DI DALAM fungsi, cuma bisa diakses di situ
# - GLOBAL scope: variabel yang dibuat DI LUAR fungsi, bisa diakses di mana saja
# ======================================================


# ------------------------------------------------------
# CONTOH 1: LOCAL SCOPE
# ------------------------------------------------------

def hitung_denda():
    denda = 15000     # variabel LOCAL, cuma hidup di dalam fungsi ini
    print(f"Denda di dalam fungsi: {denda}")

hitung_denda()
# print(denda)   # <- kalau di-uncomment: ERROR, denda tidak dikenal di luar fungsi

# Penjelasan:
# - Variabel yang dibuat di dalam fungsi otomatis LOCAL
# - Begitu fungsi selesai jalan, variabel local-nya "hilang", tidak bisa diakses lagi


# ------------------------------------------------------
# CONTOH 2: GLOBAL SCOPE (BACA SAJA, TANPA KEYWORD)
# ------------------------------------------------------

nama_aplikasi = "Sistem Perpustakaan"   # variabel GLOBAL

def tampilkan_judul():
    print(f"=== {nama_aplikasi} ===")   # bisa BACA variabel global tanpa masalah

tampilkan_judul()

# Penjelasan:
# - Fungsi BOLEH membaca variabel global tanpa keyword apapun
# - Tapi kalau mau MENGUBAH nilainya dari dalam fungsi, itu beda cerita (lihat CONTOH 3)


# ------------------------------------------------------
# CONTOH 3: MENGUBAH VARIABEL GLOBAL DARI DALAM FUNGSI
# ------------------------------------------------------

total_buku_keluar = 0

def tambah_buku_keluar_salah():
    total_buku_keluar = total_buku_keluar + 1   # <- ERROR kalau dijalankan
    # UnboundLocalError, karena Python pikir ini variabel LOCAL baru

def tambah_buku_keluar_benar():
    global total_buku_keluar        # bilang ke Python: "pakai variabel global, bukan bikin baru"
    total_buku_keluar = total_buku_keluar + 1

tambah_buku_keluar_benar()
tambah_buku_keluar_benar()
print(f"Total buku keluar: {total_buku_keluar}")

# Penjelasan:
# - Tanpa `global`, Python otomatis anggap variabel yang di-assign di dalam
#   fungsi itu LOCAL BARU, bukan mengubah yang global
# - `global nama_variabel` -> baru boleh ubah variabel global dari dalam fungsi
# - Ini persis pola yang dipakai di project perpustakaan BAB 2 kamu


# ------------------------------------------------------
# CONTOH 4: NESTED FUNCTION SCOPE (SEKILAS, LANJUT DI BAB DECORATOR)
# ------------------------------------------------------

def fungsi_luar():
    pesan = "Halo dari luar"

    def fungsi_dalam():
        print(pesan)   # fungsi dalam BISA baca variabel dari fungsi luar

    fungsi_dalam()

fungsi_luar()

# Penjelasan:
# - Fungsi di dalam fungsi bisa mengakses variabel dari fungsi pembungkusnya
# - Ini disebut "enclosing scope", dasar buat memahami closure & decorator di 08_intro_decorator.py


# ------------------------------------------------------
# CATATAN PENTING
# ------------------------------------------------------
# - Urutan pencarian variabel Python: Local -> Enclosing -> Global -> Built-in (LEGB)
# - Terlalu banyak pakai `global` bikin kode susah di-debug (efek samping tersembunyi)
# - Lebih baik: fungsi terima parameter & return hasil, daripada ubah variabel global
#   langsung -> kecuali memang butuh seperti pola project BAB 2