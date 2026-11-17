import argparse
import json
from collections import Counter
from parse_auth import citeste_esecuri, pe_ip
from collections import Counter
from parse_auth import citeste_esecuri, pe_ip

# B1. suspecți() cu valoare implicită și validare
def suspecți(counts, prag=10):
    if prag < 1:
        raise ValueError(f"prag invalid: {prag} (cel putin 1)")
    
    rezultat = [(ip, n) for ip, n in counts.items() if n >= prag]
    rezultat.sort(key=lambda x: x[1], reverse=True)
    return rezultat

# Testare B1
if __name__ == "__main__":
    c = Counter({"203.0.113.9": 13, "198.51.100.7": 2})
    print(suspecți(c))
    print(suspecți(c, prag=2))
    # B2. Testarea funcției și prinderea excepției
if __name__ == "__main__":
    c = Counter({"203.0.113.9": 13, "198.51.100.7": 2})
    
    # Test normal
    print("Prag 2:", suspecți(c, prag=2))
    
    # Test cu prag invalid prins cu try...except
    try:
        print("Prag 0:", suspecți(c, prag=0))
    except ValueError as e:
        print("Eroare prinsă cu succes:", e)
        
# B3. Argumente din linia de comandă și afișare formatată
def main():
    p = argparse.ArgumentParser(description="Detector brute force din auth.log")
    p.add_argument("log", help="Calea către fișierul auth.log")
    p.add_argument("-p", "--prag", type=int, default=10, help="Pragul minim de eșecuri")
    p.add_argument("-j", "--json", action="store_true", help="Afișează raportul în format JSON")
    
    args = p.parse_args()
    
    esecuri = citeste_esecuri(args.log)
    print(f"Esecuri de autentificare: {len(esecuri)}")
    print()
    
    counts = pe_ip(esecuri)
    for ip, n in counts.most_common():
        print(f"{ip}: {n}")
        
    try:
        sus = suspecți(counts, args.prag)
    except ValueError as e:
        print(e)
        return

    print()
    if args.json:
        raport = [{"ip": ip, "incercari": n, "status": "BRUTE FORCE"} for ip, n in sus]
        print(json.dumps(raport, indent=2))
    else:
        print("Suspecti")
        print(f"(prag {args.prag}):")
        print()
        for ip, n in sus:
            print(f"{ip}  ({n} incercari)  BRUTE FORCE")

if __name__ == "__main__":
    main()
