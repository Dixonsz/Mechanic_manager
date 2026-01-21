from flask import Blueprint, jsonify

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'ok', 'message': 'Style Manager API is running'}), 200

def register_routes(app):
    app.register_blueprint(api)
    
    from app.controllers.user_controller import user_controller
    app.register_blueprint(user_controller)
    
    from app.controllers.media_controller import media_controller
    app.register_blueprint(media_controller)
