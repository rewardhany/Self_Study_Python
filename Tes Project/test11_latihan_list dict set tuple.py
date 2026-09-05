# ==============================================================================
# 1. PERBANDINGAN LIST, TUPLE, DAN SET
# ==============================================================================
print("--- 1. LIST, TUPLE, & SET ---")

# A. LIST (Kurung Siku []) -> Bisa diubah, berurutan, boleh duplikat
data_list = ["apel", "jeruk", "apel"]
data_list[0] = "mangga" # Mengubah elemen pertama sukses
print("Output List  :", data_list) 
# Hasil: ['mangga', 'jeruk', 'apel']

# B. TUPLE (Kurung Biasa ()) -> TIDAK bisa diubah, berurutan, boleh duplikat
data_tuple = ("apel", "jeruk", "apel")
# data_tuple[0] = "mangga" -> JIKA BARIS INI DIJALANKAN, PROGRAM AKAN ERROR (TypeError)
print("Output Tuple :", data_tuple) 
# Hasil: ('apel', 'jeruk', 'apel')

# C. SET (Kurung Kurawal {}) -> Bisa ditambah/dihapus, TIDAK berurutan, otomatis HAPUS DUPLIKAT
data_set = {"apel", "jeruk", "apel"}
data_set.add("mangga")
print("Output Set   :", data_set) 
# Hasil (urutan bisa acak): {'jeruk', 'mangga', 'apel'} (Kata "apel" yang kedua otomatis hilang)


# ==============================================================================
# 2. PERBANDINGAN DICTIONARY MURNI VS LIST OF DICTIONARIES
# ==============================================================================
print("\n--- 2. DICTIONARY MURNI VS LIST OF DICTIONARIES ---")

# A. DICTIONARY MURNI (Profil 1 Orang)
# Hanya butuh 1 langkah akses: Sebut nama laci (key)-nya.
profil = {
    "nama": "Reffa",
    "jurusan": "Teknik Komputer",
    "divisi": "Keamanan"
}

print("Nama Profil      :", profil["nama"]) 
# Hasil: Reffa
print("Jurusan Profil   :", profil["jurusan"]) 
# Hasil: Teknik Komputer


# B. LIST OF DICTIONARIES (Daftar Banyak Barang)
# Butuh 2 langkah akses: 
# Langkah 1 -> Pilih nomor urut barang di List pakai angka [0], [1], dst.
# Langkah 2 -> Buka laci detail barang tersebut pakai string ["product"], ["price"]
cart_items = [
    {"id": 1, "product": "Buku", "price": 50000},   # Indeks 0
    {"id": 2, "product": "Pena", "price": 10000},   # Indeks 1
    {"id": 3, "product": "Tas", "price": 200000}    # Indeks 2
]

# Mengambil kata "Pena" (Pena ada di baris ke-1, di laci bernama "product")
nama_barang_kedua = cart_items[1]["product"]
print("Barang indeks 1  :", nama_barang_kedua) 
# Hasil: Pena

# Mengambil harga "Tas" (Tas ada di baris ke-2, di laci bernama "price")
harga_barang_ketiga = cart_items[2]["price"]
print("Harga indeks 2   :", harga_barang_ketiga) 
# Hasil: 200000