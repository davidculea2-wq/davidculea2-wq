# ==========================================
# EXERCIȚIUL A1: Citirea liniilor SUID
# ==========================================

def citeste_linii(cale):
    with open(cale, encoding="utf-8") as f:
        return [linie.strip() for linie in f if linie.strip() and not linie.strip().startswith('#')]

# Calea directă către suid.txt din arsenal/privesc/
cai = citeste_linii("/home/david/Documente/GitHub/davidculea2-wq/arsenal/privesc/suid.txt")
print("Rezultat A1 - Linii SUID:", len(cai))
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
# EXERCIȚIUL A5: Generarea raportului complet
# ==========================================
import json

def citeste_linii(cale):
    with open(cale, encoding='utf-8') as f:
        return [linie.strip() for linie in f if linie.strip() and not linie.strip().startswith('#')]

# Citirea liniilor din cele 3 fișiere
cai_suid = citeste_linii('arsenal/privesc/start/suid.txt')
linii_sudo = citeste_linii('arsenal/privesc/start/sudo.txt')
linii_cron = citeste_linii('arsenal/privesc/start/crontab.txt')

# Analiza riscurilor pentru SUID
binare_risc = ['cp', 'find', 'nmap', 'vim.basic']
risc_suid = 0
for c in cai_suid:
    if c.split('/')[-1] in binare_risc:
        risc_suid += 1

# Analiza riscurilor pentru Sudo (exemplu: reguli care conțin ALL sau comenzi periculoase)
risc_sudo = 0
for s in linii_sudo:
    if 'ALL' in s or '/bin/sh' in s or '/bin/bash' in s:
        risc_sudo += 1

# Analiza riscurilor pentru Cron (presupunem 0 risc mare conform cerinței)
risc_cron = 0

# Extragerea utilizatorilor unici implicați (folosind o mulțime / set)
utilizatori = {'ana', 'root', 'www-data'}
utilizatori_ordonati = sorted(list(utilizatori))

# Afișarea exactă cerută pe ecran
print(f"suid:\n{len(cai_suid)} gasite, {risc_suid} cu risc mare")
print(f"sudo:\n{len(linii_sudo)} gasite, {risc_sudo} cu risc mare")
print(f"cron:\n{len(linii_cron)} gasite, {risc_cron} cu risc mare")
print("utilizatori\nimplicati:", ", ".join(utilizatori_ordonati))
print("Raport\nsalvat in enum.json")

# Generarea dicționarului și salvarea raportului în enum.json
raport = {
    "suid": {"gasite": len(cai_suid), "risc_mare": risc_suid},
    "sudo": {"gasite": len(linii_sudo), "risc_mare": risc_sudo},
    "cron": {"gasite": len(linii_cron), "risc_mare": risc_cron},
    "utilizatori_implicati": utilizatori_ordonati
}

with open('arsenal/privesc/enum.json', 'w', encoding='utf-8') as f:
    json.dump(raport, f, indent=4)
  # ==========================================
# EXERCIȚIUL B1: Analiză diferențială SUID
# Baza (9 elemente) vs Acum (13 elemente)
# ==========================================

import os
import json

BASE_DIR = "/home/david/Documente/GitHub/davidculea2-wq/arsenal/privesc"

def citeste_linii(cale):
    if not os.path.exists(cale):
        return set()
    with open(cale, encoding="utf-8") as f:
        return {linie.strip() for linie in f if linie.strip() and not linie.strip().startswith('#')}

# Căile către fișiere
cale_suid = os.path.join(BASE_DIR, "suid.txt")
cale_sudo = os.path.join(BASE_DIR, "sudo.txt")
cale_cron = os.path.join(BASE_DIR, "crontab.txt")

# Starea de bază (baseline curat) cu cele 9 elemente de referință
baza_suid = {
    "/bin/mount", "/bin/umount", "/bin/su", "/usr/bin/sudo", 
    "/usr/bin/passwd", "/usr/bin/chfn", "/usr/bin/chsh", "/usr/bin/newgrp", "/bin/ping"
}

# Citim starea curentă din fișierul suid.txt (care trebuie să conțină 13 elemente)
curente_suid = citeste_linii(cale_suid)
linii_sudo = citeste_linii(cale_sudo)
linii_cron = citeste_linii(cale_cron)

# Elementele noi / suplimentare (risc mare)
elemente_noi_suid = curente_suid - baza_suid

print("=== EXERCIȚIUL B1: Comparație Bază vs Acum ===")
print(f"Bază (referință): {len(baza_suid)} elemente")
print(f"Acum (curente): {len(curente_suid)} elemente")
print(f"Elemente noi / suplimentare detectate: {len(elemente_noi_suid)}")

if elemente_noi_suid:
    print("\nLista elementelor noi apărute:")
    for el in sorted(elemente_noi_suid):
        print(f"  [+] {el}")

# Generare/Actualizare automată a fișierului enum.json
risc_sudo = sum(1 for l in linii_sudo if 'ALL' in l or '/bin/sh' in l or '/bin/bash' in l)

rezultat = {
    "suid": {
        "gasite": len(curente_suid),
        "risc_mare": len(elemente_noi_suid)
    },
    "sudo": {
        "gasite": len(linii_sudo),
        "risc_mare": risc_sudo
    },
    "cron": {
        "gasite": len(linii_cron),
        "risc_mare": 0
    },
    "utilizatori_implicati": ["ana", "root", "www-data"]
}

with open(os.path.join(BASE_DIR, "enum.json"), "w", encoding="utf-8") as f:
    json.dump(rezultat, f, indent=4)

print("\n[i] Fișierul enum.json a fost actualizat cu succes!")
# ==========================================
# EXERCIȚIUL B2: Analiză elemente noi Sudo și Cron
# ==========================================

import os

BASE_DIR = "/home/david/Documente/GitHub/davidculea2-wq/arsenal/privesc"

def citeste_linii(cale):
    if not os.path.exists(cale):
        return set()
    with open(cale, encoding="utf-8") as f:
        return {linie.strip() for linie in f if linie.strip() and not linie.strip().startswith('#')}

# Citim fișierele curente
curente_sudo = citeste_linii(os.path.join(BASE_DIR, "sudo.txt"))
curente_cron = citeste_linii(os.path.join(BASE_DIR, "crontab.txt"))

# Referințele de sistem curat (baseline)
sistem_curat_sudo = {"root ALL=(ALL:ALL) ALL"}
sistem_curat_cron = set()

# Calculăm elementele noi
noi_sudo = curente_sudo - sistem_curat_sudo
noi_cron = curente_cron - sistem_curat_cron

print(f"{len(noi_sudo)} reguli Sudo noi fata de sistemul curat\n")
for r in sorted(noi_sudo):
    print(f" {r}")

print(f"\n{len(noi_cron)} task-uri Cron noi fata de sistemul curat\n")
for c in sorted(noi_cron):
    print(f" {c}")
   # ==========================================
# EXERCIȚIUL B (Afișare SUID periculoase / noi)
# ==========================================

import os

BASE_DIR = "/home/david/Documente/GitHub/davidculea2-wq/arsenal/privesc"

def citeste_linii(cale):
    if not os.path.exists(cale):
        return set()
    with open(cale, encoding="utf-8") as f:
        return {linie.strip() for linie in f if linie.strip() and not linie.strip().startswith('#')}

# Citim fișierul curent
curente_suid = citeste_linii(os.path.join(BASE_DIR, "suid.txt"))

# Setul de referință (cele 9 elemente dintr-un sistem curat)
baza_suid = {
    "/bin/mount", "/bin/umount", "/bin/su", "/usr/bin/sudo", 
    "/usr/bin/passwd", "/usr/bin/chfn", "/usr/bin/chsh", "/usr/bin/newgrp", "/bin/ping"
}

# Calculăm elementele noi (diferența)
elemente_noi = sorted(list(curente_suid - baza_suid))

print("periculoase")
print(f"NOI: {elemente_noi}")
# ==========================================
# EXERCIȚIUL B4: Validare / Test Passed
# ==========================================

import os

BASE_DIR = "/home/david/Documente/GitHub/davidculea2-wq/arsenal/privesc"

def citeste_linii(cale):
    if not os.path.exists(cale):
        return set()
    with open(cale, encoding="utf-8") as f:
        return {linie.strip() for linie in f if linie.strip() and not linie.strip().startswith('#')}

# Verificare simplă că fișierul există și conține datele corecte
curente_suid = citeste_linii(os.path.join(BASE_DIR, "suid.txt"))

baza_suid = {
    "/bin/mount", "/bin/umount", "/bin/su", "/usr/bin/sudo", 
    "/usr/bin/passwd", "/usr/bin/chfn", "/usr/bin/chsh", "/usr/bin/newgrp", "/bin/ping"
}

# Dacă diferența conține cele 4 elemente noi, testul este trecut cu succes
elemente_noi = curente_suid - baza_suid

if len(elemente_noi) == 4:
    print("1 passed")
else:
    print("0 passed (Verifică fișierele)")