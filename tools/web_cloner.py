from pywebcopy import save_website
import os

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

def clone_website(url, folder):
    save_website(
        url=url,
        project_folder=folder,
        open_in_browser=False
    )
    print(f"\033[31mWebsite cloner dans le dossier : {folder}\033[0m")

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        show_menu()
        try:
            choice = int(input('\033[31mChoice >> \033[0m'))
            if choice == 0:
                break
            elif choice == 1:
                url = input('\033[31mWebsite Url (e.g., http://exemple.com): \033[0m').strip()
                folder = 'web-cloner'
                os.system('cls' if os.name == 'nt' else 'clear')
                clone_website(url, folder)
                input("\n\033[31mPress Enter to return to the menu...\033[0m")
            else:
                print("\033[31m[!]\033[0m Invalid choice \033[31m[!]\033[0m")
                input("\n\033[31mPress Enter to return to the menu...\033[0m")
        except ValueError:
            print("\033[31mPlease enter a valid number\033[0m")
            input("\n\033[31mPress Enter to return to the menu...\033[0m")

if __name__ == "__main__":
    main()