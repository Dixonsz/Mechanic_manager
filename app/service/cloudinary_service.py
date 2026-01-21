import cloudinary
import cloudinary.uploader
from typing import Dict, Any

class CloudinaryService:
    
    @staticmethod
    def configure(cloud_name: str, api_key: str, api_secret: str):
        cloudinary.config(
            cloud_name=cloud_name,
            api_key=api_key,
            api_secret=api_secret,
            secure=True
        )
    
    @staticmethod
    def upload_image(file, folder: str = "images") -> Dict[str, Any]:
        try:
            result = cloudinary.uploader.upload(
                file,
                folder=folder,
                resource_type="image"
            )
            return {
                'url': result['secure_url'],
                'public_id': result['public_id'],
                'format': result['format'],
                'width': result['width'],
                'height': result['height'],
                'size': result['bytes']
            }
        except Exception as e:
            raise Exception(f"Error al subir imagen a Cloudinary: {str(e)}")
            
    
    @staticmethod
    def upload_image_base64(base64_string: str, folder: str = "images") -> Dict[str, Any]:
       
        try:
            result = cloudinary.uploader.upload(
                base64_string,
                folder=folder,
                resource_type="image"
            )
            return {
                'url': result['secure_url'],
                'public_id': result['public_id'],
                'format': result['format'],
                'width': result['width'],
                'height': result['height'],
                'size': result['bytes']
            }
        except Exception as e:
            raise Exception(f"Error al subir imagen base64 a Cloudinary: {str(e)}")
    
    @staticmethod
    def upload_video(file, folder: str = "videos") -> Dict[str, Any]:
        try:
            result = cloudinary.uploader.upload(
                file,
                folder=folder,
                resource_type="video"
            )
            return {
                'url': result['secure_url'],
                'public_id': result['public_id'],
                'format': result['format'],
                'duration': result.get('duration'),
                'size': result['bytes']
            }
        except Exception as e:
            raise Exception(f"Error al subir video a Cloudinary: {str(e)}")
    
    @staticmethod
    def delete_file(public_id: str, resource_type: str = "image") -> Dict[str, Any]:
        try:
            result = cloudinary.uploader.destroy(
                public_id,
                resource_type=resource_type
            )
            return result
        except Exception as e:
            raise Exception(f"Error al eliminar archivo de Cloudinary: {str(e)}")
    
    