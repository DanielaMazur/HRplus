from flask_restx import Namespace, Resource, fields
from daos.calendar_dao import CalendarDAO

from models.calendar import Calendar as CalendarModel

api = Namespace('calendars', description='Calendars related operations')

createCalendar = api.model('create calendar', {
    'employee_id': fields.String(required=True),
    "date": fields.Date(required=True),
    "worked_hours": fields.String(required=True),
})

updateCalendar = api.model('create calendar', {
    'employee_id': fields.String(),
    "date": fields.Date(),
    "worked_hours": fields.String(),
})

calendar = api.model('calendar', {
    'id': fields.String(required=True),
    'employee_id': fields.String(required=True),
    "date": fields.Date(required=True),
    "worked_hours": fields.String(required=True),
})

calendarDAO = CalendarDAO()

@api.route('/')
@api.expect(CalendarModel)
class CalendarList(Resource):
    @api.doc('create_calendar')
    @api.expect(createCalendar)
    @api.marshal_with(calendar, code=201)
    def post(self):
        return calendarDAO.create(api.payload)

    @api.doc('get_calendars')
    @api.marshal_with(calendar, True)
    def get(self):
        return calendarDAO.getAll()

@api.route('/<string:id>')
class Calendar(Resource):
    @api.doc('update_calendar')
    @api.expect(updateCalendar)
    @api.marshal_with(calendar, code=200)
    def put(self, id):
        return calendarDAO.update(id, api.payload)

    @api.doc('delete_calendar')
    def delete(self, id):
        return calendarDAO.delete(id)