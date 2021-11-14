from flask_restx import Api
from .employee import api as employeeNamespace
from .company import api as companyNamespace
from .role import api as roleNamespace
from .calendar import api as calendarNamespace
from .meeting import api as meetingNamespace
from .replacement_cost import api as replacementCostNamespace

api = Api(
    version='1.0',
    title='HRplus',
    description='HRplus API'
)

api.add_namespace(employeeNamespace)
api.add_namespace(companyNamespace)
api.add_namespace(roleNamespace)
api.add_namespace(calendarNamespace)
api.add_namespace(meetingNamespace)
api.add_namespace(replacementCostNamespace)