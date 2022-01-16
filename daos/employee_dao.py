from models.employee import Employee
from models import db
from datetime import datetime
from sqlalchemy.exc import IntegrityError
from AppError import AppError
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from flask import _request_ctx_stack

class EmployeeDAO(object):
    def get(self, id):
        return Employee.query.get(id)
    
    def getByEmail(self, email):
        return Employee.query.filter(Employee.email==email).first()

    def getAll(self):
        return Employee.query.all()

    def getCurrentEmployee(self):
        user_profile_id = _request_ctx_stack.top.current_user['sub']
        return self.getByProfileId(user_profile_id)
    
    def getByProfileId(self, profile_id):
        return Employee.query.filter(Employee.profile_id == profile_id).first()
    
    def getCompanyEmployees(self):
        employee = self.getCurrentEmployee()
        company_id = employee.company_id
        return Employee.query.filter(Employee.company_id == company_id).all()
        
    def create(self, employee):
        currentEmployee = self.getCurrentEmployee()
        try:
            newEmployee = Employee(
                first_name = employee['first_name'] if "first_name" in employee else "",
                last_name = employee['last_name'] if "last_name" in employee else "",
                wage = float(employee['wage']) if "wage" in employee else 0,
                email = employee['email'],
                work_hours = float(employee['work_hours']) if "work_hours" in employee else 0,            
                managed_by_id = employee['managed_by_id'] if "managed_by_id" in employee else None,
                role = employee['role'],
                replacement_for_id = employee['replacement_for_id'] if "replacement_for_id" in employee else None,
                start_date = datetime.strptime(employee['start_date'], '%Y-%m-%d') if "start_date" in employee else datetime.now(),
                company_id = currentEmployee.company_id
            )
            db.session.add(newEmployee)
            db.session.commit()
            sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
            message = Mail(
                from_email=os.environ.get('SENDGRID_SENDER_EMAIL'),
                to_emails=newEmployee.email)
            message.template_id = os.environ.get('SENDGRID_TEMPLATE_ID')
            sg.send(message)
            return newEmployee
        except IntegrityError:
            raise AppError({"code":"invalid_data", "description":"Email should be unique"}, 400)
        except:
            raise AppError({"code":"invalid_data", "description":"Please check the introduced data and try again"}, 400)

    
    def getAllByCompany(self, company_id):
        return Employee.query.filter(Employee.role.company_id == company_id)
        
    def update(self, id, data):
        db.session.query(Employee).filter(Employee.id == id).update(data)
        db.session.commit()
        return self.get(id)

    def delete(self, id):
        Employee.query.filter_by(id = id).delete()
        db.session.commit()
