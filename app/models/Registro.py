from app import db 

class Registro(db.Model):
    __tablename__ = 'registros'
    idReg = db.Column(db.Integer, primary_key=True, autoincrement=True)
    idPc = db.Column(db.Integer, db.ForeignKey('pcs.idPc'))
    pc = db.relationship('Pc', back_populates='registros')
    entrada = db.Column(db.TIMESTAMP, nullable=True)
    salida = db.Column(db.TIMESTAMP, nullable=True)
    idCel = db.Column(db.Integer, db.ForeignKey('celadores.idCel'))
    celador = db.relationship('Celador', back_populates='registros')
    