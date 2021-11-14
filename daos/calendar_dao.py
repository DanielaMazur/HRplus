from models.calendar import Calendar
from models import db

class CalendarDAO(object):
    def get(self, id):
        return Calendar.query.get(id)

    def getAll(self):
        return Calendar.query.all()

    def create(self, calendar):
        newCalendar = Calendar(
            employee_id = calendar['employee_id'],
            date = calendar['date'],
            worked_hours = float(calendar['worked_hours'])
        )
        db.session.add(newCalendar)
        db.session.commit()
        return newCalendar

    def update(self, id, data):
        db.session.query(Calendar).filter(Calendar.id == id).update(data)
        db.session.commit()
        return self.get(id)

    def delete(self, id):
        Calendar.query.filter_by(id = id).delete()
        db.session.commit()
