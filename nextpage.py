import os
import time
import shutil

def get_terminal_size():
    return shutil.get_terminal_size()

def center_text(text, width):
    lines = text.splitlines()
    centered_lines = [line.center(width) for line in lines]
    return "\n".join(centered_lines)

def blinking():
    text = """
⠀⠀⠀⠀⠀⠀⠀⢀⠆⠀⢀⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡀⠀⠰⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢠⡏⠀⢀⣾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢷⡀⠀⢹⣄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣰⡟⠀⠀⣼⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣧⠀⠀⢻⣆⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢠⣿⠁⠀⣸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣇⠀⠈⣿⡆⠀⠀⠀⠀
⠀⠀⠀⠀⣾⡇⠀⢀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡀⠀⢸⣿⠀⠀⠀⠀
⠀⠀⠀⢸⣿⠀⠀⣸⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣇⠀⠀⣿⡇⠀⠀⠀
⠀⠀⠀⣿⣿⠀⠀⣿⣿⣧⣤⣤⣤⡀⠀⣀⠀⠀⣀⠀⢀⣤⣤⣤⣤⣤⣤⣤⣤⣼⣿⣿⠀⠀⣿⣿⠀⠀⠀
⠀⠀⢸⣿⡏⠀⠀⠀⠙⢉⣉⣩⣴⣶⣤⣙⣿⣶⣯⣦⣴⣼⣷⣿⣋⣤⣶⣦⣍⣉⠉⠋⠀⠀⠀⢸⣿⡇⠀⠀
⠀⠀⢿⣿⣷⣤⣶⣶⠿⠿⠛⠋⣉⡉⠙⢛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡛⠛⢉⣉⠙⠛⠿⠿⣶⣶⣾⣿⡿⠀⠀
⠀⠀⠀⠙⠻⠋⠉⠀⠀⠀⣠⣾⡿⠟⠛⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⠛⠻⢿⣷⣄⠀⠀⠀⠉⠙⠟⠋⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣤⣾⠿⠋⢀⣠⣾⠟⢫⣿⣿⣿⣿⣿⣿⣿⡍⠻⣷⣄⡀⠙⠿⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⣴⡿⠛⠁⠀⢸⣿⣿⠋⠀⢸⣿⣿⣿⣿⣿⣿⣿⡗⠀⠙⣿⣿⡇⠀⠈⠛⢿⣦⣄⠀⠀⠀⠀⠀
⢀⠀⣀⣴⣾⠟⠋⠀⠀⠀⠀⢸⣿⣿⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠙⠻⣷⣦⣀⠀⣀
⢸⣿⣿⠋⠁⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠈⠙⣿⣿⡟
⢸⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀⠀⢹⣿⣿⣿⣿⣿⡏⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⡇
⢸⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀⠀⠀⢿⣿⣿⡿⠀⠀⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⡇
⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀⠀⠀⠈⠿⠿⠁⠀⠀⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀
⠀⢻⣿⡄⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⠇⠀⠀⠀⠀⠀⠀⠀⢀⣿⡟⠀
⠀⠘⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡿⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠃⠀
⠀⠀⠸⣷⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⣾⠏⠀⠀
⠀⠀⠀⢻⡆⠀⠀⠀⠀⠀⠀⠀⠸⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⠇⠀⠀⠀⠀⠀⠀⠀⢸⡟⠀⠀⠀
⠀⠀⠀⠀⢧⠀⠀⠀⠀⠀⠀⠀⠀⢿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡿⠀⠀⠀⠀⠀⠀⠀⠀⡾⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢳⠀⠀⠀⠀⠀⠀⠀⠸⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠇⠀⠀⠀⠀⠀⠀⠀⡸⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡆⠀⠀⠀⠀⠀⠀⠀⠀⢸⡟⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠣⠀⠀⠀⠀⠀⠀⠀⠀⠜⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
  (loading..)
    """
    terminal_size = get_terminal_size()
    centered_text = center_text(text, terminal_size.columns)
    
    for _ in range(5):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"\033[31m{centered_text}\033[0m")
        time.sleep(0.5)
        os.system('cls' if os.name == 'nt' else 'clear')
        time.sleep(0.5)

def center_text(text, width):
    lines = text.splitlines()
    centered_lines = [(line.center(width)) for line in lines]
    return "\n".join(centered_lines)

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    blinking()
    
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
                                             ║
                                             ║
      ╔══════════════════════════════════════════════════════════════════════════════════╗
      ║ Cyb3rtech Tool | v1.0.4 | [0] > Support (discord)             [ - ] [ □ ] [ X ]  ║
      ║══════════════════════════════════════════════════════════════════════════════════║
      ║                                                                                  ║
      ║ [21] > Previous Page (2/2)        [31] >                                         ║
      ║ [22] >                            [32] >                                         ║
      ║ [23] >                            [33] >                                         ║
      ║ [24] >                            [34] >                                         ║
      ║ [25] >                            [35] >                                         ║
      ║ [26] >                            [36] >                                         ║
      ║ [27] >                            [37] >                                         ║
      ║ [28] >                            [38] >                                         ║
      ║ [29] >                            [39] >                                         ║
      ║ [30] >                            [40] >                                         ║
      ║                                                                                  ║
      ╚══════════════════════════════════════════════════════════════════════════════════╝
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
