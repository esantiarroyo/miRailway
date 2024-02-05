from flask import Blueprint, render_template, request, redirect, url_for
from app.models.Administrador import Administrador
from flask_login import login_user, logout_user, login_required, current_user
from app import db

bp = Blueprint('administrador', __name__)

@bp.route('/Administrador')
@login_required
def index():
    data = Administrador.query.all()
    return render_template('administrador/index.html', data=data)

@bp.route('/Administrador/add', methods=['GET', 'POST'])
@login_required
def add():
    if request.method == 'POST':
        nombre = request.form['nombreAdm']
        tipoDoc = request.form['tipoDocAdm']
        noDoc = request.form['noDocAdm']
        cel = request.form['celAdm']
        email = request.form['emailAdm']
        con = request.form['conAdm']
        
        new_administrador = Administrador(nombreAdm=nombre, tipoDocAdm=tipoDoc, noDocAdm=noDoc, celAdm=cel, emailAdm=email, conAdm=con)
        db.session.add(new_administrador)
        db.session.commit()
        
        return redirect(url_for('administrador.index'))

    return render_template('administrador/add.html')

@bp.route('/Administrador/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    administrador = Administrador.query.get_or_404(id)

    if request.method == 'POST':
        administrador.nombreAdm = request.form['nombreAdm']
        administrador.tipoDocAdm = request.form['tipoDocAdm']
        administrador.noDocAdm = request.form['noDocAdm']
        administrador.celAdm = request.form['celAdm']
        administrador.emailAdm = request.form['emailAdm']
        administrador.conAdm = request.form['conAdm']
        db.session.commit()
        return redirect(url_for('administrador.index'))

    return render_template('administrador/edit.html', administrador=administrador)
    

@bp.route('/Administrador/delete/<int:id>')
@login_required
def delete(id):
    administrador = Administrador.query.get_or_404(id)
    
    db.session.delete(administrador)
    db.session.commit()

    return redirect(url_for('administrador.index'))

@bp.route('/Administrador/admin')
@login_required
def admin():
    return render_template('administrador/admin.html')

@bp.route('/')
def home():
    return render_template('index.html')