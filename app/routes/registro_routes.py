from flask import Blueprint, render_template, request, redirect, url_for
from app.models.Registro import Registro
from flask_login import login_user, logout_user, login_required, current_user
from app.models.Pc import Pc
from app.models.Celador import Celador
from app import db
from flask_login import current_user

bp = Blueprint('registro', __name__)

@bp.route('/Registro')
@login_required
def index():
    data = Registro.query.all()
    return render_template('registro/index.html', data=data)

@bp.route('/Registro/add', methods=['GET', 'POST'])
@login_required
def add():
    if request.method == 'POST':
        pc = request.form['idPc']
        entrada = request.form['entrada']
        salida = request.form['salida']
        cel = request.form['idCel']
        
        new_registro = Registro(idPc=pc, entrada=entrada, salida=salida, idCel=cel)
        db.session.add(new_registro)
        db.session.commit()
        
        return redirect(url_for('registro.index'))
    data = Pc.query.all()
    data1 = Celador.query.all()
    return render_template('registro/add.html', data=data, data1=data1)

@bp.route('/Registro/add/<int:idPc>', methods=['GET'])
@login_required
def add1(idPc):   
    from datetime import datetime
    new_registro = Registro(idPc=idPc, idCel=current_user.get_id(), entrada = datetime.now())
    db.session.add(new_registro)
    db.session.commit()
        
    return redirect(url_for('celador.entrada'))
    
@bp.route('/Registro/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    registro = Registro.query.get_or_404(id)

    if request.method == 'POST':
        registro.idPc = request.form['idPc']
        registro.entrada = request.form['entrada']
        registro.salida = request.form['salida']
        registro.idCel = request.form['idCel']
        
        db.session.commit()
        
        return redirect(url_for('registro.index'))

    return render_template('registro/edit.html', registro=registro)

@bp.route('/Registro/edit1/<int:id>', methods=['GET'])
@login_required

def edit1(id):
    from datetime import datetime

    registro = Registro.query.filter_by(idPc=id).order_by(Registro.idReg.desc()).first() 
    registro.salida = datetime.now()
        
    db.session.commit()
    
    return redirect(url_for('celador.salida'))


@bp.route('/registro/delete/<int:id>')
@login_required
def delete(id):
    registro = Registro.query.get_or_404(id)
    
    db.session.delete(registro)
    db.session.commit()

    return redirect(url_for('registro.index'))
