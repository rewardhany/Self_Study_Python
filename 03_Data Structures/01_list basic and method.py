# ======================================================
# 01 LIST BASIC & METHODS
# ======================================================
# LIST adalah:
# Struktur data yang bisa menyimpan BANYAK nilai dalam 1 variabel,
# urut, dan BISA DIUBAH (mutable) setelah dibuat.
#
# Digunakan ketika:
# - Kamu butuh nyimpan banyak data sejenis (nama, angka, dll)
# - Urutan data penting
# - Data-nya perlu ditambah/dihapus/diubah nanti
#
# STRUKTUR DASAR:
# nama_list = [item1, item2, item3]
# ======================================================


# ------------------------------------------------------
# CONTOH 1: INDEXING & SLICING
# ------------------------------------------------------

buah = ["apel", "jeruk", "mangga", "pisang", "anggur"]

print(buah[0])       # elemen pertama -> apel
print(buah[-1])      # elemen terakhir -> anggur
print(buah[1:3])     # slicing index 1 sampai SEBELUM 3 -> ['jeruk', 'mangga']
print(buah[:2])      # dari awal sampai sebelum index 2
print(buah[2:])      # dari index 2 sampai akhir

# Penjelasan:
# - Index dimulai dari 0, bukan 1
# - Index negatif dihitung dari BELAKANG
# - Slicing [a:b] TIDAK termasuk index b


# ------------------------------------------------------
# CONTOH 2: MENAMBAH & MENGHAPUS DATA
# ------------------------------------------------------

daftar_tugas = ["Tata Tertib", "Notulensi"]

daftar_tugas.append("PPT Progress")          # nambah di akhir
daftar_tugas.insert(1, "Cek Logistik")       # nambah di posisi tertentu
print(daftar_tugas)

daftar_tugas.remove("Notulensi")             # hapus berdasarkan NILAI
selesai = daftar_tugas.pop(0)                # hapus berdasarkan INDEX, sekaligus ambil nilainya
print(f"Tugas selesai: {selesai}")
print(daftar_tugas)

# Penjelasan:
# - append()  -> selalu nambah di paling akhir
# - insert()  -> nambah di posisi spesifik
# - remove()  -> hapus berdasarkan NILAI (error kalau nilainya tidak ada)
# - pop()     -> hapus berdasarkan INDEX, dan me-return nilai yang dihapus


# ------------------------------------------------------
# CONTOH 3: SORT & REVERSE
# ------------------------------------------------------

nilai_ujian = [88, 72, 95, 60, 81]

nilai_ujian.sort()                     # urut naik (mengubah list asli)
print(nilai_ujian)

nilai_ujian.sort(reverse=True)         # urut turun
print(nilai_ujian)

nama_terurut = sorted(["Bintang", "Alya", "Keyzia", "Galan"])   # tidak mengubah list asli
print(nama_terurut)

# Penjelasan:
# - .sort() mengubah list ASLINYA langsung (tidak return apa-apa)
# - sorted() bikin list BARU yang sudah terurut, list lama tetap utuh
# - reverse=True dipakai buat urut dari besar ke kecil / Z ke A


# ------------------------------------------------------
# CONTOH 4: LIST DI DALAM LIST (NESTED LIST / PREVIEW MATRIX)
# ------------------------------------------------------

absensi_panitia = [
    ["Reffa", "Security"],
    ["Galan", "Logistik"],
    ["Bintang", "Acara"]
]

for data in absensi_panitia:
    nama, divisi = data          # unpacking otomatis
    print(f"{nama} - Divisi {divisi}")

# Penjelasan:
# - List bisa berisi list lain di dalamnya
# - nama, divisi = data -> Python otomatis "membongkar" isi list per elemen
# - Ini konsep dasar sebelum masuk ke tuple unpacking & dictionary nanti


# ------------------------------------------------------
# CATATAN PENTING LIST
# ------------------------------------------------------
# - List itu MUTABLE -> isinya bisa diubah kapan saja
# - .sort() mengubah list asli, sorted() tidak
# - remove() pakai NILAI, pop() pakai INDEX -> sering ketuker, hati-hati
# - Index selalu mulai dari 0