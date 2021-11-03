from flask_restx import Api
from .employee import api as employeeNamespace
from .company import api as companyNamespace
from .role import api as roleNamespace

api = Api(
    version='1.0',
    title='HRplus',
    description='HRplus API'
)

api.add_namespace(employeeNamespace)
api.add_namespace(companyNamespace)
api.add_namespace(roleNamespace)