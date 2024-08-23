from pywebcopy import save_website
import os
import time

menu = """
         █     █░▓█████  ▄▄▄▄       ▄████▄   ██▓     ▒█████   ███▄    █ ▓█████  ██▀███
        ▓█░ █ ░█░▓█   ▀ ▓█████▄    ▒██▀ ▀█  ▓██▒    ▒██▒  ██▒ ██ ▀█   █ ▓█   ▀ ▓██ ▒ ██▒
        ▒█░ █ ░█ ▒███   ▒██▒ ▄██   ▒▓█    ▄ ▒██░    ▒██░  ██▒▓██  ▀█ ██▒▒███   ▓██ ░▄█ ▒
        ░█░ █ ░█ ▒▓█  ▄ ▒██░█▀     ▒▓▓▄ ▄██▒▒██░    ▒██   ██░▓██▒  ▐▌██▒▒▓█  ▄ ▒██▀▀█▄
        ░░██▒██▓ ░▒████▒░▓█  ▀█▓   ▒ ▓███▀ ░░██████▒░ ████▓▒░▒██░   ▓██░░▒████▒░██▓ ▒██▒
        ░ ▓░▒ ▒  ░░ ▒░ ░░▒▓███▀▒   ░ ░▒ ▒  ░░ ▒░▓  ░░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
          ▒ ░ ░   ░ ░  ░▒░▒   ░      ░  ▒   ░ ░ ▒  ░  ░ ▒ ▒░ ░ ░░   ░ ▒░ ░ ░  ░  ░▒ ░ ▒░
          ░   ░     ░    ░    ░    ░          ░ ░   ░ ░ ░ ▒     ░   ░ ░    ░     ░░   ░
              ░       ░  ░ ░         ░ ░          ░  ░    ░ ░           ░    ░  ░   ░
                      ░    ░
"""
menu2 = """
[0] Back to main
[1] Clone Website
"""

def show_menu():
    print(f"\033[31m{menu}\033[0m")
    print(f"\033[31m{menu2}\033[0m")

def clone():
    print("\033[31mEn cours de création.. (redirection)\033[0m")
    time.sleep(2)
    os.system('python cyb3rtech.py')

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        show_menu()
        try:
            choice = int(input('\033[31mChoice >> \033[0m'))
            if choice == 0:
                os.system('python cyb3rtech.py')
                break
            elif choice == 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"\033[31m{menu}\033[0m")
                clone()
            else:
                print("\033[31m[!]\033[0m Invalid choice \033[31m[!]\033[0m")
                input("\n\033[31mPress Enter to return to the menu...\033[0m")
        except ValueError:
            print("\033[31mPlease enter a valid number\033[0m")
            input("\n\033[31mPress Enter to return to the menu...\033[0m")

if __name__ == "__main__":
    main()
