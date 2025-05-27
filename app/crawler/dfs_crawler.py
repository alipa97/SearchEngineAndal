import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from app.database import save_page
from config import MAX_DEPTH

def is_same_domain(url, seed_domain):
    return urlparse(url).netloc.endswith(seed_domain)

def crawl_dfs(seed_url, max_depth=MAX_DEPTH):
    visited = set()
    seed_domain = urlparse(seed_url).netloc
    crawl_count = 0

    def dfs(current_url, path, depth):
        nonlocal crawl_count
        if current_url in visited or depth > max_depth:
            return
        crawl_count += 1
        print(f"[DFS {crawl_count}] Crawling: {current_url} (depth={depth})")
        try:
            response = requests.get(current_url, timeout=5)
            soup = BeautifulSoup(response.text, 'html.parser')
            title = soup.title.string if soup.title else 'No Title'
            text = soup.get_text()
            save_page(current_url, title, text, path)
            visited.add(current_url)
            links = []
            for link in soup.find_all('a', href=True):
                next_url = urljoin(current_url, link['href'])
                if next_url not in visited and is_same_domain(next_url, seed_domain):
                    links.append(next_url)
            for next_url in links:
                dfs(next_url, path + [next_url], depth + 1)
        except Exception as e:
            print(f"Error crawling {current_url}: {e}")
            return

    dfs(seed_url, [seed_url], 0)
