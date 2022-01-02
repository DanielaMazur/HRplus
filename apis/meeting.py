from flask_restx import Namespace, Resource, fields
from flask_cors import cross_origin

from daos.meeting_dao import MeetingDAO
from models.meeting import Meeting as MeetingModel
from auth.decorators import requires_auth

api = Namespace('meetings', description='Meetings related operations')

createMeeting = api.model('create meeting', {
    'name': fields.String(required=True),
    'employee_id': fields.String(required=True),
    "duration": fields.String(required=True),
    "date": fields.Date(required=True),
    "worked_hours": fields.String(required=True),
    "meeting_notes": fields.String(required=False),
    "is_interview": fields.Boolean(required=False)
})

updateMeeting = api.model('create meeting', {
    'name': fields.String(),
    'employee_id': fields.String(),
    "duration": fields.String(),
    "date": fields.Date(),
    "worked_hours": fields.String(),
    "meeting_notes": fields.String(),
    "is_interview": fields.Boolean()  
})

meeting = api.model('meeting', {
    'id': fields.String(required=True),
    'name': fields.String(required=True),
    'employee_id': fields.String(required=True),
    "duration": fields.String(required=True),
    "date": fields.Date(required=True),
    "worked_hours": fields.String(required=True),
    "meeting_notes": fields.String(required=False),
    "is_interview": fields.Boolean(required=False)    
})

meetingDAO = MeetingDAO()

@api.route('/')
@api.expect(MeetingModel)
class MeetingList(Resource):
    @api.doc('create_meeting')
    @api.expect(createMeeting)
    @api.marshal_with(meeting, code=201)
    @cross_origin(headers=["Content-Type", "Authorization"])
    @requires_auth
    def post(self):
        return meetingDAO.create(api.payload)

    @api.doc('get_meetings')
    @api.marshal_with(meeting, True)
    @cross_origin(headers=["Content-Type", "Authorization"])
    @requires_auth
    def get(self):
        return meetingDAO.getAll()

@api.route('/<string:id>')
class Meeting(Resource):
    @api.doc('update_meeting')
    @api.expect(updateMeeting)
    @api.marshal_with(meeting, code=200)
    @cross_origin(headers=["Content-Type", "Authorization"])
    @requires_auth
    def put(self, id):
        return meetingDAO.update(id, api.payload)

    @api.doc('delete_meeting')
    @cross_origin(headers=["Content-Type", "Authorization"])
    @requires_auth
    def delete(self, id):
        return meetingDAO.delete(id)