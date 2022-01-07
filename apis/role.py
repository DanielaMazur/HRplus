from flask_restx import Namespace, Resource, fields
from flask_cors import cross_origin

from daos.role_dao import RoleDAO
from models.role import Role as RoleModel
from auth.decorators import requires_auth

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
class RoleList(Resource):
    @api.doc('create_role')
    @api.expect(createRole)
    @api.marshal_with(role, code=201)
    # @cross_origin(headers=["Content-Type", "Authorization"])
    # @requires_auth
    def post(self):
        return roleDAO.create(api.payload)

    @api.doc('get_roles')
    @api.marshal_with(role, True)
    # @cross_origin(headers=["Content-Type", "Authorization"])
    # @requires_auth
    def get(self):
        return roleDAO.getAll()

@api.route('/<string:id>')
class Role(Resource):
    @api.doc('delete_role')
    # @cross_origin(headers=["Content-Type", "Authorization"])
    # @requires_auth
    def delete(self, id):
        return roleDAO.delete(id)