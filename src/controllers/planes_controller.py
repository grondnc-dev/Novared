from flask import jsonify, request
from src.services.planes_service import PlanesService

class PlanesController:
    def __init__(self):
        self.service = PlanesService()

    def listar(self):
        try:
            planes = self.service.obtener_todos()
            return jsonify(planes), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    def obtener_uno(self, id):
        try:
            plan = self.service.obtener_por_id(id)
            return jsonify(plan), 200
        except ValueError as e:
            if str(e) == "PLAN_NOT_FOUND":
                return jsonify({"error": "Plan no encontrado."}), 404
            return jsonify({"error": str(e)}), 400

    def crear(self):
        try:
            datos = request.get_json()
            nuevo_plan = self.service.crear_plan(datos)
            return jsonify(nuevo_plan), 201
        except ValueError as e:
            if "VALIDATION_ERROR" in str(e):
                return jsonify({"error": str(e)}), 400
            return jsonify({"error": str(e)}), 500

    def actualizar(self, id):
        try:
            datos = request.get_json()
            self.service.actualizar_plan(id, datos)
            return jsonify({"mensaje": "Plan actualizado con éxito."}), 200
        except ValueError as e:
            if str(e) == "PLAN_NOT_FOUND":
                return jsonify({"error": "Plan no encontrado."}), 404
            if "VALIDATION_ERROR" in str(e):
                return jsonify({"error": str(e)}), 400
            return jsonify({"error": str(e)}), 500

    def eliminar(self, id):
        try:
            self.service.eliminar_plan(id)
            # CORRECCIÓN OBLIGATORIA DE LA GUÍA: Retorna una respuesta vacía con código HTTP 204 No Content
            return '', 204
        except ValueError as e:
            if str(e) == "PLAN_NOT_FOUND":
                return jsonify({"error": "Plan no encontrado."}), 404
            return jsonify({"error": str(e)}), 500
