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
