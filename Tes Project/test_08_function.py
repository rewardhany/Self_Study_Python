print("=== SECTION 1 ===")

def introduction(name, age, city, region):
    print("My name is", name)
    print("I am", age + " years old!")
    print("And i am from", city)
    print("It's a city from", region)

introduction("Budi", "20", "Bandung", "Indonesia")
introduction("John", "18", "Los Angeles", "United States")
introduction("Normy", "21", "Yogyakarta", "Indonesia")
print()

print("=== SECTION 2 ===")

def reminder(nameTask, message="What's Up"):
    print(message + ", " + "Don't forget to do your task" + ",", nameTask + " will be end at 25.59!")

reminder("Data base task")
reminder("Matematika Teknik")
print()

print("=== SECTION 3 ===")
# Without return value
def sum(x, y):
    print(x + y)

result = sum(4, 8)
print("The result is: ", result) # the results will be None because the function doesn't return any values
print()

print("=== SECTION 4 ===")
# With return values
def sumReturn(a, b, c):
    return a + b + c

result = sumReturn(3, 7, 5)
print("The result is: ", result)
print(result * 2)
print(result - 5)
print()

print("=== SECTION 5 ===")

def multiplication(x, y, z):
    return x * y * z

result = multiplication(2, 8, 2)
print("Result: ", result)
print()

print("=== SECTION 6 ===")

def pertambahan(x, y):
    return x + y

hasil = pertambahan(2, 2)
print("Hasil: ", hasil)
print(result * 2)
# because python is executed code from top to bottom so when i type print(result * 2) it executes code from the last result, so here in section 6 there is no "result" variable while it's named as "hasil" instead "result", the code is looking back to top where is the last code that has "result" variable, so the last code has named "result" var is on the section 5 which it said result = 32 so when print(result * 2) executes, it will be 64
print()

print("=== SECTION 7 ===")

def luas_segitiga(alas, tinggi, konstanta=0.5):
    print(konstanta * alas * tinggi)
hasil = luas_segitiga(10, 3)
print()

def segitiga_luas(alas, tinggi, konstanta=0.5):
    return konstanta * alas * tinggi
luas = segitiga_luas(20, 3)
print("luas segitiga adalah: ", luas)
print()

print("=== SECTION 8 ===")

def luas_persegi(sisi):
    return sisi * sisi

def keliling_persegi(sisi):
    return 4 * sisi

luas = luas_persegi(6)
keliling = keliling_persegi(5)
total_keduanya = luas + keliling
selisih = luas - keliling

print("luas persegi adalah: ", luas)
print("keliling persegi adalah: ", keliling)
print("total: ", total_keduanya)
print("selisih: ", selisih)
print()

print("=== SECTION 9 ===")

# PERBEDAAN VARIABEL LOKAL DAN GLOBAL
# LOKAL
def kuadrat(x):
    hasil = x * x 
    return hasil

print("sebelum panggil func")

nilai = kuadrat(5)

print("setelah panggil func")
print("hasil nya: ", nilai)
print()
# Pada Kode ini: variabel hasil itu adalah Variabel Lokal (cuma hidup di dalam fungsi). Di luar fungsi, kamu menangkap nilainya menggunakan variabel baru bernama "nilai". -Gemini

# GLOBAL
def kudarat(y):
    return y * y

hasil = kudarat(4)
print("hasil nya: ", hasil)
print()
# Pada Kode ini: Di dalam fungsi, kamu tidak membuat variabel apa pun. Tapi saat memanggil fungsi di luar, kamu menangkap hasilnya menggunakan variabel bernama hasil. Karena dibuat di luar fungsi, hasil di Kode ini berstatus Variabel Global. Makanya, perintah print("hasil nya: ", hasil) di baris terakhir bisa berjalan sukses tanpa error. -Gemini
# Info Penting: Cara di Kode global jauh lebih sering dipakai oleh programmer (Pythonic style) karena lebih ringkas, hemat memori, dan tidak membuat baris kode penuh dengan variabel yang sebenarnya tidak terlalu dibutuhkan.

# CONTOH ANALOGI SEDERHANA SEBAGAI BUKTI PERBEDAAN LOKAL DAN GLOBAL
# CONTOH 1
# --- INI WILAYAH GLOBAL ---
nama_toko = "Warung Kopi Mantap"       # GLOBAL: Bisa dibaca di mana saja (termasuk di dalam fungsi)

