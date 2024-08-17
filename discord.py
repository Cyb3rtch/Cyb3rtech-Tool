import os
import webbrowser

def show_menu():
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
    print(f"\033[31m{menu}")

def main():
    while True:
        show_menu()
        try:
            choice = int(input('Choose >> '))
            if choice == 1:
                os.system('python main.py')
            else:
                print("\033[31m[!] >\033[0m Invalid choice \033[31m< [!]\033[0m")
        except ValueError:
            print("Veuillez entrer un nombre valide.")
        input("\nAppuyez sur Entrée pour retourner au menu..\033[0m")

if __name__ == "__main__":
    main()