from datetime import datetime
from app.extensions import db

#Orden de servicio que relaciona una orden de trabajo con un servicio específico.
#Contiene detalles como el precio aplicado y observaciones.
#Ejemplo: Una orden de trabajo puede incluir múltiples órdenes de servicio para diferentes servicios realizados en el vehículo.
#Cada orden de servicio está asociada a un estado para rastrear su progreso.
#Aplica para gestionar y documentar los servicios realizados en el vehículo durante su mantenimiento o reparación.
#Es la parte ejecutada por el mecánico dentro del proceso de servicio del vehículo.

class ServiceOrder(db.Model):
    __tablename__ = 'service_orders'
    
    id = db.Column(db.Integer, primary_key=True)
    id_work_order = db.Column(db.Integer, db.ForeignKey('work_orders.id'), nullable=False)
    id_service = db.Column(db.Integer, db.ForeignKey('services.id'), nullable=False)
    price_aplied = db.Column(db.Float, nullable=False)
    observations = db.Column(db.String(255), nullable=True)
    id_state = db.Column(db.Integer, db.ForeignKey('states.id'), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    
    def to_dict(self):
        return {
            'id': self.id,
            'id_work_order': self.id_work_order,
            'id_service': self.id_service,
            'price_aplied': self.price_aplied,
            'observations': self.observations,
            'id_state': self.id_state,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }