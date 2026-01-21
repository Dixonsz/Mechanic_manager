from datetime import datetime
from app.extensions import db

#Vehículo del cliente, con detalles como placa, año, color, etc.
class Vehicle(db.Model):
    __tablename__ = 'vehicles'
    
    id = db.Column(db.Integer, primary_key=True)
    plate = db.Column(db.String(20), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    color = db.Column(db.String(50), nullable=False)
    model_vehicle_id = db.Column(db.Integer, db.ForeignKey('model_vehicles.id'), nullable=False)
    category_vehicle_id = db.Column(db.Integer, db.ForeignKey('category_vehicles.id'), nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    fuel_type_id = db.Column(db.Integer, db.ForeignKey('fuel_types.id'), nullable=False)
    transmission_id = db.Column(db.Integer, db.ForeignKey('transmissions.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'plate': self.plate,
            'year': self.year,
            'color': self.color,
            'model_vehicle_id': self.model_vehicle_id,
            'category_vehicle_id': self.category_vehicle_id,
            'client_id': self.client_id,
            'fuel_type_id': self.fuel_type_id,
            'transmission_id': self.transmission_id,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }