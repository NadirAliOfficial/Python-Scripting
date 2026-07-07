import requests, time, smtplib
from datetime import datetime

SITES = [
    "https://www.google.com",
    "https://github.com",
]
CHECK_INTERVAL = 60

def check(url):
    try:
        r = requests.get(url, timeout=10)
        return r.status_code < 400
    except Exception:
        return False

def monitor():
    print(f"Monitoring {len(SITES)} sites every {CHECK_INTERVAL}s...")
    while True:
        for url in SITES:
            status = "UP" if check(url) else "DOWN"
            ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"[{ts}] {url}: {status}")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    monitor()