def hitung_kembalian(uang_bayar, total_harga):
    # --- INI WILAYAH LOKAL (Di dalam fungsi) ---
    kembalian = uang_bayar - total_harga # LOKAL: Cuma hidup di dalam fungsi ini aja
    return kembalian                     # Mengirimkan nilai kembalian keluar fungsi

# Memanggil fungsi dan menyimpan hasilnya ke variabel baru
hasil_kembalian = hitung_kembalian(50000, 35000) # GLOBAL: Variabel baru untuk menampung hasil (15000)

print(nama_toko)        # SUKSES: Karena 'nama_toko' adalah variabel GLOBAL
print(hasil_kembalian)  # SUKSES: Karena 'hasil_kembalian' adalah variabel GLOBAL
#print(kembalian)        # ERROR! karena Python mencari variabel GLOBAL bernama 'kembalian', padahal 'kembalian' yang di atas sifatnya LOKAL (sudah dihapus saat fungsi selesai)
print()

# CONTOH 2
# --- INI WILAYAH GLOBAL ---
toko = "Warung Kopi Bandung"           # GLOBAL: Bisa diakses di mana saja

def hitung_kembalian(uangBayar, totalHarga):
    # --- INI WILAYAH LOKAL ---
    return uangBayar - totalHarga      # Langsung hitung & lempar nilai keluar, tanpa bikin variabel lokal

# Memanggil fungsi
kembalian = hitung_kembalian(20000, 15000) # GLOBAL: Kamu membuat variabel 'kembalian' DI LUAR fungsi. Jadi nilainya (5000) aman tersimpan di wilayah global.

print(toko)                             # SUKSES: Karena 'toko' adalah variabel GLOBAL
print(kembalian)                        # SUKSES: Karena 'kembalian' di sini dibuat di luar fungsi (GLOBAL)
print("Kembalian yang anda dapat: ", kembalian) # SUKSES: Memanggil variabel GLOBAL 'kembalian' lagi
print()

# CONTOH 3
nama_warung = "Warung ibu dedeh"

def total_belanja(barang1, barang2):
    total = barang1 + barang2
    return total

harga = total_belanja(1000, 2000)
print(nama_warung)
print(harga)
print("Total harga: ", harga)
print()

nama_warung = "Warung makan bu denok"

def harga_total(makanan1, makanan2):
    return makanan1 + makanan2

total = harga_total(5000, 3000)
print(nama_warung)
print(total)
print("total harga: ", total)
print()

# CONTOH 4
def konversi_celcius_ke_kelvin(celcius):
    return celcius + 273.15

def hitung_energi_kinetik(massa, kecepatan, debug_mode=False):
    kecepatan_kuadrat = kecepatan * kecepatan
    energi = 0.5 * massa * kecepatan_kuadrat

    if debug_mode == True:
        print("\n=== [DEBUG MODE] ===")
        print(f"Massa             : {massa} kg")
        print(f"Kecepatan Kuadrat : {kecepatan_kuadrat} m^2/s^2")
        print(f"Energi (Internal) : {energi} Joule")
        print("====================\n")

    return energi

print("--- Memulai program ---")

suhu_kelvin = konversi_celcius_ke_kelvin(27)
print(f"suhu dalam kelvin: {suhu_kelvin} K")

print("-" * 30)

energi_mobil = hitung_energi_kinetik(massa=1000, kecepatan=20)
print(f"energi kinetik mobil: :{energi_mobil} Joule")

print("-" * 30)

energi_roket = hitung_energi_kinetik(massa=50, kecepatan=10, debug_mode=True)
print(f"Energi Kinetik Roket: {energi_roket} Joule")
print()

# CONTOH 5
# VARIABEL GLOBAL (Data Pusat / Database Sementara)
NAMA_BIOSKOP = "Cinema 2026"
total_pendapatan_hari_ini = 0  # Akan terus bertambah tiap ada yang beli tiket
harga_tiket_dasar = 50000

# FUNGSI-FUNGSI
def hitung_diskon_member(status_member, total_harga):
    # Fungsi ini menggunakan variabel lokal untuk menghitung diskon
    # VARIABEL LOKAL (Cuma hidup di fungsi ini)
    persen_diskon = 0.15  # Member dapat diskon 15%
    
    if status_member == True:
        potongan = total_harga * persen_diskon  # Variabel lokal
        return potongan
    else:
        return 0  # Gak dapet diskon

