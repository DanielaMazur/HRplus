from models.role import Role
from models import db

class RoleDAO(object):
    def get(self, id):
        return Role.query.get(id)

    def getAll(self):
        return Role.query.all()

    def create(self, role):
        newRole = Role(
            name = role['name'], 
            company_id = role['company_id']
        )
        db.session.add(newRole)
        db.session.commit()
        return newRole

    def delete(self, id):
        Role.query.filter_by(id = id).delete()
        db.session.commit()
