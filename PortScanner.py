import socket

def scan_ports(target, ports):
    """
    Scanne les ports spécifiés sur l'hôte cible.
    
    :param target: adresse IP à scanner
    :param ports: ports à scanner
    """
    print(f"Scanning {target}...")
    
    for port in ports:
        # Connexion socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Timeout (au besoin)
        
        # Vérifie si port ouvert
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} ouvert.")
        else:
            print(f"Port {port} fermé.")
        
        sock.close()

# Test
if __name__ == "__main__":
    target_ip = "127.0.0.1"  # Adresse IP de la cible 
    ports_to_scan = [22, 80, 443, 8080]  # Ports à scanner
    
    scan_ports(target_ip, ports_to_scan)
