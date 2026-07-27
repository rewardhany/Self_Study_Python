# ======================================================
# 03 FINALLY & ELSE
# ======================================================
# else  -> jalan HANYA KALAU try berhasil, TANPA error sama sekali
# finally -> SELALU jalan, entah ada error atau tidak
#
# STRUKTUR DASAR:
# try:
#     kode
# except ErrorTertentu:
#     kode kalau error
# else:
#     kode kalau TIDAK ada error
# finally:
#     kode yang SELALU jalan
# ======================================================


# ------------------------------------------------------
# CONTOH 1: finally SELALU JALAN
# ------------------------------------------------------

try:
    angka = int(input("Masukkan angka: "))
    print(f"Hasil: {100 / angka}")
except ZeroDivisionError:
    print("Tidak bisa dibagi 0!")
finally:
    print("Proses selesai dijalankan.")   # ini SELALU muncul, error atau tidak

# Penjelasan:
# - finally jalan APAPUN yang terjadi -> ada error, tidak ada error, tetap jalan
# - Cocok buat kode yang HARUS dijalankan (misal: tutup file, tutup koneksi)


# ------------------------------------------------------
# CONTOH 2: else - JALAN HANYA KALAU TIDAK ADA ERROR
# ------------------------------------------------------

try:
    angka = int(input("Masukkan angka: "))
except ValueError:
    print("Input tidak valid!")
else:
    print(f"Input diterima: {angka}")   # cuma jalan kalau try SUKSES

# Penjelasan:
# - else BEDA sama kode yang ditulis langsung setelah try-except
# - else khusus jalan kalau try-nya SUKSES TOTAL, tanpa exception apapun
# - Manfaatnya: misahin dengan jelas "kode yang boleh error" (di try) dari
#   "kode lanjutan yang cuma boleh jalan kalau aman" (di else)


# ------------------------------------------------------
# CONTOH 3: KOMBINASI try-except-else-finally LENGKAP
# ------------------------------------------------------

try:
    angka1 = int(input("Angka pertama: "))
    angka2 = int(input("Angka kedua: "))
    hasil = angka1 / angka2
except ValueError:
    print("Input harus angka!")
except ZeroDivisionError:
    print("Tidak bisa dibagi 0!")
else:
    print(f"Hasil pembagian: {hasil}")
finally:
    print("=== Proses perhitungan selesai ===")

# Penjelasan:
# - Urutan eksekusi: try -> (kalau error) except -> finally
#                    try -> (kalau sukses) else -> finally
# - finally SELALU jadi yang terakhir, apapun jalur yang diambil sebelumnya


# ------------------------------------------------------
# CONTOH 4: PRAKTIK NYATA - MENUTUP RESOURCE DI finally
# ------------------------------------------------------

daftar_denda_sementara = []

try:
    hari_telat = int(input("Hari telat: "))
    denda = hari_telat * 5000
    daftar_denda_sementara.append(denda)
    print(f"Denda dihitung: Rp{denda}")
except ValueError:
    print("Input harus angka!")
finally:
    print(f"Total transaksi tercatat sementara: {len(daftar_denda_sementara)}")
    # bayangkan ini semacam 'menutup sesi pencatatan', harus selalu jalan

# Penjelasan:
# - finally cocok buat hal-hal yang "harus beres" tidak peduli hasil di atasnya
# - Nanti di BAB 7 (File I/O), pola ini penting banget buat pastikan file
#   selalu ditutup meskipun terjadi error saat membacanya


# ------------------------------------------------------
# CATATAN PENTING
# ------------------------------------------------------
# - else = "kalau try-nya SUKSES total"
# - finally = "APAPUN yang terjadi, selalu jalan di akhir"
# - Tidak wajib pakai else/finally setiap saat, pakai kalau memang butuh
#   pemisahan yang jelas