from sqlalchemy.dialects.postgresql import UUID
import uuid
from models import db

class Meeting(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(200), nullable=False)
    employee_id = db.Column(UUID(as_uuid=True), db.ForeignKey('employee.id'), nullable=False)
    duration = db.Column(db.Float, nullable=False)
    date = db.Column(db.Date, nullable=False)
    meeting_notes = db.Column(db.String(1000))
    is_interview = db.Column(db.Boolean, default=False)