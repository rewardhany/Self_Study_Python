# ======================================================
# PROJECT GABUNGAN BAB 3: USER DATABASE (UPGRADE DARI BAB 2)
# ======================================================
# Ini kelanjutan dari "PROJECT 15 (ARRAY): USER DATABASE" yang
# masih kosong di 02_Control_Flow/14_mini_project_control...py
#
# Bedanya: sekarang tiap user BUKAN cuma nama (string biasa),
# tapi dictionary lengkap. Ini pola paling umum buat "record data"
# di dunia nyata (mirip 1 baris di database sungguhan).
# ======================================================

SYSTEM_NAME = "PROFILE DATA"
database_user = []              # list of dict, bukan list of string lagi
total_users_registered = 0
is_running = True

print(f"=== {SYSTEM_NAME} SYSTEM ===")

while is_running == True:
    print("\n[1] Daftar user  [2] Lihat semua user  [3] Cari user  [4] Divisi unik  [5] Keluar")
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        nama = input("Nama: ")
        umur = int(input("Umur: "))
        divisi = input("Divisi: ")

        user_baru = {
            "nama": nama,
            "umur": umur,
            "divisi": divisi
        }

        database_user.append(user_baru)
        total_users_registered += 1
        print(f">>> [SISTEM]: {nama} berhasil didaftarkan sebagai user ke-{total_users_registered}")

    elif pilihan == "2":
        if len(database_user) == 0:
            print(">>> [PERINGATAN]: Belum ada user terdaftar.")
        else:
            print(f"\n=== DAFTAR {SYSTEM_NAME.upper()} ({len(database_user)} USER) ===")
            for i, user in enumerate(database_user, start=1):
                print(f"{i}. {user['nama']} ({user['umur']} th) - {user['divisi']}")

    elif pilihan == "3":
        kata_kunci = input("Cari nama: ").lower()
        hasil_pencarian = [u for u in database_user if kata_kunci in u["nama"].lower()]

        if len(hasil_pencarian) == 0:
            print(">>> [SISTEM]: Tidak ditemukan.")
        else:
            for user in hasil_pencarian:
                print(f"Ditemukan: {user['nama']} - Divisi {user['divisi']}")

    elif pilihan == "4":
        semua_divisi = {u["divisi"] for u in database_user}   # set comprehension, hasilnya otomatis unik
        print(f"Divisi yang ada: {semua_divisi}")

    elif pilihan == "5":
        print(f"[SISTEM] Menutup {SYSTEM_NAME}. Total user terdaftar: {total_users_registered}")
        is_running = False

    else:
        print("ERROR! Pilihan tidak valid.")

# Penjelasan konsep yang dipakai:
# - list of dict       -> database_user isinya banyak dictionary
# - list comprehension -> menu [3] Cari user, filter berdasarkan kata kunci
# - set comprehension   -> menu [4] Divisi unik, otomatis buang duplikat
# - enumerate(x, start=1) -> looping sambil dapat nomor urut, tanpa bikin counter manual
#
# Ini project yang sama semangatnya dengan "PROJECT 15" versi lama kamu,
# tapi sekarang strukturnya udah representasi data yang lebih realistis -
# persis pola yang dipakai di koleksi Firestore HelpBlue (tiap dokumen = 1 dict).