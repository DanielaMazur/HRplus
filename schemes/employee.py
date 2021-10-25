from schemes import ma
from flask_marshmallow import fields

from models.employee import Employee

class EmployeeSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Employee

    id = ma.auto_field()
    first_name = ma.auto_field()
    last_name = ma.auto_field()
    wage = ma.auto_field()
    company_id = ma.auto_field()
    email = ma.auto_field()
    password_hash = ma.auto_field()
    work_hours = ma.auto_field()
    managed_by_id = ma.auto_field()
    role_id = ma.auto_field()
    replacement_for_id =ma.auto_field()
    start_date = ma.auto_field()
    end_date = ma.auto_field()

add_employee = EmployeeSchema(exclude=("id", "password_hash"))
register_employee = EmployeeSchema(only=("email", "password_hash"))
