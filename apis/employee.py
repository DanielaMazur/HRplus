from flask_restx import Namespace, Resource, fields
from daos.employee_dao import EmployeeDAO

from models.employee import Employee as EmployeeModel

api = Namespace('employees', description='Employees related operations')

employee = api.model('create employee', {
    'first_name': fields.String(required=True),
    'last_name': fields.String(required=True),
    'wage': fields.Float(required=True),
    'company_id': fields.String(required=True),
    'email': fields.String(required=True),
    'work_hours': fields.String(required=True),
    'managed_by_id': fields.String(required=True),
    'role_id': fields.String(required=True),
    'replacement_for_id': fields.String(),
    'start_date': fields.Date(required=True)
})

@api.route('/')
@api.expect(EmployeeModel)
class Employee(Resource):
    @api.doc('create_employee')
    @api.expect(employee)
    @api.marshal_with(employee, code=201)
    def post(self):
        print(api.payload)
        return EmployeeDAO().create(api.payload)
