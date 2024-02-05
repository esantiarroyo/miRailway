from app import db


class Usuario(db.Model):
    __tablename__ = 'usuarios'
    idUsu = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pcs = db.relationship('Pc', back_populates='usuarios')
    nombreUsu = db.Column(db.String(45), nullable=False)
    tipoDocUsu = db.Column(db.String(45), nullable=False)
    noDocUsu = db.Column(db.String(45), nullable=False)
    celUsu = db.Column(db.String(45), nullable=False)
    emailUsu = db.Column(db.String(45), nullable=False)
   
