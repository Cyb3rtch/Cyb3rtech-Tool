import requests
import os
import sys

menu = """
         ▄▄▄█████▓ ██▀███   ▄▄▄       ▄████▄   ██ ▄█▀▓█████  ██▀███
         ▓  ██▒ ▓▒▓██ ▒ ██▒▒████▄    ▒██▀ ▀█   ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒
         ▒ ▓██░ ▒░▓██ ░▄█ ▒▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ ▒███   ▓██ ░▄█ ▒
         ░ ▓██▓ ░ ▒██▀▀█▄  ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄
         ▒██▒ ░ ░██▓ ▒██▒ ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄░▒████▒░██▓ ▒██▒
         ▒ ░░   ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░
         ░      ░▒ ░ ▒░  ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░
           ░         ░░   ░   ░   ▒   ░        ░ ░░ ░    ░     ░░   ░
                  ░           ░  ░░ ░      ░  ░      ░  ░   ░                                                                 ░
"""

menu2 = """
[0] Back to main
[1] Username Tracker
"""

def show_menu():
    print(f"\033[31m{menu}\033[0m")
    print(f"\033[31m{menu2}\033[0m")

def check_username(username):
    sites = {
        "GitHub": f"https://github.com/{username}",
        "Twitter": f"https://twitter.com/{username}",
        "Instagram": f"https://www.instagram.com/{username}/",
        "Reddit": f"https://www.reddit.com/user/{username}",
        "Facebook": f"https://www.facebook.com/{username}",
        "LinkedIn": f"https://www.linkedin.com/in/{username}",
        "Pinterest": f"https://www.pinterest.com/{username}",
        "Tumblr": f"https://{username}.tumblr.com",
        "YouTube": f"https://www.youtube.com/{username}",
        "Twitch": f"https://www.twitch.tv/{username}",
        "SoundCloud": f"https://soundcloud.com/{username}",
        "Steam": f"https://steamcommunity.com/id/{username}",
        "DeviantArt": f"https://www.deviantart.com/{username}",
        "Patreon": f"https://www.patreon.com/{username}",
        "WordPress": f"https://{username}.wordpress.com",
        "Spotify": f"https://open.spotify.com/user/{username}",
        "GitLab": f"https://gitlab.com/{username}",
        "Mixcloud": f"https://www.mixcloud.com/{username}",
        "PayPal": f"https://www.paypal.me/{username}",
        "TikTok": f"https://www.tiktok.com/@{username}",
        "Snapchat": f"https://www.snapchat.com/add/{username}",
        "Guns.lol": f"https://guns.lol/{username}",
        "Flickr": f"https://www.flickr.com/photos/{username}",
        "Vimeo": f"https://vimeo.com/{username}",
        "Discord": f"https://discord.com/users/{username}",
        "HackerOne": f"https://hackerone.com/{username}",
        "RedBubble": f"https://www.redbubble.com/people/{username}",
        "Medium": f"https://medium.com/@{username}",
        "Dribbble": f"https://dribbble.com/{username}",
        "Behance": f"https://www.behance.net/{username}",
        "CodePen": f"https://codepen.io/{username}",
        "ProductHunt": f"https://www.producthunt.com/@{username}",
    }
    
    print(f"\033[31mChecking usernames for '{username}'...\033[0m")
    
    for site, url in sites.items():
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                print(f"\033[32m[+] {site}: {url}\033[0m")
            else:
                print(f"\033[31m[-] {site}: {url}\033[0m")
        except requests.RequestException:
            print(f"\033[31m[-] {site}: {url}\033[0m")

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
                username = input('\033[31mPseudo >> \033[0m')
                check_username(username)
            else:
                print("\033[31m[!]\033[0m Invalid choice \033[31m[!]\033[0m")
        except ValueError:
            print("\033[31mPlease enter a valid number\033[0m")
        input("\nPress Enter to return to the menu...\033[0m")

if __name__ == "__main__":
    main()