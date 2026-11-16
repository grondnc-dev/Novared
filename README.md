# NOVARED - Gestión de planes de conectividad

**Asignatura:** Ingeniería de Software III
**Período académico:** 4.º cuatrimestre - Universidad INCCA
**Año de desarrollo:** 2026

## Integrantes

- Mercedes Del Pilar Mosquera Martínez
- Luz Amparo Sánchez Archila
- Yeisten Osvaldo Murcia Vásquez
- Alvaro Gerardo Rondón Carvajal

## Descripción

NOVARED es una aplicación académica para centralizar la administración de servicios de conectividad dirigidos a empresas PYME de Bogotá. Este avance implementa el catálogo de planes: permite registrar, consultar, actualizar y eliminar planes, validando el ancho de banda, la tarifa mensual mínima de $50.000 COP y el formato del SLA.

El proyecto incluye una API REST construida con Flask y SQLite, además de una interfaz web para administrar los planes. La página muestra el logo de NOVARED, ubicado en `evidencias/logo.png`.

## Estructura del proyecto

```text
Novared/
├── data/
│   └── app.db
├── evidencias/
│   ├── logo.png
│   └── ...
├── frontend/
│   ├── app.js
│   ├── index.html
│   └── styles.css
├── src/
│   ├── app.py
│   ├── controllers/
│   │   └── planes_controller.py
│   ├── db/
│   │   └── database.py
│   ├── repositories/
│   │   └── planes_repository.py
│   ├── routes/
│   │   └── planes_routes.py
│   └── services/
│       └── planes_service.py
├── .env
├── requirements.txt
└── README.md
```

La API sigue el flujo **Rutas → Controladores → Servicios → Repositorios**. El frontend está hecho con HTML, CSS y JavaScript y se comunica con la API mediante `fetch`.

## Requisitos

- Python 3
- `pip`

## Instalación y ejecución en Windows

Abre dos terminales en la carpeta raíz del proyecto.

### 1. Instalar dependencias

```powershell
pip install -r requirements.txt
```

### 2. Iniciar el backend

En la primera terminal, ejecuta:

```powershell
python -m src.app
```

La aplicación inicializa la tabla `planes` si todavía no existe y ejecuta el servidor en `http://127.0.0.1:3000`. El puerto se puede cambiar mediante la variable `PORT` del archivo `.env`.

### 3. Iniciar el frontend

En la segunda terminal, ejecuta:

```powershell
python -m http.server 8080 --directory frontend
```

Abre `http://127.0.0.1:8080` en el navegador. Sirve la página desde un servidor HTTP para que el navegador pueda cargar sus recursos y realizar las peticiones a la API. El logo se encuentra en `frontend/logo.png` para que también se cargue cuando `frontend/` se sirve como raíz.

## Configuración

El archivo `.env` en la raíz contiene la configuración local:

```env
PORT=3000
DB_FILE=./data/app.db
FLASK_ENV=development
```

`PORT` define el puerto del backend y `DB_FILE` la ruta de la base de datos SQLite. La configuración CORS de la API habilita las solicitudes desde el frontend.

## API REST

La base de la API es `http://127.0.0.1:3000/api/planes`.

| Método | Ruta | Descripción | Respuesta esperada |
|---|---|---|---|
| `GET` | `/` | Lista todos los planes | `200 OK` |
| `GET` | `/<id>` | Consulta un plan por ID | `200 OK` o `404 Not Found` |
| `POST` | `/` | Crea un plan | `201 Created` o `400 Bad Request` |
| `PUT` | `/<id>` | Actualiza un plan | `200 OK`, `400 Bad Request` o `404 Not Found` |
| `DELETE` | `/<id>` | Elimina un plan | `204 No Content` o `404 Not Found` |

El cuerpo de las solicitudes `POST` y `PUT` debe ser JSON con estos campos:

```json
{
  "nombre": "Plan Comercio Bogotá",
  "ancho_banda": 300,
  "tarifa": 150000,
  "sla": "99.7%"
}
```

Reglas de validación principales:

- El nombre debe tener al menos 3 caracteres.
- El ancho de banda debe ser un número positivo, en Mbps.
- La tarifa debe ser de al menos $50.000 COP.
- El SLA debe incluir el símbolo `%`.
- El cuerpo debe ser un objeto JSON válido.

## Ejemplos de solicitudes

Los siguientes ejemplos usan `curl.exe` desde PowerShell.

Listar planes:

```powershell
curl.exe http://127.0.0.1:3000/api/planes/
```

Crear un plan:

```powershell
curl.exe -X POST http://127.0.0.1:3000/api/planes/ -H "Content-Type: application/json" -d '{"nombre":"Plan Comercio Bogotá","ancho_banda":300,"tarifa":150000,"sla":"99.7%"}'
```

Consultar el plan con ID `2`:

```powershell
curl.exe http://127.0.0.1:3000/api/planes/2
```

## Interfaz web

Desde la página se pueden listar planes, registrar nuevos, editar sus datos y eliminarlos. La interfaz incluye validaciones previas al envío y presenta mensajes de éxito o error según la respuesta de la API.

La página y sus recursos, incluido el logo, están en `frontend/`. La imagen original también se conserva en `evidencias/logo.png`.

## Evidencias

Las capturas de las pruebas de la API y de la interfaz están en [`evidencias/`](./evidencias/).
