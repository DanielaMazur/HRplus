from flask_restx import Namespace, Resource, fields
from flask_cors import cross_origin

from auth.decorators import requires_auth

api = Namespace('statistics', description='Statistics related operations')

getStatistics = api.model('get statistics', {
    'start_date': fields.String(required=True),
    'end_date': fields.String(required=True)
})

statistics = api.model("statistics", {
    "absenteeism_cost": fields.Float(required=True),
    "separation_cost": fields.Float(required=True),
    "replacement_cost": fields.Float(required=True),
    "training_cost": fields.Float(required=True)
})

# @api.route('/')
# class Statistics(Resource):
#     @api.doc('get_statistics_for_a_given_perioud')
#     @api.expect(getStatistics)
#     @api.marshal_with(statistics, code=201)
#     @cross_origin(headers=["Content-Type", "Authorization"])
#     @requires_auth
#     def get(self):
#         return
        
  