from flask import Blueprint, jsonify, request
from app.service.cloudinary_service import CloudinaryService

media_controller = Blueprint('media_controller', __name__, url_prefix='/api/media')

@media_controller.route('/upload/image', methods=['POST'])
def upload_image():
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No se proporcionó ningún archivo'}), 400
        
        file = request.files['file']
        
        if file.filename == '':
            return jsonify({'error': 'Archivo sin nombre'}), 400
        
        folder = request.form.get('folder', 'images')
        
        result = CloudinaryService.upload_image(file, folder)
        
        return jsonify({
            'message': 'Imagen subida correctamente',
            'data': result
        }), 201
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@media_controller.route('/upload/image/camera', methods=['POST'])
def upload_image_camera():
    try:
        data = request.get_json(force=True)
        
        if not data or 'image' not in data:
            return jsonify({'error': 'No se proporcionó ninguna imagen en base64'}), 400
        
        base64_image = data['image']
        folder = data.get('folder', 'images')
        
        result = CloudinaryService.upload_image_base64(base64_image, folder)
        
        return jsonify({
            'message': 'Imagen de cámara subida correctamente',
            'data': result
        }), 201
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@media_controller.route('/upload/video', methods=['POST'])
def upload_video():
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No se proporcionó ningún archivo'}), 400
        
        file = request.files['file']
        
        if file.filename == '':
            return jsonify({'error': 'Archivo sin nombre'}), 400
        
        folder = request.form.get('folder', 'videos')
        
        result = CloudinaryService.upload_video(file, folder)
        
        return jsonify({
            'message': 'Video subido correctamente',
            'data': result
        }), 201
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@media_controller.route('/delete/<resource_type>/<path:public_id>', methods=['DELETE'])
def delete_file(resource_type, public_id):
    
    try:
        if resource_type not in ['image', 'video']:
            return jsonify({'error': 'Tipo de recurso inválido. Usa "image" o "video"'}), 400
        
        result = CloudinaryService.delete_file(public_id, resource_type)
        
        return jsonify({
            'message': 'Archivo eliminado correctamente',
            'data': result
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500


