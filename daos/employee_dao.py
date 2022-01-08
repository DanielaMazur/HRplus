from models.employee import Employee
from models import db
from datetime import datetime

class EmployeeDAO(object):
    def get(self, id):
        return Employee.query.get(id)
    
    def getByEmail(self, email):
        return Employee.query.filter(Employee.email==email).first()

    def getAll(self):
        return Employee.query.all()
        
    def create(self, employee):
        newEmployee = Employee(
            first_name = employee['first_name'] if "first_name" in employee else "",
            last_name = employee['last_name'] if "last_name" in employee else "",
            wage = float(employee['wage']) if "wage" in employee else 0,
            email = employee['email'],
            work_hours = float(employee['work_hours']) if "work_hours" in employee else 0,            
            managed_by_id = employee['managed_by_id'] if "managed_by_id" in employee else None,
            role_id = employee['role_id'],
            replacement_for_id = employee['replacement_for_id'] if "replacement_for_id" in employee else None,
            start_date = datetime.strptime(employee['start_date'], '%Y-%m-%d') if "start_date" in employee else datetime.now()
        )
        db.session.add(newEmployee)
        db.session.commit()
        return newEmployee
    
    def getAllByCompany(self, company_id):
        return Employee.query.filter(Employee.role.company_id == company_id)
        
    def update(self, id, data):
        db.session.query(Employee).filter(Employee.id == id).update(data)
        db.session.commit()
        return self.get(id)

    def delete(self, id):
        Employee.query.filter_by(id = id).delete()
        db.session.commit()
