# PROJECT 1 PERPUSTAKAAN
NAMA_PERPUSTAKAAN = "Gramedia"
daftar_peminjaman_aktif = [] # Isinya nanti berupa teks gabungan, contoh: "Asep - Buku Python", pakai .append utk menambahkan data, utk hapus isinya pake .remove, ini pake array jadi misal Asep - Buku Python itu terhitung satu data
total_buku_keluar = 0
total_denda = 0

def pinjam_buku(nama_peminjam, judul_buku):
    global daftar_peminjaman_aktif, total_buku_keluar

    total_buku_keluar = total_buku_keluar + 1
    daftar_peminjaman_aktif.append(f"{nama_peminjam} - {judul_buku}")

    print(f"== LAPORAN PEMINJAMAN BUKU {NAMA_PERPUSTAKAAN.upper()} ==")
    print(f"Nama peminjam: {nama_peminjam}")
    print(f"Judul buku: {judul_buku}")
    print(f"Status: aktif dipinjam")
    print("===========================\n")

def mengembalikan_buku(nama_peminjam, judul_buku, terlambat_hari):
    global daftar_peminjaman_aktif, total_denda

    daftar_peminjaman_aktif.remove(f"{nama_peminjam} - {judul_buku}")
    denda_hari_ini = 0

    if terlambat_hari > 0:
        denda_hari_ini = terlambat_hari * 5000
        total_denda = total_denda + denda_hari_ini

    print(f"== LAPORAN PENGEMBALIAN BUKU {NAMA_PERPUSTAKAAN.upper()}")
    print(f"Nama peminjam: {nama_peminjam}")
    print(f"Judul buku: {judul_buku}")
    print(f"Terlambat mengembalikan: {terlambat_hari} hari")
    print(f"Denda: {denda_hari_ini:,}")
    print("====================\n")

def laporan_perpustakaan():
    # Panggil semua variabel global yang mau kita pamerkan di laporan
    global daftar_peminjaman_aktif, total_buku_keluar, total_denda

    print(f"=========================================")
    print(f"     LAPORAN TOTAL {NAMA_PERPUSTAKAAN.upper()}     ")
    print(f"=========================================")
    print(f" Total Buku Pernah Keluar : {total_buku_keluar} kali")
    print(f" Total Pendapatan Denda  : Rp {total_denda:,}")
    print(f"-----------------------------------------")
    print(f" Buku Belum Dikembalikan : {daftar_peminjaman_aktif}")
    print(f"=========================================\n")

# SIMULASI AKTIVITAS PERPUSTAKAAN, (setelah buat semua fungsi dan tinggal buat datanya)

# 1. Thoriq dan Asep pinjam buku
pinjam_buku("Thoriq", "Buku Python")
pinjam_buku("Asep", "Buku Struktur Data")

# 2. Thoriq mengembalikan buku tepat waktu (0 hari telat)
mengembalikan_buku("Thoriq", "Buku Python", terlambat_hari=0)

# 3. Asep mengembalikan buku terlambat 3 hari
mengembalikan_buku("Asep", "Buku Struktur Data", terlambat_hari=3)

# 4. Cetak laporan akhir untuk melihat statistik perpustakaan
laporan_perpustakaan()
print()

# PROJECT 2 - STRUK PARKIR
MALL_NAME = "UBERTOS"
bike_total = 0
car_total = 0

def calculate_parking(vehicle_name, duration):
    global bike_total, car_total

    if vehicle_name == "bike":
        cost = duration * 2000
        bike_total = bike_total + 1
    elif vehicle_name == "car":
        cost = duration * 3000
        car_total = car_total + 1
    else:
        cost = 0
    
    print(f"=== {MALL_NAME} MALL PARKING REPORTS ===")
    print(f"Vehicle type: {vehicle_name}")
    print(f"Parking duration: {duration}")
    print(f"Total cost: {cost}")
    print("====================\n")

def final_calculate():
    global bike_total, car_total

    print(f"=== FINAL PARKING {MALL_NAME}'S REPORTS ===")
    print(f"Total number of motorcycles entering: {bike_total}")
    print(f"Total number of cars entering: {car_total}")
    print("====================\n")


# MAKING DATA
calculate_parking("bike", duration=3)
calculate_parking("car", duration=4)
calculate_parking("car", duration=5)
calculate_parking("bike", duration=6)

final_calculate()
print()

# PROJECT 3 - XII CINEMA TICKETING
app_name = "XII CINEMA"
total_revenue = 0

def usr_buy_ticket(customer_name, customer_age, day_type):
    global total_revenue

    if customer_age < 17:
        cost = 0
        status = "FAILED! Underage for this movie!"
    else:
        if day_type == "weekday":
            cost = 40000
        elif day_type == "weekend":
            cost = 50000
        
        total_revenue = total_revenue + cost
        status = "SUCCESS! Enjoy the movie!"

    # MAIN CODE PRINT HERE: Moved OUTSIDE the if-else blocks (unshifted to the left), avoiding error, if it still placed inside else block, < 17 age wouldn't be printed
    print(f"=== {app_name} TICKETING ===")
    print(f"Customer name: {customer_name}")
    print(f"Day type: {day_type}")
    print(f"Status: {status}")
    print(f"Total cost: Rp {cost:,}")
    print("==================\n")

