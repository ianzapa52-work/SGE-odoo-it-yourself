# **README — Módulo Odoo `izl_peluqueria`**

## **Peluquería IZL**  
**Autor:** Ian Zapatero López  
**Módulo técnico:** `izl_peluqueria`  
**Versión:** 1.0  
**Categoría:** Servicios  
**Aplicación:** Sí  

---

## **1. Introducción**

El módulo **Peluquería IZL** es una solución desarrollada para Odoo con el objetivo de gestionar de forma integral la actividad de una peluquería. Permite administrar clientes, empleados, servicios y citas, incorporando funcionalidades avanzadas como informes PDF, vistas analíticas, calendario, kanban, estadísticas y datos de demostración.

El desarrollo sigue las buenas prácticas de Odoo, manteniendo una estructura modular, identificadores coherentes y una separación clara entre modelos, vistas, seguridad y datos.

---

## **2. Nombre técnico y prefijo de identificadores**

El módulo utiliza el prefijo:

### **`izl_peluqueria`**

Siguiendo la norma *abc_keyword*, donde:

- **izl** → iniciales del alumno (Ian Zapatero López)  
- **peluqueria** → palabra clave del dominio funcional  

Este prefijo se aplica en:

- Modelos  
- Vistas  
- Acciones  
- Menús  
- Secuencias  
- Informes  
- Datos demo  

---

## **3. Objetivo y finalidad del módulo**

El módulo permite:

- Gestionar clientes de la peluquería.  
- Registrar empleados y sus especialidades.  
- Definir servicios y precios.  
- Crear y administrar citas entre clientes, empleados y servicios.  
- Analizar la actividad mediante vistas gráficas, pivot y calendario.  
- Generar informes PDF personalizados.  
- Facilitar la navegación mediante menús organizados y vistas intuitivas.  

---

## **4. Estructura general del módulo**

El módulo se compone de:

- **Modelos:** cliente, empleado, servicio y cita.  
- **Vistas:** tree, form, kanban, search, calendar, graph, pivot y activity.  
- **Menús y acciones:** navegación completa desde un menú raíz.  
- **Seguridad:** reglas de acceso y grupos.  
- **Datos:** secuencias e información de demostración.  
- **Informes:** plantilla QWeb y acción PDF.  
- **Manifest:** definición del módulo y carga de recursos.  

---

## **5. Modelos implementados**

### **Cliente**
Gestiona datos personales, foto, contacto y citas asociadas.  
Incluye un contador de citas y un botón para acceder a ellas.

### **Empleado**
Registra nombre, apellidos, contacto y especialidad.  
Genera automáticamente el nombre completo.

### **Servicio**
Define nombre, descripción, precio y empleados que pueden realizarlo.

### **Cita**
Relaciona cliente, servicio, empleado y fecha.  
Incluye validación para evitar citas en el pasado y secuencia automática.

---

## **6. Relaciones entre modelos (UML)**

**Relaciones principales:**

- Cliente 1—N Cita  
- Empleado 1—N Cita  
- Servicio 1—N Cita  
- Servicio N—M Empleado  

**Descripción UML:**

- Un **cliente** puede tener varias **citas**.  
- Un **empleado** puede atender varias **citas**.  
- Un **servicio** puede estar asociado a varias **citas**.  
- Un **servicio** puede ser realizado por varios **empleados**.  

## Diagrama UML ![Diagrama UML del módulo izl_peluqueria](odoo\addons\izl_peluqueria\assets\DiagramaIZLPeluqueria.drawio.png)

**Representación:**

@startuml
title Diagrama de Clases — Módulo izl_peluqueria

class Cliente {
    + nombre
    + apellido
    + telefono
    + email
    + fecha_nacimiento
    + image_1920
    + total_citas
}

class Empleado {
    + nombre
    + apellido
    + telefono
    + email
    + especialidad
}

class Servicio {
    + nombre
    + descripcion
    + precio
}

class Cita {
    + codigo
    + fecha
    + nota
}

