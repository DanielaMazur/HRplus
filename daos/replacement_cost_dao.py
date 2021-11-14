from models.replacement_cost import ReplacementCost
from models import db

class ReplacementCostDAO(object):
    def get(self, id):
        return ReplacementCost.query.get(id)

    def getAll(self):
        return ReplacementCost.query.all()

    def create(self, replacement_cost):
        newReplacementCost = ReplacementCost(
            name = replacement_cost['name'],
            advertising_fees_per_termination = float(replacement_cost['advertising_fees_per_termination']),
            job_availability_communication_time = float(replacement_cost['job_availability_communication_time']),
            preemployeement_admin_fun_time = float(replacement_cost['preemployeement_admin_fun_time']),
            interview_time = float(replacement_cost['interview_time']),
            number_of_interviews = replacement_cost['number_of_interviews'],
            cost_of_materials_per_person = float(replacement_cost['cost_of_materials_per_person']),
            cost_of_scoring_per_person = float(replacement_cost['cost_of_scoring_per_person']),
            number_of_test_given = replacement_cost['number_of_test_given'],
            acquiring_and_disseminating_time = float(replacement_cost['acquiring_and_disseminating_time']),
            company_id = replacement_cost['company_id'],
            start_date = replacement_cost['start_date'],
            end_date = replacement_cost['end_date'])
        db.session.add(newReplacementCost)
        db.session.commit()
        return newReplacementCost

    def update(self, id, data):
        db.session.query(ReplacementCost).filter(ReplacementCost.id == id).update(data)
        db.session.commit()
        return self.get(id)

    def delete(self, id):
        ReplacementCost.query.filter_by(id = id).delete()
        db.session.commit()
