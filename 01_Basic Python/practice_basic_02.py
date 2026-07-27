# ======================================================
# PRACTICE BASIC 02
# ======================================================
# Fokus latihan:
# - input()
# - type casting
# - operator perbandingan (>, <, >=, <=)
# - operator logika (and, or, not)
# - ternary operator
# ======================================================


# ------------------------------------------------------
# SOAL 1: CEK KELULUSAN
# ------------------------------------------------------
# Buat program yang:
# 1. Meminta input nilai ujian (0 - 100)
# 2. Tentukan apakah siswa LULUS atau TIDAK LULUS
#
# KETENTUAN:
# - LULUS jika nilai >= 75
# - TIDAK LULUS jika nilai < 75
#
# CONTOH INPUT:
# Nilai: 80
#
# OUTPUT YANG DIHARAPKAN:
# Status kelulusan: LULUS


# ------------------------------------------------------
# SOAL 2: CEK NILAI SEMPURNA
# ------------------------------------------------------
# Buat program yang:
# 1. Meminta input nilai ujian
# 2. Cek apakah nilai tersebut adalah nilai sempurna
#
# KETENTUAN:
# - Nilai sempurna adalah 100
#
# CONTOH INPUT:
# Nilai: 100
#
# OUTPUT YANG DIHARAPKAN:
# Nilai sempurna


# ------------------------------------------------------
# SOAL 3: CEK RENTANG NILAI
# ------------------------------------------------------
# Buat program yang:
# 1. Meminta input nilai
# 2. Cek apakah nilai berada di rentang 75 sampai 100
#
# PETUNJUK:
# - Gunakan operator logika AND
#
# CONTOH INPUT:
# Nilai: 85
#
# OUTPUT YANG DIHARAPKAN:
# Nilai berada dalam rentang kelulusan


# ------------------------------------------------------
# SOAL 4: CEK NILAI TIDAK VALID
# ------------------------------------------------------
# Buat program yang:
# 1. Meminta input nilai
# 2. Cek apakah nilai TIDAK valid
#
# KETENTUAN:
# - Nilai valid: 0 sampai 100
#
# PETUNJUK:
# - Gunakan operator logika OR
#
# CONTOH INPUT:
# Nilai: 120
#
# OUTPUT YANG DIHARAPKAN:
# Nilai tidak valid


# ------------------------------------------------------
# SOAL 5: STATUS KELULUSAN (TERNARY)
# ------------------------------------------------------
# Buat program yang:
# 1. Meminta input nilai
# 2. Tentukan status kelulusan menggunakan TERNARY OPERATOR
#
# KETENTUAN:
# - nilai >= 75 -> "LULUS"
# - nilai < 75  -> "TIDAK LULUS"
#
# CONTOH INPUT:
# Nilai: 60
#
# OUTPUT YANG DIHARAPKAN:
# Status: TIDAK LULUS


# ------------------------------------------------------
# SOAL 6 (BONUS): CEK KELULUSAN & NILAI SEMPURNA
# ------------------------------------------------------
# Buat program yang:
# 1. Meminta input nilai
# 2. Cek:
#    - Apakah siswa LULUS
#    - Apakah nilainya sempurna
#
# PETUNJUK:
# - Gunakan operator logika AND
#
# CONTOH INPUT:
# Nilai: 100
#
# OUTPUT YANG DIHARAPKAN:
# Status: LULUS
# Nilai sempurna

# YOUR CODE STARTS HERE !

# ==== QUESTION NO 1 ====
print("== QUESTION NO 1 ==")

nilai = int(input("Masukkan Nilai Anda: "))
if nilai < 0 or nilai > 100:
    print("Nilai tidak valid")
elif nilai >= 75:
    print("LULUS")
else:
    print("TIDAK LULUS")

# === QUESTION NO 2 ===
print("== QUESTION NO 2 ==")

nilaiAnda = int(input("Masukkan Nilai: "))
if nilaiAnda == 100:
    print("Nilai sempurna")
else:
    print("Maksimalkan lagi!")

# === QUESTION NO 3 ===
print("== QUESTION NO 3 ==")

cek_nilai = int(input("Masukkan Nilai Kamu: "))
if cek_nilai >= 75 and cek_nilai <= 100:
    print("Nilai Anda berada dalam rentang kelulusan!")
else:
    print("Anda Tidak Lulus")

# === QUESTION NO 4 ===
print("== QUESTION NO 4==")

your_grade = int(input("Enter your grade: "))
if your_grade < 0 or your_grade > 100:
    print("Nilai tidak valid!")
else:
    print(f"Nilai anda: {your_grade}")

# === QUESTION NO 5 ===
print("== QUESTION NO 5==")

nilaiKamu = int(input("Masukkan nilai kamu: "))
hasilmu = "LULUS" if nilaiKamu >= 75 else "TIDAK LULUS"
print("Status:", hasilmu)

# === QUESTION NO 6 ===
print("== QUESTION NO 6 ==")

value = int(input("Masukkan nilai kamu: "))

if value >= 75:
    print("Status: LULUS")
    if value == 100 and value >= 75:
        print("Nilai Sempurna")
else:
    print("Status: Tidak Lulus")