import time

# 1. DATA AKUN LINUX (Akun yang terdaftar di OS)
SYSTEM_USER = "reffawardany"
SYSTEM_PASS = "arch123"  # Password default untuk simulasi

def tty_login():
    """Fungsi simulasi layar login hitam (TTY) khas Linux"""
    print("\nArch Linux 6.9.1-arch1-1 (tty1)\n")
    
    while True:
        # Prompt login khas Arch
        input_user = input("archlinux login: ")
        input_pass = input("Password: ") # Di terminal asli kosong, tapi kita buat ketikan biasa dulu biar simpel
        
        # Cek apakah username & password-nya cocok
        if input_user == SYSTEM_USER and input_pass == SYSTEM_PASS:
            print("\nLogging in...")
            time.sleep(1)  # Efek loading dramatis selama 1 detik
            print("Last login: Tue Jul 14 15:20:10 on tty1")
            print("Welcome to Arch Linux! Type 'exit' to log out.\n")
            break  # Keluar dari loop login jika berhasil
        else:
            print("\nLogin incorrect")
            print("-> Hint: User adalah 'reffawardany' dan Pass adalah 'arch123'\n")


def terminal_shell():
    """Fungsi prompt terminal interaktif setelah login"""
    is_running = True
    
    while is_running:
        # Menggunakan f-string untuk membuat prompt [reffawardany@archlinux ~]$
        user_input = input(f"[{SYSTEM_USER}@archlinux ~]$ ")
        
        # Bersihkan spasi berlebih di awal/akhir inputan user
        command = user_input.strip()
        
        # 1. Jika user menekan enter kosong
        if command == "":
            continue
            
        # 2. Jika user ingin logout
        elif command == "exit":
            print("logout")
            is_running = False
            
        # 3. Jika user mengetik perintah lain (yang belum kita buat)
        else:
            print(f"bash: {command}: command not found")


# ==========================================
# ALUR JALANNYA PROGRAM (Pintu Masuk)
# ==========================================
tty_login()       # Jalankan login dulu
terminal_shell()   # Kalau lolos login, baru masuk ke prompt terminal

print()

# YOUR CODE STARTS HERE
import time

SYSTEM_USERNAME = "reffawardany"
SYSTEM_PASSWORD = "rahasia123"

command_terminal = [
    "sudo pacman -Syu",
    "sudo pacman -Syyu",
    "sudo pacman -S vscode",
    "sudo pacman -S spotify",
    "sudo pacman -Rns spotify", 
    "sudo pacman -Rns vscode"
    ]
is_system_running = True

def terminal_shell():
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
            print("\nLogin incorrect please try again.")
            
def command_shell():
    global is_system_running

    while is_system_running:
        user_input = input(f"[{SYSTEM_USERNAME}@archlinux ~]$ ")
        command = user_input.strip()

        if command == "":
            continue
        elif command == "exit":
            print("Logging out...")
            time.sleep(1)
            print("Logged out sucessfully.")
            is_system_running = False
            break

        # Mengecek apakah perintah ada dalam whitelist array
        if command in command_terminal:
            words = command.split()
            
            # System upgrade
            if words[2] == "-Syu" or words[2] == "-Syyu":
                print(f"[sudo] password for {SYSTEM_USERNAME}: ")
                sudo_pw = input()
                if sudo_pw != SYSTEM_PASSWORD:
                    print("Sorry, try again.")
                    continue

                print(":: Synchronizing package databases...")
                time.sleep(3)
                print(":: Starting full system upgrade...")
                time.sleep(1)
                print(" nothing to do (system up to date).")

            # Install apps
            elif words[2] == "-S":
                nama_aplikasi = words[3] 
                print(f"[sudo] password for {SYSTEM_USERNAME}: ")
                sudo_pw = input()
                if sudo_pw != SYSTEM_PASSWORD:
                    print("Sorry, try again.")
                    continue
                print("resolving dependencies...")
                time.sleep(1)
                print("looking for conflicting packages...\n")
                time.sleep(1)

                # Set data statis agar layout tabel terlihat presisi & rapi
                if nama_aplikasi == "vscode":
                    version, net_change, download = "1.91.0-1", "350.20 MiB", "92.50 MiB"
                    repo = "extra"
                elif nama_aplikasi == "spotify":
                    version, net_change, download = "1.2.40-3", "145.10 MiB", "48.20 MiB"
                    repo = "multilib"
                else:
                    version, net_change, download = "1.0.0-1", "10.00 MiB", "3.50 MiB"
                    repo = "core"

                # Cetak Tabel Data Paket
                print("Package (1)                  New Version   Net Change   Download Size\n")
                print(f"{repo}/{nama_aplikasi:<22} {version:<13} {net_change:<12} {download}\n")
                print(f"Total Download Size:   {download}")
                print(f"Total Installed Size:  {net_change}\n")

                # Prompt Konfirmasi Instalasi [Y/n]
                confirm = input(":: Proceed with installation? [Y/n]: ")
                
                if confirm.lower() == "y" or confirm == "":
                    print(f"\n(1/1) downloading {nama_aplikasi}... [######################] 100%")
                    time.sleep(2)
                    print(f"(1/1) checking keys...                   [######################] 100%")
                    time.sleep(3)
                    print(f"(1/1) installing {nama_aplikasi}...                  [######################] 100%")
                    time.sleep(2)
                    print(f">>> [SUCCESS] {nama_aplikasi} successfully installed.")
                else:
                    print("\n>>> [ABORT] Installation cancelled by user.")

            # Remove packages
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

terminal_shell()  # Jalankan layar login terlebih dahulu
command_shell()   # Jika lolos login, baru shell terminal ini otomatis menyala