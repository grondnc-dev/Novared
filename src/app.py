import os
from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from src.db.database import inicializar_tablas
from src.routes.planes_routes import planes_bp

load_dotenv()

app = Flask(__name__)
CORS(app)

# Inicializar Base de Datos SQLite de forma automática al arrancar
inicializar_tablas()

# Registrar Rutas con Prefijo de API Limpia
app.register_blueprint(planes_bp, url_prefix='/api/planes')

@app.errorhandler(404)
def nodo_no_encontrado(e):
    return jsonify({"error": "Endpoint no encontrado."}), 404

if __name__ == '__main__':
    port = int(os.getenv("PORT", 3000))
    app.run(port=port, debug=True)