def final_reports():
    global total_revenue

    print(f"=== {app_name} FINANCIAL REPORTS ===")
    print(f"Total daily revenue: {total_revenue:,}")
    print("==================\n")

# FINAL: INSERTING DATA TO FUNCTION
usr_buy_ticket("Reffa", customer_age=18, day_type="weekend")
usr_buy_ticket("Asep", customer_age=15, day_type="weekday")
final_reports()
print()

# PROJECT 3 - XII CINEMA TICKETING (ADDED INSERT FEATURES ON TERMINAL MANUALLY BY USER)
app_name = "XII CINEMA"
total_revenue = 0

def usr_buy_ticket(customer_name, customer_age, day_type):
    global total_revenue

    if customer_age < 17:
        cost = 0
        status = "FAILED! Underage for this movie!"
    else:
        if day_type == "weekday":
            cost = 40000
        elif day_type == "weekend":
            cost = 50000
        
        total_revenue = total_revenue + cost
        status = "SUCCESS! Enjoy the movie!"

    # MAIN CODE PRINT HERE: Moved OUTSIDE the if-else blocks (unshifted to the left), avoiding error, if it still placed inside else block, < 17 age wouldn't be printed
    print(f"=== {app_name} TICKETING ===")
    print(f"Customer name: {customer_name}")
    print(f"Day type: {day_type}")
    print(f"Status: {status}")
    print(f"Total cost: Rp {cost:,}")
    print("==================\n")

def final_reports():
    global total_revenue

    print(f"=== {app_name} FINANCIAL REPORTS ===")
    print(f"Total daily revenue: {total_revenue:,}")
    print("==================\n")

# --- INTERACTIVE TERMINAL INPUT ---

print(f"=== WELCOME TO {app_name} SYSTEM ===")

# 1. Capture the customer's name (Text/String)
name_input = input("Enter customer name: ")

# 2. Capture the age and immediately convert it to an Integer number
age_input = int(input("Enter customer age: "))

# 3. Capture the day type (Text/String)
day_input = input("Enter day type (weekday/weekend): ")

print("\nProcessing your ticket...\n")

# 4. Pass your manual inputs into your amazing function!
usr_buy_ticket(customer_name=name_input, customer_age=age_input, day_type=day_input)

# 5. Show the final financial report
final_reports()

# PROJECT 4: INTERACTIVE COUNTER SYSTEM (MADE BY GEMINI)
app_name = "REFF SYSTEM"
total_actions = 0

def log_action(user_name):
    global total_actions
    total_actions = total_actions + 1
    print(f"[{app_name}] Action recorded for: {user_name}!")
    print(f"Total actions performed so far: {total_actions}\n")

# --- THE WHILE LOOP (The Alive Machine) ---
# We use a boolean flag to keep the loop running
is_running = True

print(f"=== WELCOME TO {app_name.upper()} ===")
print("Type your name to log an action, or type 'exit' to turn off the system.\n")

while is_running == True:
    # 1. Take terminal input
    user_input = input("Enter name (or 'exit'): ")
    
    # 2. Check if the user wants to quit
    if user_input == "exit":
        print("\nShutting down the system...")
        is_running = False # This breaks the loop mathematically on the next check!
    else:
        # 3. If they didn't type exit, send the name to our function pipeline!
        log_action(user_name = user_input)

# This line only runs AFTER the loop becomes False and finishes
print("=== SYSTEM OFF. GOODBYE! ===")
print()

# PROJECT 5 - SERVER MONITOR (MADE BY GEMINI)
# SIMPLIFIED SERVER MONITOR
server_status = "ONLINE"
total_checks = 0
is_monitored = True

print("=== CYBERNET SERVER MONITOR ACTIVATED ===")
print("Commands: 'check', 'break', 'fix', 'poweroff'\n")

while is_monitored == True:
    # 1. Ask the user for a command
    command = input("Enter command: ")
    
    # 2. Check what the user typed using our trusty if-elif structure
    if command == "check":
        total_checks = total_checks + 1
        print(f"[PING] Health check #{total_checks} performed.")
        print(f"Current Status: {server_status}")
        
    elif command == "break":
        server_status = "MAINTENANCE"
        print("[ALERT] Server forced into MAINTENANCE mode!")
        
    elif command == "fix":
        server_status = "ONLINE"
        print("[RESOLVED] Server is back ONLINE!")
        
    elif command == "poweroff":
        print("Shutting down monitor system...")
        is_monitored = False # This turns off the loop switch!
        
    else:
        print("Unknown command! Please use check, break, fix, or poweroff.")
        
    print("----------------------------------------\n")

print("=== SYSTEM OFF ===")