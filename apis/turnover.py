from flask_restx import Namespace, Resource, fields
from flask_cors import cross_origin

from daos.turnover_dao import TurnoverDAO
from models.turnover import Turnover as TurnoverModel
from auth.decorators import requires_auth

api = Namespace('turnovers', description='Turnovers related operations')

createTurnover = api.model('create turnover', {
    'company_id': fields.String(required=True),
    'meeting_id':fields.String(required=True),
    'employee_id': fields.String(required=True),
})

updateTurnover = api.model('create turnover', {
    'company_id': fields.String(),
    'meeting_id':fields.String(),
    'employee_id': fields.String(),
})

turnover = api.model('turnover', {
    'id': fields.String(required=True),
    'company_id': fields.String(required=True),
    'meeting_id':fields.String(required=True),
    'employee_id': fields.String(required=True),
 })

turnoverDAO = TurnoverDAO()

@api.route('/')
@api.expect(TurnoverModel)
class TurnoverList(Resource):
    @api.doc('create_turnover')
    @api.expect(createTurnover)
     #@cross_origin(headers=["Content-Type", "Authorization"])
    @requires_auth
    @api.marshal_with(turnover, code=201)
    def post(self):
        return turnoverDAO.create(api.payload)

    @api.doc('get_turnovers')
     #@cross_origin(headers=["Content-Type", "Authorization"])
    @requires_auth
    @api.marshal_with(turnover, True)
    def get(self):
        return turnoverDAO.getAll()

@api.route('/<string:id>')
class Turnover(Resource):
    @api.doc('update_turnover')
    @api.expect(updateTurnover)
     #@cross_origin(headers=["Content-Type", "Authorization"])
    @requires_auth
    @api.marshal_with(turnover, code=200)
    def put(self, id):
        return turnoverDAO.update(id, api.payload)

    @api.doc('delete_turnover')
     #@cross_origin(headers=["Content-Type", "Authorization"])
    @requires_auth
    def delete(self, id):
        return turnoverDAO.delete(id)