import time

apps_logs = [
    "WhatsApp - Running",
    "Facebook - Running",
    "App Vault - Stopped",
    "TikTok - Running",
    "Google - Running",
    "Instagram - Stopped",
    "Youtube - Stopped",
    "Xiaomi Hyper AI - Stopped",
    "Mi Fitness - Running",
]

print("=== Boost Memory Speed ===")
print("Scanning apps run in background...")
time.sleep(3)

running_counter = {}

for app in apps_logs:
    split_app = app.split(" - ")
    name_app = split_app[0]
    status_app = split_app[1]

    if status_app == "Running":
        if name_app in running_counter:
            running_counter[name_app] += 1
        else:
            running_counter[name_app] = 1

for app, total_run in running_counter.items():
    if total_run >= 2:
        print(f"Closing {app}...")
        time.sleep(1)
        print(f"{app} closed successfully.")

print("\nMemory Boost Completed!")
