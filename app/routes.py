from flask import Blueprint, render_template, request
from app.crawler.bfs import crawl
from app.search.engine import search_keyword

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/search', methods=['POST'])
def search():
    keyword = request.form['keyword']
    results = search_keyword(keyword)
    return render_template('results.html', keyword=keyword, results=results)

@main.route('/route')
def route():
    # placeholder untuk route
    return render_template('route.html')