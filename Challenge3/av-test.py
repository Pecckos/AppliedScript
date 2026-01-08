import os
import platform
import time

system = platform.system()

if system == "Windows":
    # Continue with Windows-specific logic
    print("Windows detected. Script execution continues..")

elif system == "Linux":
    print("Linux detected. This script is intended for Windows only.")
    exit()

elif system == "Darwin":
    print("macOS detected. This script is intended for Windows only.")
    exit()

else:
    print(f"Unknown operating system ({system}). This script is intended for Windows only. Aborting execution.")
    exit()

# EICAR testfile string
# Create desktop path and file path
eicar_str = "X5O!P%@AP[4\\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*"
desktop_path = os.path.join(os.environ['USERPROFILE'], 'Desktop')
file_path = os.path.join(desktop_path, "eicar_testfile.txt")

#Write EICAR string to file
try:
    with open(file_path, "w") as f:
        f.write(eicar_str)
    print(f"EICAR testfile created: {file_path}")
except Exception as e:
    print(f"Error creating EICAR testfile: {e}")
    exit(1)
    
print("[...] Waiting for antivirus to scan the file...")
time.sleep(5)  # Wait for antivirus to scan the file

if not os.path.exists(file_path):
    print("EICAR testfile deleted.")
    print("EICAR testfile has been removed by AV/EDR.")
    print("Antivirus is functioning correctly.")
    exit(0)

try: 
    with open(file_path, "r") as f:
        content = f.read()
    if content == eicar_str:
        print("EICAR testfile is still present and intact.")
        print("Antivirus did not detect the EICAR testfile.")
    else:
        print("EICAR testfile content has been altered.")
        print("Antivirus may have partially detected the EICAR testfile.")
except Exception as e:
    print(f"[...]Could not read the EICAR testfile: {e}")
    print("Antivirus may have interfered with the EICAR testfile.")
    print("Antivirus is functioning correctly.")
