from sqlalchemy.dialects.postgresql import UUID
import uuid
from models import db

class Role(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(50), nullable=False)
    company_id = db.Column(UUID(as_uuid=True), db.ForeignKey('company.id'), nullable=False)

