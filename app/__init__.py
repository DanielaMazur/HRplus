from flask import Flask
from flask_migrate import Migrate
from models import db, company, calendar, employee, meeting, replacement_cost, role, training, turnover
from apis import api
from flask import jsonify
from auth.decorators import AuthError



def create_app():
    """Initialize the core application."""
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:test@db/hrplus'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['PROPAGATE_EXCEPTIONS']=True

    api.init_app(app)
    db.init_app(app)

    @app.errorhandler(AuthError)
    def handle_auth_error(ex):
        print("handle_auth_error")
        response = jsonify(ex.error)
        response.status_code = ex.status_code
        return response

    with app.app_context():
        migrate = Migrate(app, db)
        migrate.init_app(app)
        return app


# source venv/Scripts/activate
# python app.py