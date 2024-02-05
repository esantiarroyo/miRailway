from app import db
from flask_login import UserMixin

class Celador(db.Model, UserMixin):
    __tablename__ = 'celadores'
    idCel = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombreCel = db.Column(db.String(45), nullable=False)
    noDocCel = db.Column(db.String(45), nullable=False)
    celCel = db.Column(db.String(45), nullable=False)
    emailCel = db.Column(db.String(45), nullable=False)
    conCel = db.Column(db.String(45), nullable=False)
    registros = db.relationship('Registro', back_populates='celador')
    
    def get_id(self):
        return str(self.idCel)
   
   