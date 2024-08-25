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
                                           ║     v 1.0.3    ║                          ║ [0] > Discord Web ║
                                           ╚════════════════╝                          ║                   ║
                                                    ║                                  ╚═══════════════════╝
                                                    ║                                              ║
                             ╔══════════════════════╩══════════════════════╗                       ║
                             ║                                             ║                       ║
            ╔══════════════════════════════════════╗ ╔══════════════════════════════════════╗      ║
            ║ [21] > Previous Page (2/2)           ║ ║ [31] >                               ║      ║
            ║ [22] >                               ║ ║ [32] >                               ║══════╝
            ║ [23] >                               ║ ║ [33] >                               ║
            ║ [24] >                               ║ ║ [34] >                               ║
            ║ [25] >                               ║ ║ [35] >                               ║
            ║ [26] >                               ║ ║ [36] >                               ║
            ║ [27] >                               ║ ║ [37] >                               ║
            ║ [28] >                               ║ ║ [38] >                               ║
            ║ [29] >                               ║ ║ [39] >                               ║
            ║ [30] >                               ║ ║ [40] >                               ║
            ╚══════════════════════════════════════╝ ╚══════════════════════════════════════╝
"""
    
    while True:
        print(f"\033[31m{menu}")

        try:
            choice = int(input('Choice >> '))
            def choice_script(choice):
                if choice == 0:
                    os.system('python ./tools/discord.py')
                elif choice == 21:
                    os.system('python ./cyb3rtech.py')
                elif choice == 22:
                    os.system('python ./nextpage.py')
                elif choice == 23:
                    os.system('python ./nextpage.py')
                elif choice == 24:
                    os.system('python ./nextpage.py')
                elif choice == 25:
                    os.system('python ./nextpage.py')
                elif choice == 26:
                    os.system('python ./nextpage.py')
                elif choice == 27:
                    os.system('python ./nextpage.py')
                elif choice == 28:
                    os.system('python ./nextpage.py')
                elif choice == 29:
                    os.system('python ./nextpage.py')
                elif choice == 30:
                    os.system('python ./nextpage.py')
                elif choice == 31:
                    os.system('python ./nextpage.py')
                elif choice == 32:
                    os.system('python ./nextpage.py')
                elif choice == 33:
                    os.system('python ./nextpage.py')
                elif choice == 34:
                    os.system('python ./nextpage.py')
                elif choice == 35:
                    os.system('python ./nextpage.py')
                elif choice == 36:
                    os.system('python ./nextpage.py')
                elif choice == 37:
                    os.system('python ./nextpage.py')
                elif choice == 38:
                    os.system('python ./nextpage.py')
                elif choice == 39:
                    os.system('python ./nextpage.py')
                elif choice == 40:
                    os.system('python ./nextpage.py')
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
