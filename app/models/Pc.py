from app import db 

class Pc(db.Model):
    __tablename__ = 'pcs'
    idPc = db.Column(db.Integer, primary_key=True, autoincrement=True)
    marcaPc = db.Column(db.String(45), nullable=False)
    colorPc = db.Column(db.String(45), nullable=False)
    serialPc = db.Column(db.String(45), nullable=False)
    idUsu = db.Column(db.Integer, db.ForeignKey('usuarios.idUsu'))
    usuarios = db.relationship('Usuario')
    
    registros = db.relationship('Registro', back_populates='pc')
    