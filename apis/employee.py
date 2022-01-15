from flask_restx import Namespace, Resource, fields
from flask_cors import cross_origin
from flask import jsonify
 
from daos.employee_dao import EmployeeDAO
from models.employee import Employee as EmployeeModel
from auth.decorators import requires_auth

api = Namespace('employees', description='Employees related operations')

createEmployee = api.model('create employee', {
    'first_name': fields.String(required=True),
    'last_name': fields.String(required=True),
    'wage': fields.Float(required=True),
    'email': fields.String(required=True),
    'work_hours': fields.String(required=True),
    'managed_by_id': fields.String(required=False),
    'role': fields.String(required=True),
    'replacement_for_id': fields.String(required=False),
    'start_date': fields.Date(required=True), 
    'profile_id':fields.String()
})

editEmployee =  api.model('create employee', {
    'first_name': fields.String(),
    'last_name': fields.String(),
    'wage': fields.Float(),
    'email': fields.String(),
    'work_hours': fields.String(),
    'managed_by_id': fields.String(),
    'role': fields.String(),
    'replacement_for_id': fields.String(),
    'start_date': fields.Date(),
    'profile_id':fields.String()
})

employee = api.model('employee', {
    'id': fields.String(required=True),
    'first_name': fields.String(required=True),
    'last_name': fields.String(required=True),
    'wage': fields.Float(required=True),
    'email': fields.String(required=True),
    'work_hours': fields.String(required=True),
    'managed_by_id': fields.String(required=True),
    'role': fields.String(required=True),
    'replacement_for_id': fields.String(required=False),
    'start_date': fields.Date(required=True),
    'profile_id':fields.String()
})

employeeDAO = EmployeeDAO()

@api.route('/')
@api.expect(EmployeeModel)
class EmployeeList(Resource):
    @api.doc('create_employee')
    @api.expect(createEmployee)
    @cross_origin(headers=["Content-Type", "Authorization"])
    @requires_auth
    @api.marshal_with(employee, code=201)
    def post(self):
        return employeeDAO.create(api.payload)

    @api.doc('get_employees')
    @cross_origin(headers=["Content-Type", "Authorization"])
    @requires_auth
    @api.marshal_with(employee, True)
    def get(self):
        return employeeDAO.getAll()
    
@api.route('/<string:id>')
class Employee(Resource):
    @api.doc('get_employee')
    @api.response(404, 'Employee not found')
    @cross_origin(headers=["Content-Type", "Authorization"])
    @requires_auth
    @api.marshal_with(employee)
    def get(self, id):
        return employeeDAO.get(id)

    @api.doc('update_employee')
    @api.response(404, 'Employee not found')
    @api.expect(editEmployee)
    @cross_origin(headers=["Content-Type", "Authorization"])
    @requires_auth
    @api.marshal_with(employee)
    def put(self, id):
        return employeeDAO.update(id, api.payload)

    @api.doc('delete_employee')
    @cross_origin(headers=["Content-Type", "Authorization"])
    @requires_auth
    def delete(self, id):
        return employeeDAO.delete(id)

@api.route('/by-email/<string:email>')
class Employee(Resource):
    @api.doc('get_employee')
    @api.response(404, 'Employee not found')
    @cross_origin(headers=["Content-Type", "Authorization"])
    @requires_auth
    @api.marshal_with(employee)
    def get(self, email):
        return employeeDAO.getByEmail(email)