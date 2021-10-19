from sqlalchemy.dialects.postgresql import UUID
import uuid
from models import db

class Calendar(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    employee_id = db.Column(UUID(as_uuid=True), db.ForeignKey('employee.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    worked_hours = db.Column(db.Float, nullable=False)
