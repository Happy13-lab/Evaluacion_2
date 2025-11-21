
class InsumoModel:
<<<<<<< HEAD
    def __init__(self, id: int, nombre_usuario: str, clave: str, apellido: str,fecha_nacimiento: str, telefono: int, email: str , tipo: str, conexion: X ):
=======
    def __init__(self, id: int, nombre_usuario: str, clave: int ,apellido: str ,fecha_nacimiento: str,telefono: int,email: str,tipo: str):
>>>>>>> 11ad2a1d406bc3cb49c011abc26c751b57d6f80f
        self.id = id
        self.nombre_usuario = nombre_usuario
        self.clave = clave
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.telefono = telefono
        self.email = email
        self.tipo = tipo
<<<<<<< HEAD
        self.conexion = conexion
=======

    def Crear_insumo(self,id, nombre_usuario, clave, apellido, fecha_nacimiento, telefono, email, tipo) -> bool:
>>>>>>> 11ad2a1d406bc3cb49c011abc26c751b57d6f80f
    
    def Guardar_item(self, id, nombre_usuario, clave, apellido, fecha_nacimiento, telefono, email, tipo) -> bool:

        cursor = self.conexion.obterner_cursor()

        try:
            consulta_validacion = "select * from insumo where id = :1"
            cursor.execute(consulta_validacion, (id,))

            if len(cursor.fetchall()) >0:
                print(f"[####]: Ya existe un item con el nombre {id}")

                return  False
            
            else:
                Insertar = "insert into insumo (id, nombre_usuario, clave, apellido, fecha_nacimiento, telefono, email, tipo) values (:1, :2, :3, :4, :5, :6, :7, :8)"
                cursor.execute(Insertar, (id, nombre_usuario, clave, apellido, fecha_nacimiento, telefono, email, tipo))
                self.conexion.commit()
                print(f"[####]: Item {id} guardado correctamente")
                return True
        
        except Exception as e:
            print(f"[####]: Error al guardar el item {id} -> {e}")
            return False
        
        finally:
            if cursor: 
                cursor.close()
     