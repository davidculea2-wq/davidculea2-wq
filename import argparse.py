def citeste_linii(cale):
    with open(cale, encoding='utf-8') as f:
        return [linie.strip() for linie in f if linie.strip() and not linie.strip().startswith('#')]

# Citim liniile din fișierul suid.txt generat în folderul de start
cai = citeste_linii('arsenal/privesc/start/suid.txt')
print("linii SUID:", len(cai))