def berechne_subnetz(ip_netzwerk):
    ip, cidr = ip_netzwerk.split('/')
    ip = list(map(int, ip.split('.')))
    cidr = int(cidr)

    mask = [0, 0, 0, 0]
    for i in range(cidr):
        mask[i // 8] = mask[i // 8] + (1 << (7 - i % 8))

    netzwerk = []
    for i in range(4):
        netzwerk.append(int(ip[i]) & mask[i])

    broadcast = list(netzwerk)
    brange = 32 - cidr
    for i in range(brange):
        broadcast[3 - i // 8] = broadcast[3 - i // 8] + (1 << (i % 8))

    netzwerk_adresse = ".".join(map(str, netzwerk))
    broadcast_adresse = ".".join(map(str, broadcast))

    print("Netzwerkadresse: ", netzwerk_adresse)
    print("Broadcast-Adresse: ", broadcast_adresse)

    # Berechnung des IP-Bereichs
    ip_bereich_start = list(netzwerk)
    ip_bereich_ende = list(broadcast)

    ip_bereich_start[-1] += 1
    ip_bereich_ende[-1] -= 1

    print("IP-Bereich: ", ".".join(map(str, ip_bereich_start)), "-", ".".join(map(str, ip_bereich_ende)))


# Testen Sie das Programm mit einem IP-Netzwerk
berechne_subnetz('')
