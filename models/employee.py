from sqlalchemy.dialects.postgresql import UUID
import uuid
from models import db

class Employee(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    wage = db.Column(db.Float, nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    work_hours = db.Column(db.Float, default=8)
    managed_by_id = db.Column(UUID(as_uuid=True), db.ForeignKey('employee.id'), nullable=True)
    role = db.Column(db.String(120), nullable=False)
    replacement_for_id = db.Column(UUID(as_uuid=True), db.ForeignKey('employee.id'))
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date)
    profile_id = db.Column(db.String(100))
    company_id = db.Column(UUID(as_uuid=True), db.ForeignKey('company.id'))
 
    
 