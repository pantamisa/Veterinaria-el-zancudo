# 🏥 Sistema de Gestión Veterinaria El Zancudo

Un sistema completo de gestión para clínicas veterinarias desarrollado en Python con interfaz de línea de comandos.

## 📋 Características

- **Gestión de Usuarios**: Registro, edición y administración de usuarios del sistema
- **Gestión de Animales**: Control completo de mascotas y sus datos
- **Gestión de Citas**: Programación y seguimiento de citas veterinarias
- **Gestión de Facturas**: Sistema de facturación integrado
- **Sistema de Roles**: Diferenciación entre administradores y usuarios estándar
- **Interfaz Intuitiva**: Menús claros con iconos y navegación fácil

## 🛠️ Tecnologías Utilizadas

- **Python 3.x**: Lenguaje de programación principal
- **SQLAlchemy**: ORM para manejo de base de datos
- **PostgreSQL**: Base de datos (Neon Cloud)
- **getpass**: Para manejo seguro de contraseñas
- **os/sys**: Para funcionalidades del sistema operativo

## 📦 Estructura del Proyecto

```
proyecto/
├── main.py                 # Archivo principal del sistema
├── Entities/               # Entidades del sistema
│   └── usuario.py         # Modelo de usuario
├── Crud/                  # Operaciones CRUD
│   └── Usuario_crud.py    # CRUD de usuarios
├── Usuario.py             # Menú de gestión de usuarios
├── Animal.py              # Menú de gestión de animales
├── Citas.py               # Menú de gestión de citas
├── factura.py             # Menú de gestión de facturas
└── README.md              # Este archivo
```

## 🚀 Instalación

### Prerrequisitos

- Python 3.7 o superior
- pip (gestor de paquetes de Python)
- Conexión a internet (para la base de datos)

### Pasos de Instalación

1. **Clonar o descargar el proyecto**
   ```bash
   git clone [URL_DEL_REPOSITORIO]
   cd sistema-veterinaria-el-zancudo
   ```

2. **Instalar dependencias**
   ```bash
   pip install sqlalchemy psycopg2-binary
   ```

3. **Configurar variables de entorno (opcional)**
   Crear un archivo `.env` en la raíz del proyecto:
   ```env
   DATABASE_URL=postgresql://neondb_owner:npg_MDXR0Zj6mzvY@ep-young-boat-ae7ls9d8-pooler.c-2.us-east-2.aws.neon.tech/neondb?sslmode=require&channel_binding=require
   ```

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

## ⚠️ Solución de Problemas

### Error de Conexión a Base de Datos
```
❌ Error de conexión a la base de datos
```
**Solución**: Verificar conexión a internet y validez de la URL de base de datos.

### Módulo No Encontrado
```
ModuleNotFoundError: No module named 'sqlalchemy'
```
**Solución**: Instalar dependencias con `pip install sqlalchemy psycopg2-binary`

### Error de Importación
```
ImportError: cannot import name 'X' from 'Y'
```
**Solución**: Verificar que todos los archivos del proyecto estén presentes y la estructura sea correcta.

## 📞 Soporte

Para reportar errores o solicitar nuevas características:

1. Verificar que el error no esté en la sección de solución de problemas
2. Proporcionar información detallada del error
3. Incluir pasos para reproducir el problema
4. Especificar sistema operativo y versión de Python

## 👥 Contribuidores

- **Equipo ITM**: Desarrollo principal del sistema
- **Veterinaria El Zancudo**: Especificaciones y pruebas

## 📄 Licencia

Este proyecto es desarrollado para uso interno de la Veterinaria El Zancudo.

## 🔄 Versiones

### v1.0.0 (Actual)
- ✅ Sistema de login con validación
- ✅ Menú principal con navegación
- ✅ Gestión básica de usuarios
- ✅ Interfaz de línea de comandos mejorada
- ✅ Conexión a base de datos PostgreSQL
- ✅ Sistema de roles y permisos

### Próximas Versiones
- 🔲 Reportes avanzados
- 🔲 Backup automático de datos
- 🔲 Interfaz web (opcional)
- 🔲 Notificaciones por email
- 🔲 Integración con sistemas de pago

---

**🏥 Sistema de Gestión Veterinaria El Zancudo - v1.0.0**

*Desarrollado con ❤️ por el Equipo ITM*