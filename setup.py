import sys
import os

print("Installing the python modules required...")

try:
    if sys.platform.startswith("win"):
        os.system("python -m pip install --upgrade pip")
        os.system("python -m pip install -r requirements.txt")
        os.system("python cyb3rtech.py")

    elif sys.platform.startswith("linux") or sys.platform.startswith("darwin"):  # darwin is the platform name for macOS
        os.system("python3 -m pip install --upgrade pip")
        os.system("python3 -m pip install -r requirements.txt")
        os.system("python3 cyb3rtech.py")

    else:
        print("Unsupported platform:", sys.platform)

except Exception as e:
    print("An error occurred:", e)
    if sys.platform.startswith("win"):
        os.system("pause")
