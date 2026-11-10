# Exercitiul 21: Prima funcție
import requests

def fetch(url):
    """Returnează obiectul răspuns pentru adresa URL dată."""
    return requests.get(url, timeout=10)

print("Rezultat fetch status:", fetch("https://cybercor.org").status_code)
# Exercitiul 22: Returnarea unei singure valori
import requests
import time

def fetch(url):
    return requests.get(url, timeout=10)

def get_status(url):
    return fetch(url).status_code

print("Status /robots.txt:", get_status("https://cybercor.org/robots.txt"))
time.sleep(1)
print("Status /sitemap.xml:", get_status("https://cybercor.org/sitemap.xml"))
# Exercitiul 23: Parametri impliciți
import requests

def fetch(url, timeout=10):
    return requests.get(url, timeout=timeout)

print("Apel cu valoare implicita:", fetch("https://cybercor.org").status_code)
print("Apel cu timeout=3:", fetch("https://cybercor.org", timeout=3).status_code)
# Exercitiul 24: O singură sarcină pe funcție
def get_title(html):
    start = html.find("<title>") + len("<title>")
    end = html.find("</title>")
    return html[start:end].strip()

html_exemplu = "<html><head><title>Test Titlu</title></head><body></body></html>"
print("Titlu extras:", get_title(html_exemplu))
# Exercitiul 25: Docstring-ul
def get_title(html):
    """Extrage și returnează titlul dintr-un șir HTML dat."""
    start = html.find("<title>") + len("<title>")
    end = html.find("</title>")
    return html[start:end].strip()

# Afișarea docstring-ului funcției folosind help()
help(get_title)
# Exercitiul 26: Adnotări de tip
import requests

def get_status(url: str) -> int:
    response = requests.get(url, timeout=10)
    return response.status_code

print("Status cu adnotări de tip:", get_status("https://cybercor.org"))
# Exercitiul 27: Fără opriri neașteptate (Try / Except)
import requests

def page_exists(url: str) -> bool:
    """Returnează True dacă pagina există și răspunde cu 200, altfel False."""
    try:
        r = requests.get(url, timeout=5)
        return r.status_code == 200
    except requests.exceptions.RequestException:
        return False

print("Există site-ul corect?", page_exists("https://cybercor.org"))
print("Există domeniul invalid?", page_exists("https://this-domain-does-not-exist.invalid"))
# Exercitiul 28: Returnarea unui dicționar
import requests
import time

def get_status(url):
    return requests.get(url, timeout=10).status_code

def check_paths(base, paths):
    """Verifică o listă de căi și returnează un dicționar cu statusurile lor."""
    rezultat = {}
    for path in paths:
        url = base.rstrip('/') + '/' + path.lstrip('/')
        rezultat[path] = get_status(url)
        time.sleep(1)
    return rezultat

# Testarea funcției cu câteva căi comune
cai_de_verificat = ["/robots.txt", "/sitemap.xml"]
print("Dicționar căi și statusuri:", check_paths("https://cybercor.org", cai_de_verificat))
# Exercitiul 29: Argumente cu nume
import requests

def get_header(url, name, default="lipsește"):
    """Returnează valoarea unui antet specific sau o valoare implicită."""
    r = requests.get(url, timeout=10)
    return r.headers.get(name, default)

# Testarea funcției folosind argumente cu nume
valoare_server = get_header("https://cybercor.org", name="Server")
print("Valoare antet Server:", valoare_server)
# Exercitiul 30: Antete de securitate
import requests

def security_headers(url):
    """Verifică prezența a 5 antete esențiale de securitate."""
    r = requests.get(url, timeout=10)
    antete_cautate = [
        "Strict-Transport-Security",
        "Content-Security-Policy",
        "X-Frame-Options",
        "X-Content-Type-Options",
        "Referer-Policy"
    ]
    return {antet: antet in r.headers for antet in antete_cautate}

rezultate_securitate = security_headers("https://cybercor.org")
print("Antete de securitate:", rezultate_securitate)
# Exercitiul 31: Funcții care apelează funcții
def score_headers(results):
    """Calculează și returnează scorul sub formă de șir de caractere (ex: 3/5)."""
    true_count = sum(1 for v in results.values() if v)
    return f"{true_count}/5"

# Testare folosind un dicționar simulat de antete de securitate
rezultate_mock = {
    "Strict-Transport-Security": True,
    "Content-Security-Policy": False,
    "X-Frame-Options": True,
    "X-Content-Type-Options": True,
    "Referer-Policy": False
}

scor_obtinut = score_headers(rezultate_mock)
print("Scor antete de securitate:", scor_obtinut)
# Exercitiul 32: Două funcții, o sarcină
import requests

def fetch_robots(base):
    """Returnează textul din /robots.txt sau None dacă pagina nu există."""
    url = base.rstrip('/') + '/robots.txt'
    r = requests.get(url, timeout=10)
    return r.text if r.status_code == 200 else None

robots_text = fetch_robots("https://cybercor.org")
print("Conținut /robots.txt (primii 200 de caractere):")
print(str(robots_text)[:200])
# Exercitiul 33: Oricâte argumente (*args)
import time
import requests

def response_times(*urls):
    """Măsoară timpul de răspuns pentru oricâte URL-uri furnizate."""
    timpi = {}
    for u in urls:
        start = time.perf_counter()
        requests.get(u, timeout=10)
        timpi[u] = time.perf_counter() - start
    return timpi

# Testarea funcției cu mai multe URL-uri
rezultate_timpi = response_times("https://cybercor.org", "https://httpbin.org/get")
print("Timp de răspuns pentru URL-uri:", rezultate_timpi)
# Exercitiul 34: Argumente cu nume colectate (**kwargs)
def log_message(message, **details):
    """Afișează un mesaj formatat însoțit de detalii suplimentare transmise sub formă de kwargs."""
    detalii_str = ", ".join(f"{k}={v}" for k, v in details.items())
    print(f"[{message}] {detalii_str}")

# Testarea funcției de logare
log_message("VERIFICAT", url="https://cybercor.org", status=200, timp="0.23s")