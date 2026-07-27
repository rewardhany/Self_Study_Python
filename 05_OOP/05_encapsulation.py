# ======================================================
# 05 ENCAPSULATION
# ======================================================
# ENCAPSULATION adalah:
# Menyembunyikan/melindungi data internal object, supaya tidak diubah
# sembarangan dari luar
#
# Python tidak punya "private" beneran seperti bahasa lain, tapi punya KONVENSI:
# - nama_biasa    -> public, bebas diakses
# - _nama         -> protected (konvensi: "jangan diakses langsung dari luar")
# - __nama        -> private (name mangling, lebih susah diakses dari luar)
# ======================================================


# ------------------------------------------------------
# CONTOH 1: PUBLIC VS _PROTECTED (KONVENSI)
# ------------------------------------------------------

class Peserta:
    def __init__(self, nama, nim):
        self.nama = nama          # public -> bebas diakses/diubah dari luar
        self._nim = nim           # protected -> KONVENSI, sebaiknya jangan diakses langsung

peserta_1 = Peserta("Reffa", "2306xxxx")
print(peserta_1.nama)        # wajar, ini public
print(peserta_1._nim)        # BISA diakses, tapi ini melanggar konvensi

# Penjelasan:
# - _nim TETAP BISA diakses dari luar, underscore cuma "peringatan" buat programmer lain
# - Python percaya sama kedisiplinan programmer, bukan maksa pakai aturan ketat


# ------------------------------------------------------
# CONTOH 2: __PRIVATE (NAME MANGLING)
# ------------------------------------------------------

class RekeningHelpPay:
    def __init__(self, saldo_awal):
        self.__saldo = saldo_awal   # double underscore -> private

    def cek_saldo(self):
        return self.__saldo

rekening = RekeningHelpPay(50000)
print(rekening.cek_saldo())     # cara yang benar

# print(rekening.__saldo)       # <- kalau di-uncomment: ERROR, tidak bisa diakses langsung

# Penjelasan:
# - __saldo di belakang layar diubah namanya jadi _RekeningHelpPay__saldo
# - Ini bikin akses langsung dari luar jadi susah (bukan mustahil, tapi TIDAK DISARANKAN)
# - Cara resmi untuk baca/ubah nilainya: lewat method yang disediakan class (lihat CONTOH 3)


# ------------------------------------------------------
# CONTOH 3: GETTER & SETTER (METHOD UNTUK AKSES TERKONTROL)
# ------------------------------------------------------

class RekeningHelpPay:
    def __init__(self, saldo_awal):
        self.__saldo = saldo_awal

    def get_saldo(self):
        return self.__saldo

    def tambah_saldo(self, jumlah):
        if jumlah <= 0:
            print("Jumlah top up harus lebih dari 0!")
            return
        self.__saldo += jumlah

    def tarik_saldo(self, jumlah):
        if jumlah > self.__saldo:
            print("Saldo tidak cukup!")
            return
        self.__saldo -= jumlah

rekening = RekeningHelpPay(50000)
rekening.tambah_saldo(20000)
rekening.tarik_saldo(10000)
print(f"Saldo akhir: {rekening.get_saldo()}")

rekening.tambah_saldo(-5000)   # ditolak, sesuai validasi

# Penjelasan:
# - Daripada saldo bisa diubah sembarangan (rekening.saldo = -999999), method
#   tambah_saldo()/tarik_saldo() MEMASTIKAN perubahannya selalu valid
# - Ini alasan utama encapsulation: melindungi data dari perubahan yang tidak masuk akal


# ------------------------------------------------------
# CONTOH 4: @property (CARA PYTHON YANG LEBIH RAPI)
# ------------------------------------------------------

class RekeningHelpPay:
    def __init__(self, saldo_awal):
        self.__saldo = saldo_awal

    @property
    def saldo(self):              # bisa diakses seperti ATRIBUT biasa, bukan method
        return self.__saldo

    @saldo.setter
    def saldo(self, nilai_baru):
        if nilai_baru < 0:
            print("Saldo tidak boleh negatif!")
            return
        self.__saldo = nilai_baru

rekening = RekeningHelpPay(50000)
print(rekening.saldo)     # TANPA tanda kurung, tapi tetap lewat validasi
rekening.saldo = 70000    # ini juga lewat validasi di @saldo.setter
rekening.saldo = -100     # ditolak

# Penjelasan:
# - @property bikin method BISA diakses seperti atribut biasa (tanpa kurung)
# - @saldo.setter dipanggil otomatis saat ada yang nulis rekening.saldo = ...
# - Ini cara Python yang lebih "elegan" dibanding get_saldo()/set_saldo() manual


# ------------------------------------------------------
# CATATAN PENTING
# ------------------------------------------------------
# - Python tidak punya private yang BENAR-BENAR terkunci, semua berbasis konvensi
# - _protected = "tolong jangan diakses langsung", __private = lebih kuat tapi tetap bisa dibobol
# - Tujuan utama encapsulation BUKAN nyembunyiin data, tapi MELINDUNGI dari
#   perubahan yang tidak valid (saldo minus, umur negatif, dll)