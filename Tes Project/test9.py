import time

APP_NAME = "daily finance"
database_user = {}
active_user = None

def register():
    new_user = input("Enter username: ").strip() # berfungsi untuk menghapus spasi liar (termasuk tab atau newline) yang tidak sengaja terketik di awal dan di akhir teks.

    if not new_user:
        print("Please input your username!")
        return False

    if new_user in database_user:
        print("Username already taken!")
        return False

    while True:
        new_password = input("Enter password: ")
        if len(new_password) >= 8:                  # mengecek kondisi apakah password lebih dari 8 atau tidak
            break
        else:
            print("Password must be at least 8 characters long!")
    
    full_name = input("Enter your full name: ").strip()

    while True:
        phone_number = input("Enter phone number: ")
        if phone_number.isdigit():
            break
        else:
            print("Phone number must contain numbers only!")
    
    while True:
        email = input("Enter email: ").strip()
        if "@" in email and "." in email:
            break
        else:
            print("Invalid email format! Example: name@domain.com")
    
    database_user[new_user] = {
        "password": new_password,
        "full_name": full_name,
        "phone": phone_number,
        "email": email,
        "created_at": time.ctime(),
        "balance": 0,
        "transaction": [] # List transaksi
    }

    print(f"\n[+] Registration successful! Please login, {full_name}.")
    return True

def login():
    global active_user

    print(f"\n--- Login to {APP_NAME.title()} App ---")

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
    
    user_data = database_user[active_user]

    # jika pengeluaran, cek apakah saldo cukup
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

def show_transactions():
    """Fungsi untuk melihat riwayat transaksi & ringkasan saldo"""
    if not active_user:
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


def main_menu():
    global active_user
    while True:
        print(f"\n==============================")
        print(f"     {APP_NAME.upper()} APP")
        print(f"==============================")
        
        if active_user is None:
            # Menu sebelum login
            print("1. Register")
            print("2. Login")
            print("3. Exit")
            pilihan = input("Select menu (1-3): ").strip()

            if pilihan == "1":
                register()
            elif pilihan == "2":
                login()
            elif pilihan == "3":
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

            if pilihan == "1":
                show_profile()
            elif pilihan == "2":
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

# Jalankan Program Utama
main_menu()