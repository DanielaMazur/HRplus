from flask_restx import Namespace, Resource
from flask_wtf.csrf import generate_csrf

api = Namespace('csrf_token', description='Get csrf token')
 
@api.route('/')
class CSRFToken(Resource):
    @api.doc('get_csrf_token')
    def get(self):
        return generate_csrf()
        
