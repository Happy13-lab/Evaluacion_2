import re
from Model.Objetos_M import InsumoModel, RecetasModel, ConsultasModel, AgendaModel
from datetime import date

SUS_KEYS = [
    r";", r"--", r"/\*", r"\bOR\b", r"\bAND\b", r"\bUNION\b",
    r"\bSELECT\b", r"\bINSERT\b", r"\bUPDATE\b", r"\bDELETE\b",
    r"\bDROP\b", r"\bEXEC\b"
]

patron = re.compile("|".join(SUS_KEYS), re.IGNORECASE)


class InsumoController:
    def __init__(self, Model: InsumoModel):
        self.model = Model

    def Registro_insumo(self,id: int, nombre: str, tipo: str, stock: int):

        if patron.search(nombre) or patron.search(tipo):
            print("[####]: No se puede ingresar codigo SQL en los strings")

            return False
        else:
            return self.model.Crear_insumo(id,nombre,tipo,stock)
class RecetasController:
    def __init__(self, Model:RecetasModel):
        self.model = Model

    def Registro_Recetas(self,id: int, id_paciente: int,id_medico: int, descripcion: str):

        if patron.search(descripcion):
            print("[####]: No se puede ingresar codigo SQL en los strings")

            return False
        else:
            return self.model.insertar_receta(id, id_paciente, id_medico, descripcion)

class ConsultasController:
    def __init__(self, Model:ConsultasModel):
        self.model = Model

    def Registro_Consultas(self,id: int, id_paciente: int,id_medico: int, id_recetas: int, fecha: date, comentarios: str):

        if patron.search(fecha) or patron.search(comentarios):
            print("[####]: No se puede ingresar codigo SQL en los strings")

            return False
        else:
            return self.model.insertar_consulta(id, id_paciente, id_medico, id_recetas, fecha, comentarios)

class AgendaController:
    def __init__(self, Modelo:AgendaModel):
        self.Modelo = Modelo

    def Registro_Agenda(self,id: int, id_paciente: int,id_medico: int, fecha_consulta: date, tipo: str):

        if patron.search(fecha_consulta) or patron.search(tipo):
            print("[####]: No se puede ingresar codigo SQL en los strings")

            return False
        else:
            return self.Modelo.insertar_agenda(id, id_paciente, id_medico, fecha_consulta, tipo)


