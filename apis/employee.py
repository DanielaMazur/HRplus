from flask_restx import Namespace, Resource
from flask import request

from models import db
from models.employee import Employee as EmployeeModel
from schemes.employee import add_employee

api = Namespace('employees', description='Employees related operations')

@api.route('/')
@api.expect(EmployeeModel)
class Employee(Resource):
    def post(self):
        new_employee = EmployeeModel(
                        first_name = request.json["first_name"],
                        last_name = request.json["last_name"],
                        wage = request.json["wage"],
                        company_id = request.json["company_id"],
                        email =request.json["email"],
                        work_hours = request.json["work_hours"],
                        managed_by_id = request.json["managed_by_id"],
                        role_id = request.json["role_id"],
                        replacement_for_id = request.json["replacement_for_id"],
                        start_date = request.json["start_date"],
                        end_date = request.json["end_date"])
        db.session.add(new_employee)
        db.commit()
        return add_employee.dump(new_employee)

# @api.route('/')
# class CatList(Resource):
#     @api.doc('list_cats')
#     @api.marshal_list_with(Employee)
#     def get(self):
#         '''List all employees'''
#         return EMPLOYEES

# @api.route('/<id>')
# @api.param('id', 'The employee identifier')
# @api.response(404, 'Employee not found')
# class Cat(Resource):
#     @api.doc('get_cat')
#     @api.marshal_with(Employee)
#     def get(self, id):
#         '''Fetch an employee given its identifier'''
#         for employee in EMPLOYEES:
#             if employee['id'] == id:
#                 return employee
#         api.abort(404)