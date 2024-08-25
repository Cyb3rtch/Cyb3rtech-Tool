import os
import requests
import threading
import time
import random
import string
from datetime import datetime

menu = """
         ███▄    █  ██▓▄▄▄█████▓ ██▀███   ▒█████       ▄████ ▓█████  ███▄    █
         ██ ▀█   █ ▓██▒▓  ██▒ ▓▒▓██ ▒ ██▒▒██▒  ██▒    ██▒ ▀█▒▓█   ▀  ██ ▀█   █
        ▓██  ▀█ ██▒▒██▒▒ ▓██░ ▒░▓██ ░▄█ ▒▒██░  ██▒   ▒██░▄▄▄░▒███   ▓██  ▀█ ██▒
        ▓██▒  ▐▌██▒░██░░ ▓██▓ ░ ▒██▀▀█▄  ▒██   ██░   ░▓█  ██▓▒▓█  ▄ ▓██▒  ▐▌██▒
        ▒██░   ▓██░░██░  ▒██▒ ░ ░██▓ ▒██▒░ ████▓▒░   ░▒▓███▀▒░▒████▒▒██░   ▓██░
        ░ ▒░   ▒ ▒ ░▓    ▒ ░░   ░ ▒▓ ░▒▓░░ ▒░▒░▒░     ░▒   ▒ ░░ ▒░ ░░ ▒░   ▒ ▒
        ░ ░░   ░ ▒░ ▒ ░    ░      ░▒ ░ ▒░  ░ ▒ ▒░      ░   ░  ░ ░  ░░ ░░   ░ ▒░
           ░   ░ ░  ▒ ░  ░        ░░   ░ ░ ░ ░ ▒     ░ ░   ░    ░      ░   ░ ░
                 ░  ░              ░         ░ ░           ░    ░  ░         ░

"""
menu2 = """
[0] Back to main
[1] Nitro Generator
"""

def show_menu():
    print(f"\033[31m{menu}")
    print(f"{menu2}\033[0m")

def log_with_time(message):
    current_time = datetime.now().strftime("%H:%M:%S")
    print(f"[{current_time}] {message}")

def check_nitro(nitro_code):
    response = requests.get(f"https://discord.com/api/v9/entitlements/gift-codes/{nitro_code}")
    return response.status_code, response.url

def send_webhook(webhook_url, message):
    requests.post(webhook_url, json={"content": message})

def generate_nitro_codes():
    while True:
        code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
        yield code

def nitro_generator():
    use_webhook = input('\033[31mUse Webhook? (y/n) >> \033[0m').strip().lower() == 'y'
    webhook_url = ''
    if use_webhook:
        webhook_url = input('\033[31mWebhook URL >> \033[0m').strip()
    num_threads = int(input('\033[31mNumber of Threads >> \033[0m'))

    found = threading.Event()

    def check_codes():
        for code in generate_nitro_codes():
            if found.is_set():
                break
            status_code, url = check_nitro(code)
            full_url = f"https://discord.gift/{code}"
            if status_code == 200:
                log_with_time(f"\033[32m[+] Valid Nitro Code: {full_url}\033[0m")
                if use_webhook:
                    send_webhook(webhook_url, f"Valid Nitro Code: {full_url}")
                found.set()
            else:
                log_with_time(f"\033[31m[-] Invalid Nitro Code: {full_url}\033[0m")

    threads = [threading.Thread(target=check_codes) for _ in range(num_threads)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

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
                nitro_generator()
            else:
                log_with_time("\033[31m[!] Invalid choice \033[0m")
        except ValueError:
            log_with_time("\033[31m[!] Please enter a valid number\033[0m")
        input("\nPress Enter to return to the main menu...\033[0m")

if __name__ == "__main__":
    main()