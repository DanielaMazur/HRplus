from models.company import Company
from models import db

class CompanyDAO(object):
    def get(self, id):
        return Company.query.get(id)

    def getAll(self):
        return Company.query.all()

    def create(self, company):
        newCompany = Company(
            name = company['name']
        )
        db.session.add(newCompany)
        db.session.commit()
        return newCompany

    # def update(self, id, data):
    #     todo = self.get(id)
    #     todo.update(data)
    #     return todo

    def delete(self, id):
        Company.query.filter_by(id = id).delete()
        db.session.commit()
