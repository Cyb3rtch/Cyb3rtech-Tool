import os
import subprocess
import socket
import concurrent.futures
import platform
import requests

menu = """
      ██▓ ██▓███      ██▓     ▒█████   ▒█████   ██ ▄█▀ █    ██  ██▓███
      ▓██▒▓██░  ██▒   ▓██▒    ▒██▒  ██▒▒██▒  ██▒ ██▄█▒  ██  ▓██▒▓██░  ██▒
      ▒██▒▓██░ ██▓▒   ▒██░    ▒██░  ██▒▒██░  ██▒▓███▄░ ▓██  ▒██░▓██░ ██▓▒
      ░██░▒██▄█▓▒ ▒   ▒██░    ▒██   ██░▒██   ██░▓██ █▄ ▓▓█  ░██░▒██▄█▓▒ ▒
      ░██░▒██▒ ░  ░   ░██████▒░ ████▓▒░░ ████▓▒░▒██▒ █▄▒▒█████▓ ▒██▒ ░  ░
      ░▓  ▒▓▒░ ░  ░   ░ ▒░▓  ░░ ▒░▒░▒░ ░ ▒░▒░▒░ ▒ ▒▒ ▓▒░▒▓▒ ▒ ▒ ▒▓▒░ ░  ░
      ▒ ░░▒ ░        ░ ░ ▒  ░  ░ ▒ ▒░   ░ ▒ ▒░ ░ ░▒ ▒░░░▒░ ░ ░ ░▒ ░
      ▒ ░░░            ░ ░   ░ ░ ░ ▒  ░ ░ ░ ▒  ░ ░░ ░  ░░░ ░ ░ ░░
      ░                  ░  ░    ░ ░      ░ ░  ░  ░      ░
"""
menu2 = """
[0] Back to main
[1] IP Info
[2] IP Ping
[3] Port Scan
[4] Reverse DNS
"""

def ip_info(ip_address):
    response = requests.get(f'http://ip-api.com/json/{ip_address}')
    
    if response.status_code == 200:
        data = response.json()
        
        if data['status'] == 'success':
            pays = data.get('country', 'N/A')
            ville = data.get('city', 'N/A')
            region = data.get('regionName', 'N/A')
            zip_code = data.get('zip', 'N/A')
            isp = data.get('isp', 'N/A')
            fuseau = data.get('timezone', 'N/A')
            lat = data.get('lat', 0)
            lon = data.get('lon', 0)
            maps_url = f"https://www.google.com/maps/search/?api=1&query={lat},{lon}"
            
            result = {
                "IP": ip_address,
                "Pays": pays,
                "Ville": ville,
                "Région": region,
                "ZIP": zip_code,
                "ISP": isp,
                "Fuseau horaire": fuseau,
                "Latitude": lat,
                "Longitude": lon,
                "Google Maps": maps_url
            }
            
            for key, value in result.items():
                print(f"\033[31m{key} : {value}\033[0m")
        else:
            print("\033[31mVeuillez vérifier l'adresse IP et réessayer.\033[0m")
    else:
        print("\033[31mVeuillez réessayer plus tard **(API)**.\033[0m")
        
def ping_ip(ip_address):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    
    try:
        result = subprocess.run(['ping', param, '4', ip_address], capture_output=True, text=True, timeout=10)
        print(f"\033[31m\n{'=' * 60}\nPINGING {ip_address}\n{'=' * 60}\033[0m")
        print(f"\033[31m{result.stdout}\033[0m")
        
    except subprocess.TimeoutExpired:
        print("\033[31mLe ping a expiré (Timeout).\033[0m")
    except Exception as e:
        print(f"\033[31mUne erreur est survenue : {e}\033[0m")
        
def scan_port(ip_address, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip_address, port))
        sock.close()
        return port if result == 0 else None
    except Exception:
        return None
        
def port_scan(ip_address):
    open_ports = []
    print(f"\033[31mScanning ports on {ip_address}... This may take a while.\033[0m")
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        futures = {executor.submit(scan_port, ip_address, port): port for port in range(1, 1025)}
        for future in concurrent.futures.as_completed(futures):
            port = futures[future]
            if future.result():
                open_ports.append(port)
                print(f"\033[31mPort {port} is open\033[0m")

    if open_ports:
        print(f"\n\033[31m{'=' * 60}\nOPEN PORTS ON {ip_address}\n{'=' * 60}\033[0m")
        print(f"\033[31mPorts Ouverts: {open_ports}\033[0m")
    else:
        print(f"\033[31mAucun port ouvert trouvé sur {ip_address}.\033[0m")

def reverse_dns(ip_address):
    try:
        result = subprocess.run(['nslookup', ip_address], capture_output=True, text=True)
        print(f"\033[31m\n{'=' * 60}\nREVERSE DNS LOOKUP {ip_address}\n{'=' * 60}\033[0m")
        print(f"\033[31m{result.stdout}\033[0m")
    except FileNotFoundError:
        print("\033[31mLa commande 'nslookup' n'a pas été trouvée.\033[0m")
    except Exception as e:
        print(f"\033[31mUne erreur est survenue : {e}\033[0m")

def show_menu():
    print(f"\033[31m{menu}\033[0m")
    print(f"\033[31m{menu2}\033[0m")

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        show_menu()
        try:
            choice = int(input("\033[31mChoice >> \033[0m"))
            if choice == 0:
                os.system('python cyb3rtech.py')
                break
            elif choice == 1:
                ip_address = input("\033[31mAdresse IP >> \033[0m")
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"\033[31m{menu}\033[0m")
                ip_info(ip_address)
            elif choice == 2:
                ip_address = input("\033[31mAdresse IP >> \033[0m")
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"\033[31m{menu}\033[0m")
                ping_ip(ip_address)
            elif choice == 3:
                ip_address = input("\033[31mAdresse IP >> \033[0m")
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"\033[31m{menu}\033[0m")
                port_scan(ip_address)
            elif choice == 4:
                ip_address = input("\033[31mAdresse IP >> \033[0m")
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"\033[31m{menu}\033[0m")
                reverse_dns(ip_address)
            else:
                print("\033[31m[!]\033[0m Invalid choice \033[31m[!]\033[0m")
        except ValueError:
            print("\033[31mPlease enter a valid number\033[0m")
        input("\n\033[31mPress Enter to return to the menu...\033[0m")

if __name__ == "__main__":
    main()
