from flask import Flask

from models import db
from apis import api
from schemes import ma

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/hrplus.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

api.init_app(app)
db.init_app(app)
ma.init_app(app)

app.run(debug=True)

# source venv/Scripts/activate
# python app.py