# ======================================================
# 01 FUNCTION REVIEW
# ======================================================
# Review singkat sebelum masuk materi lanjutan.
# Function adalah blok kode yang bisa dipanggil ulang-ulang,
# supaya tidak nulis kode yang sama berkali-kali.
#
# STRUKTUR DASAR:
# def nama_fungsi(parameter):
#     kode
#     return hasil
# ======================================================


# ------------------------------------------------------
# CONTOH 1: FUNGSI DASAR - PARAMETER & RETURN
# ------------------------------------------------------

def hitung_luas_persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    return luas

hasil = hitung_luas_persegi_panjang(5, 3)
print(f"Luas: {hasil}")

# Penjelasan:
# - parameter (panjang, lebar) = "kotak kosong" yang diisi saat fungsi dipanggil
# - return = mengirim nilai balik ke tempat fungsi dipanggil
# - Fungsi TANPA return otomatis menghasilkan None


# ------------------------------------------------------
# CONTOH 2: MULTIPLE RETURN VALUES
# ------------------------------------------------------

def analisis_nilai(nilai_list):
    nilai_tertinggi = max(nilai_list)
    nilai_terendah = min(nilai_list)
    rata_rata = sum(nilai_list) / len(nilai_list)
    return nilai_tertinggi, nilai_terendah, rata_rata

tertinggi, terendah, rata2 = analisis_nilai([88, 72, 95, 60, 81])
print(f"Tertinggi: {tertinggi}, Terendah: {terendah}, Rata-rata: {rata2:.2f}")

# Penjelasan:
# - Python bisa return LEBIH DARI 1 nilai sekaligus (dibungkus jadi tuple otomatis)
# - Saat dipanggil, tinggal unpacking sekaligus seperti tuple biasa (ingat BAB 3)


# ------------------------------------------------------
# CONTOH 3: FUNCTION MEMANGGIL FUNCTION LAIN
# ------------------------------------------------------

def hitung_denda(hari_terlambat):
    return hari_terlambat * 5000

def buat_laporan_denda(nama_peminjam, hari_terlambat):
    denda = hitung_denda(hari_terlambat)
    print(f"{nama_peminjam} terlambat {hari_terlambat} hari, denda: Rp{denda:,}")

buat_laporan_denda("Reffa", 3)

# Penjelasan:
# - Memecah masalah jadi fungsi-fungsi kecil (dekomposisi) bikin kode lebih rapi
# - hitung_denda() bisa dipakai ulang di tempat lain, tidak cuma di buat_laporan_denda()
# - Ini pola yang sudah kamu pakai tanpa sadar di project perpustakaan BAB 2


# ------------------------------------------------------
# CONTOH 4: DOCSTRING - DOKUMENTASI FUNGSI
# ------------------------------------------------------

def konversi_celsius_ke_fahrenheit(celsius):
    """
    Mengubah suhu dari Celsius ke Fahrenheit.
    Parameter: celsius (float/int)
    Return: suhu dalam Fahrenheit (float)
    """
    return (celsius * 9/5) + 32

print(konversi_celsius_ke_fahrenheit(30))
print(konversi_celsius_ke_fahrenheit.__doc__)   # cara baca docstring-nya

# Penjelasan:
# - Docstring ditulis pakai triple quote persis di bawah def
# - Fungsinya: dokumentasi buat orang lain (atau kamu sendiri 2 bulan kemudian)
# - Bisa diakses lewat .__doc__ atau help(nama_fungsi)


# ------------------------------------------------------
# CATATAN PENTING
# ------------------------------------------------------
# - Nama fungsi sebaiknya kata kerja (hitung_, buat_, cek_) biar jelas fungsinya ngapain
# - Fungsi idealnya ngerjain SATU tugas spesifik, bukan banyak hal sekaligus
# - Kalau fungsi kepanjangan (>20 baris), pertanyakan: bisa dipecah lagi tidak?