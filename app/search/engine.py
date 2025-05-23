from app.database import get_pages

def search_keyword(keyword):
    keyword = keyword.lower()
    matched_urls = []
    for page in get_pages():
        if keyword in page["text"].lower():
            matched_urls.append({
                "url": page["url"],
                "title": page["title"],
                "path": page["path"]
            })
    return matched_urls

def search_keyword_bfs(keyword):
    keyword = keyword.lower()
    matched_urls = []
    for page in get_pages():
        if keyword in page["text"].lower():
            matched_urls.append({
                "url": page["url"],
                "title": page["title"],
                "path": page["path"]
            })
    return matched_urls

def search_keyword_dfs(keyword):
    keyword = keyword.lower()
    matched_urls = []
    pages = get_pages()
    visited = set()
    def dfs(idx):
        if idx in visited:
            return
        visited.add(idx)
        page = pages[idx]
        if keyword in page["text"].lower():
            matched_urls.append({
                "url": page["url"],
                "title": page["title"],
                "path": page["path"]
            })
        # DFS ke halaman berikutnya (berdasarkan urutan simpan path)
        for i, p in enumerate(pages):
            if p["path"][:-1] == page["path"] and i not in visited:
                dfs(i)
    for i in range(len(pages)):
        dfs(i)
    return matched_urls
