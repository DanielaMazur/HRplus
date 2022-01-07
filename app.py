from flask import Flask
from flask_migrate import Migrate
from models import db, company, calendar, employee, meeting, replacement_cost, role, training, turnover
from apis import api, company, employee, role


"""Initialize the core application."""
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:test@db/hrplus'
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