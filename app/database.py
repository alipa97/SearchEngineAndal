pages = []  # Placeholder simpan ke list

def save_page(url, title, text, path):
    print(f"[SAVE] {url} | {title}")  # DEBUG: tampilkan url yang disimpan
    pages.append({
        'url': url,
        'title': title,
        'text': text,
        'path': path
    })

def get_pages():
    return pages