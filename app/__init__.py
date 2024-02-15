from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.urandom(24)
    app.config.from_object('config.Config')
    
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = '/'
    
    @login_manager.user_loader
    def load_user(user_id):
        from app.models.Celador import Celador 
        from app.models.Administrador import Administrador
        user = Celador.query.get(int(user_id))
        if user is None:
            user = Administrador.query.get(int(user_id))
        return user

    from app.routes import administrador_routes, celador_routes, pc_routes, registro_routes, usuario_routes
    app.register_blueprint(administrador_routes.bp)
    app.register_blueprint(celador_routes.bp)
    app.register_blueprint(pc_routes.bp)
    app.register_blueprint(registro_routes.bp)
    app.register_blueprint(usuario_routes.bp)

    return app