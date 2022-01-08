from flask_restx import Api
from .employee import api as employeeNamespace
from .company import api as companyNamespace
from .calendar import api as calendarNamespace
from .meeting import api as meetingNamespace
from .replacement_cost import api as replacementCostNamespace
from .training import api as trainingNamespace
from .turnover import api as turnoverNamespace

authorizations = {
    'Bearer Auth': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    },
}

api = Api(
    version='1.0',
    title='HRplus',
    description='HRplus API',
    security='Bearer Auth', 
    authorizations=authorizations,
)

api.add_namespace(employeeNamespace)
api.add_namespace(companyNamespace)
api.add_namespace(calendarNamespace)
api.add_namespace(meetingNamespace)
api.add_namespace(replacementCostNamespace)
api.add_namespace(trainingNamespace)
api.add_namespace(turnoverNamespace)