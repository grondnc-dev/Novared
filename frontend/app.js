const API_BASE = 'http://127.0.0.1:3000/api/planes';

const form = document.getElementById('form-plan');
const tablaBody = document.getElementById('tabla-planes');
const alertaDiv = document.getElementById('alerta');
const btnCancelar = document.getElementById('btn-cancelar');
const formTitulo = document.getElementById('form-titulo');

function mostrarAlerta(mensaje, tipo) {
  alertaDiv.textContent = mensaje;
  alertaDiv.className = `alerta ${tipo === 'exito' ? 'alerta-exito' : 'alerta-error'}`;
  alertaDiv.classList.remove('oculto');
  setTimeout(() => alertaDiv.classList.add('oculto'), 4500);
}

async function cargarPlanes() {
  try {
    const res = await fetch(`${API_BASE}/`);
    if (!res.ok) throw new Error(`HTTP ${res.status}`);

    const planes = await res.json();
    tablaBody.innerHTML = '';

    planes.forEach(plan => {
      const fila = document.createElement('tr');
      fila.innerHTML = `
        <td>${plan.id}</td>
        <td>${plan.nombre}</td>
        <td>${plan.ancho_banda} Mbps</td>
        <td>$${Number(plan.tarifa).toLocaleString('es-CO')}</td>
        <td>${plan.sla}</td>
        <td>
          <button class="btn-editar" onclick="cargarEnFormulario(${plan.id}, '${plan.nombre}', ${plan.ancho_banda}, ${plan.tarifa}, '${plan.sla}')">Editar</button>
          <button class="btn-eliminar" onclick="eliminarPlan(${plan.id})">Eliminar</button>
        </td>
      `;
      tablaBody.appendChild(fila);
    });
  } catch (error) {
    mostrarAlerta(`Error al conectar con el servidor Flask: ${error.message}`, 'error');
  }
}

form.addEventListener('submit', async (e) => {
  e.preventDefault();

  const id = document.getElementById('plan-id').value;
  const nombre = document.getElementById('nombre').value.trim();
  const ancho_banda = Number(document.getElementById('ancho_banda').value);
  const tarifa = Number(document.getElementById('tarifa').value);
  const sla = document.getElementById('sla').value.trim();

  if (!nombre || !ancho_banda || !tarifa || !sla) {
    mostrarAlerta('Error de validación: Todos los campos son obligatorios.', 'error');
    return;
  }
  if (ancho_banda <= 0) {
    mostrarAlerta('Error de validación: El ancho de banda debe ser mayor a 0 Mbps.', 'error');
    return;
  }
  if (tarifa < 50000) {
    mostrarAlerta('Regla de negocio: La tarifa mínima operativa en Bogotá es de $50,000 COP.', 'error');
    return;
  }

  const esEdicion = Boolean(id);
  const url = esEdicion ? `${API_BASE}/${id}` : `${API_BASE}/`;
  const metodo = esEdicion ? 'PUT' : 'POST';

  try {
    const res = await fetch(url, {
      method: metodo,
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ nombre, ancho_banda, tarifa, sla })
    });

    const data = await res.json().catch(() => ({}));

    if (res.status === 201) {
      mostrarAlerta('Plan creado exitosamente (201 Created).', 'exito');
      limpiarFormulario();
      cargarPlanes();
    } else if (res.status === 200) {
      mostrarAlerta('Plan actualizado correctamente (200 OK).', 'exito');
      limpiarFormulario();
      cargarPlanes();
    } else {
      const detalle = data.error || data.mensaje || data.message || 'Datos rechazados por el servidor';
      mostrarAlerta(`Error ${res.status}: ${detalle}`, 'error');
    }
  } catch (error) {
    mostrarAlerta('Fallo de red al intentar guardar el plan.', 'error');
  }
});

async function eliminarPlan(id) {
  if (!confirm(`¿Confirmas eliminar el Plan #${id} de la base de datos?`)) return;

  try {
    const res = await fetch(`${API_BASE}/${id}`, { method: 'DELETE' });

    if (res.status === 204 || res.ok) {
      mostrarAlerta(`Plan #${id} eliminado permanentemente (204 No Content).`, 'exito');
      cargarPlanes();
    } else if (res.status === 404) {
      mostrarAlerta(`Error 404: El Plan #${id} ya no existe.`, 'error');
    } else {
      mostrarAlerta(`Error HTTP ${res.status} al eliminar el registro.`, 'error');
    }
  } catch (error) {
    mostrarAlerta('Error de conexión al intentar eliminar.', 'error');
  }
}

function cargarEnFormulario(id, nombre, ancho_banda, tarifa, sla) {
  document.getElementById('plan-id').value = id;
  document.getElementById('nombre').value = nombre;
  document.getElementById('ancho_banda').value = ancho_banda;
  document.getElementById('tarifa').value = tarifa;
  document.getElementById('sla').value = sla;
  formTitulo.textContent = `Editando Plan #${id}`;
  btnCancelar.classList.remove('oculto');
}

function limpiarFormulario() {
  form.reset();
  document.getElementById('plan-id').value = '';
  formTitulo.textContent = 'Registrar Nuevo Plan';
  btnCancelar.classList.add('oculto');
}

btnCancelar.addEventListener('click', limpiarFormulario);
document.addEventListener('DOMContentLoaded', cargarPlanes);
