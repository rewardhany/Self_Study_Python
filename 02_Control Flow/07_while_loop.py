# ======================================================
# 07_while_loop.py
# MATERI: WHILE LOOP
# ======================================================
#
# While loop = perulangan yang terus berjalan
# SELAMA kondisi masih True.
#
# Bentuk:
#
#   while kondisi:
#       kode yang diulang
#
# INGAT: Kamu harus pastikan kondisi bisa jadi False,
#        kalau tidak → infinite loop (loop tak berakhir)!
#
# ======================================================


# ------------------------------------------------------
# 1. WHILE LOOP DASAR
# ------------------------------------------------------

hitung = 1

while hitung <= 5:
    print("Hitungan:", hitung)
    hitung += 1        # hitung = hitung + 1

# Output:
# Hitungan: 1
# Hitungan: 2
# Hitungan: 3
# Hitungan: 4
# Hitungan: 5

# Yang terjadi step-by-step:
#
#   hitung = 1 → 1 <= 5? Ya → print → hitung = 2
#   hitung = 2 → 2 <= 5? Ya → print → hitung = 3
#   hitung = 3 → 3 <= 5? Ya → print → hitung = 4
#   hitung = 4 → 4 <= 5? Ya → print → hitung = 5
#   hitung = 5 → 5 <= 5? Ya → print → hitung = 6
#   hitung = 6 → 6 <= 5? TIDAK → loop berhenti


# ------------------------------------------------------
# 2. WHILE DENGAN INPUT USER
# ------------------------------------------------------
#
# Cocok untuk menu yang terus muncul sampai user keluar

print("\n--- Tebak Angka ---")
angka_rahasia = 7
tebakan = 0

while tebakan != angka_rahasia:
    tebakan = int(input("Tebak angka (1-10): "))
    if tebakan < angka_rahasia:
        print("Terlalu kecil!")
    elif tebakan > angka_rahasia:
        print("Terlalu besar!")

print("Benar! Angka rahasianya adalah", angka_rahasia)


# ------------------------------------------------------
# 3. WHILE TRUE + BREAK
# ------------------------------------------------------
#
# Pola umum untuk menu aplikasi:
# Loop jalan terus, baru berhenti kalau user ketik "keluar"

print("\n--- Menu Sederhana ---")

while True:
    pilihan = input("Ketik sesuatu (atau 'keluar' untuk berhenti): ")

    if pilihan == "keluar":
        print("Sampai jumpa!")
        break                  # keluar dari loop

    print("Kamu mengetik:", pilihan)


# ------------------------------------------------------
# 4. CONTOH AKUMULASI
# ------------------------------------------------------
#
# Hitung total belanja sampai user selesai

total  = 0
jumlah = 0

print("\n--- Input Belanja ---")

while True:
    harga = input("Masukkan harga item (atau 'selesai'): ")

    if harga == "selesai":
        break

    total  += int(harga)
    jumlah += 1

print(f"Total {jumlah} item: Rp{total:,}")


# ======================================================
# LATIHAN
# ======================================================
#
# 1. Buat program hitung mundur dari 10 ke 0
#    menggunakan while loop
#    Output: 10, 9, 8, ..., 1, 0, "Selesai!"
#
# 2. Buat program yang terus minta input angka dari user.
#    Loop berhenti jika user memasukkan angka negatif.
#    Di akhir, tampilkan jumlah total semua angka yang dimasukkan.
#
# Tulis jawaban di sini: