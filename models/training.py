from sqlalchemy.dialects.postgresql import UUID
import uuid
from models import db

class Training(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    informational_package_cost = db.Column(db.Float, nullable=False)
    training_program_length = db.Column(db.Float, nullable=False)
    avg_trainers_pay_rate = db.Column(db.Float, nullable=False)
    instruction_hours = db.Column(db.Float, nullable=False)
    experienced_employees_assigned = db.Column(db.Float, nullable=False)
    company_id = db.Column(UUID(as_uuid=True), db.ForeignKey('company.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
