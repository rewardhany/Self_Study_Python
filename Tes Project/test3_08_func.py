# This continued from test2_08_func.py file, however on this file we are going to learn more about advanced function combined with multiple materials as we wrote on others file before, but first we learn about looping such a while, for, , so we can see how loops integrated with function

# PROJECT 6 - TERMINAL INTERFACE
security_code = "cyber77"
is_locked = True

print("=== SECURE TERMINAL INTERFACE ===\n")

while is_locked == True:
    access_key = input("Enter Access key to unlock terminal: ")

    if access_key == security_code:
        print("[SUCCESS] Key verified. Decrypting files...")
        is_locked = False # This turns off the loop!
    else:
        print("[WARNING] ACCESS DENIED! Invalid Key. Try again.\n")

print("\n=== WELCOME BACK, ROOT USER ===\n")

# PROJECT 7 - LOGIN INTERFACE
password = "Wardany191407"
username = "Rearchived"
is_locked = True

print("=== LOGIN ===")

while is_locked == True:
    input_username = input("Enter your user name: ")
    input_password = input("Enter password: ")

    if input_username == username and input_password == password:
        print(f"\nLogin Successfully!")
        is_locked = False
    elif input_username == username:
        print("\nWrong password! Try again.\n")
    else:
        print("\nIncorrect username or password! Try again.\n")

print(f"=== WELCOME BACK {input_username.upper()} ===\n")

# PROJECT 8 - LOCKSCREEN UNLOCK
import time
lockscreen_pin = "121017"
is_locked = True
attempt = 0

print("=== DEVICE IS LOCKED ===")

while is_locked == True:
    input_pin = input("Enter your PIN to unlock device: ")

    if input_pin == lockscreen_pin:
        print("[SUCCESS] Device is now unlocked")
        is_locked = False
    else:
        attempt = attempt + 1
        print(f"[FAILED] Incorrect PIN (Attempts: {attempt}/5)\n")
        
        # Check if they reached the maximum limit of 5
        if attempt == 5:
            print("[CRITICAL] Too many failed attempts!")
            print("Device is locked temporarily, please wait 30 seconds...")

            time.sleep(30) # adjust time to 30s

            attempt = 0 # Reset the counter back to 0 so they get 5 fresh attempts after waiting, not continuing to 6 or 7 attempts
            print("\n=== SYSTEM READY. TRY AGAIN ===")

print("\n=== WELCOME BACK TO YOUR HOME SCREEN ===\n")

# PROJECT 9 - SMART AC AUTO REGULATOR
ac_status = "OFF"
is_monitoring = True

print("=== SMART AC AUTO REGULATOR ACTIVATED ===")
print("(Type < -50 or > 100 to power down the regulator)\n")

while is_monitoring == True: # Your loop is told to keep running as long as that switch stays True:
    input_temp = int(input("Enter current room temperature (°C): "))

    if input_temp < -50 or input_temp > 100:
        print(f"\n[CRITICAL ERROR] Insane data detected: {input_temp}°C")
        print("Shutting down regulator... Goodbye")

        is_monitoring = False # loop ended and system terminated when user type -51 or even 101 and more

    elif input_temp > 27:
        ac_status = "ON MAX (COOLING)\n"
        print("[WARNING] Temperature is too high!")
        print(f">> AC System: {ac_status}")
    
    else:
        ac_status = "OFF (ROOM SAFE)\n"
        print("[STATUS] Temperature is normal")
        print(f">> AC System: {ac_status}")
        pass

print("=== MONITORING TERMINATED. SYSTEM IS SAFELY OFFLINE. ===\n")

# PROJECT 10 - IoT SMART LED CONTROLLER
# main func
def activate_led(light_color):
    uppercase_color = light_color.upper()
    print(f">>> [LED DEVICE] Switching hardware to {uppercase_color} light! Matrix updated.")

# initializing loop logic
is_led_running = True

print("=== IoT LED INITIALIZED ===")
print("Available colors: 'red', 'green', 'blue'")
print("Type 'off' to shutdown the controller.")

while is_led_running == True:
    user_input = input("\nEnter LED color: ")

    if user_input == "off":
        print("Powering down smart LED system... Goodbye.")
        is_led_running = False # Turns off the loop
    
    elif user_input == "red" or user_input == "green" or user_input == "blue":
        activate_led(user_input)
        pass # if u let it blank use pass

    else:
        print("[ERROR] Color not supported by hardware matrix.")
print()

# PROJECT 11: NETWORK PING ANALYZER
def analyze_latency(ms):
    if ms < 100:
        return "STABLE"
    else:
        return "UNSTABLE"

monitor_active = True

print("=== NETWORK MONITOR READY ===")
print("(Type  < 0 to exit)")

while monitor_active == True:
    user_input = int(input("\nEnter network latency (ms): "))

    if user_input <= -1:
        print("Exiting Network Monitor. System offline.")
        monitor_active = False
    else:
        status = analyze_latency(user_input)
        print(f">>> [ANALYSIS]: Connection is {status}")

        if status == "STABLE":
            print(">>> [HARDWARE ACTION]: Turning on Green LED Matrix...")
        else:
            print(">>> [HARDWARE ACTION]: !!! BUZZER ALARM SOUNDED !!!")

print()

 