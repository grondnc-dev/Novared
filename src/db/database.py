import sqlite3
import os
from dotenv import load_dotenv

load_dotenv()
DB_PATH = os.getenv("DB_FILE", "./data/app.db")

def obtener_conexion():
    """Retorna una conexión limpia a la base de datos."""
    # Asegurar que la carpeta 'data' exista
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    
    conn = sqlite3.connect(DB_PATH)
    # Permite acceder a las columnas por nombre como si fuera un diccionario
    conn.row_factory = sqlite3.Row 
    return conn

def inicializar_tablas():
    """Crea las tablas automáticamente si no existen."""
    script_tabla_planes = """
    CREATE TABLE IF NOT EXISTS planes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        ancho_banda INTEGER NOT NULL, -- En Mbps
        tarifa REAL NOT NULL,         -- En COP
        sla TEXT NOT NULL             -- Acuerdo de nivel de servicio (ej: '99.5%')
    );
    """
    conn = obtener_conexion()
    try:
        conn.execute(script_tabla_planes)
        conn.commit()
        print("Tabla 'planes' verificada/creada correctamente en SQLite.")
    except Exception as e:
        print(f"Error al inicializar la base de datos: {e}")
    finally:
        conn.close()
