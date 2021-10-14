from flask_restx import Namespace, Resource, fields

api = Namespace('employees', description='Employees related operations')

Employee = api.model('Employee', {
    'id': fields.String(required=True, description='The employee identifier'),
    'name': fields.String(required=True, description='The employee name'),
})

EMPLOYEES = [
    {'id': 'felix', 'name': 'Felix'},
]

@api.route('/')
class CatList(Resource):
    @api.doc('list_cats')
    @api.marshal_list_with(Employee)
    def get(self):
        '''List all employees'''
        return EMPLOYEES

@api.route('/<id>')
@api.param('id', 'The employee identifier')
@api.response(404, 'Employee not found')
class Cat(Resource):
    @api.doc('get_cat')
    @api.marshal_with(Employee)
    def get(self, id):
        '''Fetch an employee given its identifier'''
        for employee in EMPLOYEES:
            if employee['id'] == id:
                return employee
        api.abort(404)