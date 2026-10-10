from src.db.database import obtener_conexion

class PlanesRepository:
    def get_all(self):
        with obtener_conexion() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM planes")
            rows = cursor.fetchall()
            return [dict(row) for row in rows]

    def get_by_id(self, plan_id):
        with obtener_conexion() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM planes WHERE id = ?", (plan_id,))
            row = cursor.fetchone()
            return dict(row) if row else None

    def create(self, datos):
        with obtener_conexion() as conn:
            cursor = conn.cursor()
            sql = "INSERT INTO planes (nombre, ancho_banda, tarifa, sla) VALUES (?, ?, ?, ?)"
            cursor.execute(sql, (datos['nombre'], datos['ancho_banda'], datos['tarifa'], datos['sla']))
            conn.commit()
            return cursor.lastrowid

    def update(self, plan_id, datos):
        with obtener_conexion() as conn:
            cursor = conn.cursor()
            sql = "UPDATE planes SET nombre = ?, ancho_banda = ?, tarifa = ?, sla = ? WHERE id = ?"
            cursor.execute(sql, (datos['nombre'], datos['ancho_banda'], datos['tarifa'], datos['sla'], plan_id))
            conn.commit()
            return cursor.rowcount > 0

    def delete(self, plan_id):
        with obtener_conexion() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM planes WHERE id = ?", (plan_id,))
            conn.commit()
            return cursor.rowcount > 0
