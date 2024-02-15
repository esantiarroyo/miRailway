from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from app.models.Celador import Celador
from app.models.Administrador import Administrador
from app.models.Registro import Registro
from app.models.Pc import Pc
from app import db

bp = Blueprint('celador', __name__)

@bp.route('/Celador')
@login_required
def index():
    data = Celador.query.all()
    return render_template('celador/index.html', data=data)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        logout_user()
        noDocCel = request.form['noDocCel']
        conCel = request.form['conCel']
        print("antes del user")
        usuario = Celador.query.filter_by(noDocCel=noDocCel, conCel=conCel).first()
        admin = Administrador.query.filter_by(noDocAdm=noDocCel, conAdm=conCel).first()
        print(f"despues del user {usuario}")
        print(f"despues del user {admin}")
        if usuario:
            login_user(usuario)
            print("Entra a celador ", current_user.is_authenticated)
            return redirect(url_for('celador.cel'))
        
        if admin:
            login_user(admin)
            print("Entra a admin ",current_user.is_authenticated)
            return redirect(url_for('administrador.admin'))
        
        flash("Numero de documento o contraseña incorrecto.", "error")
    if current_user.is_authenticated:
        if isinstance(current_user, Celador):
            return redirect(url_for('celador.cel'))
        else:
            return redirect(url_for('administrador.admin'))
    return render_template("index.html")

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Sesion Cerrada.', 'info')
    return redirect(url_for('celador.login'))

@bp.route('/Celador/add', methods=['GET', 'POST'])
@login_required
def add():
    if request.method == 'POST':
        nombre = request.form['nombreCel']
        noDoc = request.form['noDocCel']
        cel = request.form['celCel']
        email = request.form['emailCel']
        con = request.form['conCel']
        
        new_celador = Celador(nombreCel=nombre, noDocCel=noDoc, celCel=cel, emailCel=email, conCel=con)
        db.session.add(new_celador)
        db.session.commit()
        
        return redirect(url_for('celador.index'))

    return render_template('celador/add.html')

@bp.route('/Celador/buscar', methods=['GET'])
@login_required
def buscar():
    serialPc = request.args.get('serial')
    data = Pc.query.filter_by(serialPc=serialPc).all()
    return render_template('celador/entrada.html', data=data)

@bp.route('/Celador/entrada', methods=['GET'])
@login_required
def entrada():
    return render_template("celador/entrada.html")

@bp.route('/Celador/buscar2', methods=['GET'])
@login_required
def buscar2():
    serialPc = request.args.get('serial')
    data = Pc.query.filter_by(serialPc=serialPc).all()
    return render_template('celador/salida.html', data=data)

@bp.route('/Celador/salida', methods=['GET'])
@login_required
def salida():
    return render_template("celador/salida.html")

@bp.route('/Celador/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    celador = Celador.query.get_or_404(id)

    if request.method == 'POST':
        celador.nombreCel = request.form['nombreCel']
        celador.noDocCel = request.form['noDocCel']
        celador.celCel = request.form['celCel']
        celador.emailCel = request.form['emailCel']
        celador.conCel = request.form['conCel']
        db.session.commit()
        return redirect(url_for('celador.index'))

    return render_template('celador/edit.html', celador=celador)
    

@bp.route('/Celador/delete/<int:id>')
@login_required
def delete(id):
    celador = Celador.query.get_or_404(id)
    
    db.session.delete(celador)
    db.session.commit()

    return redirect(url_for('celador.index'))

@bp.route('/Celador/cel')
@login_required
def cel():
    return render_template('celador/cel.html')