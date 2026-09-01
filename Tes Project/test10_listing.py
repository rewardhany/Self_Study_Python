# ==============================================================================
# 📘 MODUL MASTERCLASS: PYTHON LIST (DARI DASAR SAMPAI ADVANCED)
# ==============================================================================
# Tinggal run (jalankan) file ini, semua contoh kodenya akan mencetak hasil
# di terminal supaya kamu bisa langsung lihat cara kerjanya!

print("=== MEMULAI MODUL PYTHON LIST PART 1===\n")

# ==============================================================================
# 🟢 LEVEL 1: DASAR (SANGAT MUDAH)
# ==============================================================================
print("--- LEVEL 1: DASAR ---")

# 1. MEMBUAT LIST
# List ditandai dengan kurung siku []. Isinya bisa tipe data apa saja (campuran).
list_angka = [1, 2, 3, 4, 5]
list_campuran = ["Reffa", 20, True, 3.14]

# Contoh dari kasusmu: Menyimpan urutan log kejadian
raw_logs = [
    "192.168.1.50 - FAILED",
    "10.0.0.12 - SUCCESS",
    "192.168.1.99 - FAILED"
]
print("1. Isi raw_logs saat ini:", raw_logs)

# 2. MENGAKSES DATA (INDEXING)
# Ingat: Komputer mulai menghitung dari 0, bukan 1!
# Trik: Pakai indeks minus (-) untuk mengambil dari urutan paling belakang.
print("2. Log urutan pertama (index 0) :", raw_logs[0])
print("   Log urutan terakhir (index -1):", raw_logs[-1])

# 3. MENGUBAH DATA (MUTABLE)
# Berbeda dengan string yang kaku, isi list bisa diganti kapan saja.
raw_logs[0] = "192.168.1.50 - RESOLVED"
print("3. Setelah index 0 diubah:", raw_logs)

# 4. SLICING (MEMOTONG LIST)
# Rumusnya: list[start:end] -> Mengambil dari 'start' sampai SEBELUM 'end'.
data_hari = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
print("4. Ambil indeks 1 sampai 3:", data_hari[1:4]) # Output: Selasa, Rabu, Kamis


# ==============================================================================
# 🟡 LEVEL 2: MENENGAH (METHOD & LOOPING)
# ==============================================================================
print("\n--- LEVEL 2: MENENGAH ---")

my_list = ["A", "B", "C"]

# 1. MENAMBAH DATA (.append & .insert)
my_list.append("D")          # .append() selalu menaruh data di ujung paling belakang
my_list.insert(1, "SISIPAN") # .insert(index, data) menaruh data di posisi spesifik
print("1. Tambah data:", my_list)

# 2. MENGHAPUS DATA (.remove, .pop)
my_list.remove("SISIPAN") # Menghapus berdasarkan nama nilai (value)
data_terhapus = my_list.pop() # Menghapus sekaligus MENGAMBIL data paling belakang
print("2. Hapus data:", my_list)
print("   Data yang dipop/diambil:", data_terhapus)

# 3. ITERASI (PERULANGAN) DENGAN ENUMERATE
# Ini cara paling elegan (Pythonic) untuk nge-loop list kalau kamu juga butuh NOMOR URUT
print("3. Looping List dengan Enumerate:")
daftar_log = ["Aman", "Bahaya", "Aman"]
for index, status in enumerate(daftar_log):
    print(f"   Log ke-{index}: {status}")


# ==============================================================================
# 🔴 LEVEL 3: ADVANCED (MULAI SUSAH & KOMPLEKS UNTUK PEMULA)
# ==============================================================================
print("\n--- LEVEL 3: ADVANCED ---")

# 1. NESTED LIST (LIST DI DALAM LIST / MATRIX 2D)
# Biasanya dipakai buat bikin Peta Game (X dan Y) atau tabel data.
peta_dungeon = [
    ["P", ".", "."], # Baris 0 (P = Player)
    [".", "M", "."], # Baris 1 (M = Monster)
    [".", ".", "E"]  # Baris 2 (E = Exit)
]
# Cara ngambil "M" (Ada di baris 1, kolom 1)
print("1. Akses Nested List (Monster ada di):", peta_dungeon[1][1])


