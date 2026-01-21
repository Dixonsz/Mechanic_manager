from datetime import datetime
from app.extensions import db

#Modelo de vehículo, asociado a una marca y categoría de vehículo.
#Toyota Corolla, Honda Civic, Ford Focus, etc.
class ModelVehicle(db.Model):
    __tablename__ = 'model_vehicles'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.String(255), nullable=True)
    brand_id = db.Column(db.Integer, db.ForeignKey('brands.id'), nullable=False)
    category_vehicle_id = db.Column(db.Integer, db.ForeignKey('category_vehicles.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'brand_id': self.brand_id,
            'category_vehicle_id': self.category_vehicle_id,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }