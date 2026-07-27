# ======================================================
# 05_logical_conditions.py
# MATERI: LOGICAL CONDITIONS (AND, OR, NOT)
# ======================================================
#
# Logical operator digunakan untuk menggabungkan
# atau membalik kondisi boolean.
#
# Ada 3 operator logika:
#
#   and  →  semua kondisi harus True
#   or   →  cukup satu kondisi True
#   not  →  membalik nilai (True jadi False, sebaliknya)
#
# ======================================================


# ------------------------------------------------------
# 1. OPERATOR AND
# ------------------------------------------------------
#
# Hasil True hanya jika SEMUA kondisi True
#
# True  and True  → True
# True  and False → False
# False and True  → False
# False and False → False

umur = 20
punya_ktp = True

if umur >= 17 and punya_ktp:
    print("Boleh membuat SIM")
else:
    print("Tidak memenuhi syarat")

# Output: Boleh membuat SIM
# Karena umur >= 17 (True) AND punya_ktp (True) → True


# ------------------------------------------------------
# 2. OPERATOR OR
# ------------------------------------------------------
#
# Hasil True jika MINIMAL SATU kondisi True
#
# True  or True  → True
# True  or False → True
# False or True  → True
# False or False → False

punya_kartu_mahasiswa = False
punya_kartu_pelajar   = True

if punya_kartu_mahasiswa or punya_kartu_pelajar:
    print("Dapat diskon tiket")
else:
    print("Tidak dapat diskon")

# Output: Dapat diskon tiket
# Karena salah satu True


# ------------------------------------------------------
# 3. OPERATOR NOT
# ------------------------------------------------------
#
# Membalik nilai boolean
#
# not True  → False
# not False → True

sudah_login = False

if not sudah_login:
    print("Silakan login terlebih dahulu")

# Output: Silakan login terlebih dahulu
# not False → True, jadi if-nya masuk


# ------------------------------------------------------
# 4. KOMBINASI AND, OR, NOT
# ------------------------------------------------------
#
# Bisa dikombinasikan, tapi pakai kurung () agar jelas

nilai    = 75
kehadiran = 80

lulus = nilai >= 70 and kehadiran >= 75

if lulus:
    print("Lulus mata kuliah")
else:
    print("Tidak lulus")

# Contoh kombinasi lebih kompleks:
admin    = False
moderator = True

if admin or (moderator and not False):
    print("Punya akses dashboard")


# ======================================================
# LATIHAN
# ======================================================
#
# 1. Buat program cek kelayakan kredit:
#    Syarat: penghasilan >= 3000000 AND umur >= 21
#    Gunakan input() untuk ambil data dari user
#
# 2. Buat program cek tiket konser:
#    Gratis masuk jika: punya_undangan OR (member AND bayar_tiket)
#    Coba dengan kombinasi True/False yang berbeda
#
# Tulis jawaban di sini: