# webtools.py
import requests

BASE_URL = "https://cybercor.org"
TIMEOUT = 10
DEFAULT_HEADERS = {"User-Agent": "WebLab-Student"}

def fetch(url: str):
    return requests.get(url, headers=DEFAULT_HEADERS, timeout=TIMEOUT)

def get_status(url: str) -> int:
    try:
        return fetch(url).status_code
    except:
        return 0

def get_title(html: str) -> str:
    start = html.find("<title>") + len("<title>")
    end = html.find("</title>")
    if start > len("<title>") and end != -1:
        return html[start:end].strip()
    return "Fără titlu"

def security_headers(url: str) -> dict:
    try:
        r = fetch(url)
        antete = [
            "Strict-Transport-Security", "Content-Security-Policy",
            "X-Frame-Options", "X-Content-Type-Options", "Referer-Policy"
        ]
        return {h: h in r.headers for h in antete}
    except:
        return {}

def score_headers(results: dict) -> str:
    if not results:
        return "0/5"
    return f"{sum(1 for v in results.values() if v)}/5"