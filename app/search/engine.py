from app.database import get_pages

def search_keyword(keyword):
    keyword = keyword.lower()
    results = []
    for page in get_pages():
        if keyword in page['text'].lower():
            results.append(page)
    return results[:10]  # limit result