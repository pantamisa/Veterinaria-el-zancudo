# 🐾 Veterinaria "El Zancudo"  

Este es un proyecto en **Python** que simula la gestión de una veterinaria.  
Permite manejar animales, agendar y atender citas, así como facturar los servicios realizados.  

---

## 📦 Requisitos previos  

- Python **3.10** o superior (recomendado por el uso de `match-case`).  
- Tener todos los módulos en el mismo directorio del proyecto:  
  - `Menu.py`  
  - `Manejo_animales.py`  
  - `Servicios.py`  
  - `factura.py`  
  - `Animal.py`  

---

## ▶️ Ejecución  

1. Abre una terminal en la carpeta del proyecto.  
2. Ejecuta el archivo principal:  

   ```bash
   python Menu.py
   ```

3. Se mostrará el menú principal de la aplicación.  

---

## 📋 Menú principal  

Al iniciar, verás:  

```
--Veterinaria EL Zancudo--
--------------------------
MENU DE APLICACION
1. manejo animales
2. manejo cita
3. pagar facturas
0. Salir programa
ingrese una opcion
```

---

## 🐶 Submenú de manejo de animales  

Opción `1` del menú principal.  

```
---sub-menu animales---
1. Crear
2. Eliminar
3. Buscar
0. Salir sub-menu
```

### 🔹 Crear animal  
- Solicita los datos básicos (edad, nombre, dueño, género, tipo).  
- Según el tipo (`P`, `G`, `A`) se piden datos adicionales:  
  - `P` → raza del perro  
  - `G` → raza del gato  
  - `A` → tipo de ave  

👉 Ejemplo de flujo:  
```
Ingrese la edad: 5
Ingrese el nombre: Juan
Ingrese el nombre dueño: Pedro
Ingrese el genero del animal: macho
Ingrese el tipo de la mascota:
 P-perro G-gato  A-ave
:P
Raza del perro: Labrador
Animal Juan agregado con éxito.
```

### 🔹 Eliminar animal  
Solicita el nombre del animal y lo elimina si existe.  

### 🔹 Buscar animal  
Muestra la información del animal según el nombre ingresado.  

---

## 📅 Submenú de manejo de citas  

Opción `2` del menú principal.  

```
---sub menu citas---
1. Agendar cita
2. Atender cita
0. Salir menu principal
```

### 🔹 Agendar cita  
- Pide el nombre del animal.  
- Si existe, se agenda una cita.  
- Si no existe, solicita crear el animal primero.  

### 🔹 Atender cita  
- Atiende la primera cita en la cola.  
- Al atender, se asigna un servicio al animal (ejemplo: Vacunar).  
- Ese servicio queda registrado en la **factura del animal**.  

---

## 💳 Facturación  

Opción `3` del menú principal.  

```
pasarela de pago....
Ingrese el nombre del animal que tiene la factura:
```

- Se busca al animal.  
- Si tiene servicios registrados, se muestra la factura:  

```
📄 Factura de Juan:
- Vacunar: $20000
➡ Total: $20000
```

- Si no tiene servicios registrados:  

```
⚠ No hay servicios registrados para Juan
```

---

## ❌ Salir  

Opción `0` en cualquier menú → regresa al menú anterior o cierra el programa.  

---

## 📂 Estructura recomendada del proyecto  
