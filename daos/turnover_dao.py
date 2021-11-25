from models.turnover import Turnover
from models import db

class TurnoverDAO(object):
    def get(self, id):
        return Turnover.query.get(id)

    def getAll(self):
        return Turnover.query.all()

    def create(self, turnover):
        newTurnover = Turnover(
            company_id = turnover['company_id'],
            meeting_id = turnover['meeting_id'],
            employee_id = turnover['employee_id']
        )
        db.session.add(newTurnover)
        db.session.commit()
        return newTurnover

    def update(self, id, data):
        db.session.query(Turnover).filter(Turnover.id == id).update(data)
        db.session.commit()
        return self.get(id)

    def delete(self, id):
        Turnover.query.filter_by(id = id).delete()
        db.session.commit()
