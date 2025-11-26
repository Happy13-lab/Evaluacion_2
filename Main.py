import bcrypt
from confing.db_config import ConexionOracle, validar_tablas
from Model.Personas_M import UsuarioModel,PacienteModel,MedicoModel
from Model.Objetos_M import RecetasModel,AgendaModel,InsumoModel,ConsultasModel
from Controller.Objetos_C import RecetasController, ConsultasController,InsumoController,AgendaController
from Controller.Personas_C import UsuarioController,PacienteController,MedicoController
from View.Objetos_v import RecetasView,AgendaView,ConsultaView,InsumoView
from View.Persona_v import UsuarioView,PacienteView,MedicoView
from datetime import date


def conectarBD():

    Conexion = ConexionOracle("system", "Ina.2025", "localhost:1521/xe")
    Conexion.conectar()

    validar_tablas(Conexion)

    return Conexion

def main():
    conexion = conectarBD()

    
def main():
    conexion = ConexionOracle()
    
    modelo_usuario = UsuarioModel(0, "", "", "", "", date.today(), 0, "", "", conexion)
    usuario_controller = UsuarioController(modelo_usuario)
    
    print("Registro de usuario\n")
    id = int(input("Ingrese ID: "))
    nombre_usuario = input("Ingrese nombre de usuario: ")
    clave = input("Ingrese clave: ")
    nombre = input("Ingrese nombre: ")
    apellido = input("Ingrese apellido: ")
    fecha_nacimiento = date(input("Ingrese fecha de nacimiento (YYYY-MM-DD): "))
    telefono = int(input("Ingrese teléfono: "))
    email = input("Ingrese email: ")
    tipo = input("Ingrese tipo de usuario: ")

    usuario_controller.registrar_usuario(id, nombre_usuario, clave, nombre, apellido,
                                         fecha_nacimiento, telefono, email, tipo)

    print("\nInicio de sesión\n")
    nombre_usuario = input("Ingrese nombre de usuario: ")
    clave = input("Ingrese clave: ")

    usuario_controller.validar(nombre_usuario, clave)

    conexion.desconectar()

if __name__ == "__main__":
    main()