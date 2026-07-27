# ======================================================
# 08 CLASS METHOD & STATIC METHOD
# ======================================================
# Ada 3 jenis method di dalam class:
# - INSTANCE method  -> pakai self, butuh object dulu (yang paling sering dipakai)
# - CLASS method     -> pakai cls, berhubungan sama CLASS-nya, bukan object tertentu
# - STATIC method    -> tidak pakai self/cls, cuma "numpang" di dalam class
# ======================================================


# ------------------------------------------------------
# CONTOH 1: INSTANCE METHOD (REVIEW)
# ------------------------------------------------------

class Peserta:
    def __init__(self, nama):
        self.nama = nama

    def sapa(self):              # instance method -> butuh self
        print(f"Halo, saya {self.nama}")

peserta_1 = Peserta("Reffa")
peserta_1.sapa()   # harus lewat OBJECT dulu

# Penjelasan:
# - Ini jenis method yang paling sering kamu tulis dari BAB 5 file 01-07
# - Wajib ada object dulu (peserta_1) baru bisa dipanggil


# ------------------------------------------------------
# CONTOH 2: STATIC METHOD - UTILITY, TIDAK BUTUH DATA OBJECT
# ------------------------------------------------------

class Validasi:
    @staticmethod
    def nama_valid(nama):
        return len(nama.strip()) > 0

print(Validasi.nama_valid("Reffa"))    # True
print(Validasi.nama_valid("   "))      # False

# Penjelasan:
# - @staticmethod TIDAK punya self ATAU cls -> tidak butuh object maupun class-nya
# - Bisa dipanggil LANGSUNG dari nama class, tanpa bikin object dulu
# - Cocok buat fungsi "utility" yang secara logis nyambung sama class ini,
#   tapi tidak butuh data spesifik dari object manapun


# ------------------------------------------------------
# CONTOH 3: CLASS METHOD - ALTERNATIVE CONSTRUCTOR
# ------------------------------------------------------

class Peserta:
    def __init__(self, nama, divisi):
        self.nama = nama
        self.divisi = divisi

    @classmethod
    def dari_string(cls, data_string):
        # data_string formatnya: "nama,divisi"
        nama, divisi = data_string.split(",")
        return cls(nama.strip(), divisi.strip())   # cls(...) = manggil __init__

peserta_1 = Peserta("Reffa", "Keamanan")               # cara biasa
peserta_2 = Peserta.dari_string("Galan, Logistik")     # cara alternatif, dari 1 string

print(f"{peserta_1.nama} - {peserta_1.divisi}")
print(f"{peserta_2.nama} - {peserta_2.divisi}")

# Penjelasan:
# - @classmethod pakai cls (merujuk ke CLASS-nya), bukan self (merujuk ke object)
# - cls(...) di dalam classmethod = cara lain untuk bikin object baru
# - Berguna kalau kamu butuh CARA BEDA untuk bikin object dari sumber data
#   yang formatnya beda-beda (misal dari CSV, dari API, dst)


# ------------------------------------------------------
# CONTOH 4: KETIGANYA DALAM SATU CLASS
# ------------------------------------------------------

class Denda:
    tarif_per_hari = 5000   # class attribute

    def __init__(self, nama_peminjam, hari_telat):
        self.nama_peminjam = nama_peminjam
        self.hari_telat = hari_telat

    def hitung(self):                          # instance method
        return self.hari_telat * Denda.tarif_per_hari

    @classmethod
    def ubah_tarif(cls, tarif_baru):            # class method
        cls.tarif_per_hari = tarif_baru

    @staticmethod
    def format_rupiah(angka):                   # static method
        return f"Rp{angka:,}"

denda_1 = Denda("Reffa", 3)
print(Denda.format_rupiah(denda_1.hitung()))

Denda.ubah_tarif(7000)   # ubah tarif untuk SEMUA object ke depannya
denda_2 = Denda("Galan", 3)
print(Denda.format_rupiah(denda_2.hitung()))

# Penjelasan:
# - hitung()        -> butuh data spesifik dari object (self.hari_telat) -> instance method
# - ubah_tarif()     -> mengubah sesuatu di level CLASS, bukan object tertentu -> classmethod
# - format_rupiah()  -> tidak butuh data object ATAU class, cuma numpang -> staticmethod


# ------------------------------------------------------
# CATATAN PENTING
# ------------------------------------------------------
# - Bingung pilih yang mana? Tanya: "Ini butuh data OBJECT tertentu?" -> instance
#   "Ini butuh ubah/pakai data CLASS-nya sendiri?" -> classmethod
#   "Ini tidak butuh data object maupun class sama sekali?" -> staticmethod
# - 90% method yang kamu tulis akan jadi instance method -> dua lainnya dipakai
#   secukupnya saja, tidak perlu dipaksakan