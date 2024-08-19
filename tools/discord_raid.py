import os

menu = """
         ██▀███   ▄▄▄       ██▓▓█████▄
         ▓██ ▒ ██▒▒████▄    ▓██▒▒██▀ ██▌
         ▓██ ░▄█ ▒▒██  ▀█▄  ▒██▒░██   █▌
         ▒██▀▀█▄  ░██▄▄▄▄██ ░██░░▓█▄   ▌
         ░██▓ ▒██▒ ▓█   ▓██▒░██░░▒████▓
         ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░▓   ▒▒▓  ▒
           ░▒ ░ ▒░  ▒   ▒▒ ░ ▒ ░ ░ ▒  ▒
           ░░   ░   ░   ▒    ▒ ░ ░ ░  ░
               ░           ░  ░ ░     ░
                        ░
"""
menu2 = """
[0] Back to main
[1] SelfBot Raid
[2] Bot Raid
"""

def show_menu():
    print(f"\033[31m{menu}")
    print(f"\033[31m{menu2}\033[0m")
    
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
                os.system('python ./tools/self_raid.py')
            elif choice == 2:
                os.system('python ./tools/bot_raid.py')                
            else:
                print("\033[31m[!]\033[0m Invalid choice \033[31m[!]\033[0m")
        except ValueError:
            print("\033[31mPlease enter a valid number\033[0m")
        input("\nPress Enter to return to the menu...\033[0m")

if __name__ == "__main__":
    main()