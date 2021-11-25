from models.training import Training
from models import db

class TrainingDAO(object):
    def get(self, id):
        return Training.query.get(id)

    def getAll(self):
        return Training.query.all()

    def create(self, training):
        newTraining = Training(
            informational_package_cost = training['informational_package_cost'],
            training_program_length = training['training_program_length'],
            avg_trainers_pay_rate = training['avg_trainers_pay_rate'],
            instruction_hours = training['instruction_hours'],
            experienced_employees_assigned = training['experienced_employees_assigned'],
            company_id = training['company_id'],
            date = training['date']
        )
        db.session.add(newTraining)
        db.session.commit()
        return newTraining

    def update(self, id, data):
        db.session.query(Training).filter(Training.id == id).update(data)
        db.session.commit()
        return self.get(id)

    def delete(self, id):
        Training.query.filter_by(id = id).delete()
        db.session.commit()
