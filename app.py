from flask import Flask, jsonify, request
from flask_migrate import Migrate
from models import db, company, calendar, employee, meeting, replacement_cost, training, turnover
from apis import api, company, employee
from flask_cors import CORS
from AppError import AppError
from flask_talisman import Talisman
from shadowd.flask_connector import InputFlask, OutputFlask, Connector

"""Initialize the core application."""
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://pvgomjgwtonjxj:681e2b1a1a91b62852e6d5d67b32c7c0f68f2fa63b8152a01a0c212d25370116@ec2-52-215-22-82.eu-west-1.compute.amazonaws.com:5432/d6s01vq9qjnav'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['PROPAGATE_EXCEPTIONS']=True

CORS(app)
Talisman(app, content_security_policy={
        'style-src': [
            '\'unsafe-inline\'',
            '\'self\'',
        ]
        })

api.init_app(app)
db.init_app(app)

@app.errorhandler(AppError)
def handle_app_error(ex):
    response = jsonify(ex.error)
    response.status_code = ex.status_code
    return response

@app.before_request
def before_req():
    input = InputFlask(request)
    output = OutputFlask()

    Connector().start(input, output)

if __name__ == "__main__":
    app.run()
    
with app.app_context():
    migrate = Migrate(app, db)
    migrate.init_app(app)
# source venv/Scripts/activate
# python app.py