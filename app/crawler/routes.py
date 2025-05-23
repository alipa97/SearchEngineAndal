from flask import Blueprint, request, redirect, url_for
from .crawler import crawl as do_crawl

crawler_bp = Blueprint('crawler', __name__)

@crawler_bp.route('/crawl', methods=['POST'])
def crawl_route():
    seed_url = request.form.get('seed_url')
    if not seed_url:
        seed_url = 'https://www.upi.edu/'
    do_crawl(seed_url)
    return redirect(url_for('main.index'))
