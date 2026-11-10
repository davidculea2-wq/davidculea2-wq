# Exercitiul 1: Primul import si versiunea bibliotecii requests
import requests
import urllib.request

print("Versiune requests:", requests.__version__)
print("Bibliotecile au fost importate cu succes!")
# Exercitiul 2: Doua stiluri de import
import requests
from requests import get

# Stilul 1: Folosind modulul importat complet
response_1 = requests.get("https://cybercor.org", timeout=10)
print("Status Stil 1:", response_1.status_code)
# Stilul 2: Importând direct funcția get
response_2 = get("https://cybercor.org", timeout=10)
print("Status Stil 2:", response_2.status_code)
# Exercitiul 3: Alias-uri
import requests as rq

response = rq.get("https://cybercor.org", timeout=10)
print("Status cu alias rq:", response.status_code)
# Exercitiul 4: Biblioteca standard cu ocolire SSL pentru a preveni erorile de retea
import urllib.request
import ssl

# Ignorarea erorilor de certificat SSL pentru medii online
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "https://cybercor.org"
try:
    with urllib.request.urlopen(url, context=ctx) as response:
        status = response.status
        body_snippet = response.read(200).decode('utf-8')
        
        print("Atribut status:", status)
        print("Primele 200 caractere din corp:\n", body_snippet)
except Exception as e:
    print("A aparut o eroare:", e)
    # Exercitiul 5: Privire in interiorul unui modul
import requests

elemente = dir(requests)
print("Primele 10 elemente din requests:", elemente[:10])
# Exercitiul 6: Citirea documentatiei
import requests

# Afișează documentația integrată (docstring-ul) pentru funcția get din requests
help(requests.get)
# Exercitiul 7: Cronometrarea unei cereri
import time
import requests

start_time = time.perf_counter()
response = requests.get("https://cybercor.org", timeout=10)
end_time = time.perf_counter()

print("Timp masurat cu time.perf_counter():", end_time - start_time, "secunde")
print("Timp preluat din response.elapsed:", response.elapsed)
# Exercitiul 8: Cand un import esueaza
try:
    import bs4
    print("Modulul bs4 este instalat.")
except ImportError:
    print("Instalati modulul cu: pip install beautifulsoup4")