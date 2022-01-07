from flask import Flask
from flask_migrate import Migrate
from models import db, company, calendar, employee, meeting, replacement_cost, role, training, turnover
from apis import api, company, employee, role


"""Initialize the core application."""
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://pvgomjgwtonjxj:681e2b1a1a91b62852e6d5d67b32c7c0f68f2fa63b8152a01a0c212d25370116@ec2-52-215-22-82.eu-west-1.compute.amazonaws.com:5432/d6s01vq9qjnav'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

api.init_app(app)
db.init_app(app)

if __name__ == "__main__":
    app.run()
    with app.app_context():
        migrate = Migrate(app, db)
        migrate.init_app(app)

# source venv/Scripts/activate
# python app.py