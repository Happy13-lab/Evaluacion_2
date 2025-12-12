# import bcrypt
# from config.db_config import ConexionOracle, validar_tablas
# from Model.Personas_M import UsuarioModel,PacienteModel,MedicoModel, AdministradorModel
# from Model.Objetos_M import RecetasModel,AgendaModel,InsumoModel,ConsultasModel
# from Controller.Objetos_C import RecetasController, ConsultasController,InsumoController,AgendaController
# from Controller.Personas_C import UsuarioController,PacienteController,MedicoController, AdministradorModel
# from View.Objetos_v import RecetasView,AgendaView,ConsultaView,InsumoView
# from View.Persona_v import UsuarioView,PacienteView,MedicoView
# from datetime import date, datetime
# import json



# def conectarBD():

#     Conexion = ConexionOracle("system", "vicencio0195", "localhost:1521/xe")
#     Conexion.conectar()

#     validar_tablas(Conexion)

#     return Conexion

    
# def main():
#     conexion = conectarBD()
    
    
#     modelo_usuario = UsuarioModel(0, "", "", "", "", date.today(), 0, "", "", conexion)
#     usuario_controller = UsuarioController(modelo_usuario)
    

#     print("BIENVENIDO A MEDIPLUS")
#     #Implementado json
#     def importar_usuarios_desde_json():
#     # Instancia del modelo y controlador
#     modelo = UsuarioModel()
#     controller = UsuarioController(modelo)

#     # Leer el archivo JSON
#     with open("users.json", "r", encoding="utf-8") as f:
#         data = json.load(f)

#     for u in data:
#         # Generar contraseña temporal y hashearla
#         clave_hash = bcrypt.hashpw("claveTemporal123".encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

#         # Registrar usuario usando tu controlador
#         controller.registrar_usuario(
#             id=u["id"],
#             nombre_usuario=u["username"],
#             clave=clave_hash,
#             nombre=u["name"],
#             apellido="",  # tu JSON no trae apellido separado
#             fecha_nacimiento=None,  # no está en el JSON
#             telefono=u["phone"],
#             email=u["email"],
#             tipo="usuario"
#         )





#     # print("Registro de usuario\n")
#     # id = int(input("Ingrese ID: "))
#     # nombre_usuario = input("Ingrese nombre de usuario: ")
#     # clave = input("Ingrese clave: ")
#     # nombre = input("Ingrese nombre: ")
#     # apellido = input("Ingrese apellido: ")
#     # fecha_str = date(input("Ingrese fecha de nacimiento (YYYY-MM-DD): "))

#     # ## CONVERTIMOS LA FECHA DE STRING A DATE
#     # fecha_nacimiento = datetime.strptime (fecha_str, "%y-%m-%d").date()
#     # telefono = int(input("Ingrese teléfono: "))
#     # email = input("Ingrese email: ")
#     # tipo = input("Ingrese tipo de usuario: ")





#     usuario_controller.registrar_usuario(id, nombre_usuario, clave, nombre, apellido,
#                                          fecha_nacimiento, telefono, email, tipo)

#     print("\nInicio de sesión\n")
#     nombre_usuario = input("Ingrese nombre de usuario: ")
#     clave = input("Ingrese clave: ")

#     usuario_controller.validar(nombre_usuario, clave)

#     conexion.desconectar()

# if __name__ == "__main__":
#     main()


import bcrypt
import json 
import sys
from datetime import date, datetime
from config.db_config import ConexionOracle, validar_tablas
from Model.Personas_M import UsuarioModel, PacienteModel, MedicoModel, AdministradorModel
from Model.Objetos_M import RecetasModel, AgendaModel, InsumoModel, ConsultasModel
from Controller.Objetos_C import RecetasController, ConsultasController, InsumoController, AgendaController
from Controller.Personas_C import UsuarioController, PacienteController, MedicoController, AdministradorController
from View.Objetos_v import RecetasView, AgendaView, ConsultaView, InsumoView
from View.Persona_v import UsuarioView, PacienteView, MedicoView, AdministradorView

# Tasa de cambio simulada para el requisito de CLP
TASA_CAMBIO_CLP = 950 # 1 USD = 950 CLP (ejemplo)

# --- INICIALIZACIÓN DE LA APLICACIÓN ---

