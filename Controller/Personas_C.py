import re
from datetime import date,time
from Model.Personas_M import UsuarioModel,PacienteModel,MedicoModel

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
        
class PacienteController:

    def __init__(self, Modelo: PacienteModel):
        self.Modelo = Modelo

    def registrar_paciente(self, comuna: str, fecha_primera_visita: date):

        if not comuna or not fecha_primera_visita:
            print("[####]: Hace faltan datos en el registro de paciente")
            return False
        
        if patron.search(comuna)or patron.search(fecha_primera_visita):
            print("[####]: No se puede ingresar codigo SQL en los strings")
            return False
        
        return self.Modelo.Crear_paciente(comuna, fecha_primera_visita)
    
    def listar_paciente(self) -> list:
        
        paciente = self.Modelo.Mostrar_pacientes()

        if len(paciente) > 0:
            return [ { "id": p[0], "comuna": p[1], "fecha_primera_visita": p[2] } for p in paciente ]

        else:
            return []

class MedicoController:

    def __init__(self, Modelo: MedicoModel):
        self.Modelo = Modelo

    def registrar_medico(self, especialidad: str, horario_atencion: time, fecha_ingreso:date):
        
        if not especialidad or not horario_atencion or not fecha_ingreso:

            print("[####]: Hace faltan datos en el registro de medico")
            return False
        
        if patron.search(especialidad) or patron.search(horario_atencion) or patron.search(fecha_ingreso):
            print("[####]: No se puede ingresar codigo SQL en los strings")
            return False
        
        return self.Modelo.Crear_medico(especialidad, horario_atencion, fecha_ingreso)
    
    def listar_medico(self) -> list:
        
        medico = self.Modelo.Mostrar_medicos()

        if len(medico) > 0:
            return [ { "id": m[0], "especialidad": m[1], "horario_atencion": m[2], "fecha_ingreso": m[3] } for m in medico ]

        else:
            return []

