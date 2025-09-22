from Crud.Usuario_crud import create_usuario, get_usuario, update_usuario, delete_usuario, login_usuario

# ============================
# Submenú Usuarios
# ============================
def menu_usuarios(db):
    while True:
        print("\n===== SUBMENÚ USUARIOS =====")
        print("1. Crear Usuario")
        print("2. Consultar Usuario por ID")
        print("3. Actualizar Usuario")
        print("4. Eliminar Usuario")
        print("5. Login de Usuario")
        print("0. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            email = input("Email: ")
            telefono = input("Teléfono: ")
            password = input("Contraseña: ")
            usuario = create_usuario(db, nombre, apellido, email, telefono, password)
            print("✅ Usuario creado:", usuario)

        elif opcion == "2":
            id_usuario = input("ID del usuario: ")
            usuario = get_usuario(db, id_usuario)
            print("✅ Usuario:", usuario if usuario else "❌ No encontrado")

        elif opcion == "3":
            id_usuario = input("ID del usuario a actualizar: ")
            campo = input("Campo a actualizar (nombre, apellido, email, telefono, password): ")
            valor = input("Nuevo valor: ")
            usuario = update_usuario(db, id_usuario, **{campo: valor})
            print("✅ Usuario actualizado:", usuario if usuario else "❌ No encontrado")

        elif opcion == "4":
            id_usuario = input("ID del usuario a eliminar: ")
            eliminado = delete_usuario(db, id_usuario)
            print("✅ Eliminado" if eliminado else "❌ No encontrado")

        elif opcion == "5":
            email = input("Email: ")
            password = input("Contraseña: ")
            usuario = login_usuario(db, email, password)
            print("✅ Login exitoso:", usuario if usuario else "❌ Credenciales inválidas")

        elif opcion == "0":
            break
        else:
            print("⚠️ Opción inválida")
