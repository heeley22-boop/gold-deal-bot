import requests
import re
from bs4 import BeautifulSoup

URLS = [
    "https://www.pawnamerica.com/search?q=gold",
    "https://www.unclaimedbaggage.com/search?q=gold"
]

KEYWORDS = ["14k", "18k", "22k", "24k", "diamond"]

def scan(url):
    print(f"\n🔍 Scanning: {url}")

    r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(r.text, "lxml")

    found = 0

    for a in soup.find_all("a"):
        text = a.get_text(" ", strip=True).lower()

        if any(k in text for k in KEYWORDS):
            price = re.search(r"\$(\d+)", text)
            price_val = int(price.group(1)) if price else None

            if price_val and price_val < 200:
                print("🔥 DEAL FOUND:")
                print(text[:300])
                print("-" * 40)
                found += 1

    if found == 0:
        print("No deals found this run.")

for url in URLS:
    scan(url)
