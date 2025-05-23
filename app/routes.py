from flask import Blueprint, render_template, request
from app.crawler.crawler import crawl
from app.search.engine import search_keyword_bfs, search_keyword_dfs

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
    else:
        results = search_keyword_bfs(keyword)
    return render_template('results.html', keyword=keyword, results=results)

@main.route('/route')
def route():
    # placeholder untuk route
    return render_template('route.html')