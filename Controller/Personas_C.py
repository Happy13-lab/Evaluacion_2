import re
from datetime import date,time
from Model.Personas_M import UsuarioModel,PacienteModel,MedicoModel, AdministradorModel
import bcrypt

SUS_KEYS = [
    r";", r"--", r"/\*", r"\bOR\b", r"\bAND\b", r"\bUNION\b",
    r"\bSELECT\b", r"\bINSERT\b", r"\bUPDATE\b", r"\bDELETE\b",
    r"\bDROP\b", r"\bEXEC\b"
]

patron = re.compile("|".join(SUS_KEYS), re.IGNORECASE)

class UsuarioController:

    def __init__(self, Modelo: UsuarioModel):
        self.Modelo = Modelo

    def registrar_usuario(self,id: int, nombre_usuario: str, clave: str, nombre: str, apellido: str, fecha_nacimiento: date, telefono: int, email: str, tipo: str) -> bool:

        if not id or not nombre_usuario or not clave or not nombre or not apellido or not fecha_nacimiento or not telefono or not email or not tipo:
            print("[####]: Hace faltan datos en el registro de usuario")
            return False
        
        if patron.search(nombre) or patron.search(tipo):
            print("[####]: No se puede ingresar codigo SQL en los strings")
            return False
        
        return self.Modelo.Crear_usuario(id,nombre_usuario,clave, nombre, apellido, fecha_nacimiento, telefono, email, tipo)
    
    def listar_usuario(self) -> list:
        
        usuario = self.Modelo.Mostrar_usuarios()

        if len(usuario) > 0:
            return [ { "id": u[0], "nombre_usuario": u[1], "clave": u[2],"nombre": u[3],"apellido": u[4],"fecha_nacimiento": u[5],"telefono": u[6],"email": u[7],"tipo": u[8] } for u in usuario ]

        else:
            return []
        
    def validar(self, nombre_usuario: str, clave: str) -> bool:

        usuario = self.Modelo.obtener_usuario(nombre_usuario)
        if not usuario:
            print("[####]: Usuario no encontrado")
            return False

        clave_hash = usuario[2]
        clave_bytes = clave.encode("utf-8")
        clave_hash_bytes = clave_hash.encode("utf-8")

        if bcrypt.checkpw(clave_bytes, clave_hash_bytes):
            print("[####]: Ingreso correcto")
            return True
        else:
            print("[####]: Credenciales incorrectas")
            return False
        
class PacienteController:

    def __init__(self, Modelo: PacienteModel):
        self.Modelo = Modelo

    def registrar_paciente(self,id: int, nombre_usuario: str, clave: str, nombre: str, apellido: str, fecha_nacimiento: date, telefono: int, email: str, tipo: str, comuna: str, fecha_primera_visita: date):

        if not all(id,nombre_usuario,clave,nombre,apellido,fecha_nacimiento,telefono,email,tipo,comuna,fecha_primera_visita):
            print("[####]: Hace faltan datos en el registro de paciente")
            return False
        
        if patron.search(comuna) or patron.search(nombre) or patron.search(tipo) or patron.search(nombre_usuario) or patron.search(email):
            print("[####]: No se puede ingresar codigo SQL en los strings")
            return False
        
        return self.Modelo.Crear_paciente(id,nombre_usuario,clave,nombre,apellido,fecha_nacimiento,telefono,email,tipo,comuna,fecha_primera_visita)
    
    def listar_paciente(self) -> list:
        
        paciente = self.Modelo.Mostrar_paciente()

        if len(paciente) > 0:
            return [ { "id": p[0], "nombre_usuario": p[1], "clave": p[2],"nombre": p[3],"apellido": p[4],"fecha_nacimiento": p[5],"telefono": p[6],"email": p[7],"tipo": p[8], "comuna":p[9],"fecha_primera_visita":p[9] } for p in paciente ] 

        else:
            return []
        
    def validar(self, nombre_usuario: str, clave: str) -> bool:
    
        usuario = self.Modelo.obtener_usuario(nombre_usuario)
        if not usuario:
            print("[####]:Paciente no encontrado")
            return False

        clave_hash = usuario[2]
        clave_bytes = clave.encode("utf-8")
        clave_hash_bytes = clave_hash.encode("utf-8")

        if bcrypt.checkpw(clave_bytes, clave_hash_bytes):
            print("[####]: Ingreso correcto")
            return True
        else:
            print("[####]: Credenciales incorrectas")
            return False

