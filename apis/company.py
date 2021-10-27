from flask_restx import Namespace, Resource, fields
from daos.company_dao import CompanyDAO

from models.company import Company as CompanyModel

api = Namespace('companies', description='Company related operations')

company = api.model('create company', {
    'name': fields.String(required=True),
})

@api.route('/')
@api.expect(CompanyModel)
class Company(Resource):
    @api.doc('create_company')
    @api.expect(company)
    @api.marshal_with(company, code=201)
    def post(self):
        print(api.payload)
        return CompanyDAO().create(api.payload)
