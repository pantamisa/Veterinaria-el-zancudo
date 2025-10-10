# 🏥 Sistema de Gestión Veterinaria El Zancudo

Un sistema completo de gestión para clínicas veterinarias desarrollado en Python con interfaz de línea de comandos.

## 📋 Características

- **Gestión de Usuarios**: Registro, edición y administración de usuarios del sistema
- **Gestión de Animales**: Control completo de mascotas y sus datos
- **Gestión de Citas**: Programación y seguimiento de citas veterinarias
- **Gestión de Facturas**: Sistema de facturación integrado
  
### Módulos Principales

- ✅ **Gestión de Usuarios** - Registro, autenticación, roles (admin/usuario)
- ✅ **Gestión de Animales** - Registro de mascotas con propietarios
- ✅ **Tipos y Razas** - Clasificación de animales (Perro, Gato, Ave, etc.)
- ✅ **Servicios** - Baño, Vacunas, Desparasitación, etc.
- ✅ **Citas** - Programación de servicios veterinarios
- ✅ **Facturación** - Generación y seguimiento de facturas

### Funcionalidades

- 🔐 Autenticación con hash de contraseñas (bcrypt)
- 📊 API REST completa con FastAPI
- 🖥️ Interfaz de consola interactiva
- 🗄️ Base de datos PostgreSQL en la nube (Neon)
- 📝 Documentación automática con Swagger/OpenAPI
- 🔄 Relaciones complejas entre entidades
- ✏️ CRUD completo para todas las entidades
- 📈 Seguimiento de citas y pagos

---