def conectar_bd():
    """
    Establece la conexión a la base de datos Oracle y valida las tablas.
    """
    
    conexion = ConexionOracle("system", "vicencio0195", "localhost:1521/xe")
    conexion.conectar()
    if conexion.connection:
        validar_tablas(conexion)
        return conexion
    return None

def setup_dependencies(conexion):
    """
    Instancia todos los Modelos, Controladores y Vistas.
    """
    # Instanciación de Modelos 
    # Los argumentos iniciales (0, "", etc.) son solo para inicializar el objeto.
    m_usuario = UsuarioModel(0, "", "", "", "", date.today(), 0, "", "", conexion)
    m_paciente = PacienteModel(id=0, nombre_usuario="", clave="", nombre="", apellido="", fecha_nacimiento=date.today(),telefono=0, email="", tipo="", conexion=conexion, comuna="", fecha_primera_visita=date.today())
    m_medico = MedicoModel(id=0, nombre_usuario="", clave="", nombre="", apellido="", fecha_nacimiento=date.today(),telefono=0, email="", tipo="", conexion=conexion,especialidad="", id_medico=0, horario_ingreso=datetime.now(),fecha_ingreso=date.today())
    m_admin = AdministradorModel(0, "", "", "", "", date.today(), 0, "", "", conexion)
    m_insumo = InsumoModel(0, "", "", 0, 0.0, conexion)
    m_receta = RecetasModel(id=0, id_paciente=0, id_medico=0, descripcion="", medicamentos_recetados="", costo_clp=0, conexion=conexion)
    m_consulta = ConsultasModel(id=0, id_paciente=0, id_medico=0, id_receta=0, fecha=date.today(), comentarios="", valor=0, conexion=conexion)
    m_agenda = AgendaModel(id=0, id_paciente=0, id_medico=0, fecha_consulta=date.today(), estado="",conexion=conexion)

    # Instanciación de Controladores
    c_usuario = UsuarioController(m_usuario)
    c_paciente = PacienteController(m_paciente)
    c_medico = MedicoController(m_medico)
    c_admin = AdministradorController(m_admin)
    c_insumo = InsumoController(m_insumo, TASA_CAMBIO_CLP) 
    c_receta = RecetasController(m_receta)
    c_consulta = ConsultasController(m_consulta)
    c_agenda = AgendaController(m_agenda)
    
    # Las Vistas no necesitan instanciación (son estáticas)
    vistas = {
        'Usuario': UsuarioView, 'Paciente': PacienteView, 'Medico': MedicoView, 'Admin': AdministradorView,
        'Insumo': InsumoView, 'Receta': RecetasView, 'Agenda': AgendaView, 'Consulta': ConsultaView
    }

    # Retornar un diccionario o tupla con todos los componentes
    return {
        'controllers': {'usuario': c_usuario, 'paciente': c_paciente, 'medico': c_medico, 'admin': c_admin, 'insumo': c_insumo},
        'vistas': vistas
    }

