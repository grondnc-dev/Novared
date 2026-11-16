# NOVARED - Núcleo del Servidor (Backend v1.0.0)
**Asignatura:** Ingeniería de Software III  
**Período Académico:** 4 Cuatrimestre - Universidad INCCA  
**Año de Desarrollo:** 2026  

### Integrantes / Alumnos del Proyecto:
* **Mercedes Del Pilar Mosquera Martínez**
* **Luz Amparo Sánchez Archila**
* **Yeisten Osvaldo Murcia Vásquez**
* **Alvaro Gerardo Rondón Carvajal**

---

## 1. Descripción del Proyecto y Entidad Elegida

### Contexto del Sistema (Proyecto de Aula)
**NOVARED** es una solución tecnológica diseñada para centralizar, administrar y asegurar la información operativa de conectividad orientada a empresas PYME del sector comercial en la ciudad de Bogotá. La problemática central que resuelve este sistema es la ineficiencia administrativa, la pérdida de datos de clientes, errores de facturación y las dificultades para controlar de manera estricta los Acuerdos de Nivel de Servicio (**SLA**) y anchos de banda contratados.

### Entidad Elegida para el Avance: `Planes`
Para este hito de revisión, se seleccionó el módulo de **Planes** como el núcleo estructural del negocio. Esta entidad define el catálogo de servicios de telecomunicaciones que la microempresa comercializa. Controlar esta entidad mediante una API robusta permite:
* Automatizar y estandarizar las tarifas vigentes del mercado de telecomunicaciones colombiano.
* Validar técnicamente las capacidades de conectividad (Mbps) y cumplimiento de SLAs antes de su asignación contractual.
* Evitar pérdidas económicas garantizando que ningún servicio se comercialice por debajo de los costos mínimos operativos establecidos para el sector comercial PYME de Bogotá (\$50,000 COP).

## Estructura de Directorios para NOVARED
---

## 5. Integración Frontend y Despliegue Simultáneo (Sesión No. 11)

Se implementó una interfaz desacoplada en **HTML5, CSS3 y Vanilla JavaScript (`Fetch API`)** en `/frontend` que consume los endpoints REST del módulo **Planes**, manejando códigos HTTP (`200`, `201`, `204`, `400`, `404`).

### Estructura Actualizada
```text
Novared/
├── data/app.db                 # Base de datos SQLite
├── evidencias/                 # Capturas de pruebas API/Frontend
├── frontend/                   # index.html, styles.css, app.js
├── src/app.py                  # Servidor Flask con CORS
├── requirements.txt            # Flask, python-dotenv, flask-cors
└── README.md
```

### Ejecución Local Simultánea

1. **Backend (Puerto 3000):**
   ```bash
   pip install -r requirements.txt
   python -m src.app
   ```
2. **Frontend (Puerto 8080):**
   ```bash
   cd frontend && python -m http.server 8080
   ```
   *Accede a `http://127.0.0.1:8080`.*

---

## 6. Evidencias del Ciclo CRUD

* **GET (`/api/planes/`):** Listado dinámico (`200 OK`).
* **POST (`/api/planes/`):** Alta de planes con validaciones (`201 Created` / `400 Bad Request`).
* **PUT (`/api/planes/<id>`):** Edición de registros (`200 OK`).
* **DELETE (`/api/planes/<id>`):** Borrado con confirmación (`204 No Content`).