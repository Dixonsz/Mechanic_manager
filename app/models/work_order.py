from datetime import datetime
from app.extensions import db

#Una orden de trabajo asociada a una recepción
#Es el segundo paso, generar una orden de trabajo para los servicios a realizarr en el vehículo.
#Ejemplo: Reparación de frenos, cambio de aceite, etc.
class WorkOrder(db.Model):
    __tablename__ = 'work_orders'

    id = db.Column(db.Integer, primary_key=True)
    start_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    end_date = db.Column(db.DateTime, nullable=True)
    observations = db.Column(db.String(255), nullable=True)
    id_reception = db.Column(db.Integer, db.ForeignKey('receptions.id'), nullable=False)
    id_user = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    id_state = db.Column(db.Integer, db.ForeignKey('states.id'), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)


   
    def to_dict(self):
        return {
            'id': self.id,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'observations': self.observations,
            'id_reception': self.id_reception,
            'id_user': self.id_user,
            'id_state': self.id_state,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }