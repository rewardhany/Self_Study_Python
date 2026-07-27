import time

# 1. DATA MENTAH DARI SERVER (Biasanya ribuan baris, kita ambil contoh 10 log)
# Format log: "IP_Address - STATUS"
raw_logs = [
    "192.168.1.50 - FAILED",
    "10.0.0.12 - SUCCESS",
    "192.168.1.50 - FAILED",
    "192.168.1.50 - FAILED",
    "172.16.254.1 - SUCCESS",
    "10.0.0.12 - FAILED",
    "192.168.1.50 - FAILED",
    "10.0.0.12 - FAILED",
    "10.0.0.12 - FAILED",
    "192.168.1.99 - FAILED"
]

print("=== SYSTEM SECURITY SECURITY MONITOR ===")
print("Memulai pemindaian server log...")
time.sleep(1.5)

# Dictionary kosong untuk menghitung berapa kali tiap IP melakukan percobaan gagal
# Format target: {"IP_Address": jumlah_gagal}
failed_counter = {}


# ──────────────────────────────────────────────────────────────────
# 2. LOOPING PERTAMA: Membaca log satu per satu & Menghitung yang Gagal
# ──────────────────────────────────────────────────────────────────
for log in raw_logs:
    # Kita gunting data menggunakan .split() di bagian " - "
    # Misal "192.168.1.50 - FAILED" -> ["192.168.1.50", "FAILED"]
    parts = log.split(" - ")
    ip_address = parts[0]
    status = parts[1]

    # Kita hanya peduli pada status yang "FAILED"
    if status == "FAILED":
        # Jika IP ini sudah ada di dalam dictionary failed_counter, tambah angkanya (+1)
        if ip_address in failed_counter:
            failed_counter[ip_address] += 1
        # Jika IP ini baru pertama kali gagal, masukkan ke dictionary dengan nilai awal 1
        else:
            failed_counter[ip_address] = 1


# ──────────────────────────────────────────────────────────────────
# 3. LOOPING KEDUA: Memasukkan IP Nakal ke Blacklist (Gagal >= 3x)
# ──────────────────────────────────────────────────────────────────
blacklist_ips = []

# .items() di bawah ini digunakan untuk mengambil (key, value) sekaligus dari Dictionary
for ip, total_failed in failed_counter.items():
    if total_failed >= 3:
        blacklist_ips.append(ip)  # Masukkan IP ke dalam list Blacklist


# ──────────────────────────────────────────────────────────────────
# 4. MEMBUAT LAPORAN UNTUK ATASAN
# ──────────────────────────────────────────────────────────────────
print("\nHASIL ANALISIS LOG:")
print("-" * 45)
for ip, total in failed_counter.items():
    print(f"IP: {ip:<15} | Total Gagal Login: {total} kali")
print("-" * 45)

print("\nTINDAKAN KEAMANAN OTOMATIS:")
if len(blacklist_ips) > 0:
    print("🚨 WARNING! IP berikut terdeteksi melakukan serangan Brute-Force:")
    for blocked_ip in blacklist_ips:
        # Kita looping daftar blacklist untuk dicetak
        print(f"❌ BLOCKED: {blocked_ip} -> Akses ke server resmi ditutup!")
else:
    print("✅ AMAN: Tidak ada IP mencurigakan hari ini.")