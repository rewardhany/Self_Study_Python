# misalkan 
# ini adalah list brand smartphone ditandai dengan tanda []
# tanda () adalah tuple
# tanda {} adalah dict

import time

smartphone_list = [
    {"name": "samsung s25 ultra", "price": 17000000, "stock": 10},
    {"name": "apple iphone 17 pro max", "price": 27000000, "stock": 10},
    {"name": "xiaomi 17 ultra", "price": 12000000, "stock": 10},
    {"name": "huawei pura 90s pro max", "price": 14000000, "stock": 10},
    {"name": "oppo reno 15", "price": 10000000, "stock": 10},
    {"name": "tecno camon 50 pro", "price": 8000000, "stock": 10},
    {"name": "infinix note 60", "price": 7000000, "stock": 10},
    {"name": "vivo x300 ultra", "price": 9000000, "stock": 10},
    {"name": "motorola edge 70", "price": 11000000, "stock": 10},
    {"name": "infinix hot 50", "price": 5000000, "stock": 10},
    {"name": "poco x8 pro max", "price": 13000000, "stock": 10},
    {"name": "poco f9 ultra", "price": 15000000, "stock": 10},
    {"name": "google pixel 10 pro xl", "price": 18000000, "stock": 10},
    {"name": "honor magic 7 pro", "price": 16000000, "stock": 10},
    {"name": "realme 15 pro", "price": 12000000, "stock": 10},
    {"name": "asus zenfone 11 ultra", "price": 14000000, "stock": 10}
]

# def brand_total_check():
    #total = brand.count(name_brand.lower())

#    input_name_brand = input("Check Brand Name: ")
#    total = brand.count(input_name_brand.lower())
    
#    if total > 1:
#        print(f"there are {total} {input_name_brand.lower()} in brand")
#    elif total == 1:
#        print(f"there is only 1 {input_name_brand.lower()} in brand")
#    else:
#        print("there is no such brand name")

#def add_brand_name():

#    brand_name = input("Add Brand Name: ")
#    if brand_name.lower() in brand:
#        print(f"cannot add {brand_name} because it already exist in brand")
#    else:
#        brand.append(brand_name.lower())
#        print(f"add {brand_name} into brand")

#print("Tes fungsi 1")
#brand_total_check()

#print("Tes fungsi 2")
#add_brand_name()

#print(f"this is your brand name : {brand}")
        
#brand_total_check("xiaomi")
#brand_total_check("apple")
#brand_total_check("nokia")


#brand[0] = "asus zenfone"
#print("update brand name: ", brand)

print("\n=== WELCOME TO REFFA'S STORE ===")
print("\n[AVAILABLE SMARTPHONE LIST]\n")

for index, smartphone in enumerate(smartphone_list, start=1): # enum itu buat nambahin index number di list biasanya dari nol kaya array makanya kita set start=1 biar dari 1 pas dicetak
    smartphone_name = smartphone["name"].title()
    price = smartphone["price"]
    stock = smartphone["stock"]
    
    print(f"{index}. {smartphone_name} Rp{price:,} Stok: {stock}")

print()

def user_select_smartphone():
    ask_user_buy = input("Do you want to buy? (y/n): ")
    if ask_user_buy == "y":
        user_select = int(input("Select smartphone by number: "))
    elif ask_user_buy == "n":
        print("Thank you for visiting my store!")
        return
    else:
        print("Invalid input")
        return

    if 1 <= user_select <= len(smartphone_list):
        selected_smartphone = smartphone_list[user_select - 1]
        
        if selected_smartphone["stock"] > 0:

            selected_smartphone["stock"] -= 1
            
            selected_name = selected_smartphone["name"]
            selected_price = selected_smartphone["price"]
            remain_stock = selected_smartphone["stock"]

            print(f"Ordered item: {selected_name.title()}")
            print(f"Price: Rp{selected_price:,}")
            print(f"Stock left: {remain_stock}")
            print("Thank you for your purchase!")
        else:
            print(f"Error : {selected_smartphone['name']} is out of stock")
    else:
        print("Invalid number")



user_select_smartphone()
