from datetime import datetime
from app.extensions import db

#Estado de un proceso o entidad, como 'pendiente', 'en progreso' o 'completado'.
#Se utiliza para rastrear el estado de órdenes de trabajo, recepciones u otros procesos dentro del sistema.
#Aplica para múltiples modelos que requieren un seguimiento de estado.
class State(db.Model):
    __tablename__ = 'states'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }