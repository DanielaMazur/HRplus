from sqlalchemy.dialects.postgresql import UUID
import uuid
from models import db

class Company(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(200), nullable=False)
