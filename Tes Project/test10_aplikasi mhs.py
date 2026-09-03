import time

APP_NAME = "Spot UPI EDU"
user_data = {}
active_user = none

"""
SPOT UPI EDU - Perancangan Struktur Data (Tahap 2: Data Architecture)
======================================================================
Tujuan file ini: melatih Nested Dictionary & List of Dictionaries
SEBELUM masuk ke logic (looping, if-else, function).

Cara pakai:
- Bagian yang SUDAH terisi = contoh referensi biar kamu ngerti bentuknya
- Bagian bertanda TODO      = kamu isi/kerjain sendiri sebagai latihan
"""

# ============================================================
# 1. user_data -> Nested Dictionary
#    Key luar  : ID unik user (NIM untuk mahasiswa, NIP untuk dosen)
#    Value     : dictionary profil user, dibedakan lewat key "role"
# ============================================================

user_data = {
    "1201223045": {
        "nama": "Reffa",
        "role": "mahasiswa",
        "nim": "1201223045",
        "prodi": "Teknik Komputer"
    },
    "198501012010121001": {
        "nama": "Dr. Budi Santoso",
        "role": "dosen",
        "nip": "198501012010121001",
        "matkul_diampu": ["Struktur Data", "Basis Data"]
    }
    # TODO: tambahkan minimal 1 mahasiswa lagi & 1 dosen lagi
    # supaya nanti kamu punya bahan buat tes fitur login & filter role
}


# ============================================================
# 2. assignment_database -> List of Dictionaries
#    Setiap elemen list = 1 tugas.
#    Di dalam setiap tugas ada key "submissions" yang isinya List
#    lagi -> ini yang bikin strukturnya "nested".
# ============================================================

assignment_database = [
    {
        "id_tugas": "TGS001",
        "kode_matkul": "IF2210",
        "judul": "Implementasi Linked List",
        "deskripsi": "Buat program linked list sederhana",
        "deadline": "2026-09-10",
        "dosen_pembuat": "198501012010121001",
        "submissions": [
            # TODO: setiap submission = 1 dictionary dengan key:
            # nim_mahasiswa, waktu_kumpul, isi_tugas (link/teks),
            # status ("submitted" / "graded"), nilai (default None),
            # feedback (default None)
        ]
    }
    # TODO: tambahkan minimal 1 tugas lagi (matkul beda)
]


# ============================================================
# 3. Contoh bentuk 1 submission SETELAH mahasiswa kumpul tugas
#    (ini cuma referensi visual, bukan buat langsung dipakai)
# ============================================================

contoh_submission = {
    "nim_mahasiswa": "1201223045",
    "waktu_kumpul": "2026-09-08 21:30",
    "isi_tugas": "https://github.com/reffa/linked-list-impl",
    "status": "submitted",   # berubah jadi "graded" setelah dosen menilai
    "nilai": None,
    "feedback": None
}


# ============================================================
# 4. Latihan akses data
#    Kerjakan manual (tanpa function dulu) sebelum lanjut ke tahap
#    flowchart & skeleton function. Tulis kode di bawah tiap TODO.
# ============================================================

# TODO 1: Loop semua isi user_data, cetak "nama - role" tiap user
#         Hint: gunakan user_data.items()


# TODO 2: Loop semua isi assignment_database, cetak "judul - deadline"
#         Hint: langsung loop list-nya, tiap elemen adalah dict


# TODO 3: Tambahkan 1 submission baru ke tugas "TGS001"
#         Hint: akses assignment_database[0]["submissions"], lalu .append()


# TODO 4: Cari & cetak semua submission dengan status "submitted"
#         Hint: nested loop -> loop tiap tugas, lalu loop tiap
#         submission di dalam tugas itu, cek key "status"


# TODO 5 (tantangan): Buat fungsi cari_user(id_user) yang return
#         dictionary profil user dari user_data berdasarkan ID-nya,
#         atau None kalau tidak ketemu