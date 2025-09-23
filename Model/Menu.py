import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Crud.Usuario_crud import login_usuario
from Entities.usuario import Usuario

# Importar los submenús
from Usuario import UsuarioMenu
from Animal import AnimalMenu
from Citas import CitasMenu
from factura import Factura
import uuid
import getpass

# Configuración de conexión a Neon (PostgreSQL)
DATABASE_URL = 'postgresql://neondb_owner:npg_MDXR0Zj6mzvY@ep-young-boat-ae7ls9d8-pooler.c-2.us-east-2.aws.neon.tech/neondb?sslmode=require&channel_binding=require'
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class MenuPrincipal:
    def __init__(self):
        self.db = SessionLocal()
        self.usuario_logueado = None
        
    def limpiar_pantalla(self):
        """Limpia la pantalla (funciona en Windows y Unix)"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def mostrar_banner(self):
        """Muestra el banner de bienvenida"""
        print("=" * 60)
        print("   🏥 SISTEMA DE GESTIÓN VETERINARIA EL ZANCUDO 🏥")
        print("=" * 60)
    
    def login(self):
        """Sistema de login con validación de usuario y contraseña"""
        self.limpiar_pantalla()
        self.mostrar_banner()
        print("\n🔐 INICIO DE SESIÓN")
        print("-" * 30)
        
        intentos = 3
        
        while intentos > 0:
            try:
                email = input("📧 Email: ").strip()
                if not email:
                    print("❌ El email no puede estar vacío.")
                    continue
                
                # Usar getpass para ocultar la contraseña
                password = getpass.getpass("🔑 Contraseña: ")
                if not password:
                    print("❌ La contraseña no puede estar vacía.")
                    continue
                
                # Intentar login
                usuario = login_usuario(self.db, email, password)
                
                if usuario:
                    self.usuario_logueado = usuario
                    self.limpiar_pantalla()
                    self.mostrar_banner()
                    print(f"✅ ¡Bienvenido(a), {usuario.nombre} {usuario.apellido}!")
                    print(f"📧 Email: {usuario.email}")
                    print(f"👤 Rol: {'Administrador' if usuario.es_admin else 'Usuario'}")
                    print("-" * 60)
                    input("\nPresiona Enter para continuar...")
                    return True
                else:
                    intentos -= 1
                    if intentos > 0:
                        print(f"❌ Credenciales incorrectas. Te quedan {intentos} intento(s).")
                        print()
                    else:
                        print("❌ Se agotaron los intentos. Cerrando sistema...")
                        return False
                        
            except KeyboardInterrupt:
                print("\n\n👋 Saliendo del sistema...")
                return False
            except Exception as e:
                print(f"❌ Error durante el login: {e}")
                intentos -= 1
                if intentos == 0:
                    return False
        
        return False
    
    def mostrar_info_usuario(self):
        """Muestra información del usuario logueado"""
        if self.usuario_logueado:
            print(f"👤 Usuario: {self.usuario_logueado.nombre} {self.usuario_logueado.apellido}")
            print(f"📧 Email: {self.usuario_logueado.email}")
            print(f"🔑 Rol: {'Administrador' if self.usuario_logueado.es_admin else 'Usuario'}")
    
    def menu_principal(self):
        """Muestra el menú principal con los submenús"""
        while True:
            try:
                self.limpiar_pantalla()
                self.mostrar_banner()
                self.mostrar_info_usuario()
                print("-" * 60)
                print("\n🏠 MENÚ PRINCIPAL")
                print("-" * 20)
                print("1. 👥 Gestión de Usuarios")
                print("2. 🐕 Gestión de Animales") 
                print("3. 📅 Gestión de Citas")
                print("4. 💰 Gestión de Facturas")
                print("5. ℹ️  Información del Sistema")
                print("6. 🔄 Cambiar de Usuario")
                print("0. 🚪 Salir del Sistema")
                print("-" * 60)
                
                opcion = input("Seleccione una opción (0-6): ").strip()
                
                if opcion == "1":
                    self.abrir_submenu_usuarios()
                elif opcion == "2":
                    self.abrir_submenu_animales()
                elif opcion == "3":
                    self.abrir_submenu_citas()
                elif opcion == "4":
                    self.abrir_submenu_facturas()
                elif opcion == "5":
                    self.mostrar_info_sistema()
                elif opcion == "6":
                    if self.confirmar_accion("¿Desea cambiar de usuario?"):
                        return self.iniciar_sistema()
                elif opcion == "0":
                    if self.confirmar_accion("¿Está seguro que desea salir del sistema?"):
                        self.cerrar_sistema()
                        break
                else:
                    print("❌ Opción no válida. Seleccione un número entre 0 y 6.")
                    input("Presiona Enter para continuar...")
                    
            except KeyboardInterrupt:
                print("\n\n👋 Cerrando sistema...")
                break
            except Exception as e:
                print(f"❌ Error en el menú principal: {e}")
                input("Presiona Enter para continuar...")
    
    def confirmar_accion(self, mensaje):
        """Pide confirmación para acciones importantes"""
        while True:
            respuesta = input(f"{mensaje} (s/n): ").strip().lower()
            if respuesta in ['s', 'si', 'sí', 'y', 'yes']:
                return True
            elif respuesta in ['n', 'no']:
                return False
            else:
                print("❌ Responda 's' para sí o 'n' para no.")
    
    def abrir_submenu_usuarios(self):
        """Abre el submenú de usuarios"""
        try:
            print("\n🔄 Cargando menú de usuarios...")
            submenu = UsuarioMenu()
            submenu.menu()
        except Exception as e:
            print(f"❌ Error al abrir menú de usuarios: {e}")
            input("Presiona Enter para continuar...")
    
    def abrir_submenu_animales(self):
        """Abre el submenú de animales"""
        try:
            print("\n🔄 Cargando menú de animales...")
            submenu = AnimalMenu()
            submenu.menu()
        except Exception as e:
            print(f"❌ Error al abrir menú de animales: {e}")
            input("Presiona Enter para continuar...")
    
    def abrir_submenu_citas(self):
        """Abre el submenú de citas"""
        try:
            print("\n🔄 Cargando menú de citas...")
            submenu = CitasMenu()
            submenu.menu()
        except Exception as e:
            print(f"❌ Error al abrir menú de citas: {e}")
            input("Presiona Enter para continuar...")
    
    def abrir_submenu_facturas(self):
        """Abre el submenú de facturas"""
        try:
            print("\n🔄 Cargando menú de facturas...")
            submenu = Factura()
            submenu.menu()
        except Exception as e:
            print(f"❌ Error al abrir menú de facturas: {e}")
            input("Presiona Enter para continuar...")
    
    def mostrar_info_sistema(self):
        """Muestra información del sistema"""
        self.limpiar_pantalla()
        self.mostrar_banner()
        print("\n📊 INFORMACIÓN DEL SISTEMA")
        print("-" * 40)
        
        try:
            # Estadísticas básicas
            total_usuarios = self.db.query(Usuario).count()
            
            print(f"👥 Total de usuarios registrados: {total_usuarios}")
            print(f"🗄️  Base de datos: PostgreSQL (Neon)")
            print(f"🔗 Estado de conexión: ✅ Conectado")
            print(f"👤 Usuario actual: {self.usuario_logueado.nombre} {self.usuario_logueado.apellido}")
            print(f"📧 Email: {self.usuario_logueado.email}")
            print(f"🔑 Permisos: {'Administrador' if self.usuario_logueado.es_admin else 'Usuario estándar'}")
            
            # Información adicional del sistema
            print("\n🛠️ MÓDULOS DISPONIBLES:")
            print("  • Gestión de Usuarios")
            print("  • Gestión de Animales")
            print("  • Gestión de Citas")
            print("  • Gestión de Facturas")
            
            print("\n📋 VERSIÓN DEL SISTEMA:")
            print("  • Versión: 1.0.0")
            print("  • Desarrollado por: Equipo ITM")
            print("  • Veterinaria: El Zancudo")
            
        except Exception as e:
            print(f"❌ Error al obtener información del sistema: {e}")
        
        print("-" * 40)
        input("\nPresiona Enter para volver al menú principal...")
    
    def cerrar_sistema(self):
        """Cierra el sistema correctamente"""
        try:
            self.db.close()
            self.limpiar_pantalla()
            self.mostrar_banner()
            print("\n👋 ¡Gracias por usar el Sistema de Gestión Veterinaria!")
            print(f"   Usuario: {self.usuario_logueado.nombre} {self.usuario_logueado.apellido}")
            print("   Sesión cerrada correctamente.")
            print("\n🏥 ¡Que tengas un excelente día! 🏥")
            print("=" * 60)
        except Exception as e:
            print(f"❌ Error al cerrar el sistema: {e}")
    
    def iniciar_sistema(self):
        """Inicia todo el sistema"""
        try:
            # Mostrar pantalla de bienvenida
            self.limpiar_pantalla()
            self.mostrar_banner()
            print("\n🚀 Iniciando sistema...")
            print("🔌 Conectando a la base de datos...")
            
            # Verificar conexión a BD
            try:
                self.db.query(Usuario).first()
                print("✅ Conexión establecida correctamente")
            except Exception as e:
                print(f"❌ Error de conexión a la base de datos: {e}")
                input("Presiona Enter para salir...")
                return False
            
            # Proceso de login
            if self.login():
                # Si login exitoso, mostrar menú principal
                self.menu_principal()
                return True
            else:
                print("❌ No se pudo iniciar sesión. Cerrando sistema...")
                return False
                
        except Exception as e:
            print(f"❌ Error crítico al iniciar el sistema: {e}")
            input("Presiona Enter para salir...")
            return False

def main():
    """Función principal con mejor manejo de errores"""
    try:
        # Verificar variables de entorno
        if not os.getenv('DATABASE_URL'):
            print("❌ Error: No se encontró DATABASE_URL en variables de entorno")
            print("📋 Crea un archivo .env con la configuración de la base de datos")
            return
        
        sistema = MenuPrincipal()
        sistema.iniciar_sistema()
        
    except KeyboardInterrupt:
        print("\n\n👋 Sistema cerrado por el usuario.")
    except Exception as e:
        print(f"❌ Error crítico: {e}")
        print("📋 Verifica la conexión a internet y la configuración de la base de datos")
    finally:
        print("\n🔚 Fin del programa.")
if __name__ == "__main__":
    main()