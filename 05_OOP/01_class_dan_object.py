# ======================================================
# 01 CLASS DAN OBJECT
# ======================================================
# CLASS adalah:
# "Cetakan"/blueprint untuk membuat object
#
# OBJECT adalah:
# Hasil nyata dari class tersebut (instance)
#
# Analogi: class = cetakan kue, object = kue yang jadi.
# Satu cetakan bisa bikin banyak kue, masing-masing kue terpisah.
#
# STRUKTUR DASAR:
# class NamaClass:
#     kode
#
# objek = NamaClass()
# ======================================================


# ------------------------------------------------------
# CONTOH 1: CLASS PALING SEDERHANA
# ------------------------------------------------------

class Panitia:
    pass   # class kosong dulu, belum ada isinya

panitia_1 = Panitia()   # bikin OBJECT dari class Panitia
panitia_2 = Panitia()

print(panitia_1)
print(panitia_2)

# Penjelasan:
# - class Panitia: adalah CETAKAN, belum jadi apa-apa sampai di-panggil pakai ()
# - panitia_1 dan panitia_2 adalah OBJECT (instance) yang TERPISAH
# - print() nunjukkin alamat memori masing-masing -> beda, walau dari class sama


# ------------------------------------------------------
# CONTOH 2: MENAMBAH ATRIBUT SETELAH OBJECT DIBUAT
# ------------------------------------------------------

class Peserta:
    pass

peserta_1 = Peserta()
peserta_1.nama = "Reffa"
peserta_1.divisi = "Keamanan"

print(f"{peserta_1.nama} - {peserta_1.divisi}")

# Penjelasan:
# - Atribut (nama, divisi) bisa ditempel ke object pakai titik (.)
# - Cara ini valid tapi TIDAK RAPI -> nanti di 03_constructor_init.py
#   ada cara yang jauh lebih baik


# ------------------------------------------------------
# CONTOH 3: SETIAP OBJECT ITU TERPISAH (INDEPENDEN)
# ------------------------------------------------------

peserta_2 = Peserta()
peserta_2.nama = "Galan"
peserta_2.divisi = "Logistik"

print(f"{peserta_1.nama} tetap di divisi {peserta_1.divisi}")
print(f"{peserta_2.nama} ada di divisi {peserta_2.divisi}")

# Penjelasan:
# - Mengubah peserta_2 SAMA SEKALI tidak mempengaruhi peserta_1
# - Ini beda penting dari sekadar dictionary -> tiap object punya "identitas" sendiri


# ------------------------------------------------------
# CONTOH 4: CEK TIPE OBJECT
# ------------------------------------------------------

print(type(peserta_1))
print(isinstance(peserta_1, Peserta))
print(isinstance(peserta_1, Panitia))

# Penjelasan:
# - type(objek) -> nunjukkin objek ini dibuat dari class apa
# - isinstance(objek, Class) -> True/False, cek apakah objek berasal dari class itu
# - Berguna banget nanti pas inheritance (BAB 5 file 04)


# ------------------------------------------------------
# CATATAN PENTING
# ------------------------------------------------------
# - class = blueprint, object = hasil nyata dari blueprint itu
# - Satu class bisa menghasilkan BANYAK object, masing-masing independen
# - Nama class konvensinya PascalCase (Panitia, bukan panitia)
# - Nama variabel/object biasa tetap snake_case (panitia_1, bukan Panitia1)