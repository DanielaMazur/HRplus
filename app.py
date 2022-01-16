from flask import Flask, jsonify, request
from flask_migrate import Migrate
from models import db, company, calendar, employee, meeting, replacement_cost, training, turnover
from apis import api, company, employee
from flask_cors import CORS
from AppError import AppError
from flask_talisman import Talisman
from flask_wtf.csrf import CSRFProtect
import os

"""Initialize the core application."""
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("SQLALCHEMY_DATABASE_URI")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['PROPAGATE_EXCEPTIONS']=True
app.config['WTF_CSRF_SECRET_KEY'] = os.environ.get('WTF_CSRF_SECRET_KEY')
app.secret_key = os.environ.get('WTF_CSRF_SECRET_KEY')
app.config["SECURITY_CSRF_COOKIE_NAME"] = "XSRF-TOKEN"
app.config["WTF_CSRF_TIME_LIMIT"] = None

CORS(app, resources={r"/*": {"origins": ["http://localhost:3000"]}}, supports_credentials=True)
Talisman(app, content_security_policy={
        'style-src': [
            '\'unsafe-inline\'',
            '\'self\'',
        ]
        })

api.init_app(app)
db.init_app(app)
CSRFProtect(app)

@app.errorhandler(AppError)
def handle_app_error(ex):
    response = jsonify(ex.error)
    response.status_code = ex.status_code
    return response

if __name__ == "__main__":
    app.run()
    
with app.app_context():
    migrate = Migrate(app, db)
    migrate.init_app(app)
# source venv/Scripts/activate
# python app.py