from flask_restx import Namespace, Resource, fields
from daos.training_dao import TrainingDAO

from models.training import Training as TrainingModel

api = Namespace('trainings', description='Trainings related operations')

createTraining = api.model('create training', {
    'informational_package_cost': fields.String(required=True),
    'training_program_length':fields.String(required=True),
    'avg_trainers_pay_rate': fields.String(required=True),
    'instruction_hours': fields.String(required=True),
    'experienced_employees_assigned': fields.String(required=True),
    'company_id':fields.String(required=True),
    "date": fields.Date(required=True),
})

  

updateTraining = api.model('create training', {
    'informational_package_cost': fields.String(),
    'training_program_length':fields.String(),
    'avg_trainers_pay_rate': fields.String(),
    'instruction_hours': fields.String(),
    'experienced_employees_assigned': fields.String(),
    'company_id':fields.String(),
    "date": fields.Date(),
})

training = api.model('training', {
    'id': fields.String(required=True),
    'informational_package_cost': fields.String(required=True),
    'training_program_length':fields.String(required=True),
    'avg_trainers_pay_rate': fields.String(required=True),
    'instruction_hours': fields.String(required=True),
    'experienced_employees_assigned': fields.String(required=True),
    'company_id':fields.String(required=True),
    "date": fields.Date(required=True),
 })

trainingDAO = TrainingDAO()

@api.route('/')
@api.expect(TrainingModel)
class TrainingList(Resource):
    @api.doc('create_training')
    @api.expect(createTraining)
    @api.marshal_with(training, code=201)
    def post(self):
        return trainingDAO.create(api.payload)

    @api.doc('get_trainings')
    @api.marshal_with(training, True)
    def get(self):
        return trainingDAO.getAll()

@api.route('/<string:id>')
class Training(Resource):
    @api.doc('update_training')
    @api.expect(updateTraining)
    @api.marshal_with(training, code=200)
    def put(self, id):
        return trainingDAO.update(id, api.payload)

    @api.doc('delete_training')
    def delete(self, id):
        return trainingDAO.delete(id)