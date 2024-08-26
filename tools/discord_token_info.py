import os
import requests
import json
import time
from datetime import datetime, timezone

menu = """
         ▄▄▄█████▓ ▒█████   ██ ▄█▀▓█████  ███▄    █     ██▓ ███▄    █   █████▒▒█████
         ▓  ██▒ ▓▒▒██▒  ██▒ ██▄█▒ ▓█   ▀  ██ ▀█   █    ▓██▒ ██ ▀█   █ ▓██   ▒▒██▒  ██▒
         ▒ ▓██░ ▒░▒██░  ██▒▓███▄░ ▒███   ▓██  ▀█ ██▒   ▒██▒▓██  ▀█ ██▒▒████ ░▒██░  ██▒
         ░ ▓██▓ ░ ▒██   ██░▓██ █▄ ▒▓█  ▄ ▓██▒  ▐▌██▒   ░██░▓██▒  ▐▌██▒░▓█▒  ░▒██   ██░
           ▒██▒ ░ ░ ████▓▒░▒██▒ █▄░▒████▒▒██░   ▓██░   ░██░▒██░   ▓██░░▒█░   ░ ████▓▒░
           ▒ ░░   ░ ▒░▒░▒░ ▒ ▒▒ ▓▒░░ ▒░ ░░ ▒░   ▒ ▒    ░▓  ░ ▒░   ▒ ▒  ▒ ░   ░ ▒░▒░▒░
             ░      ░ ▒ ▒░ ░ ░▒ ▒░ ░ ░  ░░ ░░   ░ ▒░    ▒ ░░ ░░   ░ ▒░ ░       ░ ▒ ▒░
           ░      ░ ░ ░ ▒  ░ ░░ ░    ░      ░   ░ ░     ▒ ░   ░   ░ ░  ░ ░   ░ ░ ░ ▒
                  ░ ░  ░  ░      ░  ░         ░     ░           ░            ░ ░

"""
menu2 = """
[0] Back to main
[1] Token Info
"""

def show_menu():
    print(f"\033[31m{menu}")
    print(f"{menu2}\033[0m")

