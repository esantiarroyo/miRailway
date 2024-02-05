from flask import Blueprint, render_template, request, redirect, url_for
from app.models.Usuario import Usuario
from flask_login import login_user, logout_user, login_required, current_user
from app import db

bp = Blueprint('usuario', __name__)

@bp.route('/Usuario')
@login_required
def index():
    data = Usuario.query.all()
    return render_template('usuario/index.html', data=data)

@bp.route('/Usuario/add', methods=['GET', 'POST'])
@login_required
def add():
    if request.method == 'POST':
        nombre = request.form['nombreUsu']
        tipoDoc = request.form['tipoDocUsu']
        noDoc = request.form['noDocUsu']
        cel = request.form['celUsu']
        email = request.form['emailUsu']
        
        new_usuario = Usuario(nombreUsu=nombre, tipoDocUsu=tipoDoc, noDocUsu=noDoc, celUsu=cel, emailUsu=email)
        db.session.add(new_usuario)
        db.session.commit()
        
        return redirect(url_for('usuario.index'))

    return render_template('usuario/add.html')

@bp.route('/Usuario/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    usuario = Usuario.query.get_or_404(id)

    if request.method == 'POST':
        usuario.nombreUsu = request.form['nombreUsu']
        usuario.tipoDocUsu = request.form['tipoDocUsu']
        usuario.noDocUsu = request.form['noDocUsu']
        usuario.celUsu = request.form['celUsu']
        usuario.emailUsu = request.form['emailUsu']
        db.session.commit()
        return redirect(url_for('usuario.index'))

    return render_template('usuario/edit.html', usuario=usuario)
    

@bp.route('/Usuario/delete/<int:id>')
@login_required
def delete(id):
    usuario = Usuario.query.get_or_404(id)
    
    db.session.delete(usuario)
    db.session.commit()

    return redirect(url_for('usuario.index'))
