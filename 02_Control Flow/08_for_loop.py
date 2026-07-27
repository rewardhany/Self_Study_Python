# ======================================================
# 08_for_loop.py
# MATERI: FOR LOOP
# ======================================================
#
# For loop = perulangan yang berjalan untuk setiap item
# dalam sebuah urutan (list, string, range, dll).
#
# Bedanya dengan while:
#
#   while → "ulangi SELAMA kondisi True"
#   for   → "ulangi UNTUK SETIAP item di dalam X"
#
# Bentuk:
#
#   for variabel in urutan:
#       kode yang diulang
#
# ======================================================


# ------------------------------------------------------
# 1. FOR LOOP DENGAN LIST
# ------------------------------------------------------

buah = ["apel", "mangga", "jeruk", "anggur"]

for item in buah:
    print("Buah:", item)

# Output:
# Buah: apel
# Buah: mangga
# Buah: jeruk
# Buah: anggur

# "item" adalah variabel sementara yang berisi
# setiap elemen list satu per satu secara otomatis


# ------------------------------------------------------
# 2. FOR LOOP DENGAN STRING
# ------------------------------------------------------
#
# String bisa di-loop juga, satu karakter per iterasi

kata = "Python"

for huruf in kata:
    print(huruf, end=" ")

# Output: P y t h o n
# end=" " artinya tidak ganti baris, tapi spasi


# ------------------------------------------------------
# 3. FOR LOOP DENGAN RANGE
# ------------------------------------------------------
#
# range() menghasilkan urutan angka
#
# range(5)       → 0, 1, 2, 3, 4
# range(1, 6)    → 1, 2, 3, 4, 5
# range(0, 10, 2)→ 0, 2, 4, 6, 8  (langkah 2)

print("\nAngka 0-4:")
for i in range(5):
    print(i, end=" ")

print("\nAngka 1-5:")
for i in range(1, 6):
    print(i, end=" ")

print("\nAngka genap 0-8:")
for i in range(0, 10, 2):
    print(i, end=" ")


# ------------------------------------------------------
# 4. AKUMULASI DENGAN FOR
# ------------------------------------------------------

nilai_ujian = [80, 90, 75, 85, 95]
total = 0

for nilai in nilai_ujian:
    total += nilai

rata_rata = total / len(nilai_ujian)
print("\n\nRata-rata nilai:", rata_rata)

# Output: Rata-rata nilai: 85.0


# ------------------------------------------------------
# 5. FOR DENGAN KONDISI (FILTER)
# ------------------------------------------------------

angka = [3, 7, 12, 5, 18, 9, 24]
print("\nAngka yang lebih dari 10:")

for n in angka:
    if n > 10:
        print(n, end=" ")

# Output: 12 18 24


# ------------------------------------------------------
# 6. NESTED FOR (FOR DI DALAM FOR)
# ------------------------------------------------------
#
# Dipakai untuk data dua dimensi atau kombinasi

print("\n\nTabel Perkalian 1-3:")

for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}", end="   ")
    print()   # ganti baris setelah setiap baris tabel

# Output:
# 1 x 1 = 1   1 x 2 = 2   1 x 3 = 3
# 2 x 1 = 2   2 x 2 = 4   2 x 3 = 6
# 3 x 1 = 3   3 x 2 = 6   3 x 3 = 9


# ======================================================
# LATIHAN
# ======================================================
#
# 1. Buat list nama teman kamu minimal 4 nama.
#    Loop dan tampilkan:
#    "No. 1 → Budi", "No. 2 → Sari", dst
#    (Petunjuk: pakai range(len(list)) atau enumerate)
#
# 2. Buat program yang mencetak semua bilangan
#    dari 1 sampai 50 yang habis dibagi 3.
#
# 3. Buat program yang menghitung berapa huruf vokal
#    (a, i, u, e, o) dalam sebuah kata.
#    Contoh: "mahasiswa" → 5 huruf vokal
#
# Tulis jawaban di sini: