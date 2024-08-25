import os
import time

def main():
    os.system('cls' if os.name == 'nt' else 'clear')

    menu = """
                 ▄████▄▓██   ██▓ ▄▄▄▄   ▓█████  ██▀███  ▄▄▄█████▓▓█████  ▄████▄   ██░ ██
                 ▒██▀ ▀█ ▒██  ██▒▓█████▄ ▓█   ▀ ▓██ ▒ ██▒▓  ██▒ ▓▒▓█   ▀ ▒██▀ ▀█  ▓██░ ██▒
                 ▒▓█    ▄ ▒██ ██░▒██▒ ▄██▒███   ▓██ ░▄█ ▒▒ ▓██░ ▒░▒███   ▒▓█    ▄ ▒██▀▀██░
                 ▒▓▓▄ ▄██▒░ ▐██▓░▒██░█▀  ▒▓█  ▄ ▒██▀▀█▄  ░ ▓██▓ ░ ▒▓█  ▄ ▒▓▓▄ ▄██▒░▓█ ░██
                 ▒ ▓███▀ ░░ ██▒▓░░▓█  ▀█▓░▒████▒░██▓ ▒██▒  ▒██▒ ░ ░▒████▒▒ ▓███▀ ░░▓█▒░██▓
                 ░ ░▒ ▒  ░ ██▒▒▒ ░▒▓███▀▒░░ ▒░ ░░ ▒▓ ░▒▓░  ▒ ░░   ░░ ▒░ ░░ ░▒ ▒  ░ ▒ ░░▒░▒
                 ░  ▒  ▓██ ░▒░ ▒░▒   ░  ░ ░  ░  ░▒ ░ ▒░    ░     ░ ░  ░  ░  ▒    ▒ ░▒░ ░
                 ░       ▒ ▒ ░░   ░    ░    ░     ░░   ░   ░         ░   ░         ░  ░░ ░
                 ░ ░     ░ ░      ░         ░  ░   ░                 ░  ░░ ░       ░  ░  ░
                 ░       ░ ░           ░                                 ░
                                                    ║
                                           ╔════════════════╗                          ╔═══════════════════╗
                                           ║    Cyb3rtech   ║                          ║                   ║
                                           ║   Beta v1.0.0  ║                          ║ [0] > Discord Web ║
                                           ╚════════════════╝                          ║                   ║
                                                    ║                                  ╚═══════════════════╝
                                                    ║                                              ║
                             ╔══════════════════════╩══════════════════════╗                       ║
                             ║                                             ║                       ║
            ╔══════════════════════════════════════╗ ╔══════════════════════════════════════╗      ║
            ║ [20] > Previous Page (2/2)           ║ ║ [30] >                               ║      ║
            ║ [21] >                               ║ ║ [31] >                               ║══════╝
            ║ [22] >                               ║ ║ [32] >                               ║
            ║ [23] >                               ║ ║ [33] >                               ║
            ║ [24] >                               ║ ║ [34] >                               ║
            ║ [25] >                               ║ ║ [35] >                               ║
            ║ [26] >                               ║ ║ [36] >                               ║
            ║ [27] >                               ║ ║ [37] >                               ║
            ║ [28] >                               ║ ║ [38] >                               ║
            ║ [29] >                               ║ ║ [39] >                               ║
            ╚══════════════════════════════════════╝ ╚══════════════════════════════════════╝
"""
    
    while True:
        print(f"\033[31m{menu}")

        try:
            choice = int(input('Choice >> '))
            def choice_script(choice):
                if choice == 0:
                    os.system('python ./tools/discord.py')
                elif choice == 19:
                    os.system('python ./cyb3rtech.py')
                elif choice == 20:
                    os.system('python ./cyb3rtech.py')
                elif choice == 21:
                    os.system('python ./cyb3rtech.py')
                elif choice == 22:
                    os.system('python ./cyb3rtech.py')
                elif choice == 23:
                    os.system('python ./cyb3rtech.py')
                elif choice == 24:
                    os.system('python ./cyb3rtech.py')
                elif choice == 25:
                    os.system('python ./cyb3rtech.py')
                elif choice == 26:
                    os.system('python ./cyb3rtech.py')
                elif choice == 27:
                    os.system('python ./cyb3rtech.py')
                elif choice == 28:
                    os.system('python ./cyb3rtech.py')
                elif choice == 29:
                    os.system('python ./cyb3rtech.py')
                elif choice == 30:
                    os.system('python ./cyb3rtech.py')
                elif choice == 31:
                    os.system('python ./cyb3rtech.py')
                elif choice == 32:
                    os.system('python ./cyb3rtech.py')
                elif choice == 33:
                    os.system('python ./cyb3rtech.py')
                elif choice == 34:
                    os.system('python ./cyb3rtech.py')
                elif choice == 35:
                    os.system('python ./cyb3rtech.py')
                elif choice == 36:
                    os.system('python ./cyb3rtech.py')
                else:
                    raise ValueError
            choice_script(choice)
            break
        except ValueError:
            print("\033[31m[!] >\033[0m Invalid choice \033[31m< [!]\033[0m")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    main()