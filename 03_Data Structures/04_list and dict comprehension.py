# ======================================================
# 04 LIST & DICT COMPREHENSION
# ======================================================
# COMPREHENSION adalah:
# Cara singkat bikin list/dict baru dari loop, dalam SATU baris
#
# Digunakan ketika:
# - Kamu mau transformasi/filter data dari list/dict lain
# - Daripada nulis for-loop 3-4 baris, cukup 1 baris
#
# STRUKTUR DASAR:
# list_baru = [ekspresi for item in list_lama]
# list_baru = [ekspresi for item in list_lama if kondisi]
# dict_baru = {key: value for item in list_lama}
# ======================================================


# ------------------------------------------------------
# CONTOH 1: LIST COMPREHENSION BASIC (VERSI PANJANG VS PENDEK)
# ------------------------------------------------------

angka = [1, 2, 3, 4, 5]

# cara biasa (for loop manual)
kuadrat_manual = []
for n in angka:
    kuadrat_manual.append(n ** 2)
print(kuadrat_manual)

# cara comprehension (1 baris, hasil SAMA PERSIS)
kuadrat_comprehension = [n ** 2 for n in angka]
print(kuadrat_comprehension)

# Penjelasan:
# - [n ** 2 for n in angka] artinya:
#   "buat list baru, isinya n**2, untuk setiap n di dalam angka"
# - Hasilnya identik dengan for-loop manual, cuma lebih ringkas


# ------------------------------------------------------
# CONTOH 2: LIST COMPREHENSION DENGAN KONDISI (IF)
# ------------------------------------------------------

nilai_ujian = [88, 72, 95, 60, 81, 55, 90]

nilai_lulus = [n for n in nilai_ujian if n >= 75]
print(f"Nilai yang lulus: {nilai_lulus}")

status = ["Lulus" if n >= 75 else "Tidak Lulus" for n in nilai_ujian]
print(status)

# Penjelasan:
# - [n for n in nilai_ujian if n >= 75]
#   -> filter: cuma ambil n yang lolos syarat if
# - ["Lulus" if n >= 75 else "Tidak Lulus" for n in nilai_ujian]
#   -> ini if/else di DEPAN for, bukan filter, tapi ubah NILAI-nya
# - Jangan ketuker: if di belakang for = filter, if...else di depan for = transformasi nilai


# ------------------------------------------------------
# CONTOH 3: DICT COMPREHENSION
# ------------------------------------------------------

nama_panitia = ["Reffa", "Galan", "Bintang", "Keyzia"]

panjang_nama = {nama: len(nama) for nama in nama_panitia}
print(panjang_nama)

# Penjelasan:
# - Sama seperti list comprehension, tapi hasilnya dictionary
# - {key: value for item in list} -> key dan value dihitung dari tiap item


# ------------------------------------------------------
# CONTOH 4: COMPREHENSION UNTUK "BERSIHKAN" DATA
# ------------------------------------------------------

input_kotor = ["  Reffa ", "GALAN", "bintang", " Keyzia"]

nama_bersih = [nama.strip().title() for nama in input_kotor]
print(nama_bersih)

# Penjelasan:
# - .strip()  -> buang spasi di awal/akhir
# - .title()  -> ubah jadi Kapital-Di-Awal-Kata
# - Comprehension bisa "chaining" beberapa method sekaligus per item,
#   ini pola umum buat bersihin data user sebelum disimpan


# ------------------------------------------------------
# CATATAN PENTING COMPREHENSION
# ------------------------------------------------------
# - Comprehension bukan wajib dipakai, for-loop biasa tetap valid
# - Kalau logikanya sudah lebih dari 1 kondisi/rumit, LEBIH BAIK pakai for-loop
#   biasa yang lebih gampang dibaca daripada maksain 1 baris
# - Aturan gampang: kalau comprehension-nya jadi susah dibaca, jangan dipakai