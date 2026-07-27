# ======================================================
# 10_break_continue_pass.py
# MATERI: BREAK, CONTINUE, PASS
# ======================================================
#
# Tiga keyword ini digunakan untuk mengontrol
# jalannya loop.
#
#   break    → HENTIKAN loop sekarang
#   continue → LEWATI iterasi ini, lanjut ke berikutnya
#   pass     → TIDAK LAKUKAN APA-APA (placeholder)
#
# ======================================================


# ======================================================
# 1. BREAK — HENTIKAN LOOP
# ======================================================
#
# Loop langsung berhenti total saat break dieksekusi

print("=== BREAK ===")

for i in range(1, 10):
    if i == 5:
        print("Ketemu 5, loop berhenti!")
        break
    print(i, end=" ")

# Output: 1 2 3 4 Ketemu 5, loop berhenti!
# Angka 6, 7, 8, 9 tidak pernah diproses

print()

# Contoh praktis: cari data
mahasiswa = ["Andi", "Budi", "Cika", "Dani", "Eva"]
cari = "Cika"
ditemukan = False

for nama in mahasiswa:
    if nama == cari:
        ditemukan = True
        break   # tidak perlu lanjut, sudah ketemu

if ditemukan:
    print(f"{cari} ditemukan!")
else:
    print(f"{cari} tidak ada dalam daftar")

# Output: Cika ditemukan!


# ======================================================
# 2. CONTINUE — LEWATI ITERASI INI
# ======================================================
#
# Langsung loncat ke iterasi berikutnya
# tanpa menjalankan kode di bawah continue

print("\n=== CONTINUE ===")

# Tampilkan semua angka KECUALI yang habis dibagi 3
for i in range(1, 11):
    if i % 3 == 0:
        continue   # lewati, jangan print
    print(i, end=" ")

# Output: 1 2 4 5 7 8 10

print()

# Contoh praktis: filter nilai yang lulus saja
nilai = [45, 80, 55, 90, 30, 75, 60]
print("Nilai yang lulus (>= 70):")

for n in nilai:
    if n < 70:
        continue   # lewati yang tidak lulus
    print(n, end=" ")

# Output: 80 90 75

print()

# BEDANYA BREAK vs CONTINUE:
#
#   break    → langsung keluar dari loop seluruhnya
#   continue → skip iterasi ini, loop tetap jalan


# ======================================================
# 3. PASS — TIDAK LAKUKAN APA-APA
# ======================================================
#
# pass dipakai sebagai "placeholder" / "isi sementara"
# supaya kode tidak error saat blok masih kosong
#
# Python tidak boleh punya blok kosong:
#
#   if kondisi:       ← ERROR! blok kosong tidak boleh
#
#   if kondisi:       ← BENAR! ada pass sebagai isi
#       pass

print("\n=== PASS ===")

angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for n in angka:
    if n % 2 == 0:
        pass   # belum diimplementasi, nanti diisi
    else:
        print(f"{n} adalah bilangan ganjil")

# pass tidak melakukan apa-apa, loop tetap jalan normal

# Kegunaan lain: function yang belum selesai ditulis
def fitur_baru():
    pass   # nanti diisi, tapi dulu supaya tidak error


# ======================================================
# 4. BREAK DAN CONTINUE DI WHILE LOOP
# ======================================================
#
# Berlaku sama di while loop

print("\n=== Di WHILE LOOP ===")

# Break di while: berhenti saat menemukan angka negatif
angka_input = [5, 3, 8, -1, 4, 2]
index = 0

print("Proses angka:")
while index < len(angka_input):
    n = angka_input[index]
    if n < 0:
        print("Ditemukan angka negatif, berhenti!")
        break
    print(n, end=" ")
    index += 1

print()

# Continue di while: skip angka 0
data = [3, 0, 7, 0, 5, 0, 9]
index = 0
print("Angka bukan nol:")

while index < len(data):
    n = data[index]
    index += 1
    if n == 0:
        continue
    print(n, end=" ")


# ======================================================
# RINGKASAN
# ======================================================
#
#   break    → keluar dari loop sepenuhnya
#   continue → skip sisa iterasi, lanjut ke berikutnya
#   pass     → tidak melakukan apa-apa (placeholder)
#
#   break    → dipakai saat sudah dapat yang dicari
#   continue → dipakai saat ingin filter/skip kondisi tertentu
#   pass     → dipakai saat blok kode belum diisi


# ======================================================
# LATIHAN
# ======================================================
#
# 1. Gunakan FOR + BREAK:
#    Cari apakah angka 13 ada dalam list berikut.
#    Berhenti mencari begitu ketemu.
#    data = [4, 7, 2, 13, 9, 1, 13, 5]
#    Tampilkan di posisi index berapa angka 13 pertama ditemukan.
#
# 2. Gunakan FOR + CONTINUE:
#    Dari list nilai = [70, 45, 90, 30, 80, 55, 85, 40]
#    Hitung rata-rata HANYA untuk nilai yang >= 60
#
# 3. Gunakan WHILE + BREAK:
#    Buat program tebak kata sederhana.
#    Kata rahasianya = "python"
#    User boleh menebak terus sampai benar.
#    Jika benar, tampilkan berapa kali percobaan.
#
# Tulis jawaban di sini: