from app.models.user import User
from app.extensions import db

class UserRepository:
    
    @staticmethod
    def create(User):
        db.session.add(User)
        db.session.commit()
        return User
    
    @staticmethod
    def get_by_id(user_id):
        return User.query.get(user_id)
    
    @staticmethod
    def get_user_by_username_or_email(username, email):
        return User.query.filter_by(username=username, email=email).first()
    
    @staticmethod
    def get_all():
        return User.query.all()
    
    @staticmethod
    def update(user):
        db.session.commit()
        return user
    
    @staticmethod
    def delete(user):
        db.session.delete(user)
        db.session.commit()

