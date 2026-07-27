# ======================================================
# 06_truthy_and_falsy.py
# MATERI: TRUTHY AND FALSY
# ======================================================
#
# Di Python, setiap nilai bisa dievaluasi sebagai
# True atau False meski bukan nilai boolean murni.
#
# FALSY (dianggap False):
#   False, 0, 0.0, "", [], {}, (), None
#
# TRUTHY (dianggap True):
#   Semua nilai SELAIN yang di atas
#
# ======================================================


# ------------------------------------------------------
# 1. CEK NILAI DENGAN bool()
# ------------------------------------------------------
#
# Gunakan bool() untuk lihat apakah nilai truthy/falsy

print(bool(0))       # False
print(bool(""))      # False
print(bool([]))      # False
print(bool(None))    # False

print(bool(1))       # True
print(bool("halo"))  # True
print(bool([1, 2]))  # True


# ------------------------------------------------------
# 2. LANGSUNG DIPAKAI DI IF
# ------------------------------------------------------
#
# Python otomatis mengevaluasi nilai di kondisi if

nama = ""

if nama:
    print("Halo,", nama)
else:
    print("Nama tidak boleh kosong!")

# Output: Nama tidak boleh kosong!
# Karena "" adalah Falsy

nama = "Reffa"

if nama:
    print("Halo,", nama)

# Output: Halo, Reffa
# Karena "Reffa" adalah Truthy


# ------------------------------------------------------
# 3. CONTOH PRAKTIS
# ------------------------------------------------------

# Cek list kosong atau tidak
keranjang_belanja = []

if keranjang_belanja:
    print("Ada", len(keranjang_belanja), "item di keranjang")
else:
    print("Keranjang belanja masih kosong")

# Output: Keranjang belanja masih kosong

keranjang_belanja = ["Buku", "Pulpen"]

if keranjang_belanja:
    print("Ada", len(keranjang_belanja), "item di keranjang")

# Output: Ada 2 item di keranjang


# Cek angka nol
saldo = 0

if saldo:
    print("Saldo kamu:", saldo)
else:
    print("Saldo habis, segera isi ulang!")

# Output: Saldo habis, segera isi ulang!


# ------------------------------------------------------
# 4. NONE — NILAI KOSONG KHUSUS PYTHON
# ------------------------------------------------------
#
# None berarti "tidak ada nilai"
# Beda dengan 0 atau ""
#
# Biasanya hasil dari function yang tidak return apapun

def cari_data(nama):
    if nama == "Reffa":
        return "Data ditemukan"
    # Jika tidak ketemu, function otomatis return None

hasil = cari_data("Budi")

if hasil is None:
    print("Data tidak ditemukan")
else:
    print(hasil)

# Output: Data tidak ditemukan


# ======================================================
# LATIHAN
# ======================================================
#
# 1. Buat program yang minta input nama dari user.
#    Jika nama diisi → tampilkan "Selamat datang, [nama]"
#    Jika kosong (user langsung enter) → tampilkan "Nama wajib diisi!"
#
# 2. Buat list nilai ujian = [85, 90, 78]
#    Cek apakah list kosong atau ada isinya
#    Jika ada isi, tampilkan nilai pertama dan terakhir
#
# Tulis jawaban di sini: