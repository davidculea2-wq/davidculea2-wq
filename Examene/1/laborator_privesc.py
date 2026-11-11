# ==========================================
# PARTEA A1: Citirea liniilor din fișier
# ==========================================
def citeste_linii(cale):
    # Deschide fișierul, ignoră liniile goale și comentariile (#)
    with open(cale, encoding='utf-8') as f:
        return [linie.strip() for linie in f if linie.strip() and not linie.strip().startswith('#')]

# Apelul pentru A1
cai = citeste_linii('arsenal/privesc/start/suid.txt')
print("linii SUID (A1):", len(cai))
# ==========================================
# EXERCIȚIUL A2: Extragerea și filtrarea elementelor unice
# ==========================================

def citeste_linii(cale):
    with open(cale, encoding='utf-8') as f:
        return [linie.strip() for linie in f if linie.strip() and not linie.strip().startswith('#')]

# Citim liniile SUID
cai = citeste_linii('arsenal/privesc/start/suid.txt')

# Extragem doar valorile unice folosind set() și le sortăm
binare_unice = sorted(list(set(cai)))

print("Rezultat A2 - Număr binare SUID unice:", len(binare_unice))
print("Lista binarelor unice:")
for binar in binare_unice:
    print(f" - {binar}")
   # ==========================================
# EXERCIȚIUL A3: Analiza SUID și detectarea riscurilor
# ==========================================

def citeste_linii(cale):
    with open(cale, encoding='utf-8') as f:
        return [linie.strip() for linie in f if linie.strip() and not linie.strip().startswith('#')]

# Citim liniile din fișierul SUID
cai = citeste_linii('arsenal/privesc/start/suid.txt')

# Lista binarelor considerate cu risc mare
binare_risc = ['cp', 'find', 'nmap', 'vim.basic']

# Filtrăm binarele cu risc mare găsite în fișier (fără duplicate, păstrând ordinea)
gasite_risc = []
for c in cai:
    nume_binar = c.split('/')[-1]
    if nume_binar in binare_risc and nume_binar not in gasite_risc:
        gasite_risc.append(nume_binar)

gasite_risc.sort()

# Afișarea exactă cerută pentru A3
print(f"{len(cai)}")
print(f"SUID, {len(gasite_risc)} cu risc mare")
print(gasite_risc)
# ==========================================
# EXERCIȚIUL A4: Analiza drepturilor Sudo
# ==========================================

def citeste_linii(cale):
    with open(cale, encoding='utf-8') as f:
        return [linie.strip() for linie in f if linie.strip() and not linie.strip().startswith('#')]

# Citim liniile din fișierul sudo.txt
linii_sudo = citeste_linii('arsenal/privesc/start/sudo.txt')

print(f"Total reguli Sudo găsite: {len(linii_sudo)}")
print("Lista intrărilor:")
for r in linii_sudo:
    print(f" - {r}")
    # ==========================================
# EXERCIȚIUL A5: Analiza task-urilor Crontab
# ==========================================

def citeste_linii(cale):
    with open(cale, encoding='utf-8') as f:
        return [linie.strip() for linie in f if linie.strip() and not linie.strip().startswith('#')]

# Citim liniile din fișierul crontab.txt
linii_cron = citeste_linii('arsenal/privesc/start/crontab.txt')

print(f"Total task-uri Crontab găsite: {len(linii_cron)}")
print("Lista task-urilor programate:")
for t in linii_cron:
    print(f" - {t}")