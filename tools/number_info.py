import phonenumbers
from phonenumbers import geocoder, carrier, timezone
import sys
import time
import os

menu = """
         ███▄    █  █    ██  ███▄ ▄███▓ ▄▄▄▄   ▓█████  ██▀███
         ██ ▀█   █  ██  ▓██▒▓██▒▀█▀ ██▒▓█████▄ ▓█   ▀ ▓██ ▒ ██▒
         ▓██  ▀█ ██▒▓██  ▒██░▓██    ▓██░▒██▒ ▄██▒███   ▓██ ░▄█ ▒
         ▓██▒  ▐▌██▒▓▓█  ░██░▒██    ▒██ ▒██░█▀  ▒▓█  ▄ ▒██▀▀█▄
         ▒██░   ▓██░▒▒█████▓ ▒██▒   ░██▒░▓█  ▀█▓░▒████▒░██▓ ▒██▒
         ░ ▒░   ▒ ▒ ░▒▓▒ ▒ ▒ ░ ▒░   ░  ░░▒▓███▀▒░░ ▒░ ░░ ▒▓ ░▒▓░
         ░ ░░   ░ ▒░░░▒░ ░ ░ ░  ░      ░▒░▒   ░  ░ ░  ░  ░▒ ░ ▒░
         ░   ░ ░  ░░░ ░ ░ ░      ░    ░    ░    ░     ░░   ░
             ░    ░            ░    ░         ░  ░   ░                                                                         ░
"""
menu2 = """
[0] Back to main
[1] Phone Number Tracker
"""

def show_menu():
    print(f"\033[31m{menu}\033[0m")
    print(f"\033[31m{menu2}\033[0m")

def track_phone_number(phone_number):
    # Remove spaces and other non-digit characters
    phone_number = ''.join(filter(str.isdigit, phone_number))
    try:
        parsed_number = phonenumbers.parse(f"+{phone_number}", None)
        if not phonenumbers.is_valid_number(parsed_number):
            print("\033[31m[!] Invalid phone number format [!]\033[0m")
            return
        
        number_info = {
            "Country": geocoder.description_for_number(parsed_number, 'en'),
            "ISP": carrier.name_for_number(parsed_number, 'en'),
            "Time Zone": ", ".join(timezone.time_zones_for_number(parsed_number)),
            "National Number": phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.NATIONAL),
            "International Number": phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL),
            "E.164 Format": phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164),
            "Number Type": phonenumbers.number_type(parsed_number),
            "Possible Number": phonenumbers.is_possible_number(parsed_number)
        }
        
        print(f"\033[31mRecherche pour le numéro '+{phone_number}'..\n\033[0m")
        time.sleep(2)
        for key, value in number_info.items():
            print(f"\033[31m{key}: {value}\033[0m")
    
    except phonenumbers.NumberParseException:
        print("\033[31m[!] Failed to parse phone number [!]\033[0m")

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
                phone_number = input('\033[31mPhone Number >> \033[0m')
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"\033[31m{menu}\033[0m")
                track_phone_number(phone_number)
            else:
                print("\033[31m[!]\033[0m Invalid choice \033[31m[!]\033[0m")
        except ValueError:
            print("\033[31mPlease enter a valid number\033[0m")
        input("\nPress Enter to return to the menu...\033[0m")

if __name__ == "__main__":
    main()