# 2. LIST COMPREHENSION (Sihir 1 Baris Python)
# Ini adalah cara "Pro" bikin list baru dari list lama dengan cepat.
# Kasus: Kita mau menyaring 'raw_logs' TAPI HANYA AMBIL YANG "FAILED" SAJA.

# Cara Pemula (Butuh 4 baris):
log_gagal_pemula = []
for log in raw_logs:
    if "FAILED" in log:
        log_gagal_pemula.append(log)

# Cara Advanced (List Comprehension - Cuma 1 baris!):
# Rumus: [hasil_yang_dimasukkan for item in daftar if kondisi]
log_gagal_pro = [log for log in raw_logs if "FAILED" in log]

print("2. Hasil Filter List Comprehension:", log_gagal_pro)


# 3. TRAP PEMULA: JEBAKAN REFERENCE (COPY LIST)
# Ini bug nomor 1 yang paling sering bikin pemula pusing tujuh keliling!
print("3. Jebakan Copy List:")

list_asli = ["Kopi", "Teh", "Susu"]
# Kalau kamu pakai tanda sama dengan '=', kamu TIDAK membuat list baru!
# Kamu hanya membuat 'nama panggilan baru' untuk laci yang sama!
list_palsu = list_asli 

# Mari kita ubah list_palsu:
list_palsu[0] = "RACUN"

# Lihat apa yang terjadi pada list_asli? 
# Dia IKUT BERUBAH jadi RACUN karena lacinya sama!
print("   Isi List Asli  :", list_asli)  
print("   Isi List Palsu :", list_palsu)

# CARA MENGCOPY YANG BENAR (Membeli laci baru yang isinya sama):
list_benar = list_asli.copy() # ATAU list_asli[:]
list_benar[0] = "OBAT"

print("   Isi List Copy Benar:", list_benar)
print("   Isi List Asli (Tetap Aman):", list_asli)

print("\n=== MODUL SELESAI ===")

# ==============================================================================
# 📘 MODUL MASTERCLASS PART 2: OPERASI, FUNGSI, & METHOD PADA LIST
# ==============================================================================
print("=== MEMULAI MODUL LIST PART 2 ===\n")

# ==============================================================================
# 🟢 1. OPERASI DASAR PADA LIST (MATEMATIKA LIST)
# ==============================================================================
# List di Python sangat fleksibel, merespons operator '+' dan '*' mirip seperti teks (string).
print("--- 1. OPERASI DASAR ---")

# A. Concatenation (Penggabungan) menggunakan '+'
list_a = [1, 2, 3]
list_b = [4, 5, 6]
gabung = list_a + list_b
print("A. Hasil Penggabungan (+) :", gabung) # Output: [1, 2, 3, 4, 5, 6]

# B. Repetition (Pengulangan) menggunakan '*'
# Sangat berguna untuk membuat list dengan nilai default dengan cepat
list_ulang = ['Halo!'] * 4
print("B. Hasil Pengulangan (*)  :", list_ulang) # Output: ['Halo!', 'Halo!', 'Halo!', 'Halo!']

# C. Membership (Pengecekan Keanggotaan) menggunakan 'in'
# Mengembalikan nilai True jika data ada di dalam list, False jika tidak ada.
cek_angka = 2 in [1, 2, 3]
print("C. Apakah 2 ada di list?  :", cek_angka) # Output: True

# D. Iteration (Perulangan)
# Mencetak semua isi list ke samping (pakai parameter end=' ')
print("D. Hasil Iterasi (for)    :", end=" ")
for x in [1, 2, 3]:
    print(x, end=" ")
print("\n")


# ==============================================================================
# 🟡 2. INDEXING, SLICING, DAN MATRIX (REVIEW & KASUS BARU)
# ==============================================================================
print("--- 2. INDEXING & SLICING ---")
L = ['C++', 'Java', 'Python']

# Indexing Positif (Dihitung dari Kiri, mulai dari 0)
print("1. Index 2 (L[2])         :", L[2])  # Output: 'Python'

# Indexing Negatif (Dihitung dari Kanan, mulai dari -1)
print("2. Index -2 (L[-2])       :", L[-2]) # Output: 'Java' (Mundur 2 langkah dari belakang)

# Slicing (Memotong sebagian List)
print("3. Slicing L[1:]          :", L[1:]) # Output: ['Java', 'Python'] (Mulai dari 1 sampai habis)


# ==============================================================================
# 🟠 3. BUILT-IN FUNCTIONS (FUNGSI BAWAAN PYTHON UNTUK LIST)
# ==============================================================================
# Fungsi bawaan ini bisa langsung dipakai dengan memasukkan list ke dalam kurungnya.
print("\n--- 3. BUILT-IN FUNCTIONS ---")
angka = [45, 10, 99, 2]

print("1. len(angka) :", len(angka)) # Memberikan total panjang list (Output: 4)
print("2. max(angka) :", max(angka)) # Mencari nilai paling besar (Output: 99)
print("3. min(angka) :", min(angka)) # Mencari nilai paling kecil (Output: 2)

# Mengubah tipe data lain (seperti Tuple) menjadi List
data_tuple = ("HTML", "CSS", "Tailwind") # Ini Tuple (pakai kurung biasa)
data_list = list(data_tuple)             # Disulap jadi List (pakai kurung siku)
print("4. list()     :", type(data_list), data_list)


# ==============================================================================
# 🔴 4. BUILT-IN METHODS (KEMAMPUAN KHUSUS MILIK LIST)
# ==============================================================================
# Method adalah fungsi yang nempel langsung pada variabel list (dipanggil pakai titik '.')
print("\n--- 4. LIST METHODS ---")
bahasa = ['Python', 'C++', 'JavaScript']

# 1. .append(obj) -> Menambah HANYA 1 objek ke paling belakang
bahasa.append('React')
print("1. Setelah .append() :", bahasa)

# 2. .extend(seq) -> Menambah BANYAK objek dari list lain ke belakang (Penting!)
# Beda dengan append, extend membongkar list barunya dan menggabungkannya
bahasa.extend(['NodeJS', 'PHP'])
print("2. Setelah .extend() :", bahasa)

# 3. .insert(index, obj) -> Menyisipkan data di posisi indeks tertentu
bahasa.insert(1, 'Golang') # Golang akan merebut posisi indeks 1 (C++ akan geser)
print("3. Setelah .insert() :", bahasa)

# 4. .remove(obj) -> Menghapus data berdasarkan NAMA NILAINYA (Hanya hapus yang pertama ketemu)
bahasa.remove('PHP')
print("4. Setelah .remove() :", bahasa)

# 5. .pop(index) -> Menghapus & mengambil data berdasarkan INDEX (Default: paling belakang)
terakhir = bahasa.pop()
print("5. Setelah .pop()    :", bahasa, "| Data yang terbuang:", terakhir)

# 6. .index(obj) -> Mencari di indeks ke berapa sebuah data berada
posisi_python = bahasa.index('Python')
print("6. Posisi 'Python'   : Indeks ke-", posisi_python)

# 7. .count(obj) -> Menghitung berapa kali suatu data muncul di dalam list
daftar_nilai = [80, 90, 80, 100, 80]
print("7. Jumlah nilai 80   :", daftar_nilai.count(80), "kali")

# 8. .sort() dan .reverse() -> Mengurutkan dan Membalikkan List
angka_acak = [5, 2, 9, 1]
angka_acak.sort() # Mengurutkan dari kecil ke besar (Ascending)
print("8a. Setelah .sort()  :", angka_acak)

angka_acak.reverse() # Membalikkan urutan saat ini (menjadi besar ke kecil)
print("8b. Setelah .reverse():", angka_acak)

print("\n=== MODUL SELESAI ===")

# ==============================================================================
# 📘 MODUL MASTERCLASS PART 3: ADVANCED LIST MANIPULATION & TRICKS
# ==============================================================================
# Modul ini membahas teknik List tingkat lanjut yang sering dipakai di dunia
# professional (Data Engineering, Backend, & Cyber Security).

print("=== MEMULAI MODUL LIST PART 3 (ADVANCED) ===\n")

# ==============================================================================
# 🟢 1. STEP SLICING (MEMOTONG DENGAN LOMPATAN/POLA)
# ==============================================================================
# Rumus lengkap slicing: list[start : end : step]
# 'step' menentukan arah dan berapa lompatan data yang diambil.
print("--- 1. STEP SLICING ---")
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# A. Mengambil angka genap saja (Lompat 2 dari indeks 0)
genap = numbers[0::2]
print("A. Angka Genap (step 2)      :", genap)   # Output: [0, 2, 4, 6, 8]

# B. Mengambil angka ganjil (Lompat 2 dari indeks 1)
ganjil = numbers[1::2]
print("B. Angka Ganjil (start 1)    :", ganjil)  # Output: [1, 3, 5, 7, 9]

# C. Trik Cepat Membalikkan List (Reversing Slicing)
# Menggunakan step -1 akan membalikkan list secara instan tanpa merusak variabel asli.
reversed_nums = numbers[::-1]
print("C. Reversing via Slicing [::-1]:", reversed_nums)


# ==============================================================================
# 🟡 2. LIST UNPACKING & ASTERISK (*) OPERATOR
# ==============================================================================
# Unpacking memungkinkan kita membongkar elemen List langsung ke variabel terpisah.
print("\n--- 2. LIST UNPACKING ---")

# A. Basic Unpacking (Jumlah variabel harus pas dengan jumlah data)
koordinat = [10, 20]
x, y = koordinat
print(f"A. Koordinat X: {x}, Y: {y}")

# B. Extended Unpacking (Pakai operator '*' untuk menampung sisa data ke dalam List baru)
data_server = ["192.168.1.1", "ONLINE", "CPU: 12%", "RAM: 45%", "DISK: 80%"]
ip, status, *metrics = data_server

print("B. IP Server     :", ip)
print("   Status        :", status)
print("   Metrics (List):", metrics) # Output: ['CPU: 12%', 'RAM: 45%', 'DISK: 80%']


# ==============================================================================
# 🟠 3. DEEP COPY VS SHALLOW COPY (PENTING AGAR TIDAK BUG)
# ==============================================================================
# Saat membuat List di dalam List (Nested List), metode .copy() biasa (shallow copy)
# masih menyimpan referensi ke list di dalamnya. Kita butuh 'copy.deepcopy'!
print("\n--- 3. DEEP COPYING ---")
import copy

# Peta matrix 2D (Nested List)
grid_original = [
    ["A", "B"],
    ["C", "D"]
]

# Shallow copy (Biasa) vs Deep copy (Sempurna)
grid_shallow = grid_original.copy()
grid_deep = copy.deepcopy(grid_original)

# Mengubah data di dalam nested list
grid_original[0][0] = "X"

print("Original Grid        :", grid_original) # Transformed to X
print("Shallow Copy (IKUT UBAH!):", grid_shallow)  # Ikut berubah jadi X (Bug!)
print("Deep Copy (AMAN TETAP A) :", grid_deep)     # Tetap A (Benar-benar independen)


# ==============================================================================
# 🔴 4. CUSTOM SORTING DENGAN LAMBDA (PENGURUTAN KOMPLEKS)
# ==============================================================================
# Method .sort() standar hanya mengurutkan huruf/angka biasa.
# Gunakan parameter key=lambda untuk mengurutkan List berisi Dictionary atau Tuple.
print("\n--- 4. CUSTOM SORTING ---")

users = [
    {"name": "Reffa", "age": 20},
    {"name": "Budi", "age": 17},
    {"name": "Andi", "age": 25}
]

# Mengurutkan user berdasarkan Umur (Age) dari termuda ke tertua
users.sort(key=lambda item: item["age"])
print("1. User Diurutkan Umur (Ascending):")
for u in users:
    print(f"   - {u['name']}: {u['age']} tahun")

# Mengurutkan user berdasarkan panjang Karakter Nama
users.sort(key=lambda item: len(item["name"]), reverse=True)
print("2. User Diurutkan Panjang Nama (Descending):")
for u in users:
    print(f"   - {u['name']}")


# ==============================================================================
# 🟣 5. FUNCTIONAL LIST MANIPULATION (MAP, FILTER, REDUCE)
# ==============================================================================
# Gaya penulisan fungsional untuk mengolah List secara elegan tanpa loop manual.
print("\n--- 5. MAP, FILTER, REDUCE ---")
from functools import reduce

angka_raw = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# A. MAP: Mengubah semua isi list (Misal: Kalikan 2 semua elemen)
dikali_dua = list(map(lambda x: x * 2, angka_raw))
print("A. Map (Semua * 2)       :", dikali_dua)

# B. FILTER: Menyaring isi list berdasarkan syarat (Misal: Ambil yang > 5 saja)
diatas_lima = list(filter(lambda x: x > 5, angka_raw))
print("B. Filter (Hanya > 5)    :", diatas_lima)

# C. REDUCE: Mengakumulasi seluruh elemen list menjadi 1 nilai tunggal (Misal: Total Penjumlahan)
total_akumulasi = reduce(lambda acc, x: acc + x, angka_raw)
print("C. Reduce (Total Angka)  :", total_akumulasi)

print("\n=== MODUL 3 SELESAI ===")

# ==============================================================================
# 📘 MODUL MASTERCLASS PART 4: STRUCTURING DATA & LAMBDA ANATOMY
# ==============================================================================
# Di modul ini kita pelajari 3 hal penting:
# 1. Struktur Data Campuran: List di dalam List vs Dict di dalam List
# 2. Pembongkaran Sintaks Lambda (Fungsi 1 Baris)
# 3. Cara Kerja Map & Filter Secara Manusiawi (Bandingkan dengan For Loop)

print("=== MEMULAI MODUL PART 4 ===\n")


# ==============================================================================
# 🟢 1. BEDAH STRUKTUR: DIC DI DALAM LIST (NESTED STRUCTURE)
# ==============================================================================
print("--- 1. NESTED STRUCTURE (KURUNG SIKU + KURUNG KURAWAL) ---")

# Bayangkan kamu punya keranjang belanjaan:
# Kurung siku [...] artinya: "Ini adalah DAFTAR/LIST barang-barang belanjaan"
# Kurung kurawal {...} artinya: "Ini adalah Rincian Detail dari 1 barang"

cart_items = [
    {"product": "Book", "price": 50000, "qty": 2},  # Barang Indeks 0
    {"product": "Pen",  "price": 10000, "qty": 5},  # Barang Indeks 1
    {"product": "Bag",  "price": 200000, "qty": 1}  # Barang Indeks 2
]

# CARA BACA KODE DI ATAS:
# cart_items[0]                 -> Mengambil 1 barang pertama yaitu: {"product": "Book", "price": 50000, "qty": 2}
# cart_items[0]["product"]      -> Mengambil NAMA barang pertama, yaitu: "Book"
# cart_items[0]["price"]        -> Mengambil HARGA barang pertama, yaitu: 50000

print("Barang pertama             :", cart_items[0]["product"])
print("Harga barang pertama       : Rp", cart_items[0]["price"])

# Kalau mau menghitung total tanpa 'reduce' (Pakai Loop Biasa yang Manusiawi):
total_belanja = 0
for item in cart_items:
    # item adalah dictionary satu per satu dari cart_items
    subtotal = item["price"] * item["qty"]
    total_belanja += subtotal

