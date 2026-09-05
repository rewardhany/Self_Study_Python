# misalkan 

brand = [
    "samsung", 
    "apple", 
    "xiaomi", 
    "huawei", 
    "oppo", 
    "tecno", 
    "infinix", 
    "vivo",
    "xiaomi"
]
print(brand[2:5])
# output xiaomi, huawei, oppo

print("apple brand count is:", brand.count("apple"))
# output 1
# this is method 1: which means PRINT DENGAN KOMA (Argumen Terpisah)
# how it works : sends 2 data separated to print()
# Python automatically gives 1 space between commas.

print("xiaomi brand count is {} ".format(brand.count("xiaomi")))
# output 2
# this is method 2: METODE .format() (String Formatting)
# Cara kerja: Tanda {} adalah penampung.
# Nilai di dalam .format() akan menggantikan posisi {} tersebut.

print(f"huawei brand count:{brand.count('huawei')}")
# output 1
# this is method 3: F-STRING (Formatted String Literal)
# Cara kerja: "f" di depan string membuat Python bisa membaca variabel
#             langsung di dalam tanda {}.
# Kelebihan: Paling singkat dan mudah dibaca.

# sesuaikan aja balik lagi ke diri sendiri enaknya pake yang mana

brand[0] = "nokia"
print(f"\nthis is brand that just updated: {brand}")

# add brand by insert at index 0
brand.insert(0, "realme")
print(f"this is brand that just inserted: {brand}")

# del brand by remove first item in list
brand.remove("realme")
print(f"this is brand that just removed: {brand}")

# add brand by append at the end of list
brand.append("motorola")
print(f"this is brand that just appended: {brand}")

# update brand at index 2
brand[2] = "nokia"
print(f"this is brand that just updated: {brand}")

# del brand by remove at index 2
brand.pop(2)
print(f"this is brand that just removed: {brand}")

# count the brand name
print(f"brand count: {brand.count("apple")}")

# remove all brand
brand.clear()
print(f"this is brand that just removed: {brand}")
