from flask import Blueprint, render_template, request, redirect, url_for
from app.models.Pc import Pc
from flask_login import login_user, logout_user, login_required, current_user
from app.models.Usuario import Usuario
from app import db

bp = Blueprint('pc', __name__)

@bp.route('/Pc')
@login_required
def index():
    data = Pc.query.all()
    return render_template('pc/index.html', data=data)

@bp.route('/Pc/add', methods=['GET', 'POST'])
@login_required
def add():
    if request.method == 'POST':
        marca = request.form['marcaPc']
        color = request.form['colorPc']
        serial = request.form['serialPc']
        usuario = request.form['idUsu']
        
        new_pc = Pc(marcaPc=marca, colorPc=color, serialPc=serial, idUsu=usuario)
        db.session.add(new_pc)
        db.session.commit()
        
        return redirect(url_for('pc.index'))
    data = Usuario.query.all()
    return render_template('pc/add.html', data=data)


@bp.route('/Pc/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    pc = Pc.query.get_or_404(id)

    if request.method == 'POST':
        pc.marcaPc = request.form['marcaPc']
        pc.colorPc = request.form['colorPc']
        pc.serialPc = request.form['serialPc']
        pc.idUsu = request.form['idUsu']
        
        db.session.commit()
        
        return redirect(url_for('pc.index'))
    data = Usuario.query.all()
    return render_template('pc/edit.html', pc=pc, data=data)

@bp.route('/Pc/delete/<int:id>')
@login_required
def delete(id):
    pc = Pc.query.get_or_404(id)
    
    db.session.delete(pc)
    db.session.commit()

    return redirect(url_for('pc.index'))