print(f"Total Belanja (Pakai Loop) : Rp {total_belanja:,}\n")


# ==============================================================================
# 🟡 2. ANATOMY SINTAKS 'LAMBDA' (FUNGSI TANPA NAMA / SHORTCUT)
# ==============================================================================
print("--- 2. ANATOMI LAMBDA ---")

# Lambda itu SEBENARNYA HANYA FUNGSI BIASA (def), tapi ditulis ringkas 1 baris.
# Contoh Kasus: Buat fungsi perkalian 2 angka.

# --- CARA BIASA (Pakai def) ---
def kali_biasa(a, b):
    return a * b

# --- CARA LAMBDA ---
# Rumus: lambda parameter : hasil_return
kali_lambda = lambda a, b: a * b

print("Hasil fungsi biasa  :", kali_biasa(5, 4))
print("Hasil fungsi lambda :", kali_lambda(5, 4))

# Contoh lain: Mengambil harga dari 1 objek belanjaan
dapatkan_harga = lambda item: item["price"]
print("Harga dari barang[1]:", dapatkan_harga(cart_items[1])) # Output: 10000
print()


# ==============================================================================
# 🟠 3. BEDA MAP DAN FILTER (DISANDINGKAN DENGAN FOR LOOP)
# ==============================================================================
print("--- 3. BEDA MAP VS FILTER ---")

# Anggap kita punya list angka:
angka = [1, 2, 3, 4, 5, 6]

# ------------------------------------------------------------------------------
# A. MAP = MENGUBAH / MENGOLAH SEMUA ELEMEN
# Konsep Map: "Ubah SEMUA item di list menjadi bentuk baru" (Jumlah data TETAP SAMA)
# ------------------------------------------------------------------------------

# Kasus: Kalikan semua angka dengan 10.

# Cara Loop Biasa:
hasil_map_loop = []
for x in angka:
    hasil_map_loop.append(x * 10)

# Cara Map + Lambda:
# map(fungsi_pengubah, daftar_data)
hasil_map_pro = list(map(lambda x: x * 10, angka))

print("Hasil Map (Semua * 10)  :", hasil_map_pro)


# ------------------------------------------------------------------------------
# B. FILTER = MENYARING ELEMEN
# Konsep Filter: "Seleksi item di list, ambil yang LULUS SYARAT saja" (Jumlah data BISA BERKURANG)
# ------------------------------------------------------------------------------

# Kasus: Ambil angka yang LEBIH BESAR DARI 3 saja.

# Cara Loop Biasa:
hasil_filter_loop = []
for x in angka:
    if x > 3:
        hasil_filter_loop.append(x)

# Cara Filter + Lambda:
# filter(fungsi_syarat_true_false, daftar_data)
hasil_filter_pro = list(filter(lambda x: x > 3, angka))

print("Hasil Filter (Angka > 3):", hasil_filter_pro)
print()


# ==============================================================================
# 💡 KANTONG ISTILAH / KAMUS KECIL (BIAR GAK BINGUNG LAGI)
# ==============================================================================
"""
1. REST API : 
   Format komunikasi standar via HTTP/URL antara aplikasi client (Frontend/Mobile) 
   dan server tempat data diproses (Backend).

2. FastAPI & Django :
   Framework / 'Alat Perkakas Ready-to-use' di Python untuk membuat sistem Backend / Web API.
   - FastAPI -> Ringan, sangat cepat, modern.
   - Django  -> Lengkap, bawaan baterai (ada admin panel, sistem auth otomatis, dll).

3. Lambda : 
   Trik penulisan fungsi 1 baris yang praktis saat butuh fungsi cepat tanpa perlu nulis 'def'.

4. Map & Filter :
   Metode bawaan Python untuk mengolah (Map) atau menyaring (Filter) isi List tanpa
   perlu membuat variabel penampung kosong dan 'for loop' secara manual.
"""

print("=== MODUL PART 4 SELESAI ===")