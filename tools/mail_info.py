import os
import re
import dns.resolver

menu = """
          ███▄ ▄███▓ ▄▄▄       ██▓ ██▓        ██▓ ███▄    █   █████▒▒█████
         ▓██▒▀█▀ ██▒▒████▄    ▓██▒▓██▒       ▓██▒ ██ ▀█   █ ▓██   ▒▒██▒  ██▒
         ▓██    ▓██░▒██  ▀█▄  ▒██▒▒██░       ▒██▒▓██  ▀█ ██▒▒████ ░▒██░  ██▒
         ▒██    ▒██ ░██▄▄▄▄██ ░██░▒██░       ░██░▓██▒  ▐▌██▒░▓█▒  ░▒██   ██░
         ▒██▒   ░██▒ ▓█   ▓██▒░██░░██████▒   ░██░▒██░   ▓██░░▒█░   ░ ████▓▒░
         ░ ▒░   ░  ░ ▒▒   ▓▒█░░▓  ░ ▒░▓  ░   ░▓  ░ ▒░   ▒ ▒  ▒ ░   ░ ▒░▒░▒░
         ░  ░      ░  ▒   ▒▒ ░ ▒ ░░ ░ ▒  ░    ▒ ░░ ░░   ░ ▒░ ░       ░ ▒ ▒░
         ░      ░     ░   ▒    ▒ ░  ░ ░       ▒ ░   ░   ░ ░  ░ ░   ░ ░ ░ ▒
                ░         ░  ░ ░      ░  ░    ░           ░            ░ ░

"""
menu2 = """
[0] Back to main
[1] Email Info
"""

def show_menu():
    print(f"\033[31m{menu}")
    print(f"\033[31m{menu2}\033[0m")

# Configure the DNS resolver globally with a custom nameserver to avoid using /etc/resolv.conf
resolver = dns.resolver.Resolver(configure=False)
resolver.nameservers = ['8.8.8.8', '8.8.4.4']

def get_email_info(email):
    info = {}
    try:
        domain_all = email.split('@')[-1]
    except:
        domain_all = None

    try:
        name = email.split('@')[0]
    except:
        name = None

    try:
        domain = re.search(r"@([^@.]+)\.", email).group(1)
    except:
        domain = None

    try:
        tld = f".{email.split('.')[-1]}"
    except:
        tld = None

    try:
        mx_records = resolver.resolve(domain_all, 'MX')
        mx_servers = [str(record.exchange) for record in mx_records]
        info["mx_servers"] = mx_servers
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        info["mx_servers"] = None

    try:
        spf_records = resolver.resolve(domain_all, 'SPF')
        info["spf_records"] = [str(record) for record in spf_records]
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        info["spf_records"] = None

    try:
        dmarc_records = resolver.resolve(f'_dmarc.{domain_all}', 'TXT')
        info["dmarc_records"] = [str(record) for record in dmarc_records]
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        info["dmarc_records"] = None

    if "mx_servers" in info and info["mx_servers"]:
        for server in info["mx_servers"]:
            if "google.com" in server:
                info["google_workspace"] = True
            elif "outlook.com" in server:
                info["microsoft_365"] = True

    return info, domain_all, domain, tld, name

def email_info():
    email = input("\033[31mEmail >> \033[0m")
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"\033[31m{menu}\033[0m")
    info, domain_all, domain, tld, name = get_email_info(email)

    try:
        mx_servers = info["mx_servers"]
        mx_servers = ' / '.join(mx_servers) if mx_servers else None
    except:
        mx_servers = None

    try:
        spf_records = info["spf_records"]
    except:
        spf_records = None

    try:
        dmarc_records = info["dmarc_records"]
        dmarc_records = ' / '.join(dmarc_records) if dmarc_records else None
    except:
        dmarc_records = None

    try:
        google_workspace = info.get("google_workspace", None)
    except:
        google_workspace = None

    print(f"""
\033[31m
    [+] Email      : {email}
    [+] Name       : {name}
    [+] Domain     : {domain}
    [+] Tld        : {tld}
    [+] Domain All : {domain_all}
    [+] Servers    : {mx_servers}
    [+] Spf        : {spf_records}
    [+] Dmarc      : {dmarc_records}
    [+] Workspace  : {google_workspace}
\033[0m
    """)

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
                email_info()
            else:
                print("\033[31m[!]\033[0m Invalid choice \033[31m[!]\033[0m")
        except ValueError:
            print("\033[31mPlease enter a valid number\033[0m")
        input("\nPress Enter to return to the menu...\033[0m")

if __name__ == "__main__":
    main()