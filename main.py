import ipaddress

def berechne_subnetz(ip_netzwerk):
    netzwerk = ipaddress.ip_network(ip_netzwerk)
    netzwerk_adresse = netzwerk.network_address
    broadcast_adresse = netzwerk.broadcast_address
    ip_bereich = [str(ip) for ip in netzwerk.hosts()]

    print("Netzwerkadresse: ", netzwerk_adresse)
    print("Broadcast-Adresse: ", broadcast_adresse)
    print("IP-Bereich: ", ip_bereich[0], "-", ip_bereich[-1])

# Testen Sie das Programm mit einem IP-Netzwerk
berechne_subnetz('192.168.20.24/29')

