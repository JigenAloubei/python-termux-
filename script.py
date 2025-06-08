# script.py
import os
import datetime

def system_info():
    print("📱 Termux Python Script")
    print(f"🕒 Time: {datetime.datetime.now()}")
    print("📂 Current Directory Contents:\n")
    os.system("ls -la")

if __name__ == "__main__":
    system_info()
