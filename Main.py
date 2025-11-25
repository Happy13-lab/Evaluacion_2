import bcrypt
from confing.db_config import ConexionOracle, validar_tablas
from Model.Personas_M import UsuarioModel,PacienteModel,MedicoModel
from Model.Objetos_M import RecetasModel,AgendaModel,InsumoModel,ConsultasModel
from Controller.Objetos_C import RecetasController, ConsultasController,InsumoController,AgendaController
from Controller.Personas_C import UsuarioController,PacienteController,MedicoController
from View.Objetos_v import RecetasView,AgendaView,ConsultaView,InsumoView
from View.Persona_v import UsuarioView,PacienteView,MedicoView


def conectarBD():

    Conexion = ConexionOracle("system", "Ina.2025", "localhost:1521/xe")
    Conexion.conectar()

    validar_tablas(Conexion)

    return Conexion

def main():
    conexion = conectarBD()

    print("Inicio de sesión, ingrese sus credenciales\n")
    usuario = str(input("Ingrese su nombre de usuario: "))
    clave = str(input("Ingrese su clave: "))
    clave = bytes(clave, encoding="utf-8")

    salt = bcrypt.gensalt()
    clave_encriptada = bcrypt.hashpw(clave, salt)
    clave_encriptada = clave_encriptada.decode(encoding="utf-8")

    cursor = conexion.obtener_cursor()

    consulta = "insert into usuarios (nombre_usuario, clave) values (:1, :2)"
    cursor.execute(consulta, (usuario, clave_encriptada,))
    conexion.connection.commit()

    usuario = str(input("Ingrese su nombre de usuario: "))
    clave = str(input("Ingrese su clave: "))

    consulta = "select clave from usuarios where nombre_usuario = :1"
    cursor.execute(consulta, (usuario,))
    clave_bd = cursor.fetchone()
    clave_bytes = bytes(clave, encoding="utf-8")
    clave_test = bytes(clave_bd[0], encoding="utf-8",)

    validacion_clave = bcrypt.checkpw(clave_bytes, clave_test)

    if validacion_clave:
        print("Ingreso correcto")
    else:
        print("Credenciales incorrectas")

    conexion.desconectar()

if __name__ == "__main__":
    main()