Sistema completo de gestión veterinaria desarrollado con FastAPI, SQLAlchemy y PostgreSQL (Neon). Incluye gestión de usuarios, animales, citas, servicios y facturación.

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115.0-green.svg)](https://fastapi.tiangolo.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Neon-blue.svg)](https://neon.tech/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 🛠️ Tecnologías Utilizadas
  
### Backend
- **Python 3.9+**
- **FastAPI 0.115.0** - Framework web moderno
- **SQLAlchemy 2.0.23** - ORM para base de datos
- **Pydantic 2.10.0** - Validación de datos
- **PostgreSQL** - Base de datos relacional

### Seguridad
- **Bcrypt 4.1.2** - Hash de contraseñas
- **Passlib 1.7.4** - Utilidades de seguridad

### Base de Datos
- **Neon PostgreSQL** - Base de datos serverless
- **Alembic 1.13.1** - Migraciones de base de datos
- **psycopg2-binary 2.9.10** - Adaptador PostgreSQL

### Servidor
- **Uvicorn 0.32.0** - Servidor ASGI de alto rendimiento

---
## 📋 Requisitos Previos

- Python 3.9 o superior
- pip (gestor de paquetes de Python)
- Cuenta en [Neon](https://neon.tech) (base de datos PostgreSQL)
- Git (opcional)

---

## 🚀 Instalación

### 1. Clonar el repositorio
```bash
git clone https://github.com/tu-usuario/veterinaria-el-zancudo.git
cd veterinaria-el-zancudo
## ▶️ Ejecución

Para iniciar el sistema, ejecutar:

```bash
python main.py
```

## 🔐 Usuario de Prueba

Para acceder al sistema, utilice las siguientes credenciales de administrador:

- **Email**: `Admin@admin.com`
- **Contraseña**: `abc1234`

> **Nota**: para acceder a distintas funcionalidades se recomienda primero selecionar la opcion de mostrar todos los registros y copiar el id del animal 

## 📚 Uso del Sistema

### Inicio de Sesión
1. Al iniciar el programa, se mostrará la pantalla de login
2. Ingrese el email y contraseña del usuario de prueba
3. El sistema validará las credenciales y mostrará el menú principal

### Navegación
- Use los números del menú para navegar entre opciones
- Presione `0` para volver al menú anterior o salir
- Use `Ctrl+C` para salir del programa en cualquier momento

# 🗄️ Base de Datos - Sistema Veterinaria El Zancudo

Este documento describe las tablas principales del sistema de gestión veterinaria, incluyendo su estructura y datos iniciales.

## 📊 Estructura de la Base de Datos

### 🐕 Tabla: razas

Almacena las diferentes razas de animales disponibles en el sistema.

**Estructura:**
- `id_raza` (UUID): Identificador único de la raza
- `nombreRaza` (VARCHAR): Nombre de la raza
- `id_tipoAnimal` (UUID): Referencia al tipo de animal

**Datos Iniciales:**

| ID Raza | Nombre Raza | ID Tipo Animal |
|---------|-------------|----------------|
| `05a6e2c6-cc69-45ef-b28f-7ad1c7813634` | Loro | `3413fa22-62e3-4e5d-b0f8-18fa135042d8` |
| `0f2327ab-1146-47b3-9d4c-85b8574c06b8` | Persa | `fbab3f31-6936-4788-88f2-c2280b7086de` |
| `2e3558e0-0fd6-4541-bdaf-2949d86fd69c` | Golden Retriever | `be866cb3-85f6-431d-b369-a1c842b5366f` |
| `4b3dcc9b-4ecf-4443-8d18-6026530d5694` | Siamés | `fbab3f31-6936-4788-88f2-c2280b7086de` |
| `51efa198-62f9-435d-b732-3ba53c2d560a` | Cacatúa | `3413fa22-62e3-4e5d-b0f8-18fa135042d8` |
| `666d6565-a19b-4b55-bd44-05d5dab84d73` | Periquito | `3413fa22-62e3-4e5d-b0f8-18fa135042d8` |
| `7d26ff7d-30df-40a3-b818-6d3dda9ca078` | Pastor Alemán | `be866cb3-85f6-431d-b369-a1c842b5366f` |
| `821b0047-a9ce-4f42-b850-87beb41a939a` | Labrador | `be866cb3-85f6-431d-b369-a1c842b5366f` |
| `a019c9ca-6470-4fa8-9c5b-553d6d01f47d` | Británico | `fbab3f31-6936-4788-88f2-c2280b7086de` |
| `cce29d1e-976e-4b55-a6e1-9bd525225bb3` | Canario | `3413fa22-62e3-4e5d-b0f8-18fa135042d8` |
| `fc078baf-b1b8-450b-b000-9a0b1e1b1836` | Bulldog | `be866cb3-85f6-431d-b369-a1c842b5366f` |
| `fd1dbf7d-83aa-44ee-a036-3549799e643d` | Maine Coon | `fbab3f31-6936-4788-88f2-c2280b7086de` |

**Análisis por Tipo de Animal:**
- **Perros** (`be866cb3-85f6-431d-b369-a1c842b5366f`): 5 razas
  - Golden Retriever, Pastor Alemán, Labrador, Bulldog
- **Gatos** (`fbab3f31-6936-4788-88f2-c2280b7086de`): 4 razas
  - Persa, Siamés, Británico, Maine Coon
- **Aves** (`3413fa22-62e3-4e5d-b0f8-18fa135042d8`): 4 razas
  - Loro, Cacatúa, Periquito, Canario

---

### 💰 Tabla: servicios

Catálogo de servicios veterinarios disponibles con sus respectivos costos.

**Estructura:**
- `id_servicio` (UUID): Identificador único del servicio
- `nombre_ser` (VARCHAR): Nombre del servicio
- `costo` (DECIMAL): Precio del servicio

**Datos Iniciales:**

| ID Servicio | Nombre del Servicio | Costo (COP) |
|-------------|-------------------|-------------|
| `47b33b58-4c2c-410f-96d2-3c0961afae71` | Baño | $15,000 |
| `a7f4ea96-408c-4271-b223-7e1e5227c708` | Vacunas | $100,000 |
| `e4777988-2266-45a3-9d21-72c08d0e22ef` | Desparasitar | $200000 |

**Notas sobre Servicios:**
- ✅ **Baño**: Servicio básico de aseo y limpieza
- ✅ **Vacunas**: Inmunización preventiva (precio alto por ser servicio médico)
- ⚠️ **Desparasitar**: desparacitacion del animal

---

### ⚧ Tabla: genero

Clasificación de géneros para los animales en el sistema.

**Estructura:**
- `id_genero` (UUID): Identificador único del género
- `nombre_genero` (VARCHAR): Nombre del género

**Datos Iniciales:**

| ID Género | Nombre del Género |
|-----------|------------------|
| `89c83dbd-0a70-4bc0-8007-891a2154a624` | Macho |
| `900001c5-9dbe-4e20-ba0f-c7b39176ab99` | Otro |
| `fb96ce8d-6a19-40ae-af82-3880d6e5a00c` | Hembra |

**Características:**
- **Macho**: Género masculino tradicional
- **Hembra**: Género femenino tradicional  
- **Otro**: Opción inclusiva para casos especiales o indefinidos

---

### Menús Disponibles

#### 🏠 Menú Principal
- **Opción 1**: Gestión de Usuarios
- **Opción 2**: Gestión de Animales  
- **Opción 3**: Gestión de Citas
- **Opción 4**: Gestión de Facturas
- **Opción 5**: Información del Sistema
- **Opción 6**: Cambiar de Usuario
- **Opción 0**: Salir del Sistema

#### 👥 Gestión de Usuarios
- Crear nuevos usuarios
- Editar información de usuarios existentes
- Eliminar usuarios
- Listar todos los usuarios
- Asignar roles (Admin/Usuario estándar)

#### 🐕 Gestión de Animales
- Registrar nuevas mascotas
- Actualizar información de animales
- Consultar historial de mascotas
- Asociar animales con propietarios

#### 📅 Gestión de Citas
- Programar nuevas citas
- Modificar citas existentes
- Cancelar citas
- Ver agenda diaria/semanal
- Seguimiento de citas completadas

#### 💰 Gestión de Facturas
- Generar facturas de servicios
- Consultar historial de pagos
- Gestionar precios de servicios
- Reportes financieros

## 🔧 Configuración

### Base de Datos
El sistema está configurado para usar PostgreSQL en Neon Cloud. La cadena de conexión está incluida en el código, pero se recomienda usar variables de entorno para mayor seguridad.

### Personalización
- Modifique los emojis y textos en `main.py` para personalizar la interfaz
- Ajuste los permisos de usuario en los módulos CRUD
- Personalice los campos de las entidades según las necesidades

## 🛡️ Seguridad

- Las contraseñas se ocultan durante la entrada usando `getpass`
- Sistema de intentos limitados para login (3 intentos máximo)
- Validación de permisos por rol de usuario
- Conexión segura a base de datos con SSL

## ⚙️ Configuración

-1. Variables de Entorno
Crea un archivo .env en la raíz del proyecto:
env# Base de Datos
DATABASE_URL=postgresql://usuario:contraseña@host:puerto/database

# Configuración de la aplicación
APP_NAME=Veterinaria El Zancudo
APP_VERSION=1.0.0
DEBUG=True

# Seguridad
SECRET_KEY=tu-clave-secreta-muy-segura
-2. Configurar Base de Datos
Edita Database/config.py con tu URL de conexión de Neon:
pythonDATABASE_URL = 'postgresql://tu_usuario:tu_contraseña@tu-host.neon.tech/tu_database?sslmode=require'
-3. Crear las tablas
bashpython -c "from Database.config import create_tables; create_tables()"
-4. Poblar datos iniciales (opcional)
bashpython Poblar.py
Esto creará:
Géneros (Macho, Hembra, Otro)
Tipos de animales (Perro, Gato, Ave)
Razas básicas
Servicios (Baño, Vacunas, Desparasitar)
Usuarios de prueba



🎮 Uso
-Opción 1: API REST (Recomendado)
Iniciar el servidor
bashpython Main_api.py
El servidor estará disponible en:

-API: http://localhost:8000
Documentación Swagger: http://localhost:8000/docs
ReDoc: http://localhost:8000/redoc

-Ejemplos de uso de la Apis

-Probar la API
bash# Healthcheck
curl http://localhost:8000/

-Listar usuarios
curl http://localhost:8000/usuarios/

-Crear usuario
curl -X POST http://localhost:8000/usuarios/ \
  -H "Content-Type: application/json" \
  -d '{
    "nombre": "Juan",
    "apellido": "Pérez",
    "email": "juan@example.com",
    "telefono": "123456789",
    "password": "password123",
    "es_admin": false
  }'

# Login
curl -X POST http://localhost:8000/autenticar/login \
  -H "Content-Type: application/json" \
  -d '{
    "email": "juan@example.com",
    "password": "password123"
  }'
Opción 2: Menú de Consola
bashpython Menu/menu_principal.py
Credenciales de prueba:

Email: kelvin@example.com
Contraseña: miClaveSegura


##📡 API Endpoints
|Autenticación|link                |funcionalidad|
|-------------|-------------------|-------------|
|POST  | /autenticar/login          |# Iniciar sesión|
|POST  | /autenticar/registro       |# Registrar nuevo usuario|

|Usuarios|link                |funcionalidad|
|-------------|-------------------|-------------|
|GET    |/usuarios/                 |# Listar todos los usuarios|
|GET    |/usuarios/{id}             |# Obtener usuario por ID|
|GET    |/usuarios/email/{email}    |# Obtener usuario por email|
|POST   |/usuarios/                 |# Crear nuevo usuario|
|PUT    |/usuarios/{id}             |# Actualizar usuario|
|DELETE |/usuarios/{id}             |# Eliminar usuario|
|GET    |/usuarios/admin/lista      |# Listar administradores|

|Animales|link                |funcionalidad|
|-------------|-------------------|-------------|
|GET    |/animales/                | # Listar animales|
|GET   |/animales/{id}             |# Obtener animal por ID|
|POST   |/animales/                | # Crear animal|
|PUT    |/animales/{id}            | # Actualizar animal|
|DELETE |/animales/{id}            | # Eliminar animal|
|GET    |/animales/propietario/{id}| # Animales por propietario|

|Servicios|link                |funcionalidad|
|-------------|-------------------|-------------|
|GET    |/servicios/               | # Listar servicios|
|GET    |/servicios/{id}           | # Obtener servicio por ID|
|POST   |/servicios/              |  # Crear servicio|
|PUT    |/servicios/{id}          |  # Actualizar servicio|
|DELETE |/servicios/{id}          |  # Eliminar servicio|

|Citas|link                |funcionalidad|
|-------------|-------------------|-------------|
|GET    |/citas/                  |  # Listar citas|
|GET   | /citas/{id}              |  # Obtener cita por ID|
|POST  | /citas/                   |# Crear cita|
|PUT   | /citas/{id}               |# Actualizar cita|
|DELETE| /citas/{id}                |# Eliminar cita|
|GET   | /citas/animal/{id}        | # Citas por animal|
|GET   | /citas/pendientes         | # Citas pendientes|

|Facturas|link                |funcionalidad|
|-------------|-------------------|-------------|
|GET   | /facturas/                | # Listar facturas|
|GET    |/facturas/{id}            | # Obtener factura por ID|
|POST  | /facturas/                | # Crear factura|
|PUT   | /facturas/{id}            | # Actualizar factura|
|DELETE | /facturas/{id}           |  # Eliminar factura|
|PATCH | /facturas/{id}/pagar      | # Marcar como pagada|
|GET   | /facturas/pendientes      | # Facturas pendientes|

|Tipos de Animales|link                |funcionalidad|
|-------------|-------------------|-------------|
|GET    |/tipoanimal/              |# Listar tipos|
|GET    |/tipoanimal/{id}         | # Obtener tipo por ID|
|POST  | /tipoanimal/             |  # Crear tipo|
|PUT    |/tipoanimal/{id}         |  # Actualizar tipo|
|DELETE | /tipoanimal/{id}         |  # Eliminar tipo|

|Razas|link                |funcionalidad|
|-------------|-------------------|-------------|
|GET    |/razas/                  |  # Listar razas|
|GET    |/razas/{id}              |  # Obtener raza por ID|
|GET    |/razas/tipo/{tipo_id}    | # Razas por tipo|
|POST   |/razas/                  |  # Crear raza|
|PUT    |/razas/{id}              |  # Actualizar raza|
|DELETE |/razas/{id}              |  # Eliminar raza|

🖥️ Menú de Consola
El sistema incluye una interfaz de consola interactiva con las siguientes características:
Sistema de Login

Autenticación con email y contraseña
3 intentos antes de bloquear acceso
Contraseña oculta durante escritura

Menús Disponibles

Gestión de Usuarios - CRUD completo
Gestión de Animales - Registro y seguimiento
Gestión de Citas - Programación de servicios
Gestión de Facturas - Control de pagos
Información del Sistema - Estadísticas

Características

✅ Interfaz amigable con emojis
✅ Validación de UUIDs
✅ Confirmación para acciones críticas
✅ Manejo robusto de errores
✅ Navegación intuitiva


## 📞 Soporte

Para reportar errores o solicitar nuevas características:

1. Verificar que el error no esté en la sección de solución de problemas
2. Proporcionar información detallada del error
3. Incluir pasos para reproducir el problema
4. Especificar sistema operativo y versión de Python

## 📄 Licencia

Este proyecto es desarrollado para uso interno de la Veterinaria El Zancudo.

## 🔄 Versiones



---

**🏥 Sistema de Gestión Veterinaria El Zancudo - v1.1.0**

