import re
from collections import Counter

# A1. Scheletul și funcția care întoarce o fișă
TIPAR = re.compile(r'Failed password for (?:invalid user )?(\S+) from (\S+) port')

def esec(linie):
    m = TIPAR.search(linie)
    if m is None:
        return None
    return (m.group(1), m.group(2))

# A2. Lista de eșecuri, robustă la rânduri stricate
def citeste_esecuri(cale):
    esecuri = []
    try:
        with open(cale, encoding='utf-8') as f:
            for linie in f:
                r = esec(linie)
                if r is not None:
                    esecuri.append({"user": r[0], "ip": r[1]})
    except FileNotFoundError:
        print("nu gasesc", cale)
    return esecuri
from collections import Counter

# A3. Numărarea pe IP: o funcție cu return
def pe_ip(esecuri):
    return Counter(e['ip'] for e in esecuri)

esecuri = citeste_esecuri("arsenal/aparare/start/auth.log")
counts = pe_ip(esecuri)
for ip, n in counts.most_common():
    print(f"{ip}: {n}")
    # A4. Rezumatul
def main():
    cale = "arsenal/aparare/start/auth.log"
    esecuri = citeste_esecuri(cale)
    print("Esecuri de autentificare:", len(esecuri))
    
    counts = pe_ip(esecuri)
    for ip, n in counts.most_common():
        print(f"{ip}: {n}")

if __name__ == "__main__":
    main()
  