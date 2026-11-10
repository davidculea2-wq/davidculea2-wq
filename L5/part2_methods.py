# Exercitiul 9: Elemente de baza ale raspunsului
import requests

BASE_URL = "https://cybercor.org"
response = requests.get(BASE_URL, timeout=10)

print("status_code:", response.status_code)     # Atribut
print("ok:", response.ok)                       # Atribut
print("url:", response.url)                     # Atribut
print("encoding:", response.encoding)           # Atribut
# Exercitiul 10: Tratarea erorilor cu o metoda
import requests

BASE_URL = "https://cybercor.org"

try:
    err_resp = requests.get(f"{BASE_URL}/pagina-inexistenta", timeout=10)
    err_resp.raise_for_status()
except requests.exceptions.HTTPError as e:
    print("Eroare HTTP prinsa cu succes:", e)
    # Exercitiul 11: Toate antetele
import requests

BASE_URL = "https://cybercor.org"
response = requests.get(BASE_URL, timeout=10)

for key, value in response.headers.items():
    print(f"{key}: {value}")
    # Exercitiul 12: Metode de dicționar pentru antete
import requests

BASE_URL = "https://cybercor.org"
response = requests.get(BASE_URL, timeout=10)

print("Server:", response.headers.get('Server'))
print("Content-Type:", response.headers.get('Content-Type'))
print("content-type (lowercase):", response.headers.get('content-type'))
# Exercitiul 13: Inlantuirea metodelor de sir
import requests

BASE_URL = "https://cybercor.org"
response = requests.get(BASE_URL, timeout=10)

cyber_count = response.text.lower().count("cyber")
print("Aparitii cuvant 'cyber':", cyber_count)
# Exercitiul 14: Gasirea titlului
import requests

BASE_URL = "https://cybercor.org"
response = requests.get(BASE_URL, timeout=10)

html = response.text
start_idx = html.find("<title>") + len("<title>")
end_idx = html.find("</title>")
title = html[start_idx:end_idx].strip()

print("Titlu pagina:", title)
# Exercitiul 15: Numararea liniilor
import requests

BASE_URL = "https://cybercor.org"
response = requests.get(BASE_URL, timeout=10)

lines_count = len(response.text.splitlines())
print("Numar linii HTML:", lines_count)
# Exercitiul 16: Verificarea HTTPS
import requests

BASE_URL = "https://cybercor.org"
response = requests.get(BASE_URL, timeout=10)

print("Incepe cu https://?", response.url.startswith("https://"))
# Exercitiul 17: Urmarirea redirectionarilor
import requests

redirect_resp = requests.get("http://cybercor.org", timeout=10)

print("Istoric redirectionari:", [r.url for r in redirect_resp.history])
print("URL final:", redirect_resp.url)
# Exercitiul 18: HEAD versus GET
import requests

BASE_URL = "https://cybercor.org"
head_resp = requests.head(BASE_URL, timeout=10)
response = requests.get(BASE_URL, timeout=10)

print("Lungime continut HEAD (fara corp):", len(head_resp.content))
print("Lungime continut GET:", len(response.content))
# Exercitiul 19: Cookie-uri
import requests

BASE_URL = "https://cybercor.org"
cookies_resp = requests.get(BASE_URL, timeout=10)

if cookies_resp.cookies:
    for cookie in cookies_resp.cookies:
        print(f"Cookie: {cookie.name} = {cookie.value}")
else:
    print("Niciun cookie setat de server.")
    # Exercitiul 20: Sesiuni
import requests

ECHO_URL = "https://httpbin.org"
session = requests.Session()
session.headers.update({"User-Agent": "WebLab-Student"})

sess_resp = session.get(f"{ECHO_URL}/headers", timeout=10)
print("Raspuns sesiune headers (JSON):\n", sess_resp.json())
