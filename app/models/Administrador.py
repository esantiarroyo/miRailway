from app import db
from flask_login import UserMixin

class Administrador(db.Model, UserMixin):
    __tablename__ = 'administradores'
    idAdm = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombreAdm = db.Column(db.String(45), nullable=False)
    tipoDocAdm = db.Column(db.String(45), nullable=False)
    noDocAdm = db.Column(db.String(45), nullable=False)
    celAdm = db.Column(db.String(45), nullable=False)
    emailAdm = db.Column(db.String(45), nullable=False)
    conAdm = db.Column(db.String(45), nullable=False)
   
    def get_id(self):
        return str(self.idAdm)