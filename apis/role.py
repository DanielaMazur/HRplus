from flask_restx import Namespace, Resource, fields
from daos.role_dao import RoleDAO

from models.role import Role as RoleModel

api = Namespace('roles', description='Roles related operations')

createRole = api.model('create role', {
    'name': fields.String(required=True),
    'company_id': fields.String(required=True)
})

role = api.model('role', {
    'id': fields.String(required=True),
    'name': fields.String(required=True),
    'company_id': fields.String(required=True)
})

roleDAO = RoleDAO()

@api.route('/')
@api.expect(RoleModel)
class Employee(Resource):
    @api.doc('create_role')
    @api.expect(createRole)
    @api.marshal_with(role, code=201)
    def post(self):
        return roleDAO.create(api.payload)
    @api.doc('get_roles')
    @api.marshal_with(role, True)
    def get(self):
        return roleDAO.getAll()
