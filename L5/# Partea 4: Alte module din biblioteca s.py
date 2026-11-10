# Exercitiul 35: Descompunerea unui URL
import urllib.parse

url = "https://cybercor.org/path?q=1#top"
parsed = urllib.parse.urlparse(url)

print("Schemă:", parsed.scheme)
print("Netloc:", parsed.netloc)
print("Path:", parsed.path)
print("Query:", parsed.query)
print("Fragment:", parsed.fragment)
# Exercitiul 36: Compunerea URL-urilor
import urllib.parse

base = "https://cybercor.org"
relativ = "/about"
complet = urllib.parse.urljoin(base, relativ)

print("URL complet compus:", complet)
# Exercitiul 37: Extragerea legăturilor
import re

def extract_links(html: str) -> list:
    """Extrage toate legăturile (href) dintr-un șir HTML."""
    links = re.findall(r'href=["\'](.*?)["\']', html)
    return list(set(links))

html_test = '<a href="/about">Despre</a> <a href="https://google.com">Google</a> <a href="/about">Duplicat</a>'
print("Legături unice extrase:", extract_links(html_test))
# Exercitiul 38: Interne sau externe?
def split_links(links: list, domain: str) -> tuple:
    """Separa legaturile in interne (care contin domeniul sau incep cu /) si externe."""
    internal = [l for l in links if domain in l or l.startswith('/')]
    external = [l for l in links if l not in internal]
    return internal, external

toate_linkurile = ["/contact", "https://cybercor.org/cursuri", "https://extern.com"]
intern, extern = split_links(toate_linkurile, "cybercor.org")
print("Legaturi interne:", intern)
print("Legaturi externe:", extern)
# Exercitiul 39: Propriile metode (HTMLParser)
from html.parser import HTMLParser

class ImageFinder(HTMLParser):
    """Clasă pentru parsarea HTML și extragerea adreselor imaginilor (src din tag-ul img)."""
    def __init__(self):
        super().__init__()
        self.images = []

    def handle_starttag(self, tag, attrs):
        if tag == 'img':
            attr_dict = dict(attrs)
            src = attr_dict.get('src')
            if src:
                self.images.append(src)

test_html = '<img src="logo.png"><IMG SRC="poza.jpg"><img alt="fără src">'
finder = ImageFinder()
finder.feed(test_html)
print("Imagini găsite:", finder.images)
# Exercitiul 40: Amprenta paginii
import hashlib
import requests

def page_fingerprint(url: str) -> str:
    """Calculează amprenta SHA256 pentru conținutul descărcat de la URL-ul dat."""
    r = requests.get(url, timeout=10)
    return hashlib.sha256(r.content).hexdigest()

amprenta = page_fingerprint("https://cybercor.org")
print("Amprentă SHA256:", amprenta)
# Exercitiul 41: Salvarea în JSON
import json
import requests

response = requests.get("https://cybercor.org", timeout=10)
with open("headers.json", "w", encoding="utf-8") as f:
    json.dump(dict(response.headers), f, indent=2)

print("Antetele au fost salvate cu succes în fișierul headers.json")
# Exercitiul 42: Interogare DNS
import socket

def resolve(hostname: str) -> str:
    """Interogare DNS pentru a obține adresa IP a unui hostname."""
    return socket.gethostbyname(hostname)

ip_cybercor = resolve("cybercor.org")
print("Adresa IP pentru cybercor.org:", ip_cybercor)
# Exercitiul 43: Expirarea certificatului
import socket
import ssl
import datetime

def cert_days_left(hostname: str) -> int:
    """Calculează numărul de zile rămase până la expirarea certificatului SSL."""
    context = ssl.create_default_context()
    with socket.create_connection((hostname, 443), timeout=10) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            cert = ssock.getpeercert()
            not_after = cert['notAfter']
            # Format exemplu: 'May 15 12:00:00 2027 GMT'
            exp_date = datetime.datetime.strptime(not_after, "%b %d %H:%M:%S %Y %Z")
            return (exp_date - datetime.datetime.utcnow()).days

try:
    zile_ramase = cert_days_left("cybercor.org")
    print("Zile până la expirarea certificatului SSL:", zile_ramase)
except Exception as e:
    print("Eroare la citirea certificatului:", e)