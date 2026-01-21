from datetime import datetime
from app.extensions import db

#Foto asociada a una recepción del vehículo, utilizada para documentar el estado del vehículo al momento de la recepción.
class ReceptionPhoto(db.Model):
    __tablename__ = 'reception_photos'

    id = db.Column(db.Integer, primary_key=True)
    photo_url = db.Column(db.String(255), nullable=False)
    id_reception = db.Column(db.Integer, db.ForeignKey('receptions.id'), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    reception = db.relationship('Reception', backref=db.backref('photos', lazy=True))

    def to_dict(self):
        return {
            'id': self.id,
            'photo_url': self.photo_url,
            'id_reception': self.id_reception,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
