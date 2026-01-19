from flask import Blueprint, jsonify

# Crear blueprint
api = Blueprint('api', __name__, url_prefix='/api')

# Ruta básica
@api.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'ok', 'message': 'Style Manager API is running'}), 200

def register_routes(app):
    """Registrar todos los blueprints en la aplicación"""
    app.register_blueprint(api)
    
    # Registrar controlador de usuarios
    from app.controllers.user_controller import user_controller
    app.register_blueprint(user_controller)
