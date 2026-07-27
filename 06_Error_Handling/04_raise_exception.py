# ======================================================
# 04 RAISE EXCEPTION
# ======================================================
# raise adalah:
# Cara MEMUNCULKAN error secara SENGAJA, bukan menunggu Python
# yang munculin error-nya sendiri
#
# Digunakan ketika:
# - Kamu tahu suatu kondisi itu SALAH secara logika, walau bukan error
#   Python bawaan (misal: umur negatif, saldo minus)
#
# STRUKTUR DASAR:
# raise JenisError("pesan error")
# ======================================================


# ------------------------------------------------------
# CONTOH 1: raise SEDERHANA
# ------------------------------------------------------

umur = -5

if umur < 0:
    raise ValueError("Umur tidak boleh negatif!")

# Penjelasan:
# - raise langsung MENGHENTIKAN program (kecuali ditangkap try-except)
# - ValueError("pesan") -> pesan ini yang akan muncul di traceback error
# - Baris di bawah raise TIDAK akan pernah dijalankan


# ------------------------------------------------------
# CONTOH 2: raise DI DALAM FUNGSI UNTUK VALIDASI
# ------------------------------------------------------

def daftar_peserta(nama, umur):
    if umur < 0:
        raise ValueError("Umur tidak boleh negatif!")
    if nama.strip() == "":
        raise ValueError("Nama tidak boleh kosong!")
    print(f"{nama} ({umur} th) berhasil didaftarkan")

try:
    daftar_peserta("Reffa", 20)
    daftar_peserta("", 18)          # ini akan raise error
except ValueError as e:
    print(f"Gagal mendaftar: {e}")

# Penjelasan:
# - Fungsi yang raise error TIDAK harus punya try-except di dalamnya sendiri
# - Yang menangkap error itu adalah kode yang MEMANGGIL fungsi ini
# - Pola ini bikin validasi terpusat di 1 tempat (di dalam fungsi), dipakai
#   berkali-kali di mana saja fungsi ini dipanggil


# ------------------------------------------------------
# CONTOH 3: RE-RAISE - MELEMPAR ULANG ERROR SETELAH DITANGKAP
# ------------------------------------------------------

def proses_pembayaran(jumlah):
    try:
        if jumlah <= 0:
            raise ValueError("Jumlah pembayaran tidak valid")
        print(f"Membayar Rp{jumlah}")
    except ValueError as e:
        print(f"[LOG SISTEM] Error tercatat: {e}")
        raise   # <- raise TANPA argumen = lempar ulang error yang SAMA

try:
    proses_pembayaran(-1000)
except ValueError:
    print("Pembayaran dibatalkan oleh sistem utama.")

# Penjelasan:
# - `raise` tanpa argumen di dalam except = lempar ulang error yang SAMA
# - Berguna kalau kamu mau LOG dulu errornya, tapi tetap mau error itu
#   "naik" supaya bisa ditangani lagi di level yang lebih atas


# ------------------------------------------------------
# CONTOH 4: assert VS raise
# ------------------------------------------------------

def hitung_rata_rata(data):
    assert len(data) > 0, "Data tidak boleh kosong"   # cara singkat cek + raise
    return sum(data) / len(data)

print(hitung_rata_rata([80, 90, 70]))

try:
    print(hitung_rata_rata([]))
except AssertionError as e:
    print(f"Gagal hitung: {e}")

# Penjelasan:
# - assert kondisi, "pesan" = cara singkat untuk "kalau kondisi False, raise
#   AssertionError dengan pesan ini"
# - assert lebih cocok buat CEK INTERNAL / debugging saat development
# - raise ValueError/dst lebih cocok buat VALIDASI yang memang bagian dari
#   logika program (misal validasi input user)


# ------------------------------------------------------
# CATATAN PENTING
# ------------------------------------------------------
# - raise dipakai untuk error yang "logikanya salah", bukan cuma error Python
# - raise tanpa argumen di dalam except = lempar ulang error yang sama
# - assert cocok buat cek internal, raise cocok buat validasi ke user