from flask import Flask

from models import db
from apis import api

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///hrplus'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

api.init_app(app)
db.init_app(app)

with app.app_context():
    db.create_all()

# app.run(debug=True)


# source venv/Scripts/activate
# python app.py