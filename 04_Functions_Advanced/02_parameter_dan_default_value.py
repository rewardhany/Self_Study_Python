# ======================================================
# 02 PARAMETER & DEFAULT VALUE
# ======================================================
# DEFAULT VALUE adalah:
# Nilai otomatis yang dipakai parameter KALAU tidak diisi saat pemanggilan
#
# STRUKTUR DASAR:
# def nama_fungsi(parameter=nilai_default):
#     kode
# ======================================================


# ------------------------------------------------------
# CONTOH 1: PARAMETER WAJIB VS DEFAULT VALUE
# ------------------------------------------------------

def sapa_panitia(nama, divisi="Belum ditentukan"):
    print(f"Halo {nama}, kamu di divisi {divisi}")

sapa_panitia("Reffa", "Keamanan")   # divisi diisi
sapa_panitia("Galan")               # divisi pakai default

# Penjelasan:
# - nama = parameter WAJIB, harus selalu diisi
# - divisi = punya default value, boleh tidak diisi
# - Parameter yang punya default HARUS ditulis SETELAH parameter wajib


# ------------------------------------------------------
# CONTOH 2: POSITIONAL VS KEYWORD ARGUMENT
# ------------------------------------------------------

def buat_profil(nama, umur, jurusan):
    print(f"{nama} ({umur} th) - {jurusan}")

buat_profil("Reffa", 20, "Teknik Komputer")             # positional -> urutan penting
buat_profil(nama="Reffa", jurusan="Teknik Komputer", umur=20)   # keyword -> urutan bebas

# Penjelasan:
# - Positional argument: urutan penulisan MENENTUKAN parameter mana yang diisi
# - Keyword argument: sebut nama parameternya langsung, urutan jadi bebas
# - Keyword argument bikin pemanggilan fungsi lebih jelas dibaca, terutama kalau parameternya banyak


# ------------------------------------------------------
# CONTOH 3: JEBAKAN DEFAULT VALUE YANG MUTABLE
# ------------------------------------------------------

# SALAH (jangan ditiru):
def tambah_barang_salah(barang, daftar=[]):
    daftar.append(barang)
    return daftar

print(tambah_barang_salah("Laptop"))
print(tambah_barang_salah("Kabel"))   # <- daftar sebelumnya IKUT KEBAWA, bukan list baru!

# BENAR:
def tambah_barang_benar(barang, daftar=None):
    if daftar is None:
        daftar = []
    daftar.append(barang)
    return daftar

print(tambah_barang_benar("Laptop"))
print(tambah_barang_benar("Kabel"))   # sekarang list baru tiap dipanggil

# Penjelasan:
# - Default value list/dict itu HANYA DIBUAT SEKALI, bukan tiap fungsi dipanggil
# - Ini bug klasik Python yang sering bikin bingung pemula
# - Solusi standar: default-nya None, baru dibuat list baru DI DALAM fungsi


# ------------------------------------------------------
# CONTOH 4: KOMBINASI POSITIONAL + KEYWORD + DEFAULT
# ------------------------------------------------------

def daftar_peserta(nama, acara, sudah_bayar=False, catatan="-"):
    status = "LUNAS" if sudah_bayar else "BELUM LUNAS"
    print(f"{nama} - {acara} - {status} - Catatan: {catatan}")

daftar_peserta("Reffa", "ODWH 2026")
daftar_peserta("Galan", "ODWH 2026", sudah_bayar=True)
daftar_peserta("Bintang", "ODWH 2026", sudah_bayar=True, catatan="Bayar cash")

# Penjelasan:
# - nama & acara wajib diisi (positional)
# - sudah_bayar & catatan opsional, dipanggil pakai keyword biar jelas maksudnya


# ------------------------------------------------------
# CATATAN PENTING
# ------------------------------------------------------
# - Parameter dengan default HARUS di posisi setelah parameter wajib
# - JANGAN pakai list/dict kosong sebagai default value langsung -> pakai None + cek di dalam
# - Keyword argument bikin kode lebih gampang dibaca, apalagi kalau parameternya > 3