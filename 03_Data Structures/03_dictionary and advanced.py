# ======================================================
# 03 DICTIONARY BASIC & ADVANCED
# ======================================================
# DICTIONARY adalah:
# Struktur data yang nyimpan data dalam bentuk KEY-VALUE, bukan index angka
#
# Digunakan ketika:
# - Data punya "label" yang lebih jelas daripada sekadar index 0,1,2
# - Kamu butuh cari data berdasarkan NAMA/KATEGORI, bukan urutan
#
# STRUKTUR DASAR:
# nama_dict = {"key1": value1, "key2": value2}
# ======================================================


# ------------------------------------------------------
# CONTOH 1: KEY-VALUE BASIC & get()
# ------------------------------------------------------

profil = {
    "nama": "Reffa",
    "jurusan": "Teknik Komputer",
    "divisi": "Keamanan"
}

print(profil["nama"])                          # akses langsung
print(profil.get("divisi"))                     # akses pakai get()
print(profil.get("nim", "Belum diisi"))         # get() dengan default value

# Penjelasan:
# - profil["key"] -> ERROR kalau key-nya tidak ada
# - profil.get("key") -> lebih aman, return None kalau tidak ada
# - profil.get("key", default) -> kasih nilai default kalau key tidak ditemukan


# ------------------------------------------------------
# CONTOH 2: UPDATE, POP, KEYS/VALUES/ITEMS
# ------------------------------------------------------

profil["nim"] = "2306xxxx"          # nambah key baru
profil["divisi"] = "Keamanan ODWH"  # update key yang sudah ada

divisi_lama = profil.pop("divisi")  # hapus key, sekaligus ambil value-nya
print(f"Divisi dihapus: {divisi_lama}")

print(list(profil.keys()))
print(list(profil.values()))
print(list(profil.items()))

# Penjelasan:
# - dict["key"] = value -> nambah key baru ATAU update kalau sudah ada
# - .pop("key") -> hapus key tertentu, return value-nya
# - .keys() / .values() / .items() -> ambil semua key, semua value, atau pasangan keduanya


# ------------------------------------------------------
# CONTOH 3: NESTED DICTIONARY
# ------------------------------------------------------

data_panitia = {
    "Reffa": {"divisi": "Keamanan", "role": "Anggota"},
    "Sultan": {"divisi": "Ketua Pelaksana", "role": "Ketua"},
    "Iqbal":  {"divisi": "Supervisor", "role": "Supervisor"}
}

print(data_panitia["Reffa"]["divisi"])
print(data_panitia["Sultan"]["role"])

# Penjelasan:
# - Dictionary bisa berisi dictionary lain di dalamnya
# - Aksesnya tinggal "rantai" key satu per satu: dict["key_luar"]["key_dalam"]
# - Pola ini yang dipakai buat data JSON dari API nanti di BAB 9


# ------------------------------------------------------
# CONTOH 4: LOOPING DICTIONARY DENGAN .items()
# ------------------------------------------------------

for nama, detail in data_panitia.items():
    print(f"{nama} -> Divisi: {detail['divisi']}, Role: {detail['role']}")

# Penjelasan:
# - .items() ngasih dua nilai sekaligus tiap loop: key dan value-nya
# - detail di sini adalah dictionary lagi (karena nested), makanya dipanggil
#   pakai detail['divisi'] bukan detail.divisi


# ------------------------------------------------------
# CATATAN PENTING DICTIONARY
# ------------------------------------------------------
# - Key HARUS unik, kalau key sama ditulis 2x, yang terakhir yang dipakai
# - Key TIDAK BISA pakai list/dict sebagai key (harus tipe yang immutable: string, angka, tuple)
# - Kombinasi list + dict (list of dict / dict of dict) adalah pola paling
#   sering dipakai buat merepresentasikan data nyata (lihat PROJECT gabungan)

# ==============================================================================
# 📙 MODUL MASTERCLASS: PYTHON DICTIONARY & NESTED DICT
# ==============================================================================
# Konsep Utama: Dictionary adalah tempat penyimpanan data berbasis LABEL (Key).
# Berbeda dengan List yang menggunakan nomor urut (0, 1, 2), Dictionary
# menggunakan "Kata Kunci" (Key) untuk memanggil datanya (Value).
# 
# Analogi: Lemari Laci. Setiap laci punya stiker label nama, dan di dalamnya ada barang.

print("=== MEMULAI MODUL PYTHON DICTIONARY ===\n")

# ==============================================================================
# 🟢 LEVEL 1: DASAR (CRUD - Create, Read, Update, Delete)
# ==============================================================================
print("--- LEVEL 1: OPERASI DASAR DICTIONARY ---")

# 1. MEMBUAT DICTIONARY (Pakai kurung kurawal {})
# Format: {"kunci": "nilai"}
user_profile = {
    "username": "reffawardany",
    "role": "admin",
    "saldo": 150000
}
print("1. Isi Dictionary awal :", user_profile)

