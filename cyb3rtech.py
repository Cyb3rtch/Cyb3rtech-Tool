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
            ║ [1] > Tool Info                      ║ ║ [10] > Discord Token Info            ║      ║
            ║ [2] > IP Info                        ║ ║ [11] > Discord Token Nuker           ║══════╝
            ║ [3] > Web Cloner                     ║ ║ [12] > Discord Token Joiner          ║
            ║ [4] > Username Tracker               ║ ║ [13] > Discord Token BruteForce      ║
            ║ [5] > Phone Number Lookup            ║ ║ [14] > Discord Token Spammer         ║
            ║ [6] > Mail Info                      ║ ║ [15] > Discord Token Generator       ║
            ║ [7] > SQL Vulnerability              ║ ║ [16] > Discord Nitro Generator       ║
            ║ [8] > Dox Tracker                    ║ ║ [17] > Discord Server Info           ║
            ║ [9] > Discord Raid                   ║ ║ [18] > Next Page (1/2)               ║
            ╚══════════════════════════════════════╝ ╚══════════════════════════════════════╝
    """

    while True:
        print(f"\033[31m{menu}")

        try:
            choice = int(input('Choice >> '))
            def choice_script(choice):
                if choice == 0:
                    os.system('python ./tools/discord.py')
                elif choice == 1:
                    os.system('python ./tools/tool_info.py')
                elif choice == 2:
                    os.system('python ./tools/geoip.py')
                elif choice == 3:
                    os.system('python ./tools/web_cloner.py')
                elif choice == 4:
                    os.system('python ./tools/username_tracker.py')
                elif choice == 5:
                    os.system('python ./tools/phone_number.py')
                elif choice == 6:
                    os.system('python ./cyb3rtech.py')
                elif choice == 7:
                    os.system('python ./tools/sql_vulnerability.py')
                elif choice == 8:
                    os.system('python ./cyb3rtech.py')
                elif choice == 9:
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
