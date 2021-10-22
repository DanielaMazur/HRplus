from sqlalchemy.dialects.postgresql import UUID
import uuid
from models import db

class ReplacementCost(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(200), nullable=False)
    advertising_fees_per_termination = db.Column(db.Float, nullable=False)
    job_availability_communication_time = db.Column(db.Float, nullable=False)
    preemployeement_admin_fun_time = db.Column(db.Float, nullable=False)
    interview_time = db.Column(db.Float, nullable=False)
    number_of_interviews = db.Column(db.Integer, nullable=False)
    cost_of_materials_per_person = db.Column(db.Float, nullable=False)
    cost_of_scoring_per_person = db.Column(db.Float, nullable=False)
    number_of_test_given = db.Column(db.Integer, nullable=False)
    acquiring_and_disseminating_time = db.Column(db.Float, nullable=False)
    company_id = db.Column(UUID(as_uuid=True), db.ForeignKey('company.id'), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    