class MedicoController:

    def __init__(self, Modelo: MedicoModel):
        self.Modelo = Modelo

    def registrar_medico(self,id: int, nombre_usuario: str, clave: str, nombre: str, apellido: str, fecha_nacimiento: date, telefono: int, email: str, tipo: str, especialidad: str, horario_atencion: time, fecha_ingreso:date):
        
        if not all(id,nombre_usuario,clave, nombre, apellido, fecha_nacimiento, telefono, email, tipo,especialidad):

            print("[####]: Hace faltan datos en el registro de medico")
            return False
        
        if patron.search(especialidad) or patron.search(nombre) or patron.search(tipo) or patron.search(nombre_usuario) or patron.search(apellido) or patron.search(email) or patron.search(clave):
            print("[####]: No se puede ingresar codigo SQL en los strings")
            return False
        
        return self.Modelo.Crear_medico(especialidad, horario_atencion, fecha_ingreso)
    
    def listar_medico(self) -> list:
        
        medico = self.Modelo.mostrar_medico()

        if len(medico) > 0:
            return [ { "id": m[0], "especialidad": m[1], "horario_atencion": m[2], "fecha_ingreso": m[3] } for m in medico ]

        else:
            return []
        
    def validar(self, nombre_usuario: str, clave: str) -> bool:
    
        usuario = self.Modelo.obtener_usuario(nombre_usuario)
        if not usuario:
            print("[####]: Doctor no encontrado")
            return False

        clave_hash = usuario[2]
        clave_bytes = clave.encode("utf-8")
        clave_hash_bytes = clave_hash.encode("utf-8")

        if bcrypt.checkpw(clave_bytes, clave_hash_bytes):
            print("[####]: Ingreso correcto")
            return True
        else:
            print("[####]: Credenciales incorrectas")
            return False
        
class AdministradorController:
    
    def __init__(self, Modelo: AdministradorModel):
        self.Modelo = Modelo

    def registrar_administrador(self,id: int, nombre_usuario: str, clave: str, nombre: str, apellido: str, fecha_nacimiento: date, telefono: int, email: str, tipo: str) -> bool:

        if not id or not nombre_usuario or not clave or not nombre or not apellido or not fecha_nacimiento or not telefono or not email or not tipo:
            print("[####]: Hace faltan datos en el registro de usuario")
            return False
        
        if patron.search(nombre) or patron.search(tipo):
            print("[####]: No se puede ingresar codigo SQL en los strings")
            return False
        
        return self.Modelo.Crear_administrador(id,nombre_usuario,clave, nombre, apellido, fecha_nacimiento, telefono, email, tipo)
    
    def listar_administrador(self) -> list:
        
        usuario = self.Modelo.Mostrar_usuarios()

        if len(usuario) > 0:
            return [ { "id": u[0], "nombre_usuario": u[1], "clave": u[2],"nombre": u[3],"apellido": u[4],"fecha_nacimiento": u[5],"telefono": u[6],"email": u[7],"tipo": u[8] } for u in usuario ]

        else:
            return []
        
    def validar(self, nombre_usuario: str, clave: str) -> bool:

        usuario = self.Modelo.obtener_usuario(nombre_usuario)
        if not usuario:
            print("[####]: administrador no encontrado")
            return False

        clave_hash = usuario[2]
        clave_bytes = clave.encode("utf-8")
        clave_hash_bytes = clave_hash.encode("utf-8")

        if bcrypt.checkpw(clave_bytes, clave_hash_bytes):
            print("[####]: Ingreso correcto")
            return True
        else:
            print("[####]: Credenciales incorrectas")
            return False