def importar_usuarios_desde_json(usuario_controller, admin_controller):
    """
    Carga usuarios iniciales (y un administrador por defecto) desde el JSON.
    """
    # 1. Crear un Administrador por defecto (si no existe)
    # Esto asegura que siempre haya un usuario de tipo 'Administrador'
    # La clave debe ser hasheada por el controlador!
    print("\n[INFO]: Asegurando existencia de Administrador por defecto...")
    usuario_controller.registrar_usuario(
        id=1,
        nombre_usuario="admin",
        clave="admin123", # El controlador DEBE hashear esto
        nombre="Super",
        apellido="Admin",
        fecha_nacimiento=date(1990, 1, 1),
        telefono=900000000,
        email="admin@mediplus.cl",
        tipo="Administrador"
    )

    # 2. Importar usuarios del JSON
    try:
        with open("users.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            
        print("[INFO]: Importando usuarios desde users.json...")

        for u in data:
            # Usar un ID mayor para evitar colisión con el admin por defecto
            user_id = u["id"] + 100 
            
            # Usar clave temporal, el controlador la hashea.
            usuario_controller.registrar_usuario(
                id=user_id,
                nombre_usuario=u["username"],
                clave="temp" + str(user_id), # Clave temporal para usuarios importados
                nombre=u["name"],
                apellido=u.get("surname", "N/A"),
                fecha_nacimiento=date(2000, 1, 1), # Fecha por defecto
                telefono=u["phone"],
                email=u["email"],
                tipo="Paciente" # Asignamos un tipo por defecto, ejemplo: Paciente
            )
        print("[INFO]: Importación de usuarios finalizada.")

    except FileNotFoundError:
        print("[ADVERTENCIA]: El archivo 'users.json' no se encontró. Omite la importación.")
    except Exception as e:
        print(f"[ERROR]: Ocurrió un error durante la importación: {e}")

def menu_principal(controllers, vistas, usuario_autenticado):
    """
    Muestra el menú principal según el tipo de usuario.
    """
    tipo_usuario = usuario_autenticado['tipo']
    nombre = usuario_autenticado['nombre']
    
    print(f"\n--- BIENVENIDO {nombre.upper()} ({tipo_usuario}) ---")
    
    if tipo_usuario == 'Administrador':
        # Menú del Administrador
        print("\n** MENÚ ADMINISTRADOR **")
        print("1. Gestión de Usuarios (CRUD de Médicos/Pacientes)")
        print("2. Gestión de Insumos (CRUD)")
        print("3. Editar mi Perfil")
        print("4. Cerrar Sesión")
        # Aquí se implementaría la lógica de sub-menús llamando a los Controladores/Vistas

    elif tipo_usuario == 'Medico':
        # Menú del Médico
        print("\n** MENÚ MÉDICO **")
        print("1. Ver Agenda de Consultas")
        print("2. Registrar Receta/Consulta (a Paciente)")
        print("3. Ver Historial de Pacientes")
        print("4. Editar mi Perfil")
        print("5. Cerrar Sesión")

    elif tipo_usuario == 'Paciente':
        # Menú del Paciente
        print("\n** MENÚ PACIENTE **")
        print("1. Solicitar Hora Médica (Agenda)")
        print("2. Ver Próximas Consultas")
        print("3. Ver Historial Médico (Recetas/Consultas)")
        print("4. Editar mi Perfil")
        print("5. Cerrar Sesión")
    
    # ... (La lógica de lectura de input y dispatching de funciones iría aquí)
    # Por ejemplo, si el admin elige 2, llamar a: gestion_insumos(controllers, vistas)

def menu_login(usuario_controller):
    """
    Maneja el inicio de sesión y devuelve el usuario autenticado.
    """
    print("\n--- INICIO DE SESIÓN ---")
    while True:
        nombre_usuario = input("Ingrese nombre de usuario: ")
        clave = input("Ingrese clave: ")
        
        # El controlador.validar debe devolver el diccionario del usuario autenticado si es exitoso
        usuario = usuario_controller.validar(nombre_usuario, clave) 
        
        if usuario:
            print("\n[ÉXITO]: Sesión iniciada correctamente.")
            return usuario
        else:
            print("[ERROR]: Nombre de usuario o clave incorrectos. Intente de nuevo.")
            opcion = input("¿Desea intentarlo de nuevo (s/n)?: ").lower()
            if opcion != 's':
                return None

def main():
    print("BIENVENIDO AL SISTEMA MEDIPLUS")
    
    # 1. Conexión e Inicialización de BD
    conexion = conectar_bd()
    if not conexion:
        print("[FATAL]: No se pudo establecer conexión con la BD. Saliendo.")
        sys.exit(1)
        
    # 2. Instanciación de Dependencias (Modelos, Controladores, Vistas)
    dependencias = setup_dependencies(conexion)
    usuario_controller = dependencias['controllers']['usuario']
    
    # 3. Importación de Usuarios (Solo se hace una vez)
    # Esto es útil para poblar la BD en el primer inicio.
    importar_usuarios_desde_json(usuario_controller, dependencias['controllers']['admin'])
    
    # 4. Flujo de Login
    usuario_autenticado = menu_login(usuario_controller)
    
    # 5. Menú Principal (si el login es exitoso)
    if usuario_autenticado:
        menu_principal(dependencias['controllers'], dependencias['vistas'], usuario_autenticado)

    # 6. Desconexión
    conexion.desconectar()

if __name__ == '__main__':
    main()
    