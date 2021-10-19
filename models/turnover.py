from sqlalchemy.dialects.postgresql import UUID
import uuid
from models import db

class Turnover(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    company_id = db.Column(UUID(as_uuid=True), db.ForeignKey('company.id'), nullable=False)
    meeting_id = db.Column(UUID(as_uuid=True), db.ForeignKey('meeting.id'), nullable=False)
    employee_id = db.Column(UUID(as_uuid=True), db.ForeignKey('employee.id'), nullable=False)
