from app.database import get_pages

def search_keyword(keyword):
    keyword = keyword.lower()
    matched_urls = []
    for url, data in index.items():
        if keyword in data["text"]:
            path = crawler.shortest_path.get(url, [url])
            matched_urls.append({
                "url": url,
                "title": data["title"],
                "path": path
            })
    return matched_urls
