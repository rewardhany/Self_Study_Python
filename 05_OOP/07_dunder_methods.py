# ======================================================
# 07 DUNDER METHODS
# ======================================================
# DUNDER (Double UNDERscore) METHODS adalah:
# Method spesial Python yang namanya diapit __ (misal __init__, __str__)
#
# Digunakan untuk:
# - Bikin object buatanmu bisa "berperilaku" seperti tipe data bawaan Python
#   (bisa di-print rapi, dibandingkan, dihitung panjangnya, dll)
# ======================================================


# ------------------------------------------------------
# CONTOH 1: __str__ - TAMPILAN SAAT DI-PRINT
# ------------------------------------------------------

class Peserta:
    def __init__(self, nama, divisi):
        self.nama = nama
        self.divisi = divisi

peserta_1 = Peserta("Reffa", "Keamanan")
print(peserta_1)   # <- tanpa __str__, hasilnya alamat memori yang tidak jelas

class PesertaRapi:
    def __init__(self, nama, divisi):
        self.nama = nama
        self.divisi = divisi

    def __str__(self):
        return f"Peserta({self.nama}, divisi={self.divisi})"

peserta_2 = PesertaRapi("Galan", "Logistik")
print(peserta_2)   # sekarang tampilannya jelas

# Penjelasan:
# - Tanpa __str__, print(object) nampilin sesuatu kayak <__main__.Peserta object at 0x...>
# - __str__ dipanggil OTOMATIS setiap kali object di-print() atau di str()
# - Ini dunder method yang paling sering dipakai


# ------------------------------------------------------
# CONTOH 2: __len__ - SUPAYA BISA DIPAKAI len()
# ------------------------------------------------------

class Antrian:
    def __init__(self):
        self.daftar = []

    def tambah(self, nama):
        self.daftar.append(nama)

    def __len__(self):
        return len(self.daftar)

antrian = Antrian()
antrian.tambah("Reffa")
antrian.tambah("Galan")

print(len(antrian))   # bisa langsung dipakai len(), karena ada __len__

# Penjelasan:
# - __len__ dipanggil otomatis saat len(object) ditulis
# - Ini contoh nyata dari polymorphism di file sebelumnya: len() bekerja
#   untuk string, list, dict, DAN sekarang class buatanmu sendiri


# ------------------------------------------------------
# CONTOH 3: __eq__ - MEMBANDINGKAN DUA OBJECT
# ------------------------------------------------------

class Peserta:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim

    def __eq__(self, lainnya):
        return self.nim == lainnya.nim   # dianggap "sama" kalau NIM sama

peserta_a = Peserta("Reffa", "2306001")
peserta_b = Peserta("Reffa F.", "2306001")   # nama beda dikit, NIM sama
peserta_c = Peserta("Galan", "2306002")

print(peserta_a == peserta_b)   # True, karena NIM sama
print(peserta_a == peserta_c)   # False

# Penjelasan:
# - Tanpa __eq__, Python bandingin object berdasarkan "apakah ini object yang
#   PERSIS SAMA di memori", bukan berdasarkan isinya
# - __eq__ bikin kamu yang nentuin sendiri apa artinya "sama" untuk class ini


# ------------------------------------------------------
# CONTOH 4: __repr__ VS __str__
# ------------------------------------------------------

class Peserta:
    def __init__(self, nama):
        self.nama = nama

    def __str__(self):
        return f"Peserta bernama {self.nama}"          # buat manusia baca (print)

    def __repr__(self):
        return f"Peserta(nama='{self.nama}')"           # buat developer/debugging

peserta_1 = Peserta("Reffa")
print(peserta_1)          # pakai __str__
print([peserta_1])        # list of object pakai __repr__, bukan __str__

# Penjelasan:
# - __str__ = versi "ramah manusia", dipakai print()
# - __repr__ = versi "teknis", dipakai saat object ditaruh di dalam list/dict,
#   atau dipanggil langsung lewat repr(object)
# - Kalau cuma sempat bikin salah satu, prioritaskan __str__ dulu


# ------------------------------------------------------
# CATATAN PENTING
# ------------------------------------------------------
# - Dunder method TIDAK dipanggil manual (jarang nulis object.__str__()) -
#   dia jalan OTOMATIS lewat print(), len(), ==, dst
# - Tidak semua class butuh semua dunder method, tambahkan yang relevan saja
# - __init__ (BAB 5 file 03) sebenarnya juga dunder method - kamu sudah pakai
#   dari awal tanpa sadar