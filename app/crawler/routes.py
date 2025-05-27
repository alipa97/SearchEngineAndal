from flask import Blueprint, request, redirect, url_for
from .bfs_crawler import crawl as do_crawl
from .dfs_crawler import crawl_dfs

crawler_bp = Blueprint('crawler', __name__)

@crawler_bp.route('/crawl', methods=['POST'])
def crawl_route():
    seed_url = request.form.get('seed_url')
    crawl_algo = request.form.get('crawl_algo', 'bfs')
    if not seed_url:
        seed_url = 'https://www.upi.edu/'
    if crawl_algo == 'dfs':
        crawl_dfs(seed_url)
    else:
        do_crawl(seed_url)
    return redirect(url_for('main.index'))
