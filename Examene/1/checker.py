from checker import build_url, is https, show_response, check_site,
scan_sites, check_headers, retry_check


def build_url(host, path):
    if not path.startswith("/"):
        path = "/" + path
    return "https://" + host + path


def is_https(url):
    return url.startswith("https://")


# Testarea functiei build_url()
print(build_url("example.com", "login"))
print(build_url("example.com", "/login"))

# Partea1 Testarea functiei is_https()
print(is_https("https://example.com"))
print(is_https("http://example.com"))


#Partea 2:
import requests

def show_response(url):
    response = requests.get(url)

    print("Status:", response.status_code)
    print("Content-Type:", response.headers.get("Content-Type"))


show_response("https://example.com")
 

      #Partea 3: 
import requests

def check_site(url):
    try:
        response = requests.get(url, timeout=5)

        return {
            "status": response.status_code,
            "content_type": response.headers.get("Content-Type"),
            "length": len(response.content),
            "server": response.headers.get("Server", "unknown")
        }

    except requests.exceptions.RequestException as error:
        return {
            "status": None,
            "error": str(error)[:100]
        }


SITES = [
    "https://example.com",
    "https://httpbin.org/status/200",
    "https://this-site-does-not-exist-123456.com"
]

for site in SITES:
    print(site, check_site(site))

Partea 4:
def scan_sites():
    results = []

    # Verificam fiecare site
    for site in SITES:
        result = check_site(site)
        result["url"] = site
        results.append(result)

    # Pastram doar site-urile cu status 200
    successful = [
        result for result in results
        if result.get("status") == 200
    ]

    # Sortam dupa dimensiune, descrescator
    successful.sort(
        key=lambda result: result.get("length", 0),
        reverse=True
    )

    # Afisam site-urile reusite
    for result in successful:
        print(
            f'{result["url"]} -> '
            f'200, {result["length"]} octeti'
        )

    # Calculam rezumatul
    failed = len(results) - len(successful)

    print(f"Reusite: {len(successful)} | Esuate: {failed}")


scan_sites()

 Partea 5: 
import requests

SECURITY_HEADERS = [
    "Strict-Transport-Security",
    "Content-Security-Policy",
    "X-Frame-Options",
    "X-Content-Type-Options"
]


def check_headers(url):
    try:
        response = requests.get(url, timeout=5)

        # Transformam numele antetelor in litere mici
        received_headers = {
            header.lower()
            for header in response.headers
        }

        present = []
        missing = []

        # Verificam antetele in ordinea din lista
        for header in SECURITY_HEADERS:
            if header.lower() in received_headers:
                present.append(header)
            else:
                missing.append(header)

        # Calculam scorul de securitate
        score = int(len(present) / len(SECURITY_HEADERS) * 100)

        return {
            "present": present,
            "missing": missing,
            "score": score
        }

    except requests.exceptions.RequestException as error:
        return {
            "status": None,
            "error": str(error)[:100]
        }


# Testarea functiei
print(check_headers("https://example.com"))
print(check_headers("https://google.com"))
print(check_headers("https://this-site-does-not-exist-123456.com"))


Partea 6:  
def retry_check(url, attempts=3):
    last_status = None
    last_error = None
    tries = 0

    for _ in range(attempts):
        tries += 1

        try:
            response = requests.get(url, timeout=5)
            last_status = response.status_code
            last_error = None

            # Pentru statusuri sub 500, ne oprim
            if last_status < 500:
                break

        except requests.exceptions.RequestException as error:
            last_status = None
            last_error = str(error)[:100]

    result = {
        "status": last_status,
        "attempts": tries
    }

    if last_status is None and last_error is not None:
        result["error"] = last_error

    return result




