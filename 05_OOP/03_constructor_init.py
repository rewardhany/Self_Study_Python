# ======================================================
# 03 CONSTRUCTOR (__init__)
# ======================================================
# __init__ adalah:
# Method spesial yang OTOMATIS jalan tiap kali object baru dibuat
#
# Digunakan untuk:
# - Langsung ngisi atribut object saat pertama kali dibuat
# - Tidak perlu manggil method set_data() terpisah kayak sebelumnya
#
# STRUKTUR DASAR:
# class NamaClass:
#     def __init__(self, parameter):
#         self.atribut = parameter
# ======================================================


# ------------------------------------------------------
# CONTOH 1: TANPA __init__ VS DENGAN __init__
# ------------------------------------------------------

# Cara lama (dari file sebelumnya, tanpa __init__):
class PesertaLama:
    def set_data(self, nama):
        self.nama = nama

peserta_lama = PesertaLama()
peserta_lama.set_data("Reffa")   # harus manggil method terpisah

# Cara baru (pakai __init__):
class Peserta:
    def __init__(self, nama):
        self.nama = nama

peserta_baru = Peserta("Reffa")   # langsung terisi saat object dibuat!

print(peserta_lama.nama)
print(peserta_baru.nama)

# Penjelasan:
# - __init__ otomatis jalan begitu Peserta("Reffa") dipanggil
# - Argumen yang dikirim ke Peserta(...) langsung masuk ke parameter __init__
# - Ini cara STANDAR di OOP Python, bukan pakai method set_data() terpisah


# ------------------------------------------------------
# CONTOH 2: __init__ DENGAN BEBERAPA PARAMETER + DEFAULT VALUE
# ------------------------------------------------------

class Peserta:
    def __init__(self, nama, divisi, sudah_bayar=False):
        self.nama = nama
        self.divisi = divisi
        self.sudah_bayar = sudah_bayar

    def status(self):
        return "LUNAS" if self.sudah_bayar else "BELUM LUNAS"

peserta_1 = Peserta("Reffa", "Keamanan")
peserta_2 = Peserta("Galan", "Logistik", sudah_bayar=True)

print(f"{peserta_1.nama}: {peserta_1.status()}")
print(f"{peserta_2.nama}: {peserta_2.status()}")

# Penjelasan:
# - __init__ bisa punya default value, sama seperti fungsi biasa (ingat BAB 4)
# - sudah_bayar=False jadi default kalau tidak diisi saat bikin object


# ------------------------------------------------------
# CONTOH 3: __init__ MEMANGGIL METHOD LAIN UNTUK SETUP AWAL
# ------------------------------------------------------

class Peserta:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
        self.kategori = self._tentukan_kategori()   # dihitung otomatis saat init

    def _tentukan_kategori(self):
        if self.umur < 18:
            return "Remaja"
        return "Dewasa"

peserta_1 = Peserta("Reffa", 20)
print(f"{peserta_1.nama} - Kategori: {peserta_1.kategori}")

# Penjelasan:
# - __init__ boleh manggil method lain di dalam class yang sama
# - _tentukan_kategori (pakai underscore di depan) = konvensi "method ini buat
#   internal aja", akan dibahas lebih detail di 05_encapsulation.py


# ------------------------------------------------------
# CONTOH 4: SETIAP OBJECT PUNYA DATA INIT SENDIRI-SENDIRI
# ------------------------------------------------------

daftar_peserta = [
    Peserta("Reffa", 20),
    Peserta("Galan", 17),
    Peserta("Bintang", 22)
]

for p in daftar_peserta:
    print(f"{p.nama} ({p.umur} th) - {p.kategori}")

# Penjelasan:
# - Tiap Peserta(...) di list punya __init__ yang jalan SENDIRI-SENDIRI
# - Data satu object tidak tercampur dengan object lain, walau dari class sama


# ------------------------------------------------------
# CATATAN PENTING
# ------------------------------------------------------
# - __init__ selalu punya self sebagai parameter pertama, sisanya bebas
# - __init__ TIDAK boleh punya `return nilai` (cuma boleh return None / tanpa return)
# - Ini method yang HAMPIR SELALU ada di setiap class yang kamu buat mulai sekarang