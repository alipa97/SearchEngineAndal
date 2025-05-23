import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from collections import deque
from app.database import save_page

def is_same_domain(url, seed_domain):
    return urlparse(url).netloc.endswith(seed_domain)

def crawl(seed_url, max_pages=100):
    visited = set()
    queue = deque([(seed_url, [seed_url])])
    seed_domain = urlparse(seed_url).netloc

    while queue and len(visited) < max_pages:
        current_url, path = queue.popleft()
        if current_url in visited:
            continue
        try:
            response = requests.get(current_url, timeout=5)
            soup = BeautifulSoup(response.text, 'html.parser')
            title = soup.title.string if soup.title else 'No Title'
            text = soup.get_text()
            save_page(current_url, title, text, path)
            visited.add(current_url)

            for link in soup.find_all('a', href=True):
                next_url = urljoin(current_url, link['href'])
                if next_url not in visited and is_same_domain(next_url, seed_domain):
                    queue.append((next_url, path + [next_url]))
        except:
            continue