# ======================================================
# 04 INHERITANCE
# ======================================================
# INHERITANCE adalah:
# Class baru yang "mewarisi" atribut & method dari class lain
#
# Digunakan ketika:
# - Beberapa class punya kesamaan, tapi masing-masing juga punya hal spesifik
#
# STRUKTUR DASAR:
# class ClassAnak(ClassInduk):
#     kode tambahan
# ======================================================


# ------------------------------------------------------
# CONTOH 1: CLASS INDUK & CLASS ANAK SEDERHANA
# ------------------------------------------------------

class Orang:
    def __init__(self, nama):
        self.nama = nama

    def perkenalan(self):
        print(f"Halo, nama saya {self.nama}")

class Panitia(Orang):   # Panitia MEWARISI semua yang ada di Orang
    pass

panitia_1 = Panitia("Reffa")
panitia_1.perkenalan()   # method dari Orang, otomatis bisa dipakai Panitia

# Penjelasan:
# - class Panitia(Orang) artinya Panitia adalah "anak" dari Orang
# - Panitia otomatis punya __init__ dan perkenalan() dari Orang, tanpa nulis ulang
# - Ini mengurangi duplikasi kode kalau ada banyak class yang mirip-mirip


# ------------------------------------------------------
# CONTOH 2: OVERRIDE METHOD DI CLASS ANAK
# ------------------------------------------------------

class Panitia(Orang):
    def perkenalan(self):   # method dengan NAMA SAMA -> menimpa punya Orang
        print(f"Halo, saya {self.nama}, panitia acara ini")

panitia_1 = Panitia("Reffa")
panitia_1.perkenalan()   # sekarang pakai versi Panitia, bukan versi Orang

# Penjelasan:
# - Kalau class anak punya method dengan nama SAMA PERSIS, itu OVERRIDE
# - Python akan pakai versi milik class anak, versi induk "ditimpa"
# - Berguna kalau perilaku dasarnya sama tapi butuh sedikit penyesuaian


# ------------------------------------------------------
# CONTOH 3: super() - MEMANGGIL VERSI INDUK DARI DALAM ANAK
# ------------------------------------------------------

class Panitia(Orang):
    def __init__(self, nama, divisi):
        super().__init__(nama)   # panggil __init__ milik Orang dulu
        self.divisi = divisi     # baru tambahin yang spesifik ke Panitia

    def perkenalan(self):
        super().perkenalan()     # tetap pakai perkenalan versi Orang...
        print(f"...dan saya di divisi {self.divisi}")   # ...ditambah info baru

panitia_1 = Panitia("Reffa", "Keamanan")
panitia_1.perkenalan()

# Penjelasan:
# - super() = "panggil versi class induk", supaya tidak perlu nulis ulang kodenya
# - Sangat umum dipakai di __init__: setup dasar dari induk, baru tambahin yang khusus
# - Ini pola paling standar dan paling sering dipakai di inheritance


# ------------------------------------------------------
# CONTOH 4: BEBERAPA CLASS ANAK DARI INDUK YANG SAMA
# ------------------------------------------------------

class Peserta(Orang):
    def __init__(self, nama, sudah_bayar=False):
        super().__init__(nama)
        self.sudah_bayar = sudah_bayar

    def perkenalan(self):
        super().perkenalan()
        status = "sudah" if self.sudah_bayar else "belum"
        print(f"...saya peserta, {status} bayar")

daftar_orang = [
    Panitia("Reffa", "Keamanan"),
    Peserta("Galan", sudah_bayar=True)
]

for orang in daftar_orang:
    orang.perkenalan()
    print()

# Penjelasan:
# - Panitia dan Peserta SAMA-SAMA anak dari Orang, tapi masing-masing punya
#   perkenalan() versi sendiri
# - Loop di atas manggil perkenalan() yang SAMA NAMANYA, tapi hasilnya beda
#   tergantung object-nya -> ini bibit dari POLYMORPHISM (BAB 5 file 06)


# ------------------------------------------------------
# CATATAN PENTING
# ------------------------------------------------------
# - class Anak(Induk) -> Anak otomatis punya semua milik Induk
# - Override = bikin method nama sama di Anak untuk menimpa versi Induk
# - super() dipakai supaya tidak perlu nulis ulang kode dari Induk
# - Gunakan inheritance kalau ada relasi "Anak ITU SEBUAH Induk" (Panitia ITU
#   SEBUAH Orang) -> bukan cuma karena kebetulan mirip