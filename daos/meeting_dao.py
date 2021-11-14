from models.meeting import Meeting
from models import db

class MeetingDAO(object):
    def get(self, id):
        return Meeting.query.get(id)

    def getAll(self):
        return Meeting.query.all()

    def create(self, meeting):
        newMeeting = Meeting(
            name = meeting["name"],
            employee_id = meeting['employee_id'],
            duration = float(meeting['duration']),
            date = meeting['date'],
            meeting_notes = meeting['meeting_notes'],
            is_interview = meeting['is_interview'])
        db.session.add(newMeeting)
        db.session.commit()
        return newMeeting

    def update(self, id, data):
        db.session.query(Meeting).filter(Meeting.id == id).update(data)
        db.session.commit()
        return self.get(id)

    def delete(self, id):
        Meeting.query.filter_by(id = id).delete()
        db.session.commit()
