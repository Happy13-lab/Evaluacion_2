
class InsumoModel:
    def __init__(self, id: int, nombre_usuario: str, clave: int ,apellido: str ,fecha_nacimiento: str,telefono: int,email: str,tipo: str):
        self.id = id
        self.nombre_usuario = nombre_usuario
        self.clave = clave
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.telefono = telefono
        self.email = email
        self.tipo = tipo

    def Crear_insumo(self,id, nombre_usuario, clave, apellido, fecha_nacimiento, telefono, email, tipo) -> bool:
    



