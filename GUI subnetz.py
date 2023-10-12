import tkinter as tk
def berechne_subnetz():
    ip_netzwerk = eingabe.get()
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

    # Berechnung des IP-Bereichs
    ip_bereich_start = list(netzwerk)
    ip_bereich_ende = list(broadcast)

    ip_bereich_start[-1] += 1
    ip_bereich_ende[-1] -= 1

    ausgabe.delete(1.0, tk.END)
    ausgabe.insert(tk.END, "Netzwerkadresse: " + netzwerk_adresse + "\n")
    ausgabe.insert(tk.END, "Broadcast-Adresse: " + broadcast_adresse + "\n")
    ausgabe.insert(tk.END,
                   "IP-Bereich: " + ".".join(map(str, ip_bereich_start)) + " - " + ".".join(map(str, ip_bereich_ende)))


# Erstellen Sie das Tkinter-Fenster
fenster = tk.Tk()
fenster.title("Subnetz-Rechner")

# Eingabefeld für das IP-Netzwerk
eingabe_label = tk.Label(fenster, text="Geben Sie das IP-Netzwerk ein:")
eingabe_label.pack()
eingabe = tk.Entry(fenster)
eingabe.pack()

# Ausgabefeld für die Ergebnisse
ausgabe_label = tk.Label(fenster, text="Ergebnisse:")
ausgabe_label.pack()
ausgabe = tk.Text(fenster)
ausgabe.pack()

# Schaltfläche zum Berechnen des Subnetzes
berechne_button = tk.Button(fenster, text="Berechne", command=berechne_subnetz)
berechne_button.pack()

# Starten Sie die Tkinter-Schleife
fenster.mainloop()
