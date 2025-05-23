pages = []  # Placeholder simpan ke list

def save_page(url, title, text, path):
    pages.append({
        'url': url,
        'title': title,
        'text': text,
        'path': path
    })

def get_pages():
    return pages