def beli_tiket(nama_film, jumlah_tiket, apakah_member):
    # Fungsi utama untuk memproses pembelian tiket
    # Kita panggil variabel global ke dalam fungsi menggunakan kata kunci 'global'
    # supaya kita bisa mengubah nilainya yang di luar sana
    global total_pendapatan_hari_ini 
    
    # VARIABEL LOKAL (Cuma dipakai saat proses transaksi film ini saja)
    total_awal = harga_tiket_dasar * jumlah_tiket
    potongan_harga = hitung_diskon_member(apakah_member, total_awal)
    total_akhir = total_awal - potongan_harga
    
    # Mengupdate VARIABEL GLOBAL pusat
    total_pendapatan_hari_ini = total_pendapatan_hari_ini + total_akhir
    
    # Cetak Struk
    print(f"--- STRUK PEMBELIAN {NAMA_BIOSKOP} ---")
    print(f"Film         : {nama_film}")
    print(f"Jumlah Tiket : {jumlah_tiket} tiket")
    print(f"Total Bayar  : Rp {total_akhir:,}")
    print("------------------------------------\n")


# MENJALANKAN PROGRAM (MAIN PROGRAM)

# Transaksi 1: Budi beli 2 tiket Avatar, dia bukan member
beli_tiket("Avatar 3", 2, apakah_member=False)

# Transaksi 2: Susi beli 3 tiket Avengers, dia member
beli_tiket("Avengers: Secret Wars", 3, apakah_member=True)

# Di akhir hari, kita cek total pendapatan bioskop dari variabel global
print(f"LAPORAN KEUANGAN {NAMA_BIOSKOP}:")
print(f"Total Pendapatan Hari Ini: Rp {total_pendapatan_hari_ini:,}")
print()

# CONTOH 6
# HELPBLUE PLATFORM
APP_NAME = "Helpblue"
total_pemasukan_harian = 0
total_order_selesai = 0

def hitung_tarif_dasar(jenis_layanan, durasi_jam):
    if jenis_layanan == "teknisi":
        total_tarif = durasi_jam * 50000
        return total_tarif
    elif jenis_layanan == "kebersihan":
        total_tarif = durasi_jam * 30000
        return total_tarif

def proses_order(nama_pelanggan, jenis_layanan, durasi_jam, pakai_promo):
    global total_pemasukan_harian, total_order_selesai

    harga_awal = hitung_tarif_dasar(jenis_layanan, durasi_jam)

    if pakai_promo == True:
        harga_akhir = harga_awal - 10000
    else:
        harga_akhir = harga_awal

    total_pemasukan_harian = total_pemasukan_harian + harga_akhir
    total_order_selesai = total_order_selesai + 1

proses_order("Thoriq", "teknisi", 2, pakai_promo=False)
proses_order("Asep", "kebersihan", 3, pakai_promo=True)

print(f"== LAPORAN HARIAN {APP_NAME.upper()} ==")
print(f"Total pendapatan : Rp {total_pemasukan_harian:,}")
print(f"Total orderan : {total_order_selesai} orderan")
print("=============================")
print()

# CONTOH 7
print("=== CONTOH 7 ===")
NAMA_WARUNG = "Warung Bu Denok"
pemasukan_hari_ini = 0
jumlah_terjual = 0 # ex sayur, barang, dan lain sebagainya
total_hutang_belum_bayar = 0
total_kerugian = 0
daftar_penghutang = [] # pakai array buat list nama

def penjualan(nama_barang, total_terjual, harga_satuan):
    global pemasukan_hari_ini, jumlah_terjual

    harga_bayar = total_terjual * harga_satuan
    pemasukan_hari_ini = pemasukan_hari_ini + harga_bayar
    jumlah_terjual = jumlah_terjual + total_terjual

    # NOTA
    print(f"== LAPORAN PENJUALAN {NAMA_WARUNG} HAR INI ==")
    print(f"Nama barang: {nama_barang}")
    print(f"Jumlah : {total_terjual} pcs/kg")
    print(f"Total bayar : Rp {harga_bayar:,}")
    print("=================\n")