Cliente "1" --> "0..*" Cita : tiene >
Empleado "1" --> "0..*" Cita : atiende >
Servicio "1" --> "0..*" Cita : incluye >
Servicio "0..*" --> "0..*" Empleado : puede realizar >
@enduml

---

## **7. Vistas y experiencia de usuario**

### **Clientes**
- Tree: listado general.  
- Form: ficha completa con foto, citas y botones de acción.  
- Kanban: vista visual agrupada por apellido.  
- Search: filtros por citas, agrupaciones y campos clave.  
- Activity: gestión de actividades.

### **Empleados**
- Tree y Form.  
- Search con filtros por especialidad.

### **Servicios**
- Tree y Form.  
- Many2many editable para empleados.

### **Citas**
- Tree y Form con chatter.  
- Search con filtros de citas futuras/pasadas.  
- Calendar para planificación.  
- Graph y Pivot para análisis.

---

## **8. Menús y acciones**

Menú raíz: **Peluquería IZL**

Submenús:

- Clientes  
- Citas  
- Empleados  
- Servicios  

Cada uno con su acción correspondiente y vistas adecuadas.

---

## **9. Seguridad y control de acceso**

Incluye:

- Archivo `ir.model.access.csv` con permisos para cada modelo.  
- Archivo `izl_peluqueria_groups.xml` para definir grupos.  

---

## **10. Datos de demostración**

Incluye:

- 3 clientes  
- 3 empleados  
- 4 servicios  
- 5 citas futuras  

Permiten validar el funcionamiento del módulo sin introducir datos manualmente.

---

## **11. Informes generados**

### **Informe PDF del Cliente**
Incluye:

- Foto del cliente  
- Nombre  
- Listado de citas con fecha, servicio y empleado  

Se genera desde un botón en la vista formulario del cliente.

---

## **12. Actividades realizadas**

- Diseño de la estructura del módulo.  
- Implementación de modelos y relaciones.  
- Creación de vistas tree, form, kanban, calendar, graph y pivot.  
- Configuración de menús y acciones.  
- Implementación de secuencias y validaciones.  
- Desarrollo de informe PDF.  
- Creación de datos demo.  
- Pruebas funcionales en Odoo.  

---

## **13. Problemas encontrados**

- Ajuste de la secuencia para generar códigos de cita.  
- Validación de fechas para evitar citas en el pasado.  
- Alineación de vistas heredadas del cliente.  
- Configuración del informe PDF para mostrar imágenes correctamente.  
- Ajustes en el Many2many editable del servicio.  

---

## **14. Conclusiones personales**

El desarrollo del módulo ha permitido comprender:

- La arquitectura de Odoo.  
- La relación entre modelos, vistas y acciones.  
- El uso de QWeb para informes.  
- La importancia de la coherencia en identificadores.  
- La utilidad de los datos demo para validar funcionalidades.  

El resultado es un módulo completo, funcional y alineado con las buenas prácticas de desarrollo en Odoo.

---

## **15. Sugerencias de mejora**

- Añadir un sistema de facturación integrado.  
- Implementar recordatorios automáticos por correo.  
- Añadir un panel de control (dashboard) con KPIs.  
- Incorporar un sistema de fidelización de clientes.  
- Añadir disponibilidad de empleados para evitar solapamientos.  

---

## **16. Referencias bibliográficas (con enlaces)**

Aquí tienes una lista ampliada, con enlaces reales y útiles:

### **Documentación oficial de Odoo**
- Documentación general:  
  `https://www.odoo.com/documentation`
- Desarrollo de módulos:  
  `https://www.odoo.com/documentation/17.0/developer`
- Framework ORM:  
  `https://www.odoo.com/documentation/17.0/developer/reference/backend/orm`
- Vistas y QWeb:  
  `https://www.odoo.com/documentation/17.0/developer/reference/frontend/qweb`
- Seguridad en Odoo:  
  `https://www.odoo.com/documentation/17.0/developer/reference/security`

### **Recursos adicionales**
- Tutoriales de Odoo (Odoo Mates):  
  `https://www.youtube.com/@OdooMates`
- StackOverflow (etiqueta Odoo):  
  `https://stackoverflow.com/questions/tagged/odoo`