def token_info(token_discord):
    try:
        api = requests.get('https://discord.com/api/v8/users/@me', headers={'Authorization': token_discord}).json()
        response = requests.get('https://discord.com/api/v8/users/@me', headers={'Authorization': token_discord, 'Content-Type': 'application/json'})
        status = "Valid" if response.status_code == 200 else "Invalid"

        username_discord = api.get('username', "None") + '#' + api.get('discriminator', "None")
        display_name_discord = api.get('global_name', "None")
        user_id_discord = api.get('id', "None")
        email_discord = api.get('email', "None")
        email_verified_discord = api.get('verified', "None")
        phone_discord = api.get('phone', "None")
        mfa_discord = api.get('mfa_enabled', "None")
        country_discord = api.get('locale', "None")
        avatar_discord = api.get('avatar', "None")
        avatar_decoration_discord = api.get('avatar_decoration_data', "None")
        public_flags_discord = api.get('public_flags', "None")
        flags_discord = api.get('flags', "None")
        banner_discord = api.get('banner', "None")
        banner_color_discord = api.get('banner_color', "None")
        accent_color_discord = api.get("accent_color", "None")
        nsfw_discord = api.get('nsfw_allowed', "None")

        created_at_discord = datetime.fromtimestamp(((int(api.get('id', 'None')) >> 22) + 1420070400000) / 1000, timezone.utc) if api.get('id') else "None"

        nitro_discord = {
            0: 'False',
            1: 'Nitro Classic',
            2: 'Nitro Boosts',
            3: 'Nitro Basic'
        }.get(api.get('premium_type', 'None'), 'False')

        avatar_url_discord = f"https://cdn.discordapp.com/avatars/{user_id_discord}/{api['avatar']}.gif" if requests.get(f"https://cdn.discordapp.com/avatars/{user_id_discord}/{api['avatar']}.gif").status_code == 200 else f"https://cdn.discordapp.com/avatars/{user_id_discord}/{api['avatar']}.png"

        linked_users_discord = ' / '.join(api.get('linked_users', [])) or "None"
        bio_discord = api.get('bio', "None") or "None"
        authenticator_types_discord = ' / '.join(api.get('authenticator_types', [])) or "None"

        guilds_response = requests.get('https://discord.com/api/v9/users/@me/guilds?with_counts=true', headers={'Authorization': token_discord})
        guilds = guilds_response.json() if guilds_response.status_code == 200 else []
        guild_count = len(guilds)
        owner_guilds = [guild for guild in guilds if guild['owner']]
        owner_guild_count = f"({len(owner_guilds)})"
        owner_guilds_names = "\n" + "\n".join(f"{guild['name']} ({guild['id']})" for guild in owner_guilds) if owner_guilds else "None"

        billing_discord = requests.get('https://discord.com/api/v6/users/@me/billing/payment-sources', headers={'Authorization': token_discord}).json() or []
        payment_methods_discord = ' / '.join({
            1: 'CB',
            2: 'Paypal'
        }.get(method['type'], 'Other') for method in billing_discord) or "None"

        friends_discord = []
        for friend in requests.get('https://discord.com/api/v8/users/@me/relationships', headers={'Authorization': token_discord}).json():
            data = f"{friend['user']['username']}#{friend['user']['discriminator']} ({friend['user']['id']})"
            if len('\n'.join(friends_discord)) + len(data) >= 1024:
                break
            friends_discord.append(data)
        friends_discord = '\n' + ' / '.join(friends_discord) if friends_discord else "None"

        gift_codes_discord = []
        for gift_codes in requests.get('https://discord.com/api/v9/users/@me/outbound-promotions/codes', headers={'Authorization': token_discord}).json() or []:
            name = gift_codes['promotion']['outbound_title']
            code = gift_codes['code']
            data = f"Gift: {name}\nCode: {code}"
            if len('\n\n'.join(gift_codes_discord)) + len(data) >= 1024:
                break
            gift_codes_discord.append(data)
        gift_codes_discord = '\n\n'.join(gift_codes_discord) if gift_codes_discord else "None"

        print(f"""
\033[31m[INFO] Status       : {status}
[INFO] Token        : {token_discord}
[INFO] Username     : {username_discord}
[INFO] Display Name : {display_name_discord}
[INFO] Id           : {user_id_discord}
[INFO] Created      : {created_at_discord}
[INFO] Country      : {country_discord}
[INFO] Email        : {email_discord}
[INFO] Verified     : {email_verified_discord}
[INFO] Phone        : {phone_discord}
[INFO] Nitro        : {nitro_discord}
[INFO] Linked Users : {linked_users_discord}
[INFO] Avatar Decor : {avatar_decoration_discord}
[INFO] Avatar       : {avatar_discord}
[INFO] Avatar URL   : {avatar_url_discord}
[INFO] Accent Color : {accent_color_discord}
[INFO] Banner       : {banner_discord}
[INFO] Banner Color : {banner_color_discord}
[INFO] Flags        : {flags_discord}
[INFO] Public Flags : {public_flags_discord}
[INFO] NSFW         : {nsfw_discord}
[INFO] Multi-Factor Authentication : {mfa_discord}
[INFO] Authenticator Type          : {authenticator_types_discord}
[INFO] Billing      : {payment_methods_discord}
[INFO] Gift Code    : {gift_codes_discord}
[INFO] Guilds       : {guild_count}
[INFO] Owner Guilds : {owner_guild_count}{owner_guilds_names}
[INFO] Bio          : {bio_discord}
[INFO] Friend       : {friends_discord}
\033[0m""")
    except Exception as e:
        print(f"\033[31m[ERROR] Error when retrieving information: {e}\033[0m")

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
                token_discord = input('\033[31mToken >> \033[0m')
                token_info(token_discord)
            else:
                print("\033[31m[!] > Invalid choice < [!]\033[0m")
        except ValueError:
                print("\033[31m[!] Please enter a valid number\033[0m")
        input("\nPress Enter to return to the main menu...\033[0m")

if __name__ == "__main__":
    main()
