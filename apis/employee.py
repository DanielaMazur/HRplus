from flask_restx import Namespace, Resource, fields
from daos.employee_dao import EmployeeDAO

from models.employee import Employee as EmployeeModel

api = Namespace('employees', description='Employees related operations')

createEmployee = api.model('create employee', {
    'first_name': fields.String(required=True),
    'last_name': fields.String(required=True),
    'wage': fields.Float(required=True),
    'company_id': fields.String(required=True),
    'email': fields.String(required=True),
    'work_hours': fields.String(required=True),
    'managed_by_id': fields.String(required=True),
    'role_id': fields.String(required=True),
    'replacement_for_id': fields.String(required=False),
    'start_date': fields.Date(required=True)
})

employee = api.model('employee', {
    'id': fields.String(required=True),
    'first_name': fields.String(required=True),
    'last_name': fields.String(required=True),
    'wage': fields.Float(required=True),
    'company_id': fields.String(required=True),
    'email': fields.String(required=True),
    'work_hours': fields.String(required=True),
    'managed_by_id': fields.String(required=True),
    'role_id': fields.String(required=True),
    'replacement_for_id': fields.String(required=False),
    'start_date': fields.Date(required=True)
})

employeeDAO = EmployeeDAO()

@api.route('/')
@api.expect(EmployeeModel)
class Employee(Resource):
    @api.doc('create_employee')
    @api.expect(createEmployee)
    @api.marshal_with(employee, code=201)
    def post(self):
        return employeeDAO.create(api.payload)
    # @api.doc('get_employee')
    # @api.route('/<string:id>')
    # @api.response(404, 'Employee not found')
    # @api.param('id', 'The employee identifier')
    # def get(self, id):
    #     return employeeDAO.get(id)
    @api.doc('get_employees')
    @api.marshal_with(employee, True)
    def get(self):
        return employeeDAO.getAll()
