import time

APP_NAME = "daily finance"
database_user = {}
active_user = None

def register():
    new_user = input("Enter username: ").strip() # berfungsi untuk menghapus spasi liar (termasuk tab atau newline) yang tidak sengaja terketik di awal dan di akhir teks.

    if not new_user:
<<<<<<< HEAD
        print("Please input your username!")
=======
        print("Please input your username")
>>>>>>> 1dc58dadeeea7e684dea25d4b73b936e14044a82
        return False

    if new_user in database_user:
        print("Username already taken!")
        return False

    while True:
        new_password = input("Enter password: ")
        if len(new_password) >= 8:                  # mengecek kondisi apakah password lebih dari 8 atau tidak
            break
        else:
<<<<<<< HEAD
            print("Password must be at least 8 characters long!")
=======
            print("Password must 8 characters")
>>>>>>> 1dc58dadeeea7e684dea25d4b73b936e14044a82
    
    full_name = input("Enter your full name: ").strip()

    while True:
        phone_number = input("Enter phone number: ")
        if phone_number.isdigit():
            break
        else:
<<<<<<< HEAD
            print("Phone number must contain numbers only!")
=======
            print("Phone must numbers!")
>>>>>>> 1dc58dadeeea7e684dea25d4b73b936e14044a82
    
    while True:
        email = input("Enter email: ").strip()
        if "@" in email and "." in email:
            break
        else:
            print("Invalid email format! Example: name@domain.com")
    
<<<<<<< HEAD
    database_user[new_user] = {
=======
    database[new_user] = {
>>>>>>> 1dc58dadeeea7e684dea25d4b73b936e14044a82
        "password": new_password,
        "full_name": full_name,
        "phone": phone_number,
        "email": email,
        "created_at": time.ctime(),
        "balance": 0,
        "transaction": [] # List transaksi
    }

<<<<<<< HEAD
    print(f"\n[+] Registration successful! Please login, {full_name}.")
=======
    print(f"Registration success! Please login {full_name}")
>>>>>>> 1dc58dadeeea7e684dea25d4b73b936e14044a82
    return True

def login():
    global active_user

<<<<<<< HEAD
    print(f"\n--- Login to {APP_NAME.title()} App ---")
=======
    print(f"Login to {APP_NAME}.title() App")
>>>>>>> 1dc58dadeeea7e684dea25d4b73b936e14044a82

    username = input("Enter username: ").strip()
    password = input("Enter password: ")

    if username not in database_user:
        print("Username not found! Please register first.")
        return False

    if database_user[username]["password"] == password:
        active_user = username
        print(f"\n[+] Login success! Welcome back, {database_user[username]['full_name']}.")
        return True
    else:
        print("Incorrect password! Login failed.")
        return False

def show_profile():
    if not active_user:
<<<<<<< HEAD
        print("You are not logged in!")
        return
    
    user_info = database_user[active_user]
    print(f"\n=== User Profile ({active_user}) ===")
    print(f"Full name        : {user_info['full_name']}")
    print(f"Phone number     : {user_info['phone']}")
    print(f"Email            : {user_info['email']}")
    print(f"Current balance  : Rp {user_info['balance']:,}")
    print(f"Register time    : {user_info['created_at']}")

def add_transaction(transaction_type):
    if not active_user:
        print("You haven't logged in, please login first!")
        return

    print(f"\n=== Add {transaction_type.title()} ===")

    while True:
        try:
            nominal = int(input("Enter amount (Rp): "))
            if nominal <= 0:
                print("Amount must be greater than 0!")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter numbers only.")

    description = input("Enter description (ex: Salary, Lunch): ").strip()
=======
        print("Anda belum login!")
        return
    
    user_info = database_user[active_user]
    print(f"\n=== User profile ({active_user}) ===")
    print(f"Full name        : {user_info['full_name']}")
    print(f"Phone number     : {user_info['phone_number']}")
    print(f"Email            : {user_info['email']}")
    print(f"Current balance  : Rp {user_info['saldo']:,}")
    print(f"Register time    : {user_info['created_at']}")

def add_transaction(tipe):
    if not active_user:
        print("You haven't login, please login first!")
        return

    print(f"\n=== Add {tipe.title()} ===")

    while True:
        try:
            nominal = int(input("Input nomimal (Rp): "))
            if nominal <= 0:
                print("Nominal must greater than 0!")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter number.")

    keterangan = input("Enter information (ex: Salary, Lunch): ").strip()
>>>>>>> 1dc58dadeeea7e684dea25d4b73b936e14044a82
    
    user_data = database_user[active_user]

    # jika pengeluaran, cek apakah saldo cukup
<<<<<<< HEAD
    if transaction_type == "expense" and nominal > user_data["balance"]:
        print(f"\n[-] Transaction FAILED! Insufficient balance. (Current balance: Rp {user_data['balance']:,})")
        return

    # Update saldo
    if transaction_type == "income":
        user_data["balance"] += nominal
    elif transaction_type == "expense":
        user_data["balance"] -= nominal

    # Catat data transaksi ke riwayat
    catatan = {
        "type": transaction_type,
        "nominal": nominal,
        "description": description,
        "time": time.strftime("%d-%m-%Y %H:%M")
    }
    user_data["transaction"].append(catatan)

    print(f"\n[+] {transaction_type.title()} recorded successfully!")
    print(f"Updated Balance: Rp {user_data['balance']:,}")
=======
    if tipe == "pengeluaran" and nominal > user_data["saldo"]:
        print(f"\n[-] Transaksi GAGAL! Saldo Anda tidak cukup. (Saldo saat ini: Rp {user_data['saldo']:,})")
        return

    # Update saldo
    if tipe == "pemasukan":
        user_data["saldo"] += nominal
    elif tipe == "pengeluaran":
        user_data["saldo"] -= nominal

    # Catat data transaksi ke riwayat
    catatan = {
        "tipe": tipe,
        "nominal": nominal,
        "keterangan": keterangan,
        "waktu": time.strftime("%d-%m-%Y %H:%M")
    }
    user_data["transaksi"].append(catatan)

    print(f"\n[+] {tipe.title()} berhasil dicatat!")
    print(f"Saldo terbaru Anda: Rp {user_data['saldo']:,}")
>>>>>>> 1dc58dadeeea7e684dea25d4b73b936e14044a82

def show_transactions():
    """Fungsi untuk melihat riwayat transaksi & ringkasan saldo"""
    if not active_user:
<<<<<<< HEAD
        print("You are not logged in!")
        return

    user_data = database_user[active_user]
    riwayat = user_data["transaction"]

    print(f"\n=== Transaction History & Financials [{active_user}] ===")
    print(f"Current Balance: Rp {user_data['balance']:,}\n")

    if not riwayat:
        print("No transaction records found.")
        return

    print(f"{'No':<3} | {'Time':<16} | {'Type':<11} | {'Amount':<12} | {'Description'}")
    print("-" * 65)

    for i, item in enumerate(riwayat, start=1):
        tanda = "+" if item["type"] == "income" else "-"
        nominal_str = f"{tanda}Rp {item['nominal']:,}"
        print(f"{i:<3} | {item['time']:<16} | {item['type'].title():<11} | {nominal_str:<12} | {item['description']}")
=======
        print("Anda belum login!")
        return

    user_data = database_user[active_user]
    riwayat = user_data["transaksi"]

    print(f"\n=== Riwayat Transaksi & Keuangan [{active_user}] ===")
    print(f"Saldo Saat Ini: Rp {user_data['saldo']:,}\n")

    if not riwayat:
        print("Belum ada riwayat transaksi.")
        return

    print(f"{'No':<3} | {'Waktu':<16} | {'Tipe':<11} | {'Nominal':<12} | {'Keterangan'}")
    print("-" * 65)

    for i, item in enumerate(riwayat, start=1):
        tanda = "+" if item["tipe"] == "pemasukan" else "-"
        nominal_str = f"{tanda}Rp {item['nominal']:,}"
        print(f"{i:<3} | {item['waktu']:<16} | {item['tipe'].title():<11} | {nominal_str:<12} | {item['keterangan']}")
>>>>>>> 1dc58dadeeea7e684dea25d4b73b936e14044a82


def main_menu():
    global active_user
    while True:
        print(f"\n==============================")
<<<<<<< HEAD
        print(f"     {APP_NAME.upper()} APP")
=======
        print(f"   APLIKASI {APP_NAME.upper()}")
>>>>>>> 1dc58dadeeea7e684dea25d4b73b936e14044a82
        print(f"==============================")
        
        if active_user is None:
            # Menu sebelum login
            print("1. Register")
            print("2. Login")
<<<<<<< HEAD
            print("3. Exit")
            pilihan = input("Select menu (1-3): ").strip()
=======
            print("3. Keluar")
            pilihan = input("Pilih menu (1-3): ").strip()
>>>>>>> 1dc58dadeeea7e684dea25d4b73b936e14044a82

            if pilihan == "1":
                register()
            elif pilihan == "2":
                login()
            elif pilihan == "3":
<<<<<<< HEAD
                print("Thank you for using this app!")
                break
            else:
                print("Invalid choice!")
        else:
            # Menu setelah login (Ditambahkan Fitur Keuangan)
            print(f"Status: Logged in as [{active_user}]")
            print("1. View Profile & Balance")
            print("2. Add Income (+)")
            print("3. Add Expense (-)")
            print("4. View Transaction History")
            print("5. Logout")
            print("6. Exit App")
            pilihan = input("Select menu (1-6): ").strip()
=======
                print("Terima kasih telah menggunakan aplikasi ini!")
                break
            else:
                print("Pilihan tidak valid!")
        else:
            # Menu setelah login (Ditambahkan Fitur Keuangan)
            print(f"Status: Logged in as [{active_user}]")
            print("1. Lihat Profil & Saldo")
            print("2. Catat Pemasukan (+)")
            print("3. Catat Pengeluaran (-)")
            print("4. Lihat Riwayat Transaksi")
            print("5. Logout")
            print("6. Keluar Aplikasi")
            pilihan = input("Pilih menu (1-6): ").strip()
>>>>>>> 1dc58dadeeea7e684dea25d4b73b936e14044a82

            if pilihan == "1":
                show_profile()
            elif pilihan == "2":
<<<<<<< HEAD
                add_transaction("income")
            elif pilihan == "3":
                add_transaction("expense")
            elif pilihan == "4":
                show_transactions()
            elif pilihan == "5":
                print(f"User {active_user} successfully logged out.")
                active_user = None
            elif pilihan == "6":
                print("Thank you for using this app!")
                break
            else:
                print("Invalid choice!")
=======
                add_transaction("pemasukan")
            elif pilihan == "3":
                add_transaction("pengeluaran")
            elif pilihan == "4":
                show_transactions()
            elif pilihan == "5":
                print(f"User {active_user} berhasil logout.")
                active_user = None
            elif pilihan == "6":
                print("Terima kasih telah menggunakan aplikasi ini!")
                break
            else:
                print("Pilihan tidak valid!")
>>>>>>> 1dc58dadeeea7e684dea25d4b73b936e14044a82

# Jalankan Program Utama
main_menu()