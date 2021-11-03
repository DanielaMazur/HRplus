from models.employee import Employee
from models import db
from datetime import datetime

class EmployeeDAO(object):
    def get(self, id):
        return Employee.query.get(id)

    def getAll(self):
        return Employee.query.all()
        
    def create(self, employee):
        newEmployee = Employee(
            first_name = employee['first_name'],
            last_name = employee['last_name'],
            wage = float(employee['wage']),
            company_id = employee['company_id'],
            email = employee['email'],
            work_hours = float(employee['work_hours']),            
            managed_by_id = employee['managed_by_id'],
            role_id = employee['role_id'],
            replacement_for_id = employee['replacement_for_id'],
            start_date = datetime.strptime(employee['start_date'], '%Y-%m-%d')
        )
        newEmployee.set_password("test_password")
        db.session.add(newEmployee)
        db.session.commit()
        return newEmployee

    # def update(self, id, data):
    #     todo = self.get(id)
    #     todo.update(data)
    #     return todo

    def delete(self, id):
        Employee.query.filter_by(id = id).delete()
        db.session.commit()
