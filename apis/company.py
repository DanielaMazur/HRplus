from flask_restx import Namespace, Resource, fields
from daos.company_dao import CompanyDAO

api = Namespace('companies', description='Company related operations')

createCompany = api.model('create company', {
    'name': fields.String(required=True),
})

company = api.model("company", {
    "id": fields.String(required=True),
    'name': fields.String(required=True),
})

companyDAO = CompanyDAO()

@api.route('/')
class CompanyList(Resource):
    @api.doc('create_company')
    @api.expect(createCompany)
    @api.marshal_with(company, code=201)
    def post(self):
        return companyDAO.create(api.payload)
        
    @api.doc('get_companies')
    @api.marshal_with(company, True, code=200)
    def get(self):
        return companyDAO.getAll()


@api.route('/<string:id>')
class Company(Resource):
    @api.doc('update_company')
    @api.expect(createCompany)
    @api.marshal_with(company, code=200)
    def put(self, id):
        return companyDAO.update(id, api.payload)

    @api.doc('delete_company')
    def delete(self, id):
        return companyDAO.delete(id)