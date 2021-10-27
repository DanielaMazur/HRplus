from models.employee import Employee
from models import db

class EmployeeDAO(object):
    def get(self, id):
        return Employee.query.get(id)
        
    def create(self, employee):
        print(employee['first_name'])
        newEmployee = Employee(
            first_name = employee['first_name']
        )
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
