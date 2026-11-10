import requests

BASE = "https://httpbin.org"
PATHS = ["/get", "/redirect/2", "/delay/1", "/status/404", "/delay/5"]

# Partea 1: parametri în URL
def search(params):
    """GET pe /get cu parametri în URL; returnează parametrii primiți de server."""[cite: 1]
    r = requests.get(f"{BASE}/get", params=params)[cite: 3]
    return r.json()["args"][cite: 3]

def search_url(params):
    """Returnează adresa completă construită de requests, cu tot cu parametri."""[cite: 1, 2]
    r = requests.get(f"{BASE}/get", params=params)[cite: 3]
    return r.url[cite: 3]


# Partea 2: anteturi
def fetch_with_agent(agent):
    """GET pe /headers cu User-Agent=agent; returnează User-Agent-ul văzut de server."""[cite: 2]
    r = requests.get(f"{BASE}/headers", headers={"User-Agent": agent})[cite: 3]
    return r.json()["headers"]["User-Agent"][cite: 3]

def default_agent():
    """Returnează User-Agent-ul trimis de requests când nu setezi nimic."""[cite: 2]
    r = requests.get(f"{BASE}/headers")[cite: 3]
    return r.json()["headers"]["User-Agent"][cite: 3]


# Partea 3: trimiterea datelor
def post_json(data):
    """POST cu datele ca JSON pe /post; returnează JSON-ul primit de server."""[cite: 2]
    r = requests.post(f"{BASE}/post", json=data)[cite: 3]
    return r.json()["json"][cite: 3]

def post_form(data):
    """POST cu datele ca formular pe /post; returnează formularul primit de server."""[cite: 2]
    r = requests.post(f"{BASE}/post", data=data)[cite: 3]
    return r.json()["form"][cite: 3]


# Partea 4: coduri de stare
def describe_status(code):
    """GET pe /status/<code>; returnează 'succes', 'eroare client' sau 'eroare server'."""[cite: 2]
    r = requests.get(f"{BASE}/status/{code}")[cite: 4]
    if 200 <= r.status_code < 300:[cite: 4]
        return "succes"[cite: 4]
    elif 400 <= r.status_code < 500:[cite: 4]
        return "eroare client"[cite: 4]
    elif 500 <= r.status_code < 600:[cite: 4]
        return "eroare server"[cite: 4]

def is_ok(code):
    """GET pe /status/<code>; returnează True dacă cererea a reușit, altfel False."""[cite: 2]
    try:
        r = requests.get(f"{BASE}/status/{code}")[cite: 4]
        r.raise_for_status()[cite: 4]
        return True[cite: 4]
    except requests.HTTPError:[cite: 4]
        return False[cite: 4]


# Partea 5: redirecționări
def count_redirects(n):
    """GET pe /redirect/<n>; returnează câte redirecționări au fost urmate."""[cite: 2, 4]
    r = requests.get(f"{BASE}/redirect/{n}")[cite: 4]
    return len(r.history)[cite: 4]

def final_url(n):
    """GET pe /redirect/<n>; returnează adresa la care ai ajuns."""[cite: 3, 4]
    r = requests.get(f"{BASE}/redirect/{n}")[cite: 4]
    return r.url[cite: 4]

def first_hop(n):
    """GET pe /redirect/<n> FĂRĂ a urma redirecționarea; returnează antetul Location."""[cite: 3, 4]
    r = requests.get(f"{BASE}/redirect/{n}", allow_redirects=False)[cite: 4]
    return r.headers.get("Location")[cite: 4]


# Partea 6: sesiuni și cookie-uri
def cookie_demo(name, value):
    """Setează un cookie, apoi citește cookie-urile înapoi folosind o SINGURĂ sesiune."""[cite: 3, 5]
    s = requests.Session()[cite: 4, 5]
    s.get(f"{BASE}/cookies/set?{name}={value}")[cite: 4, 5]
    r = s.get(f"{BASE}/cookies")[cite: 4, 5]
    return r.json()["cookies"][cite: 4, 5]

def no_session_demo(name, value):
    """Fă același lucru cu apeluri simple requests.get; returnează cookie-urile văzute de server."""[cite: 3, 5]
    requests.get(f"{BASE}/cookies/set?{name}={value}")[cite: 5]
    r = requests.get(f"{BASE}/cookies")[cite: 5]
    return r.json()["cookies"][cite: 5]


# Partea 7: raportul final
def report(path):
    """Returnează un dicționar care descrie pagina de la BASE + path."""[cite: 3, 5]
    try:
        r = requests.get(f"{BASE}{path}", timeout=3)[cite: 5]
        return {
            "status": r.status_code,[cite: 5]
            "final_url": r.url,[cite: 5]
            "redirects": len(r.history),[cite: 5]
            "seconds": round(r.elapsed.total_seconds(), 2),[cite: 5]
            "content_type": r.headers.get("Content-Type")[cite: 5]
        }
    except requests.RequestException:[cite: 6]
        return {"status": None, "error": "timeout sau eroare de conexiune"}[cite: 5]

def main():
    results = []
    success_count = 0
    error_count = 0

    for path in PATHS:[cite: 1, 5]
        rep = report(path)[cite: 5]
        results.append((path, rep))[cite: 5]
        if rep["status"] == 200:[cite: 5]
            success_count += 1
        else:
            error_count += 1

    # Sortăm după seconds (cele mai lente prime) doar paginile cu status 200
    valid_results = [r for r in results if r[1]["status"] == 200][cite: 5]
    valid_results.sort(key=lambda x: x[1]["seconds"], reverse=True)[cite: 5]

    for path, rep in valid_results:[cite: 5]
        print(f"{path} -> {rep['status']}, {rep['seconds']} secunde")[cite: 6]

    print(f"Reușite: {success_count} | Eșuate: {error_count}")[cite: 6]


# Bonus: autentificare
def check_login(user, password):
    """Returnează True dacă serverul acceptă datele de autentificare, altfel False."""[cite: 3, 6]
    try:
        r = requests.get(f"{BASE}/basic-auth/admin/secret", auth=(user, password), timeout=3)[cite: 6]
        return r.status_code == 200[cite: 6]
    except requests.RequestException:[cite: 6]
        return False[cite: 6]


if __name__ == "__main__":
    main()[cite: 3]