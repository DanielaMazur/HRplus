from flask_restx import Api
from .employee import api as employeeNamespace

api = Api(
    version='1.0',
    title='HRplus',
    description='HRplus API'
)

api.add_namespace(employeeNamespace)
