import sys
import os

    print("Installing the python modules required 
    ..")

    if sys.platform.startswith("win"):
        os.system("python -m pip install --upgrade pip")
        os.system("python -m pip install -r requirements.txt")
        os.system("python cyb3rtech.py")

    elif sys.platform.startswith("linux"):
        os.system("python3 -m pip3 install --upgrade pip")
        os.system("python3 -m pip3 install -r requirements.txt")
        os.system("python3 cyb3rtech.py")

except Exception as e:
    print(e)
    os.system("pause")
