from datetime import datetime
from app.extensions import db

#Recepción de un vehículo en el taller para su mantenimiento o reparación.
#Primera etapa del proceso de servicio del vehículo.
class Reception(db.Model):
    __tablename__ = 'receptions'

    id = db.Column(db.Integer, primary_key=True)
    start_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    mileage = db.Column(db.String(50), nullable=False)
    fuel_level = db.Column(db.String(20), nullable=False)
    observations_client = db.Column(db.Text, nullable=True)
    observations_mechanic = db.Column(db.Text, nullable=True)
    id_vehicle = db.Column(db.Integer, db.ForeignKey('vehicles.id'), nullable=False)
    id_user = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    id_state = db.Column(db.Integer, db.ForeignKey('states.id'), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)


   

    def to_dict(self):
        return {
            'id': self.id,
            'start_date': self.start_date,
            'mileage': self.mileage,
            'fuel_level': self.fuel_level,
            'observations_client': self.observations_client,
            'observations_mechanic': self.observations_mechanic,
            'id_vehicle': self.id_vehicle,  
            'id_user': self.id_user,
            'id_state': self.id_state,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }