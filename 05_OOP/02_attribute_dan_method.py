# ======================================================
# 02 ATTRIBUTE & METHOD
# ======================================================
# ATTRIBUTE adalah:
# Data/variabel yang "menempel" pada object
#
# METHOD adalah:
# Fungsi yang "menempel" pada class, dipanggil lewat object
#
# STRUKTUR DASAR:
# class NamaClass:
#     def nama_method(self, parameter):
#         kode
# ======================================================


# ------------------------------------------------------
# CONTOH 1: METHOD SEDERHANA DENGAN self
# ------------------------------------------------------

class Peserta:
    def sapa(self):
        print("Halo, saya peserta ODWH!")

peserta_1 = Peserta()
peserta_1.sapa()

# Penjelasan:
# - self WAJIB jadi parameter pertama tiap method -> merujuk ke OBJECT itu sendiri
# - Kamu tidak perlu isi self secara manual, Python otomatis ngirim object-nya
# - peserta_1.sapa() sebenarnya = Peserta.sapa(peserta_1) di belakang layar


# ------------------------------------------------------
# CONTOH 2: METHOD YANG MENGAKSES ATRIBUT LEWAT self
# ------------------------------------------------------

class Peserta:
    def set_data(self, nama, divisi):
        self.nama = nama         # nempelin atribut ke object ini
        self.divisi = divisi

    def tampilkan_profil(self):
        print(f"{self.nama} - Divisi {self.divisi}")

peserta_1 = Peserta()
peserta_1.set_data("Reffa", "Keamanan")
peserta_1.tampilkan_profil()

# Penjelasan:
# - self.nama = nama -> nyimpen nilai ke ATRIBUT milik object ini
# - self.nama di method lain (tampilkan_profil) bisa BACA atribut yang sama
# - self adalah "jembatan" supaya semua method dalam 1 object bisa saling akses data


# ------------------------------------------------------
# CONTOH 3: ATTRIBUTE MILIK OBJECT VS ATTRIBUTE MILIK CLASS
# ------------------------------------------------------

class Peserta:
    nama_event = "ODWH 2026"    # CLASS attribute -> sama untuk SEMUA object

    def set_nama(self, nama):
        self.nama = nama          # INSTANCE attribute -> beda untuk tiap object

peserta_1 = Peserta()
peserta_2 = Peserta()
peserta_1.set_nama("Reffa")
peserta_2.set_nama("Galan")

print(f"{peserta_1.nama} ikut {peserta_1.nama_event}")
print(f"{peserta_2.nama} ikut {peserta_2.nama_event}")

# Penjelasan:
# - nama_event ditulis LANGSUNG di dalam class (bukan di dalam method) -> class attribute
# - self.nama ditulis DI DALAM method -> instance attribute, beda tiap object
# - Class attribute dipakai bareng-bareng semua object, instance attribute punya masing-masing


# ------------------------------------------------------
# CONTOH 4: JEBAKAN MENGUBAH CLASS ATTRIBUTE LEWAT OBJECT
# ------------------------------------------------------

peserta_1.nama_event = "ODWH 2027"   # ini bikin INSTANCE attribute BARU di peserta_1 saja!

print(peserta_1.nama_event)   # ODWH 2027 (cuma punya peserta_1)
print(peserta_2.nama_event)   # ODWH 2026 (class attribute aslinya tetap utuh)

# Penjelasan:
# - peserta_1.nama_event = "..." TIDAK mengubah class attribute aslinya
# - Ini malah bikin instance attribute baru yang "menutupi" class attribute, HANYA di peserta_1
# - Kalau memang mau ubah punya SEMUA object, harus lewat nama class-nya:
#   Peserta.nama_event = "ODWH 2027"


# ------------------------------------------------------
# CATATAN PENTING
# ------------------------------------------------------
# - self selalu jadi parameter pertama method (Python isi otomatis)
# - Instance attribute (self.xxx) beda-beda tiap object
# - Class attribute (ditulis langsung di class) dipakai bareng semua object,
#   HATI-HATI ubahnya lewat nama class, bukan lewat object