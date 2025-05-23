from flask import Flask
from .routes import main
from .crawler.routes import crawler_bp

def create_app():
    app = Flask(__name__)

    # Daftarkan blueprint utama
    app.register_blueprint(main)

    # Daftarkan blueprint untuk crawler
    app.register_blueprint(crawler_bp)

    return app
