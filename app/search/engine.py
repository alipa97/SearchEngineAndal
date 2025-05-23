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
    return search_keyword(keyword)

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
        # DFS ke anak (berdasarkan parent di path)
        for i, p in enumerate(pages):
            if len(p["path"]) > 1 and p["path"][-2] == page["url"]:
                dfs(i)
    # Mulai DFS dari root
    for i, page in enumerate(pages):
        if len(page["path"]) == 1:
            dfs(i)
    return matched_urls

def get_bfs_all_routes():
    # BFS traversal, return list of (url, depth)
    pages = get_pages()
    result = []
    queue = []
    for i, page in enumerate(pages):
        if len(page["path"]) == 1:
            queue.append((i, 0))
    visited = set()
    while queue:
        idx, depth = queue.pop(0)
        if idx in visited:
            continue
        visited.add(idx)
        page = pages[idx]
        result.append((page["url"], depth))
        for i, p in enumerate(pages):
            if len(p["path"]) > 1 and p["path"][-2] == page["url"]:
                queue.append((i, depth+1))
    return result

def get_dfs_all_routes():
    # DFS traversal, return list of (url, depth)
    pages = get_pages()
    result = []
    visited = set()
    def dfs(idx, depth):
        if idx in visited:
            return
        visited.add(idx)
        page = pages[idx]
        result.append((page["url"], depth))
        for i, p in enumerate(pages):
            if len(p["path"]) > 1 and p["path"][-2] == page["url"]:
                dfs(i, depth+1)
    for i, page in enumerate(pages):
        if len(page["path"]) == 1:
            dfs(i, 0)
    return result
