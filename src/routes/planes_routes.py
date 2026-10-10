from flask import Blueprint
from src.controllers.planes_controller import PlanesController

planes_bp = Blueprint('planes', __name__)
controller = PlanesController()

@planes_bp.route('/', methods=['GET'])
def listar_planes():
    return controller.listar()

@planes_bp.route('/<int:id>', methods=['GET'])
def obtener_plan(id):
    return controller.obtener_uno(id)

@planes_bp.route('/', methods=['POST'])
def crear_plan():
    return controller.crear()

@planes_bp.route('/<int:id>', methods=['PUT'])
def actualizar_plan(id):
    return controller.actualizar(id)

@planes_bp.route('/<int:id>', methods=['DELETE'])
def eliminar_plan(id):
    return controller.eliminar(id)
