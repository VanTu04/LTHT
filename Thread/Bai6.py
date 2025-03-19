import threading
import requests

def fetch_url(url):
    response = requests.get(url)
    print(f"Content from {url[:50]}...: {response.status_code}")

urls = ["https://example.com", "https://google.com", "https://github.com"]
threads = []

for url in urls:
    thread = threading.Thread(target=fetch_url, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
