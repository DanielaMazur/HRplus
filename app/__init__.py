from flask import Flask
from flask_migrate import Migrate
from models import db, company, calendar, employee, meeting, replacement_cost, role, training, turnover
from apis import api

def create_app():
    """Initialize the core application."""
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:test@db/hrplus'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    api.init_app(app)
    db.init_app(app)

    with app.app_context():
        migrate = Migrate(app, db)
        migrate.init_app(app)
        return app


# source venv/Scripts/activate
# python app.py