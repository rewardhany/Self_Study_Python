# ======================================================
# 07 MAP, FILTER, REDUCE
# ======================================================
# Tiga fungsi bawaan Python untuk MEMPROSES list tanpa nulis for-loop manual
#
# - map()    -> ubah SETIAP elemen jadi sesuatu yang baru
# - filter() -> ambil elemen yang LOLOS kondisi tertentu
# - reduce() -> gabungkan SEMUA elemen jadi satu nilai
# ======================================================

from functools import reduce   # reduce tidak bawaan langsung, harus di-import


# ------------------------------------------------------
# CONTOH 1: map() - MENGUBAH SETIAP ELEMEN
# ------------------------------------------------------

harga_barang = [15000, 20000, 8000, 50000]

harga_setelah_diskon = list(map(lambda h: h * 0.9, harga_barang))
print(harga_setelah_diskon)

# Penjelasan:
# - map(fungsi, list) menjalankan fungsi ke SETIAP elemen list
# - Hasilnya objek map, makanya dibungkus list() biar bisa dilihat isinya
# - Sama hasilnya kalau ditulis pakai list comprehension:
#   [h * 0.9 for h in harga_barang]


# ------------------------------------------------------
# CONTOH 2: filter() - MENYARING ELEMEN
# ------------------------------------------------------

nilai_ujian = [88, 72, 95, 60, 81, 55, 90]

nilai_lulus = list(filter(lambda n: n >= 75, nilai_ujian))
print(nilai_lulus)

# Penjelasan:
# - filter(fungsi, list) cuma AMBIL elemen yang bikin fungsi-nya True
# - Sama hasilnya dengan list comprehension:
#   [n for n in nilai_ujian if n >= 75]
# - map() ubah nilai, filter() nyaring nilai -> jangan ketuker


# ------------------------------------------------------
# CONTOH 3: reduce() - MENGGABUNGKAN JADI SATU NILAI
# ------------------------------------------------------

angka = [2, 4, 6, 8]

hasil_kali = reduce(lambda a, b: a * b, angka)
print(hasil_kali)   # 2*4*6*8 = 384

# Penjelasan:
# - reduce(fungsi, list) proses elemen SATU PER SATU, digabung terus-menerus
# - Langkahnya: (2*4)=8 -> (8*6)=48 -> (48*8)=384
# - Untuk kasus sederhana kayak ini, sum()/math.prod() lebih simpel,
#   tapi reduce() dipakai kalau logika gabungannya lebih custom


# ------------------------------------------------------
# CONTOH 4: KOMBINASI KETIGANYA DALAM 1 ALUR
# ------------------------------------------------------

transaksi = [15000, -5000, 20000, -2000, 8000]   # minus = pengeluaran

pemasukan_saja = list(filter(lambda t: t > 0, transaksi))
setelah_pajak = list(map(lambda t: t * 0.98, pemasukan_saja))
total_bersih = reduce(lambda a, b: a + b, setelah_pajak)

print(f"Pemasukan saja  : {pemasukan_saja}")
print(f"Setelah pajak 2%: {setelah_pajak}")
print(f"Total bersih    : {total_bersih:.2f}")

# Penjelasan:
# - filter dulu -> ambil yang relevan
# - map dulu -> ubah/proses tiap elemen
# - reduce terakhir -> gabungkan jadi satu angka final
# - Pola filter -> map -> reduce ini sangat umum di data processing (nyambung ke BAB 11 nanti)


# ------------------------------------------------------
# CATATAN PENTING
# ------------------------------------------------------
# - map() dan filter() sering digantikan list comprehension karena lebih
#   gampang dibaca -> keduanya valid, pilih yang paling jelas buat kamu
# - reduce() TIDAK ada penggantinya di comprehension, harus tetap di-import
#   dari functools kalau butuh
# - Untuk pemula: kalau bingung mana yang lebih jelas, list comprehension
#   biasanya lebih mudah dibaca daripada map()/filter()