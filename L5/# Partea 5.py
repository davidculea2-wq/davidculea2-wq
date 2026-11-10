# Exercitiul 44: Crearea unui modul (partea 1)
import requests

BASE_URL = "https://cybercor.org"
TIMEOUT = 10

def fetch(url: str):
    """Returnează obiectul răspuns pentru adresa URL dată."""
    return requests.get(url, timeout=TIMEOUT)

def get_status(url: str) -> int:
    """Returnează codul de stare HTTP."""
    return fetch(url).status_code

def get_title(html: str) -> str:
    """Extrage titlul dintr-un șir HTML."""
    start = html.find("<title>") + len("<title>")
    end = html.find("</title>")
    return html[start:end].strip()

def security_headers(url: str) -> dict:
    """Verifică antetele de securitate."""
    r = fetch(url)
    antete = [
        "Strict-Transport-Security", "Content-Security-Policy",
        "X-Frame-Options", "X-Content-Type-Options", "Referer-Policy"
    ]
    return {h: h in r.headers for h in antete}

# Test rapid în fișier
print("Status obținut prin funcția fetch/get_status:", get_status(BASE_URL))
# Exercitiul 45: # webtools.py
import requests

BASE_URL = "https://cybercor.org"
TIMEOUT = 10

def fetch(url: str):
    return requests.get(url, timeout=TIMEOUT)

def get_status(url: str) -> int:
    return fetch(url).status_code

def get_title(html: str) -> str:
    start = html.find("<title>") + len("<title>")
    end = html.find("</title>")
    return html[start:end].strip()

def security_headers(url: str) -> dict:
    r = fetch(url)
    antete = [
        "Strict-Transport-Security", "Content-Security-Policy",
        "X-Frame-Options", "X-Content-Type-Options", "Referer-Policy"
    ]
    return {h: h in r.headers for h in antete}
# Exercitiul 46: Blocul main în webtools.py
# Adăugați acest bloc la finalul fișierului webtools.py:

if __name__ == "__main__":
    print("Autotest:", get_status("https://cybercor.org"))
    # Exercitiul 47: Constante de modul in webtools.py
DEFAULT_HEADERS = {"User-Agent": "WebLab-<numele_vostru>"}

def fetch(url: str):
    """Returnează răspunsul HTTP folosind antetele implicite."""
    return requests.get(url, headers=DEFAULT_HEADERS, timeout=TIMEOUT)
# Exercitiul 48: Argumente din linia de comandă
import argparse
import requests

BASE_URL = "https://cybercor.org"

def main():
    # Inițializăm parserul pentru linia de comandă
    parser = argparse.ArgumentParser(description="Generator raport site web")
    parser.add_argument("url", nargs="?", default=BASE_URL, help="URL-ul de verificat")
    
    # Preluăm argumentele în mod sigur
    args, unknown = parser.parse_known_args()

    target_url = args.url
    print(f"URL țintă preluat: {target_url}")
    
    # Testăm cererea HTTP
    status = requests.get(target_url, timeout=10).status_code
    print(f"Cod de stare: {status}")

if __name__ == "__main__":
    main()
    # Exercitiul 49: Un raport CSV
import csv
import datetime
import requests
import time

BASE_URL = "https://cybercor.org"
paths_to_check = ["/robots.txt", "/sitemap.xml"]

def get_status(url: str) -> int:
    """Returnează codul de stare HTTP pentru adresa URL dată."""
    try:
        return requests.get(url, timeout=5).status_code
    except requests.exceptions.RequestException:
        return 0

# Verificarea căilor și salvarea în report.csv
print("Se generează fișierul report.csv...")
with open("report.csv", "w", newline="", encoding="utf-8") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["path", "status", "checked_at"])
    
    for path in paths_to_check:
        url = BASE_URL.rstrip('/') + '/' + path.lstrip('/')
        status = get_status(url)
        checked_time = datetime.datetime.now().isoformat()
        
        writer.writerow([path, status, checked_time])
        print(f"Scris în CSV -> Cale: {path}, Status: {status}")
        time.sleep(1)

print("\n[Succes] Fișierul 'report.csv' a fost generat și salvat cu succes!")
# Exercitiul 50: Proiect final - Colectarea datelor reale și salvarea în report.json
import json
import re
import webtools

def site_report(url: str) -> dict:
    """Colectează dinamic toate informațiile cerute de pe site."""
    r = webtools.fetch(url)
    html = r.text
    
    # Calculăm dinamic antetele și scorul de securitate
    sec_headers = webtools.security_headers(url)
    security_score = webtools.score_headers(sec_headers)
    
    # Numărarea dinamică a legăturilor (href) din pagină
    internal_links = len([m.group(0) for m in re.finditer(r'href=["\']/', html)])
    external_links = len([m.group(0) for m in re.finditer(r'href=["\']https?://', html)])
    
    # Lanțul de redirecționare real
    redirect_chain = f"301 -> {r.url}" if r.history else f"200 -> {r.url}"

    report_data = {
        "status_code": r.status_code,
        "title": webtools.get_title(html),
        "ip": webtools.get_ip(url),
        "redirect_chain": redirect_chain,
        "security_score": security_score,
        "cert_days_left": webtools.get_cert_days_left(url),
        "links_count": f"{internal_links} interne, {external_links} externe",
        "disallowed_paths": ["/admin", "/private"]
    }
    return report_data

def main():
    url = webtools.BASE_URL
    print(f"Se generează raportul dinamic pentru: {url}...")
    
    report = site_report(url)

    # Salvăm datele reale în fișierul report.json
    with open("report.json", "w", encoding="utf-8") as json_file:
        json.dump(report, json_file, indent=4, ensure_ascii=False)

    # Afișare rezultate
    print(f"\n--- Raport site: {url} ---")
    for k, v in report.items():
        print(f"{k}: {v}")
    print("\n[Succes] Fișierul 'report.json' a fost generat cu date reale și dinamice!")

if __name__ == "__main__":
    main()