import time

APP_NAME = "daily finance"
database_user = {}
active_user = None

def register():
    new_user = input("Enter username: ").strip() # berfungsi untuk menghapus spasi liar (termasuk tab atau newline) yang tidak sengaja terketik di awal dan di akhir teks.

    if not new_user:
        print("Please input your username")
        return False

    if new_user in database_user:
        print("Username already taken!")
        return False

    while True:
        new_password = input("Enter password: ")
        if len(new_password) >= 8:                  # mengecek kondisi apakah password lebih dari 8 atau tidak
            break
        else:
            print("Password must 8 characters")
    
    full_name = input("Enter your full name: ").strip()

    while True:
        phone_number = input("Enter phone number: ")
        if phone_number.isdigit():
            break
        else:
            print("Phone must numbers!")
    
    while True:
        email = input("Enter email: ").strip()
        if "@" in email and "." in email:
            break
        else:
            print("Invalid email format! Example: name@domain.com")
    
    database[new_user] = {
        "password": new_password,
        "full_name": full_name,
        "phone": phone_number,
        "email": email,
        "created_at": time.ctime(),
        "balance": 0,
        "transaction": [] # List transaksi
    }

    print(f"Registration success! Please login {full_name}")
    return True

def login():
    global active_user

    print(f"Login to {APP_NAME}.title() App")

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
    
    user_data = database_user[active_user]

    # jika pengeluaran, cek apakah saldo cukup
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

def show_transactions():
    """Fungsi untuk melihat riwayat transaksi & ringkasan saldo"""
    if not active_user:
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


def main_menu():
    global active_user
    while True:
        print(f"\n==============================")
        print(f"   APLIKASI {APP_NAME.upper()}")
        print(f"==============================")
        
        if active_user is None:
            # Menu sebelum login
            print("1. Register")
            print("2. Login")
            print("3. Keluar")
            pilihan = input("Pilih menu (1-3): ").strip()

            if pilihan == "1":
                register()
            elif pilihan == "2":
                login()
            elif pilihan == "3":
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

            if pilihan == "1":
                show_profile()
            elif pilihan == "2":
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

# Jalankan Program Utama
main_menu()