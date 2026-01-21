from app.models.user import User
from app.repositories.user_repository import UserRepository

class UserService:

    @staticmethod
    def create_user(data):
        if UserRepository.get_user_by_username_or_email(
            data.get('username'), data.get('email')
            ):
                raise ValueError("El usuario o correo ya existe.")
        user =  User( 
            username=data['username'],
            email=data['email'],
            password_hash=data.get('password_hash') or data.get('password'),
            is_active=data.get('is_active', True),
            rol_id=data.get('rol_id')
         )
        return UserRepository.create(user)
    
    @staticmethod
    def get_user_by_id(user_id):
        return UserRepository.get_by_id(user_id)
    
    @staticmethod
    def get_all_users():
        return UserRepository.get_all()
    
    @staticmethod
    def update_user(user_id, data): 
        user = UserRepository.get_by_id(user_id)
        if not user:
            raise ValueError("Usuario no encontrado.")
        
        user.username = data.get('username', user.username)
        user.password_hash = data.get('password_hash') or data.get('password') or user.password_hash
        user.email = data.get('email', user.email)
        user.is_active = data.get('is_active', user.is_active)
        
        return UserRepository.update(user)
    
    @staticmethod
    def delete_user(user_id):
        user = UserRepository.get_by_id(user_id)
        if not user:
            raise ValueError("Usuario no encontrado.")
        
        UserRepository.delete(user)