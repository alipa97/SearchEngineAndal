from flask import Blueprint, render_template, request
from app.crawler.bfs_crawler import crawl
from app.search.engine import search_keyword_bfs, search_keyword_dfs, get_bfs_all_routes, get_dfs_all_routes

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/search', methods=['POST'])
def search():
    keyword = request.form['keyword']
    algo = request.form.get('algo', 'bfs')
    if algo == 'dfs':
        results = search_keyword_dfs(keyword)
        all_routes = get_dfs_all_routes()
    else:
        results = search_keyword_bfs(keyword)
        all_routes = get_bfs_all_routes()

    # Ambil seluruh rute yang hanya menuju hasil pencarian saja
    all_routes_by_keyword = []
    seen = set()
    for result in results:
        for depth, url in enumerate(result['path']):
            if (url, depth) not in seen:
                all_routes_by_keyword.append((url, depth))
                seen.add((url, depth))
    return render_template('results.html', keyword=keyword, results=results, algo=algo, all_routes=all_routes, all_routes_by_keyword=all_routes_by_keyword)

@main.route('/route')
def route():
    # placeholder untuk route
    return render_template('route.html')