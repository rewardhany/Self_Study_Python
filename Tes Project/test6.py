# ===================================================
# PROJECT 16: ARCH LINUX PACMAN TERMINAL SIMULATOR
# VERSION: DICTIONARY UPGRADE (NO MORE IF-ELIF STACK)
# ===================================================
import time

SYSTEM_USERNAME = "reffawardany"
SYSTEM_PASSWORD = "rahasia123"

# 1. WHITELIST PERINTAH YANG DIIZINKAN
command_terminal = [
    "sudo pacman -Syu",
    "sudo pacman -Syyu",
    "sudo pacman -S vscode",
    "sudo pacman -S spotify",
    "sudo pacman -Rns spotify", 
    "sudo pacman -Rns vscode"
]

# 2. KATALOG DATABASE APLIKASI (DICTIONARY) Biar ga nulis if else banyak banyak (bisa di lihat di file test5.py if else nya banyak tanpa dictionary)
# Jika mau nambah aplikasi baru, cukup edit di sini saja!
repo_database = {
    "vscode": {
        "version": "1.91.0-1", 
        "net_change": "350.20 MiB", 
        "download": "92.50 MiB", 
        "repo": "extra"
    },
    "spotify": {
        "version": "1.2.40-3", 
        "net_change": "145.10 MiB", 
        "download": "48.20 MiB", 
        "repo": "multilib"
    }
}

is_system_running = True


def terminal_shell():
    """Fungsi simulasi login TTY"""
    while True:
        print("Arch Linux 6.9.1-arch1-1 (tty1)\n")

        input_user = input("Enter username: ")
        input_pw = input("Enter password: ")

        if input_user == SYSTEM_USERNAME and input_pw == SYSTEM_PASSWORD:
            print("\nLogging in...")
            time.sleep(1)
            print("Last login: Tue Jul 14 15:20:10 on tty1")
            print("Welcome to Arch Linux! Type 'exit' to log out.\n")
            break
        else:
            print("\nLogin incorrect please try again.\n")
            
            
def command_shell():
    """Fungsi prompt shell terminal utama"""
    global is_system_running

    while is_system_running:
        user_input = input(f"[{SYSTEM_USERNAME}@archlinux ~]$ ")
        command = user_input.strip()

        if command == "":
            continue
        elif command == "exit":
            print("Logging out...")
            time.sleep(1)
            print("Logged out successfully.")
            is_system_running = False
            break
        
        # Mengecek apakah perintah ada dalam whitelist array kamu
        if command in command_terminal:
            words = command.split()
            
            # ──────────────────────────────────────────────────
            # [SKENARIO 1] SYSTEM UPGRADE (-Syu)
            # ──────────────────────────────────────────────────
            if words[2] == "-Syu" or words[2] == "-Syyu":
                print(f"[sudo] password for {SYSTEM_USERNAME}: ")
                sudo_pw = input()
                if sudo_pw != SYSTEM_PASSWORD:
                    print("Sorry, try again.")
                    continue

                print(":: Synchronizing package databases...")
                time.sleep(2)
                print(":: Starting full system upgrade...")
                time.sleep(1)
                print(" nothing to do (system up to date).")

            # ──────────────────────────────────────────────────
            # [SKENARIO 2] INSTALASI APLIKASI (-S)
            # ──────────────────────────────────────────────────
            elif words[2] == "-S":
                nama_aplikasi = words[3] 
                print(f"[sudo] password for {SYSTEM_USERNAME}: ")
                sudo_pw = input()
                if sudo_pw != SYSTEM_PASSWORD:
                    print("Sorry, try again.")
                    continue
                    
                print("resolving dependencies...")
                time.sleep(0.5)
                print("looking for conflicting packages...\n")
                time.sleep(0.5)

                # --- PROSES AMBIL DATA DARI DICTIONARY ---
                if nama_aplikasi in repo_database:
                    app_data = repo_database[nama_aplikasi]
                    version = app_data["version"]
                    net_change = app_data["net_change"]
                    download = app_data["download"]
                    repo = app_data["repo"]
                else:
                    # Fallback jika aplikasi lolos whitelist tapi lupa diinput ke dictionary
                    version, net_change, download, repo = "1.0.0-1", "10.00 MiB", "3.50 MiB", "core"

                # Cetak Tabel Data Paket
                print("Package (1)                  New Version   Net Change   Download Size\n")
                print(f"{repo}/{nama_aplikasi:<22} {version:<13} {net_change:<12} {download}\n")
                print(f"Total Download Size:   {download}")
                print(f"Total Installed Size:  {net_change}\n")

                # Prompt Konfirmasi Instalasi [Y/n]
                confirm = input(":: Proceed with installation? [Y/n]: ")
                
                if confirm.lower() == "y" or confirm == "":
                    print(f"\n(1/1) downloading {nama_aplikasi}... [######################] 100%")
                    time.sleep(1)
                    print(f"(1/1) checking keys...                   [######################] 100%")
                    time.sleep(0.5)
                    print(f"(1/1) installing {nama_aplikasi}...                  [######################] 100%")
                    time.sleep(1)
                    print(f">>> [SUCCESS] {nama_aplikasi} successfully installed.")
                else:
                    print("\n>>> [ABORT] Installation cancelled by user.")

            # ──────────────────────────────────────────────────
            # [SKENARIO 3] PENGHAPUSAN APLIKASI (-Rns)
            # ──────────────────────────────────────────────────
            elif words[2] == "-Rns":
                nama_aplikasi = words[3]
                print("Apps found")
                time.sleep(1)
                print(f"Removing {nama_aplikasi}...")
                time.sleep(1)
                print(f"{nama_aplikasi} successfully removed.")

            else: 
                print(f"error: invalid option '{words[2]}'")
        else:
            print(f"bash: {command}: command not found")


# ==========================================
# RUN SIMULATOR
# ==========================================
terminal_shell()  
command_shell()

# CATATAN:
# {nama_aplikasi:<22}, artinya Python bakal membuatkan kotak kosong selebar 22 karakter.
# contohnya
# [v][s][c][o][d][e][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ] -> Kotak vscode (22 karakter)
# [s][p][o][t][i][f][y][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ] -> Kotak spotify (22 karakter)

# MAKSUD DARI .split()
# contoh
# kalimat = "sudo pacman -S vscode"
# maka Kalau kamu panggil fungsi .split(), Python akan bekerja seperti ini di balik layar:
# Input:  "sudo pacman -S vscode"
#          ↓      ↓     ↓
# Gunting! [spasi] [spasi] [spasi]
#          ↓      ↓     ↓
# Output: ["sudo", "pacman", "-S", "vscode"]  <-- Menjadi Array!
# Dengan kita potong pakai .split(), barulah kita bisa menunjuk kata-katanya secara spesifik lewat indeks array-nya:
# perintah = "sudo pacman -S vscode"
# words = perintah.split()

# Sekarang kita bisa panggil satu-satu:
# print(words[0])  # Output: sudo     (kata pertama)
# print(words[1])  # Output: pacman   (kata kedua)
# print(words[2])  # Output: -S       (kata ketiga, buat ngecek aksi)
# print(words[3])  # Output: vscode   (kata keempat, nama aplikasinya!)