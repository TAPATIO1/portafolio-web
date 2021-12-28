from flask import Flask
import os

def create_app():
    app = Flask(__name__)

    app.config.from_mapping(
        SENGRID_KEY=os.environ.get('SENGRID_KEY'),
    )

    from  . import portfolio

    app.register_blueprint(portfolio.bp)

    return app