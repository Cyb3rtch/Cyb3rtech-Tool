import os
import webbrowser
import time

menu = """
             ▓█████▄  ██▓  ██████  ▄████▄   ▒█████   ██▀███  ▓█████▄
             ▒██▀ ██▌▓██▒▒██    ▒ ▒██▀ ▀█  ▒██▒  ██▒▓██ ▒ ██▒▒██▀ ██▌
             ░██   █▌▒██▒░ ▓██▄   ▒▓█    ▄ ▒██░  ██▒▓██ ░▄█ ▒░██   █▌
             ░▓█▄   ▌░██░  ▒   ██▒▒▓▓▄ ▄██▒▒██   ██░▒██▀▀█▄  ░▓█▄   ▌
             ░▒████▓ ░██░▒██████▒▒▒ ▓███▀ ░░ ████▓▒░░██▓ ▒██▒░▒████▓
             ▒▒▓  ▒ ░▓  ▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░ ▒▒▓  ▒
             ░ ▒  ▒  ▒ ░░ ░▒  ░ ░  ░  ▒     ░ ▒ ▒░   ░▒ ░ ▒░ ░ ▒  ▒
             ░ ░  ░  ▒ ░░  ░  ░  ░        ░ ░ ░ ▒    ░░   ░  ░ ░  ░
             ░     ░        ░  ░ ░          ░ ░     ░        ░
             ░                   ░
"""
menu2 = """
[0] Back to main
"""
def show_menu():
    print(f"\033[31m{menu}")
    print(f"{menu2}\033[0m")
   
time.sleep(1) 
webbrowser.open('https://discord.gg/mP6NvAgF2q')

def main():
    while True:
    os.system('cls' if os.name == 'nt' else 'clear')
        show_menu()
        try:
            choice = int(input('Choose >> '))
            if choice == 1:
                os.system('python cyb3rtech.py')
            else:
                print("\033[31m[!] >\033[0m Invalid choice \033[31m< [!]\033[0m")
        except ValueError:
            print("Veuillez entrer un nombre valide.")
        input("\nPress Enter to return to the main menu...\033[0m")

if __name__ == "__main__":
    main()
