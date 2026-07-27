# Explaining the difference using pass and without pass
# EXAMPLE 1 WITH PASS
temperature = 40

if temperature < 30:
    pass # Tells Python: "I am deliberately doing nothing here."
else:
    print("ALERT: It is too hot!")

print("System check complete.\n")

# EXAMPLE 2 WITHOUT PASS
#temperature = 25

#if temperature < 30:
    
#else:
 #   print("ALERT: It is too hot!")

#print("System check complete.")
# output: error because if statements is empty without pass

# PROJECT 12: AUDIO STREAM OPTIMIZER
APP_NAME = "CUSTOM UI PANEL"

def calculate_audio_quality(speed):
    if speed < 5:
        return "LOW"
    elif speed < 15:
        return "MEDIUM"
    else:
        return "HIGH"

is_panel_active = True

print(f"=== {APP_NAME}: AUDIO SETTINGS ===")
print("(Type < 0 to close panel)\n")

while is_panel_active == True:
    user_speed = float(input("Enter internet download speed (Mbps): "))

    if user_speed < 0:
        print("Closing OS Settings Panel. Goodbye!")
        is_panel_active = False
    else:
        quality_result = calculate_audio_quality(user_speed)
        print(f">>> [OS CORE]: Quality set to {quality_result}")
        
        if quality_result == "LOW":
            print("[UI NOTICE]: Performance Mode Active. Lowering bitrates to prevent buffer.\n")
        elif quality_result == "MEDIUM":
            print("[UI NOTICE]: Performance set to medium.\n")
        else:
            print("[UI STATUS]: Lossless Audio Matrix Enabled! Enjoy your Spotify tracks.\n")

print()

# PROJECT 13 (ARRAY): OS MUSIC QUEUE SERVICE
queue = []
is_service_running = True

print("=== MUSIC PLAYER ===")

while is_service_running == True:
    print("[1] Add Song  [2] Play Next  [3] View Queue  [4] Exit")
    user_input = input("Select operation: ")

    if user_input == "1":
        enter_song = input("Enter song name: ")
        queue.append(enter_song) # append = nambah data baru ke array
        print(f">>> [SYSTEM]: '{enter_song}' added to queue.")

    elif user_input == "2":
        if len(queue) == 0: # len = Menghitung ada berapa jumlah data di array
            print(">>> [WARNING]: There's no queue! Please add song to queue first.")
        else:
            enter_song = queue.pop(0) # pop = Mengambil dan menghapus data di urutan tertentu
            print(f">>> [PLAYER]: Now playing -> {enter_song}")

    elif user_input == "3":
        total_songs = len(queue)
        print(f">>> [SYSTEM]: Queue ({total_songs} songs): {queue}")

    elif user_input == "4":
        print("Closing OS Music Service. Goodbye!\n")
        is_service_running = False # Mematikan loop while

    else:
        print("[ERROR] Invalid operation command.\n")

# PENJELASAN POP(0):
# pop(0): Mengambil dan menghapus data di urutan tertentu.
# pop(0) akan selalu mengambil data paling depan (index 0).
# Cocok banget buat sistem "Play Next Song"!

# CONTOHNYA:
# antrean = ["Lagu A", "Lagu B", "Lagu C"]
# lagu_diputar = antrean.pop(0) 
# print(lagu_diputar) # Output: Lagu A
# print(antrean)      # Output: ['Lagu B', 'Lagu C'] (Lagu A sudah hilang dari antrean)

# PROJECT 14 (ARRAY): Kehadiran mhs
APP_NAME = "Attendance List"

name = []
is_attendance = True

print("=== TEST LISAN SEJARAH ===")

while is_attendance == True:
    print("[1] Enter name [2] See next person [3] View Queue [4] EXIT")
    select_input = input("Select: ")

    if select_input == "1":
        nama_mhs = input("Student name: ")
        name.append(nama_mhs) # masuk ke daftar array
        print(f"{nama_mhs} added to queue as {APP_NAME.lower()}")
    
    elif select_input == "2":
        if len(name) == 0:
            print("Tambahkan mahasiswa terlebih dahulu")
        else:
            nama_mhs = name.pop(0)
            print(f"Urutan ujian lisan sekarang -> {nama_mhs}")
    
    elif select_input == "3":
        total_mhs = len(name)
        print(f"Queue ({total_mhs} mhs): {name}")

    elif select_input == "4":
        print("[SISTEM] Keluar dari aplikasi...")
        is_attendance = False
    
    else:
        print("ERROR! Please input the correct number selection")
        

