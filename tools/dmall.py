import os
import requests
import time

menu = """
         ▓█████▄  ███▄ ▄███▓ ▄▄▄       ██▓     ██▓
         ▒██▀ ██▌▓██▒▀█▀ ██▒▒████▄    ▓██▒    ▓██▒
         ░██   █▌▓██    ▓██░▒██  ▀█▄  ▒██░    ▒██░
         ░▓█▄   ▌▒██    ▒██ ░██▄▄▄▄██ ▒██░    ▒██░
         ░▒████▓ ▒██▒   ░██▒ ▓█   ▓██▒░██████▒░██████▒
         ▒▒▓  ▒ ░ ▒░   ░  ░ ▒▒   ▓▒█░░ ▒░▓  ░░ ▒░▓  ░
           ░ ▒  ▒ ░  ░      ░  ▒   ▒▒ ░░ ░ ▒  ░░ ░ ▒  ░
           ░ ░  ░ ░      ░     ░   ▒     ░ ░     ░ ░
             ░           ░         ░  ░    ░  ░    ░  ░
           ░
"""
menu2 = """
[0] Back to main
[1] Dmall Friends (SelfBot)
[2] Dmall Dm Open (SelfBot)
[3] Dmall Server (Bot)
"""

def show_menu():
    print(f"\033[31m{menu}")
    print(f"{menu2}\033[0m")

def dmall_friends(token_discord):
    message = input('\033[31mMessage ({user} pour mentionner): \033[0m')
    header = {'Authorization': token_discord, 'Content-Type': 'application/json'}

    try:
        response = requests.get('https://discord.com/api/v9/users/@me/relationships', headers=header)
        if response.status_code != 200:
            print(f"\033[31m[!] Erreur lors de la récupération des amis ({response.status_code})\033[0m")
            return

        friends = response.json()
        for friend in friends:
            try:
                user_id = friend['user']['id']
                username = friend['user']['username']
                discriminator = friend['user']['discriminator']
                mention = f"<@{user_id}>"
                user_message = message.replace("{user}", mention)
                
                try:
                    channel_response = requests.post(
                        'https://discord.com/api/v9/users/@me/channels',
                        headers=header,
                        json={"recipient_id": user_id}
                    )
                    if channel_response.status_code != 200:
                        print(f"\033[31m[!] Erreur lors de la création du canal pour {username}#{discriminator} ({channel_response.status_code})\033[0m")
                        continue

                    channel_id = channel_response.json()['id']
                    dm_response = requests.post(
                        f'https://discord.com/api/v9/channels/{channel_id}/messages',
                        headers=header,
                        json={"content": user_message}
                    )

                    if dm_response.status_code == 200:
                        print(f"\033[32m[+] Message envoyé à {username}#{discriminator}\033[0m")
                    else:
                        print(f"\033[31m[!] Message non envoyé à {username}#{discriminator} ({dm_response.status_code})\033[0m")

                    time.sleep(0.5)
                    
                except Exception as e:
                    print(f"\033[31m[!] Erreur : {e}\033[0m")

            except KeyError as e:
                print(f"\033[31m[!] Clé manquante dans la réponse : {e}\033[0m")
                print(f"Réponse complète pour cet utilisateur : {friend}\033[0m")

    except Exception as e:
        print(f"\033[31m[!] Erreur lors de la récupération des amis : {e}\033[0m")

def dmall_open(token_discord):
    message = input('\033[31mMessage ({user} pour mentionner): \033[0m')
    header = {'Authorization': token_discord, 'Content-Type': 'application/json'}

    try:
        response = requests.get('https://discord.com/api/v9/users/@me/channels', headers=header)
        if response.status_code != 200:
            print(f"\033[31m[!] Erreur lors de la récupération des DM ouverts ({response.status_code})\033[0m")
            return

        open_dms = response.json()
        for dm in open_dms:
            try:
                user_id = dm['recipients'][0]['id']
                username = dm['recipients'][0]['username']
                discriminator = dm['recipients'][0]['discriminator']
                mention = f"<@{user_id}>"
                user_message = message.replace("{user}", mention)
                
                dm_response = requests.post(
                    f'https://discord.com/api/v9/channels/{dm["id"]}/messages',
                    headers=header,
                    json={"content": user_message}
                )

                if dm_response.status_code == 200:
                    print(f"\033[32m[+] Message envoyé à {username}#{discriminator}\033[0m")
                else:
                    print(f"\033[31m[!] Message non envoyé à {username}#{discriminator} ({dm_response.status_code})\033[0m")

                time.sleep(0.5)
            except Exception as e:
                print(f"\033[31m[!] Erreur : {e}\033[0m")

    except Exception as e:
        print(f"\033[31m[!] Erreur lors de la récupération des DM ouverts : {e}\033[0m")

def dmall_server(token_bot, server_id):
    message = input('\033[31mMessage ({user} pour mentionner): \033[0m')
    header = {'Authorization': f'Bot {token_bot}', 'Content-Type': 'application/json'}

    try:
        response = requests.get(f'https://discord.com/api/v9/guilds/{server_id}/members?limit=1000', headers=header)
        if response.status_code != 200:
            print(f"\033[31m[!] Erreur lors de la récupération des membres du serveur ({response.status_code})\033[0m")
            return

        members = response.json()
        for member in members:
            try:
                user_id = member['user']['id']
                username = member['user']['username']
                discriminator = member['user']['discriminator']
                mention = f"<@{user_id}>"
                user_message = message.replace("{user}", mention)
                
                try:
                    channel_response = requests.post(
                        'https://discord.com/api/v9/users/@me/channels',
                        headers=header,
                        json={"recipient_id": user_id}
                    )
                    if channel_response.status_code != 200:
                        print(f"\033[31m[!] Erreur lors de la création du canal pour {username}#{discriminator} ({channel_response.status_code})\033[0m")
                        continue

                    channel_id = channel_response.json()['id']
                    dm_response = requests.post(
                        f'https://discord.com/api/v9/channels/{channel_id}/messages',
                        headers=header,
                        json={"content": user_message}
                    )

                    if dm_response.status_code == 200:
                        print(f"\033[32m[+] Message envoyé à {username}#{discriminator}\033[0m")
                    else:
                        print(f"\033[31m[!] Erreur lors de l'envoi du message à {username}#{discriminator} ({dm_response.status_code})\033[0m")

                    time.sleep(0.5)

                except Exception as e:
                    print(f"\033[31m[!] Erreur : {e}\033[0m")

            except KeyError as e:
                print(f"\033[31m[!] Clé manquante dans la réponse : {e}\033[0m")
                print(f"Réponse complète pour cet utilisateur : {member}\033[0m")

    except Exception as e:
        print(f"\033[31m[!] Erreur : {e}\033[0m")

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
                token_discord = input('\033[31mToken : \033[0m')
                dmall_friends(token_discord)
            elif choice == 2:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"\033[31m{menu}")
                token_discord = input('\033[31mToken : \033[0m')
                dmall_open(token_discord)
            elif choice == 3:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"\033[31m{menu}")
                token_bot = input('\033[31mToken : \033[0m')
                server_id = input('\033[31mGuild ID : \033[0m')
                dmall_server(token_bot, server_id)
            else:
                print("\033[31m[!] > Invalid choice < [!]\033[0m")
        except ValueError:
            print("\033[31m[!] Please enter a valid number\033[0m")
        input("\nPress Enter to return to the main menu...\033[0m")

if __name__ == "__main__":
    main()