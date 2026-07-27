# ======================================================
# 02 TUPLE & SET
# ======================================================
# TUPLE adalah:
# Seperti list, TAPI tidak bisa diubah setelah dibuat (immutable)
#
# SET adalah:
# Kumpulan data yang isinya PASTI UNIK (tidak ada duplikat), tidak berurutan
#
# Digunakan ketika:
# - Tuple: data yang memang seharusnya TIDAK BOLEH berubah (koordinat, tanggal lahir)
# - Set: kamu butuh memastikan tidak ada data ganda, atau butuh operasi himpunan
#
# STRUKTUR DASAR:
# tuple_contoh = (item1, item2)
# set_contoh   = {item1, item2}
# ======================================================


# ------------------------------------------------------
# CONTOH 1: TUPLE BASIC & IMMUTABILITY
# ------------------------------------------------------

lokasi_odwh = ("Aula UPI", -6.8615, 107.5936)   # nama, latitude, longitude

print(lokasi_odwh[0])
print(lokasi_odwh[1], lokasi_odwh[2])

# lokasi_odwh[0] = "GOR UPI"   # <- kalau baris ini di-uncomment: ERROR
# Penjelasan errornya: 'tuple' object does not support item assignment

# Penjelasan:
# - Tuple ditulis pakai kurung ()
# - Begitu dibuat, ISINYA TIDAK BISA DIUBAH lagi
# - Cocok buat data yang secara logika memang harus tetap (koordinat, konstanta)


# ------------------------------------------------------
# CONTOH 2: TUPLE UNPACKING
# ------------------------------------------------------

peserta = ("Reffa", 20, "Teknik Komputer")

nama, umur, jurusan = peserta
print(f"{nama} ({umur} tahun) - {jurusan}")

# Penjelasan:
# - Unpacking = ambil semua nilai tuple sekaligus ke variabel terpisah
# - Jumlah variabel di kiri HARUS PAS dengan jumlah item di tuple


# ------------------------------------------------------
# CONTOH 3: SET BASIC & UNIQUE VALUE
# ------------------------------------------------------

divisi_hadir = ["Keamanan", "Acara", "Logistik", "Keamanan", "Acara", "Konsumsi"]

divisi_unik = set(divisi_hadir)
print(divisi_unik)              # otomatis hilang duplikatnya
print(f"Jumlah divisi berbeda yang hadir: {len(divisi_unik)}")

# Penjelasan:
# - set() otomatis membuang nilai yang duplikat
# - Urutan di dalam set TIDAK DIJAMIN sama seperti list aslinya
# - Cara paling cepat buat "berapa banyak nilai UNIK yang ada"


# ------------------------------------------------------
# CONTOH 4: OPERASI HIMPUNAN (UNION, INTERSECTION, DIFFERENCE)
# ------------------------------------------------------

panitia_odwh = {"Reffa", "Galan", "Bintang", "Keyzia", "Alya"}
panitia_logistik_hima = {"Reffa", "Bintang", "Sultan", "Iqbal"}

gabungan = panitia_odwh | panitia_logistik_hima          # union: semua nama, tanpa duplikat
sama_sama_ikut = panitia_odwh & panitia_logistik_hima     # intersection: yang ikut KEDUANYA
hanya_odwh = panitia_odwh - panitia_logistik_hima         # difference: yang HANYA di ODWH

print(f"Gabungan semua panitia   : {gabungan}")
print(f"Ikut kedua acara         : {sama_sama_ikut}")
print(f"Hanya ikut ODWH          : {hanya_odwh}")

# Penjelasan:
# - | (union)        -> gabungkan semua, tanpa duplikat
# - & (intersection) -> cari yang ADA DI KEDUA set
# - - (difference)   -> ada di set pertama TAPI TIDAK ada di set kedua


# ------------------------------------------------------
# CATATAN PENTING TUPLE & SET
# ------------------------------------------------------
# - Tuple = list yang "dikunci", tidak bisa diubah lagi
# - Set = otomatis unik, cocok buat cek duplikat / bandingkan 2 kelompok data
# - Set TIDAK punya index -> tidak bisa set_contoh[0]
# - Kalau butuh data yang boleh berubah dan berurutan -> tetap pakai list