from flask import Blueprint, request, redirect, url_for
from .crawler import crawl  # sesuaikan kalau beda

crawler_bp = Blueprint('crawler', __name__)

@crawler_bp.route('/crawl', methods=['POST'])
def crawl():
    seed_url = request.form.get('seed_url')
    if seed_url:
        crawl(seed_url)  # fungsi crawling kamu
        return redirect(url_for('main.index'))  # ganti sesuai route utama kamu
    return 'No seed URL provided', 400