# 2. MENGAKSES DATA (Read)
# Menggunakan kurung siku berisi String Label/Key-nya
print("2. Ambil username      :", user_profile["username"])

# TIPS PRO: Gunakan method .get() agar aplikasi tidak CRASH/ERROR kalau key-nya tidak ada!
# Jika pakai ["umur"] -> akan ERROR KeyError.
# Jika pakai .get("umur") -> akan mengembalikan nilai 'None' (Lebih aman).
print("   Ambil umur (.get)   :", user_profile.get("umur", "Tidak ditemukan!"))

# 3. MENAMBAH & MENGUBAH DATA (Update)
# Jika key sudah ada, nilainya di-TUMPUK (Update). 
# Jika key belum ada, laci baru akan DIBUAT (Add).
user_profile["saldo"] = 500000       # UPDATE (saldo berubah)
user_profile["status"] = "Active"    # ADD (kunci baru)
print("3. Setelah di-Update   :", user_profile)

# 4. MENGHAPUS DATA (Delete)
del user_profile["role"]             # Menghapus laci "role" selamanya
status_terhapus = user_profile.pop("status") # Menghapus sekaligus mengambil isinya
print("4. Setelah di-Delete   :", user_profile)
print("   Data yang dipop     :", status_terhapus)


# ==============================================================================
# 🟡 LEVEL 2: LOOPING PADA DICTIONARY (ITERASI)
# ==============================================================================
print("\n--- LEVEL 2: LOOPING DICTIONARY ---")
laptop = {
    "merk": "Lenovo ThinkPad",
    "ram": "16GB",
    "storage": "512GB SSD"
}

# A. Looping hanya mengambil KUNCI (Keys)
print("A. Mengambil Keys:")
for kunci in laptop.keys():
    print(f"   - {kunci}")

# B. Looping hanya mengambil NILAI (Values)
print("B. Mengambil Values:")
for nilai in laptop.values():
    print(f"   - {nilai}")

# C. Looping mengambil KEDUANYA (Items) -> PALING SERING DIPAKAI!
print("C. Mengambil Key & Value bersamaan (.items()):")
for kunci, nilai in laptop.items():
    print(f"   {kunci.upper()} = {nilai}")


# ==============================================================================
# 🟠 LEVEL 3: NESTED DICTIONARY (DICTIONARY BERSARANG)
# ==============================================================================
# Ini adalah arsitektur untuk data kompleks, seperti yang kamu buat di aplikasi Finance!
print("\n--- LEVEL 3: NESTED DICTIONARY ---")

# Kasus: Database banyak user
database_user = {
    "user_01": {
        "nama": "Reffa",
        "email": "reffa@mail.com"
    },
    "user_02": {
        "nama": "Budi",
        "email": "budi@mail.com"
    }
}

# Cara akses bertingkat: sebutkan label laci besarnya dulu, baru laci kecilnya.
print("1. Email punya user_01 :", database_user["user_01"]["email"])
print("2. Nama punya user_02  :", database_user["user_02"]["nama"])

# Menambah data di dalam nested dictionary
database_user["user_01"]["kota"] = "Bandung"
print("3. Setelah Reffa diupdate:", database_user["user_01"])


# ==============================================================================
# 🔴 LEVEL 4: LIST OF DICTIONARIES (MENJAWAB KEBINGUNGAN TENTANG JSON/REST API)
# ==============================================================================
# Menggabungkan Kurung Siku [] dan Kurung Kurawal {}
# Inilah bentuk asli dari JSON yang dikirim oleh REST API!
print("\n--- LEVEL 4: LIST OF DICTIONARIES (Data API) ---")

# Bayangkan ini balasan dari Server Toko Online (REST API)
# Tanda [...] berarti ini List yang punya urutan (0, 1, 2)
# Tanda {...} berarti detail barang di indeks tersebut
cart_items = [
    {"id": 1, "product": "Buku", "price": 50000},   # Indeks 0
    {"id": 2, "product": "Pena", "price": 10000},   # Indeks 1
    {"id": 3, "product": "Tas", "price": 200000}    # Indeks 2
]

# Cara mengambil harga "Pena" (Pena ada di baris/indeks 1)
harga_pena = cart_items[1]["price"]
print("1. Harga Pena          : Rp", harga_pena)

# Cara menghitung total semua harga di keranjang menggunakan Loop
print("2. Struk Belanja:")
total_belanja = 0
for index, item in enumerate(cart_items, start=1):
    nama_barang = item["product"]
    harga_barang = item["price"]
    
    print(f"   {index}. {nama_barang} -> Rp {harga_barang:,}")
    total_belanja += harga_barang

print(f"   ----------------------- +")
print(f"   TOTAL: Rp {total_belanja:,}")

print("\n=== MODUL DICTIONARY SELESAI ===")