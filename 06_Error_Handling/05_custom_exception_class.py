# ======================================================
# 05 CUSTOM EXCEPTION CLASS
# ======================================================
# CUSTOM EXCEPTION adalah:
# Jenis error buatan sendiri, dibuat dengan class yang mewarisi Exception
#
# Digunakan ketika:
# - Error bawaan Python (ValueError, dst) tidak cukup jelas menggambarkan
#   masalah SPESIFIK di project kamu
#
# STRUKTUR DASAR:
# class NamaErrorku(Exception):
#     pass
# ======================================================


# ------------------------------------------------------
# CONTOH 1: CUSTOM EXCEPTION PALING SEDERHANA
# ------------------------------------------------------

class SaldoTidakCukupError(Exception):
    pass

def tarik_saldo(saldo, jumlah):
    if jumlah > saldo:
        raise SaldoTidakCukupError("Saldo tidak mencukupi untuk penarikan ini")
    return saldo - jumlah

try:
    tarik_saldo(50000, 100000)
except SaldoTidakCukupError as e:
    print(f"Transaksi ditolak: {e}")

# Penjelasan:
# - class SaldoTidakCukupError(Exception) -> "warisi" semua perilaku dasar Exception
# - pass artinya tidak nambahin apa-apa, cukup KASIH NAMA yang jelas
# - Sekarang error-nya bernama SESUAI masalah aslinya, bukan generic ValueError


# ------------------------------------------------------
# CONTOH 2: MENANGKAP CUSTOM EXCEPTION SECARA SPESIFIK
# ------------------------------------------------------

class DivisiTidakDitemukanError(Exception):
    pass

data_panitia = {"Reffa": "Keamanan", "Galan": "Logistik"}

def cari_divisi(nama):
    if nama not in data_panitia:
        raise DivisiTidakDitemukanError(f"'{nama}' tidak terdaftar sebagai panitia")
    return data_panitia[nama]

try:
    print(cari_divisi("Sultan"))
except DivisiTidakDitemukanError as e:
    print(f"[ERROR] {e}")
except Exception as e:
    print(f"Error tak terduga: {e}")

# Penjelasan:
# - Custom exception bisa ditangkap SPESIFIK, terpisah dari error umum lain
# - Ini bikin kode pemanggil bisa kasih respons yang beda untuk masalah yang beda


# ------------------------------------------------------
# CONTOH 3: CUSTOM EXCEPTION DENGAN DATA TAMBAHAN
# ------------------------------------------------------

class DendaTerlaluBesarError(Exception):
    def __init__(self, jumlah_denda, batas_maksimal):
        self.jumlah_denda = jumlah_denda
        self.batas_maksimal = batas_maksimal
        pesan = f"Denda Rp{jumlah_denda} melebihi batas maksimal Rp{batas_maksimal}"
        super().__init__(pesan)   # tetap panggil __init__ Exception biar pesan errornya jalan normal

def hitung_denda(hari_telat, batas_maksimal=50000):
    denda = hari_telat * 5000
    if denda > batas_maksimal:
        raise DendaTerlaluBesarError(denda, batas_maksimal)
    return denda

try:
    hitung_denda(20)   # 20 hari * 5000 = 100000, melebihi batas default
except DendaTerlaluBesarError as e:
    print(f"[ERROR] {e}")
    print(f"Selisih dari batas: Rp{e.jumlah_denda - e.batas_maksimal}")

# Penjelasan:
# - Custom exception BOLEH punya __init__ sendiri, sama seperti class biasa (BAB 5)
# - super().__init__(pesan) memastikan pesan error tetap bisa dibaca lewat str(e)
# - Data tambahan (jumlah_denda, batas_maksimal) bisa DIAKSES lagi di except-nya,
#   ini yang tidak bisa dilakukan pakai Exception bawaan


# ------------------------------------------------------
# CONTOH 4: BEBERAPA CUSTOM EXCEPTION DALAM SATU SISTEM
# ------------------------------------------------------

class InputTidakValidError(Exception):
    pass

class StokHabisError(Exception):
    pass

def pinjam_buku(judul, stok_tersedia, jumlah_pinjam):
    if jumlah_pinjam <= 0:
        raise InputTidakValidError("Jumlah pinjam harus lebih dari 0")
    if jumlah_pinjam > stok_tersedia:
        raise StokHabisError(f"Stok '{judul}' tidak mencukupi")
    return stok_tersedia - jumlah_pinjam

try:
    sisa_stok = pinjam_buku("Laskar Pelangi", 2, 5)
except InputTidakValidError as e:
    print(f"[VALIDASI] {e}")
except StokHabisError as e:
    print(f"[STOK] {e}")

# Penjelasan:
# - Satu sistem boleh punya BANYAK custom exception, masing-masing untuk
#   masalah yang berbeda
# - Ini bikin sistem error jadi terbaca seperti "bahasa" project kamu sendiri,
#   bukan cuma ValueError generik di mana-mana


# ------------------------------------------------------
# CATATAN PENTING
# ------------------------------------------------------
# - Custom exception SELALU mewarisi Exception (langsung atau tidak langsung)
# - Beri nama yang jelas dan diakhiri "Error" sebagai konvensi
# - Baru buat custom exception kalau error bawaan Python memang tidak cukup
#   jelas menggambarkan masalahnya -> jangan bikin custom exception untuk
#   semua hal kalau ValueError biasa sudah cukup jelas