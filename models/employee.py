from models import db
from werkzeug.security import generate_password_hash, check_password_hash

class Employee(db.Model):
    #TODO replace Integer ids with uuid
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    wage = db.Column(db.Float, nullable=False)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password_hash = db.Column(db.String(128), nullable=False)
    work_hours = db.Column(db.Float, default=8)
    managed_by_id = db.Column(db.Integer, db.ForeignKey('employee.id'), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False)
    replacement_for_id = db.Column(db.Integer, db.ForeignKey('employee.id'))
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date)

    company = db.relationship('Company', backref=db.backref('employees', lazy=True))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
# https://dev.to/kaelscion/authentication-hashing-in-sqlalchemy-1bem