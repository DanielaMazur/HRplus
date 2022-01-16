from flask_restx import Namespace, Resource, fields
from flask_cors import cross_origin
from models.employee import Employee

from daos.company_dao import CompanyDAO
from auth.decorators import requires_auth
from daos.employee_dao import EmployeeDAO

api = Namespace('companies', description='Company related operations')

createCompany = api.model('create company', {
    'name': fields.String(required=True),
    "email": fields.String(required=True)
})

company = api.model("company", {
    "id": fields.String(required=True),
    'name': fields.String(required=True),
})

companyDAO = CompanyDAO()
employeeDAO = EmployeeDAO()

@api.route('/')
class CompanyList(Resource):
    @api.doc('create_company')
    @api.expect(createCompany)
    @api.marshal_with(company, code=201)
    def post(self):
        company = companyDAO.create(api.payload)
        employee = {"email": api.payload["email"], "role": "admin", "company_id": company.id }
        employeeDAO.create(employee)
        return company
        
    @api.doc('get_companies')
    # @cross_origin(headers=["Content-Type", "Authorization"])
    @requires_auth
    @api.marshal_with(company, True, code=200)
    def get(self):
        return companyDAO.getAll()


@api.route('/<string:id>')
class Company(Resource):
    @api.doc('update_company')
    @api.expect(createCompany)
    @cross_origin(headers=["Content-Type", "Authorization"])
    @requires_auth
    @api.marshal_with(company, code=200)
    def put(self, id):
        return companyDAO.update(id, api.payload)

    @api.doc('delete_company')
    @cross_origin(headers=["Content-Type", "Authorization"])
    @requires_auth
    def delete(self, id):
        return companyDAO.delete(id)