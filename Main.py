import bcrypt
from confing.db_config import ConexionOracle, validar_tablas
from Model.Personas_M import UsuarioModel,PacienteModel,MedicoModel, AdministradorModel
from Model.Objetos_M import RecetasModel,AgendaModel,InsumoModel,ConsultasModel
from Controller.Objetos_C import RecetasController, ConsultasController,InsumoController,AgendaController
from Controller.Personas_C import UsuarioController,PacienteController,MedicoController, AdministradorModel
from View.Objetos_v import RecetasView,AgendaView,ConsultaView,InsumoView
from View.Persona_v import UsuarioView,PacienteView,MedicoView
from datetime import date, datetime


def conectarBD():

    Conexion = ConexionOracle("system", "vicencio0195", "localhost:1521/xe")
    Conexion.conectar()

    validar_tablas(Conexion)

    return Conexion

    
def main():
    conexion = conectarBD()
    
    
    modelo_usuario = UsuarioModel(0, "", "", "", "", date.today(), 0, "", "", conexion)
    usuario_controller = UsuarioController(modelo_usuario)
    

    print("BIENVENIDO A MEDIPLUS")
    #Implementado json
    def importar_usuarios_desde_json():
    # Instancia del modelo y controlador
    modelo = UsuarioModel()
    controller = UsuarioController(modelo)

    # Leer el archivo JSON
    with open("users.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    for u in data:
        # Generar contraseña temporal y hashearla
        clave_hash = bcrypt.hashpw("claveTemporal123".encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

        # Registrar usuario usando tu controlador
        controller.registrar_usuario(
            id=u["id"],
            nombre_usuario=u["username"],
            clave=clave_hash,
            nombre=u["name"],
            apellido="",  # tu JSON no trae apellido separado
            fecha_nacimiento=None,  # no está en el JSON
            telefono=u["phone"],
            email=u["email"],
            tipo="usuario"
        )


    # print("Registro de usuario\n")
    # id = int(input("Ingrese ID: "))
    # nombre_usuario = input("Ingrese nombre de usuario: ")
    # clave = input("Ingrese clave: ")
    # nombre = input("Ingrese nombre: ")
    # apellido = input("Ingrese apellido: ")
    # fecha_str = date(input("Ingrese fecha de nacimiento (YYYY-MM-DD): "))

    # ## CONVERTIMOS LA FECHA DE STRING A DATE
    # fecha_nacimiento = datetime.strptime (fecha_str, "%y-%m-%d").date()
    # telefono = int(input("Ingrese teléfono: "))
    # email = input("Ingrese email: ")
    # tipo = input("Ingrese tipo de usuario: ")

    usuario_controller.registrar_usuario(id, nombre_usuario, clave, nombre, apellido,
                                         fecha_nacimiento, telefono, email, tipo)

    print("\nInicio de sesión\n")
    nombre_usuario = input("Ingrese nombre de usuario: ")
    clave = input("Ingrese clave: ")

    usuario_controller.validar(nombre_usuario, clave)

    conexion.desconectar()

if __name__ == "__main__":
    main()