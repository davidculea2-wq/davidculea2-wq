"""Small HTTP helpers used by the HTTP toolkit exercise."""

import requests

BASE = "https://httpbin.org"
PATHS = ["/get", "/redirect/2", "/delay/1", "/status/404", "/delay/5"]


def search(params):
    response = requests.get(BASE + "/get", params=params)
    response.raise_for_status()
    return response.json()["args"]


def search_url(params):
    response = requests.get(BASE + "/get", params=params)
    return response.url


def fetch_with_agent(agent):
    response = requests.get(BASE + "/headers", headers={"User-Agent": agent})
    response.raise_for_status()
    return response.json()["headers"]["User-Agent"]


def default_agent():
    response = requests.get(BASE + "/headers")
    response.raise_for_status()
    return response.json()["headers"]["User-Agent"]


def post_json(data):
    response = requests.post(BASE + "/post", json=data)
    response.raise_for_status()
    return response.json()["json"]


def post_form(data):
    response = requests.post(BASE + "/post", data=data)
    response.raise_for_status()
    return response.json()["form"]


def describe_status(code):
    response = requests.get(f"{BASE}/status/{code}")
    status = response.status_code
    if 200 <= status < 300:
        return "succes"
    if 400 <= status < 500:
        return "eroare client"
    if 500 <= status < 600:
        return "eroare server"
    return "eroare client" if status >= 400 else "succes"


def is_ok(code):
    try:
        response = requests.get(f"{BASE}/status/{code}")
        response.raise_for_status()
        return True
    except requests.HTTPError:
        return False


def count_redirects(n):
    response = requests.get(f"{BASE}/redirect/{n}")
    return len(response.history)


def final_url(n):
    response = requests.get(f"{BASE}/redirect/{n}")
    return response.url


def first_hop(n):
    response = requests.get(f"{BASE}/redirect/{n}", allow_redirects=False)
    return response.headers.get("Location")


def cookie_demo(name, value):
    with requests.Session() as session:
        session.get(BASE + "/cookies/set", params={name: value})
        response = session.get(BASE + "/cookies")
        response.raise_for_status()
        return response.json()["cookies"]


def no_session_demo(name, value):
    requests.get(BASE + "/cookies/set", params={name: value})
    response = requests.get(BASE + "/cookies")
    response.raise_for_status()
    return response.json()["cookies"]


def report(path):
    try:
        response = requests.get(BASE + path, timeout=3)
        return {
            "status": response.status_code,
            "final_url": response.url,
            "redirects": len(response.history),
            "seconds": response.elapsed.total_seconds(),
            "content_type": response.headers.get("Content-Type"),
        }
    except requests.RequestException as error:
        message = str(error).splitlines()[0] or error.__class__.__name__
        return {"status": None, "error": message}


def main():
    results = []
    for path in PATHS:
        result = report(path)
        result["path"] = path
        results.append(result)

    successful = [item for item in results if item.get("status") == 200]
    for item in sorted(successful, key=lambda item: item.get("seconds", 0), reverse=True):
        print(f'{item["path"]} -> 200, {item["seconds"]:.2f} secunde')

    failed_count = len(results) - len(successful)
    print(f"Reușite: {len(successful)} | Eșuate: {failed_count}")
    return results


def check_login(user, password):
    try:
        response = requests.get(
            f"{BASE}/basic-auth/admin/secret", auth=(user, password), timeout=3
        )
        return response.status_code == 200
    except requests.RequestException:
        return False


if __name__ == "__main__":
    main()
