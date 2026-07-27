# ======================================================
# 02 MULTIPLE EXCEPTIONS
# ======================================================
# Satu blok try bisa punya BEBERAPA except, untuk jenis error yang berbeda
#
# STRUKTUR DASAR:
# try:
#     kode
# except JenisError1:
#     kode
# except JenisError2:
#     kode
# ======================================================


# ------------------------------------------------------
# CONTOH 1: BEBERAPA except UNTUK ERROR BERBEDA
# ------------------------------------------------------

try:
    angka1 = int(input("Angka pertama: "))
    angka2 = int(input("Angka kedua: "))
    hasil = angka1 / angka2
    print(f"Hasil: {hasil}")
except ValueError:
    print("Input harus berupa angka!")
except ZeroDivisionError:
    print("Tidak bisa membagi dengan 0!")

# Penjelasan:
# - Python cek except SATU PER SATU dari atas, berhenti di yang cocok
# - ValueError -> kalau input bukan angka
# - ZeroDivisionError -> kalau angka2 = 0
# - Masing-masing dapat pesan yang SESUAI dengan masalahnya, bukan pesan generik


# ------------------------------------------------------
# CONTOH 2: MENANGKAP BEBERAPA ERROR SEKALIGUS DI 1 except
# ------------------------------------------------------

try:
    data = [1, 2, 3]
    index = int(input("Masukkan index: "))
    print(data[index])
except (ValueError, IndexError):
    print("Input tidak valid atau index di luar jangkauan!")

# Penjelasan:
# - except (ErrorA, ErrorB): menangkap DUA jenis error dalam satu blok
# - Dipakai kalau responsnya SAMA untuk beberapa jenis error
# - IndexError terjadi kalau index yang diminta tidak ada di list


# ------------------------------------------------------
# CONTOH 3: URUTAN except PENTING (SPESIFIK DULU, UMUM BELAKANGAN)
# ------------------------------------------------------

try:
    angka = int(input("Masukkan angka: "))
    hasil = 100 / angka
except ZeroDivisionError:            # spesifik -> dicek duluan
    print("Tidak bisa dibagi 0!")
except Exception as e:               # umum -> fallback kalau bukan yang di atas
    print(f"Terjadi error lain: {e}")

# Penjelasan:
# - Exception adalah "induk" dari HAMPIR SEMUA jenis error di Python
# - Kalau Exception ditulis PALING ATAS, dia akan "menangkap duluan" semua
#   error, bikin except yang lebih spesifik di bawahnya TIDAK PERNAH kepakai
# - Aturan: dari yang PALING SPESIFIK ke yang PALING UMUM


# ------------------------------------------------------
# CONTOH 4: VALIDASI INPUT LENGKAP (BEBERAPA KEMUNGKINAN ERROR)
# ------------------------------------------------------

daftar_peserta = ["Reffa", "Galan", "Bintang"]

while True:
    try:
        index = int(input(f"Pilih index (0-{len(daftar_peserta)-1}): "))
        nama_terpilih = daftar_peserta[index]
        print(f"Terpilih: {nama_terpilih}")
        break
    except ValueError:
        print("Harus masukkan angka!")
    except IndexError:
        print("Index di luar jangkauan, coba lagi.")

# Penjelasan:
# - Ini gabungan dari CONTOH 1-3: beberapa except spesifik + loop validasi
# - Program terus minta input SAMPAI benar-benar valid, tanpa pernah crash


# ------------------------------------------------------
# CATATAN PENTING
# ------------------------------------------------------
# - except (A, B): untuk beberapa error dengan respons SAMA
# - except A: lalu except B: terpisah, untuk respons yang BEDA per jenis error
# - Selalu taruh except paling SPESIFIK di atas, except Exception paling bawah
# - Exception adalah fallback terakhir, bukan pengganti except yang spesifik