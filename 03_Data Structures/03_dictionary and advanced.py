# ======================================================
# 03 DICTIONARY BASIC & ADVANCED
# ======================================================
# DICTIONARY adalah:
# Struktur data yang nyimpan data dalam bentuk KEY-VALUE, bukan index angka
#
# Digunakan ketika:
# - Data punya "label" yang lebih jelas daripada sekadar index 0,1,2
# - Kamu butuh cari data berdasarkan NAMA/KATEGORI, bukan urutan
#
# STRUKTUR DASAR:
# nama_dict = {"key1": value1, "key2": value2}
# ======================================================


# ------------------------------------------------------
# CONTOH 1: KEY-VALUE BASIC & get()
# ------------------------------------------------------

profil = {
    "nama": "Reffa",
    "jurusan": "Teknik Komputer",
    "divisi": "Keamanan"
}

print(profil["nama"])                          # akses langsung
print(profil.get("divisi"))                     # akses pakai get()
print(profil.get("nim", "Belum diisi"))         # get() dengan default value

# Penjelasan:
# - profil["key"] -> ERROR kalau key-nya tidak ada
# - profil.get("key") -> lebih aman, return None kalau tidak ada
# - profil.get("key", default) -> kasih nilai default kalau key tidak ditemukan


# ------------------------------------------------------
# CONTOH 2: UPDATE, POP, KEYS/VALUES/ITEMS
# ------------------------------------------------------

profil["nim"] = "2306xxxx"          # nambah key baru
profil["divisi"] = "Keamanan ODWH"  # update key yang sudah ada

divisi_lama = profil.pop("divisi")  # hapus key, sekaligus ambil value-nya
print(f"Divisi dihapus: {divisi_lama}")

print(list(profil.keys()))
print(list(profil.values()))
print(list(profil.items()))

# Penjelasan:
# - dict["key"] = value -> nambah key baru ATAU update kalau sudah ada
# - .pop("key") -> hapus key tertentu, return value-nya
# - .keys() / .values() / .items() -> ambil semua key, semua value, atau pasangan keduanya


# ------------------------------------------------------
# CONTOH 3: NESTED DICTIONARY
# ------------------------------------------------------

data_panitia = {
    "Reffa": {"divisi": "Keamanan", "role": "Anggota"},
    "Sultan": {"divisi": "Ketua Pelaksana", "role": "Ketua"},
    "Iqbal":  {"divisi": "Supervisor", "role": "Supervisor"}
}

print(data_panitia["Reffa"]["divisi"])
print(data_panitia["Sultan"]["role"])

# Penjelasan:
# - Dictionary bisa berisi dictionary lain di dalamnya
# - Aksesnya tinggal "rantai" key satu per satu: dict["key_luar"]["key_dalam"]
# - Pola ini yang dipakai buat data JSON dari API nanti di BAB 9


# ------------------------------------------------------
# CONTOH 4: LOOPING DICTIONARY DENGAN .items()
# ------------------------------------------------------

for nama, detail in data_panitia.items():
    print(f"{nama} -> Divisi: {detail['divisi']}, Role: {detail['role']}")

# Penjelasan:
# - .items() ngasih dua nilai sekaligus tiap loop: key dan value-nya
# - detail di sini adalah dictionary lagi (karena nested), makanya dipanggil
#   pakai detail['divisi'] bukan detail.divisi


# ------------------------------------------------------
# CATATAN PENTING DICTIONARY
# ------------------------------------------------------
# - Key HARUS unik, kalau key sama ditulis 2x, yang terakhir yang dipakai
# - Key TIDAK BISA pakai list/dict sebagai key (harus tipe yang immutable: string, angka, tuple)
# - Kombinasi list + dict (list of dict / dict of dict) adalah pola paling
#   sering dipakai buat merepresentasikan data nyata (lihat PROJECT gabungan)