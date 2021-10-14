from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from apis import api

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/hrplus.db'
api.init_app(app)
db = SQLAlchemy(app)

app.run(debug=True)

# source venv/Scripts/activate
# python app.py