# PROJECT 15 (ARRAY): USER DATABASE
SYSTEM_NAME = "PROFILE DATA"
database_user = []
total_users_registered = 0
is_system_online = True

def register_user(nama, alamat, no_hp, username, password):
    global database_user, total_users_registered
    
    data_format = f"Nama: {nama}\nAlamat: {alamat}\nNo HP: {no_hp}\nUsername: {username}\nPassword: {password}\n"
    
    database_user.append(data_format) # tambah data ke array
    total_users_registered = total_users_registered + 1
    
def check_database():
    global database_user
    print(f"\n==[SYSTEM LOG: {SYSTEM_NAME}]==")
    
    total_sekarang = len(database_user) # Menghitung ada berapa jumlah data di array
    print(f"Total users currently in Database: {total_sekarang}")
    print(f"Total history registration: {total_users_registered}\n")
    
    print("[PERSONAL DATA]")
    for user_data in database_user:
        print(user_data)
        
while is_system_online == True:
    print("=== DATABASE USER PROFILE ===")
    print("[1] Register new user [2] View data [3] EXIT")
    user_choice = input("Select operation: ")
    
    if user_choice == "1":
        print("\n[NEW USER REGISTRATION]")
        input_name = input("Enter your name: ")
        input_address = input("Enter your address: ")
        input_phone = int(input("Enter your phone number: "))
        input_username = input("Enter username: ")
        input_password = input("Enter password: ")
        
        register_user(input_name, input_address, input_phone, input_username, input_password)
        print(">>> [SUCCESS]: Data has been encrypted and saved to database.")
    
    elif user_choice == "2":
        check_database()
        
    elif user_choice == "3":
        print("\n[SYSTEM] Exiting from DATABASE application...\n")
        is_system_online = False
    
    else: 
        print("Error! Unauthorized command execution.")


# PROJECT 16 ARRAY & LOOP: ARCH PACKAGE MANAGER
SYSTEM_NAME = "ARCH LINUX PACMAN SIMULATOR"

repo_apps = ["hyprland", "waybar", "kitty", "rofi", "dolphin", "ags", "neovim"]
installed_apps = ["kitty"] # ex kitty has installed
is_system_running = True

def search_package(keyword):
    global repo_apps
    found = False

    print(f"\n-> Searching {keyword} in the repository...")

    for app_name in repo_apps:
        if keyword == app_name:
            print(f"core/{app_name} 0.40.0-1")
            print("    Dynamic tiling Wayland compositor / application packages")
            found = True
            break # stopped looping if it has been found

    if not found:
        print(f"error: package '{keyword}' not found (or you mistyped)")

def install_package(name_app):
    global repo_apps, installed_apps
    found = False

    for app_name in repo_apps:
        if app_name == name_app:
            found = True
            break

    if found and name_app not in installed_apps:
        print("\nresolving dependencies...")
        print(f"looking for conflicting packages...")
        confirm = input(f":: Proceed with installation of {name_app}? [Y/n]: ")

        if confirm.lower() == 'y' or confirm == '':
            installed_apps.append(name_app)
            print(f"(1/1) installing {name_app}... [######################] 100%")
            print(f">>> [SUCCESS] '{name_app}' has been installed successfully.")
        else:
            print(">>> [ABORT] Installation cancelled by user.")

    elif name_app in installed_apps:
        print(f"\nwarning: {name_app} is up to date -- skipping installation")
    
    else:
        print(f"error: '{name_app}' not found in repository.")

def list_installed():
    global installed_apps

    if len(installed_apps) == 0:
        print("\nerror: no packages installed")
        return
    
    print("\n=== INSTALLED PACKAGES (pacman -Q) ===")
    for app_name in installed_apps:
        print(f"- {app_name} 0.40.0-1")
    
    total_installed = len(installed_apps)
    print(f"\n Total {total_installed} packages installed")

# MAIN CONTROL

print(f"\n=== WELCOME TO {SYSTEM_NAME} ===")

while is_system_running == True:
    print("\n[1] Search Package (pacman -Ss)")
    print("[2] Install Package (pacman -S)")
    print("[3] List Installed (pacman -Q)")
    print("[4] EXIT")
    
    user_choice = input("Select operation (1/2/3/4): ")

    if user_choice == "1":
        search = input("Enter app name: ")
        search_package(search)

    elif user_choice == "2":
        target = input("Enter app you want to install: ")
        install_package(target)
    
    elif user_choice == "3":
        list_installed()

    elif user_choice == "4":
        print("\nGoodbye! Keep your system up to date. Segfault avoided. 🚀")
        is_system_running = False
    
    else:
        print("[ERR] Command not found.")
    

        
    