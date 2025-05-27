import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from collections import deque
from app.database import save_page
from config import MAX_DEPTH

def is_same_domain(url, seed_domain):
    return urlparse(url).netloc.endswith(seed_domain)

def crawl(seed_url, max_depth=MAX_DEPTH):
    visited = set()
    queue = deque([(seed_url, [seed_url], 0)])  # (url, path, depth)
    seed_domain = urlparse(seed_url).netloc
    crawl_count = 0

    current_depth = 0
    neighbors_this_depth = 0
    max_neighbors_per_depth = 100
    next_level_queue = deque()

    while queue:
        current_url, path, depth = queue.popleft()
        if current_url in visited or depth > max_depth:
            continue
        if depth > current_depth:
            # Move to next depth
            current_depth = depth
            neighbors_this_depth = 0
            queue.extend(next_level_queue)
            next_level_queue.clear()
        if neighbors_this_depth >= max_neighbors_per_depth:
            # Simpan ke next_level_queue, proses di depth berikutnya
            next_level_queue.append((current_url, path, depth))
            continue
        neighbors_this_depth += 1
        crawl_count += 1
        print(f"[{crawl_count}] Crawling: {current_url} (depth={depth})")
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
                    queue.append((next_url, path + [next_url], depth + 1))
        except Exception as e:
            print(f"Error crawling {current_url}: {e}")
            continue
