from flask import Blueprint

bp = Blueprint('main', __name__)

from app.routes import administrador_routes, celador_routes, pc_routes, registro_routes, usuario_routes
