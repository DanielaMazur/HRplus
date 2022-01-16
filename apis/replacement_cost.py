from flask_restx import Namespace, Resource, fields
from flask_cors import cross_origin

from daos.replacement_cost_dao import ReplacementCostDAO
from models.replacement_cost import ReplacementCost as ReplacementCostModel
from auth.decorators import requires_auth

api = Namespace('replacement_costs', description='ReplacementCosts related operations')

createReplacementCost = api.model('create replacement_cost', {
    'name': fields.String(required=True),
    'advertising_fees_per_termination': fields.String(required=True),
    'job_availability_communication_time': fields.String(required=True),
    'preemployeement_admin_fun_time': fields.String(required=True),
    'interview_time': fields.String(required=True),
    'number_of_interviews': fields.String(required=True),
    'cost_of_materials_per_person': fields.String(required=True),
    'cost_of_scoring_per_person': fields.String(required=True),
    'number_of_test_given': fields.Integer(required=True),
    'acquiring_and_disseminating_time': fields.String(required=True),
    'company_id': fields.String(required=True),
    "start_date": fields.Date(required=True),
    "end_date": fields.Date(required=True),
})

updateReplacementCost = api.model('create replacement_cost', {
    'name': fields.String(),
    'advertising_fees_per_termination': fields.String(),
    'job_availability_communication_time': fields.String(),
    'preemployeement_admin_fun_time': fields.String(),
    'interview_time': fields.String(),
    'number_of_interviews': fields.String(),
    'cost_of_materials_per_person': fields.String(),
    'cost_of_scoring_per_person': fields.String(),
    'number_of_test_given': fields.Integer(),
    'acquiring_and_disseminating_time': fields.String(),
    'company_id': fields.String(),
    "start_date": fields.Date(),
    "end_date": fields.Date()
})

replacement_cost = api.model('replacement_cost', {
    'id': fields.String(required=True),
    'name': fields.String(required=True),
    'advertising_fees_per_termination': fields.String(required=True),
    'job_availability_communication_time': fields.String(required=True),
    'preemployeement_admin_fun_time': fields.String(required=True),
    'interview_time': fields.String(required=True),
    'number_of_interviews': fields.String(required=True),
    'cost_of_materials_per_person': fields.String(required=True),
    'cost_of_scoring_per_person': fields.String(required=True),
    'number_of_test_given': fields.Integer(required=True),
    'acquiring_and_disseminating_time': fields.String(required=True),
    'company_id': fields.String(required=True),
    "start_date": fields.Date(required=True),
    "end_date": fields.Date(required=True)
})

replacement_costDAO = ReplacementCostDAO()

@api.route('/')
@api.expect(ReplacementCostModel)
class ReplacementCostList(Resource):
    @api.doc('create_replacement_cost')
    @api.expect(createReplacementCost)
     #@cross_origin(headers=["Content-Type", "Authorization"])
    @requires_auth
    @api.marshal_with(replacement_cost, code=201)
    def post(self):
        return replacement_costDAO.create(api.payload)

    @api.doc('get_replacement_costs')
     #@cross_origin(headers=["Content-Type", "Authorization"])
    @requires_auth
    @api.marshal_with(replacement_cost, True)
    def get(self):
        return replacement_costDAO.getAll()

@api.route('/<string:id>')
class ReplacementCost(Resource):
    @api.doc('update_replacement_cost')
     #@cross_origin(headers=["Content-Type", "Authorization"])
    @requires_auth
    @api.expect(updateReplacementCost)
    def put(self, id):
        return replacement_costDAO.update(id, api.payload)

    @api.doc('delete_replacement_cost')
     #@cross_origin(headers=["Content-Type", "Authorization"])
    @requires_auth
    def delete(self, id):
        return replacement_costDAO.delete(id)