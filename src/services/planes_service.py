from src.repositories.planes_repository import PlanesRepository

class PlanesService:
    def __init__(self):
        self.repository = PlanesRepository()

    def obtener_todos(self):
        return self.repository.get_all()

    def obtener_por_id(self, plan_id):
        plan = self.repository.get_by_id(plan_id)
        if not plan:
            raise ValueError("PLAN_NOT_FOUND")
        return plan

    def crear_plan(self, datos):
        self._validar_datos_plan(datos)
        nuevo_id = self.repository.create(datos)
        return {"id": nuevo_id, **datos}

    def actualizar_plan(self, plan_id, datos):
        self.obtener_por_id(plan_id) # Valida existencia primero
        self._validar_datos_plan(datos)
        return self.repository.update(plan_id, datos)

    def eliminar_plan(self, plan_id):
        self.obtener_por_id(plan_id) # Valida existencia primero
        return self.repository.delete(plan_id)

    def _validar_datos_plan(self, datos):
        nombre = datos.get('nombre')
        ancho_banda = datos.get('ancho_banda')
        tarifa = datos.get('tarifa')
        sla = datos.get('sla')

        if not nombre or len(str(nombre).strip()) < 3:
            raise ValueError("VALIDATION_ERROR: El nombre del plan debe tener al menos 3 caracteres.")
        if ancho_banda is None or not isinstance(ancho_banda, (int, float)) or ancho_banda <= 0:
            raise ValueError("VALIDATION_ERROR: El ancho de banda debe ser un número positivo en Mbps.")
        if tarifa is None or not isinstance(tarifa, (int, float)) or tarifa < 50000:
            raise ValueError("VALIDATION_ERROR: La tarifa mínima comercial para PYMEs en Bogotá es de $50,000 COP.")
        if not sla or '%' not in str(sla):
            raise ValueError("VALIDATION_ERROR: El SLA es requerido y debe especificar un formato de porcentaje (ej: 99.9%).")