def catatan_hutang(nama_pelanggan, nominal_hutang):
    global total_hutang_belum_bayar, daftar_penghutang

    total_hutang_belum_bayar = total_hutang_belum_bayar + nominal_hutang
    daftar_penghutang.append(nama_pelanggan)

    print(f"== CATATAN HUTANG ==")
    print(f"Nama pelanggan: {nama_pelanggan}")
    print(f"Total hutang : Rp {nominal_hutang:,}")
    print(f"Status : Belum bayar")
    print("================\n")

def catat_barang_rusak(nama_barang, total_rugi):
    global total_kerugian
    total_kerugian = total_kerugian + total_rugi
    print(f"[BARANG RUSAK/BUSUK] {nama_barang} senilai Rp {total_rugi:,} dicatat.\n")

def laporan_akhir_hari():
    global pemasukan_hari_ini, jumlah_terjual, total_hutang_belum_bayar, total_kerugian, daftar_penghutang
    
    # Hitung keuntungan bersih (Pemasukan dikurangi kerugian barang rusak)
    keuntungan_bersih = pemasukan_hari_ini - total_kerugian
    
    print(f"=========================================")
    print(f"      LAPORAN AKHIR HARI {NAMA_WARUNG.upper()}      ")
    print(f"=========================================")
    print(f" Total Barang Terjual : {jumlah_terjual} pcs/kg")
    print(f" Total Pemasukan      : Rp {pemasukan_hari_ini:,}")
    print(f" Total Kerugian       : Rp {total_kerugian:,}")
    print(f" Keuntungan Bersih    : Rp {keuntungan_bersih:,}")
    print(f"-----------------------------------------")
    print(f" Total Hutang Warga   : Rp {total_hutang_belum_bayar:,}")
    print(f" Daftar Orang Ngutang : {daftar_penghutang}")
    print(f"=========================================\n")


# JALANKAN PROGRAM (SIMULASI TRANSAKSI)
# 1. Ada pembeli lunas
penjualan("Minyak Goreng", total_terjual=2, harga_satuan=15000)
penjualan("Telur Ayam", total_terjual=5, harga_satuan=2000)

# 2. Ada tetangga yang ngutang
catatan_hutang("Pak Thoriq", nominal_hutang=50000)
catatan_hutang("Bu Susi", nominal_hutang=25000)

# 3. Ada barang yang busuk/rusak
catat_barang_rusak("Tomat Busuk", total_rugi=12000)

# 4. Bu Denok tutup warung, cetak laporan totalnya
laporan_akhir_hari()

# =====================================================================
# CHATATAN BELAJAR: MANIPULASI LIST (ARRAY) DI PYTHON
# =====================================================================
# List ibarat sebuah "laci penyimpanan" untuk menampung banyak data.
# Python menyediakan tombol kendali (method) untuk mengatur isi laci ini.

# 1. .append() -> Tombol "Masukkan Barang"
# Digunakan untuk memasukkan data baru ke urutan PALING BELAKANG di list.
# Cara pakai: nama_list.append(data_baru)
keranjang_belanja = ["bayam", "tomat"]
keranjang_belanja.append("tempe")  # 'tempe' masuk ke posisi terakhir
# Hasilnya sekarang: ["bayam", "tomat", "tempe"]


# 2. len() -> Tombol "Hitung Jumlah Barang"
# Singkatan dari 'Length'. Digunakan untuk menghitung TOTAL ISI di dalam list.
# Cara pakai: len(nama_list)
total_isi_keranjang = len(keranjang_belanja)  # Python menghitung, total ada 3 barang
# Hasilnya: total_isi_keranjang bernilai 3


# 3. .remove() -> Tombol "Buang Barang"
# Digunakan untuk menghapus data SPESIFIK yang kita pilih dari dalam list.
# Cara pakai: nama_list.remove(data_yang_mau_dihapus)
keranjang_belanja.remove("tomat")  # 'tomat' dibuang dari laci keranjang
# Hasilnya sekarang: ["bayam", "tempe"]


# =====================================================================
# RINGKASAN CEPAT:
# * Mau TAMBAH data paling belakang? -> .append()
# * Mau HITUNG total data saat ini?  -> len()
# * Mau HAPUS data tertentu?         -> .remove()
# =====================================================================