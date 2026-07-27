# ======================================================
# 06 POLYMORPHISM
# ======================================================
# POLYMORPHISM adalah:
# Method dengan NAMA SAMA, tapi PERILAKU BEDA tergantung object-nya
#
# "Poly" = banyak, "morph" = bentuk -> "banyak bentuk"
#
# Digunakan ketika:
# - Beberapa class punya method dengan tujuan sama, tapi cara kerjanya beda
# ======================================================


# ------------------------------------------------------
# CONTOH 1: METHOD SAMA, HASIL BEDA (LEWAT INHERITANCE)
# ------------------------------------------------------

class LaporanKegiatan:
    def buat_laporan(self):
        return "Laporan umum kegiatan"

class LaporanKeamanan(LaporanKegiatan):
    def buat_laporan(self):
        return "Laporan keamanan: notulensi rapat & tata tertib"

class LaporanLogistik(LaporanKegiatan):
    def buat_laporan(self):
        return "Laporan logistik: rekap inventaris & pengeluaran"

for laporan in [LaporanKegiatan(), LaporanKeamanan(), LaporanLogistik()]:
    print(laporan.buat_laporan())

# Penjelasan:
# - Ketiga class punya method buat_laporan() dengan NAMA SAMA
# - Tapi tiap class punya IMPLEMENTASI yang beda (ini override, dari BAB 5 file 04)
# - Loop di atas manggil method yang sama, hasilnya otomatis menyesuaikan object-nya


# ------------------------------------------------------
# CONTOH 2: FUNGSI YANG BEKERJA UNTUK "SEMUA JENIS" OBJECT
# ------------------------------------------------------

def cetak_semua_laporan(daftar_laporan):
    for laporan in daftar_laporan:
        print(f"-> {laporan.buat_laporan()}")

semua_laporan = [LaporanKeamanan(), LaporanLogistik(), LaporanKegiatan()]
cetak_semua_laporan(semua_laporan)

# Penjelasan:
# - cetak_semua_laporan() TIDAK PERLU tahu jenis object-nya spesifik apa
# - Yang penting, semua object di dalam list punya method buat_laporan()
# - Ini inti dari polymorphism: kode jadi lebih fleksibel, tidak perlu if/elif
#   buat tiap jenis object


# ------------------------------------------------------
# CONTOH 3: DUCK TYPING (TANPA HARUS SATU KELUARGA INHERITANCE)
# ------------------------------------------------------

class Musik:
    def putar(self):
        print("Memutar lagu...")

class Video:
    def putar(self):
        print("Memutar video...")

class Podcast:
    def putar(self):
        print("Memutar podcast...")

# Ketiga class ini TIDAK saling mewarisi, tapi sama-sama punya method putar()
daftar_konten = [Musik(), Video(), Podcast()]

for konten in daftar_konten:
    konten.putar()

# Penjelasan:
# - Musik, Video, Podcast SAMA SEKALI TIDAK berhubungan lewat inheritance
# - Tapi karena semuanya punya method putar(), kode di atas tetap jalan
# - Prinsip "duck typing": "kalau jalan seperti bebek dan bersuara seperti bebek,
#   anggap saja itu bebek" -> Python tidak peduli class aslinya apa, yang
#   penting method-nya ADA


# ------------------------------------------------------
# CONTOH 4: POLYMORPHISM DENGAN FUNGSI BAWAAN PYTHON
# ------------------------------------------------------

print(len("Reffa"))         # panjang string
print(len([1, 2, 3]))       # panjang list
print(len({"a": 1, "b": 2}))  # jumlah key dictionary

# Penjelasan:
# - len() adalah contoh polymorphism yang SUDAH kamu pakai dari BAB 1-3
# - Fungsi yang SAMA, tapi cara kerjanya menyesuaikan tipe data yang dikasih
# - Ini kenapa dunder method (__len__) di file berikutnya penting -> supaya
#   class buatanmu sendiri juga bisa dipakai dengan len()


# ------------------------------------------------------
# CATATAN PENTING
# ------------------------------------------------------
# - Polymorphism = method sama, hasil beda, tergantung object-nya
# - Tidak harus lewat inheritance -> duck typing juga valid selama method-nya ada
# - Manfaat utama: kode pemanggil (cetak_semua_laporan, dll) jadi tidak perlu
#   tahu detail tiap class, cukup tahu method apa yang tersedia