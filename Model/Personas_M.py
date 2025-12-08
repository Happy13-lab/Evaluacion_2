from confing.db_config import ConexionOracle
from datetime import date
from datetime import time
class UsuarioModel:
    def __init__(self, id: int, nombre_usuario: str, clave: str, nombre: str, apellido: str, fecha_nacimiento: date, telefono: int, email: str, tipo: str, conexion: ConexionOracle):
        self.id = id
        self.nombre_usuario = nombre_usuario
        self.clave = clave
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.telefono = telefono
        self.email = email
        self.tipo = tipo
        self.conexion = conexion
    
    def Crear_usuario(self,id, nombre_usuario, clave, nombre, apellido, fecha_nacimiento, telefono, email, tipo) -> bool:

        cursor = self.conexion.obtener_cursor()

        try:
            Validacion = "select * from LVMS_usuarios where id = :1"
            cursor.execute(Validacion, (id,))

            if len(cursor.fetchall()) > 0:
                print(f"[####]: El usuario con el id: {id} proporcionado ya existe.")
                return False
            
            else: 
                Insertar = "insert into LVMS_usuarios (id, nombre_usuario, clave, nombre, apellido, fecha_nacimiento, telefono, email, tipo) values (:1, :2, :3, :4, :5, :6, :7, :8, :9)"
                cursor.execute(Insertar, (id, nombre_usuario, clave, nombre, apellido, fecha_nacimiento, telefono, email, tipo))
                self.conexion.connection.commit()
                print(f"[####]: Usuario con el id: {id} creado correctamente.")
                return True
        except Exception as e:
            print(f"[####]: Ocurrió un error al crear el usuario → {e}")
            return False
        finally:
            if cursor:
                cursor.close()
    
    def Editar_usuario(self, id: int, *dato: tuple) -> bool:

        cursor  = self.conexion.obtener_cursor()

        try:
            validacion = "select * from LVMS_usuarios where id = :1 "
            cursor.execute(validacion,(id,))

            if len(cursor.fetchall()) == 0:
                print(f"El archivo que esta intentado editar no existe")
                return False
            else:
                
                Editar = "update LVMS_usuarios set nombre_usuario = :1, clave = :2, nombre = :3, apellido = :4, fecha_nacimiento = :5, telefono = :6, email = :7, tipo = :8 where id = :9"
                cursor.execute(Editar,(dato[0],dato[1],dato[2],dato[3],dato[4],dato[5],dato[6],dato[7],dato[8],id,))
                self.conexion.connection.commit()
                print(f"[####] El usuario a actualizado sus datos con exito")
                return True
        
        except Exception as e:
            print("[####] No se puede guardar el usuario")
            return False
        
        finally:
            if cursor:
                cursor.close()
    
    def Eliminar_usuario(self, id: int) -> bool:

            cursor = self.conexion.obtener_cursor()

            try:
                validacion = "select * from LVMS_usuarios where id = :1"
                cursor.execute(validacion, (id,))
            
                if len(cursor.fetchall()) == 0:
                    print(f"[####] No se ha encontrado ningun usuario")
                    return False
                
                else:
                    eliminar =  "delete from LVMS_usuarios where id = :1"
                    cursor.execute(eliminar,(id,))
                    self.conexion.connection.commit()
                    print(f"[####] Se a eliminado el usuario correctamente")
                    return True
            except Exception as e:
                print(f"[####] Error al eliminar al usuario -> {e}")
                return False
            finally:
                if cursor:
                    cursor.close()

    def Mostrar_usuarios(self) -> list:

        cursor = self.conexion.obtener_cursor()

        try:
            Mostrar = "select id,nombre_usuario, clave, nombre, apellido, fecha_nacimiento, telefono, email, tipo from LVMS_usuarios"
            cursor.execute(Mostrar)
            dato = cursor.fetchall()

            if len(dato) == 0:
                print(f"[####] no hay usuarios registrados")

                return []
            else:
                print("[####] Usuarios mostrados correctamente")
                return dato
        
        except Exception as e:
            print(f"[####] Error al mostrar el usuario -> {e}")
        
        finally:
            if cursor:
                cursor.close()


class PacienteModel(UsuarioModel):
    def __init__(self, id: int, nombre_usuario: str, clave: str, nombre: str, apellido: str, fecha_nacimiento: date, telefono: int, email: str, tipo: str, comuna: str, fecha_primera_visita: date, conexion: ConexionOracle):
        super().__init__(id, nombre_usuario, clave, nombre, apellido, fecha_nacimiento, telefono, email, tipo, conexion)
        
        self.comuna = comuna
        self.fecha_primera_visita = fecha_primera_visita
        self.conexion = conexion
    
    def Crear_paciente(self, id, nombre_usuario, clave, nombre, apellido, fecha_nacimiento, telefono, email, tipo, comuna, fecha_primera_visita) -> bool:

        cursor = self.conexion.obtener_cursor()

        try:
            Validacion = "select * from LVMS_paciente where id = :1"
            cursor.execute(Validacion, (id,))

            if len(cursor.fetchall()) > 0:
                print(f"[####]: El paciente con el id {id} proporcionado ya existe.")
                return False
            
            else: 
                Insertar = "insert into LVMS_paciente (id, nombre_usuario, clave, nombre, apellido, fecha_nacimiento, telefono, email, tipo, comuna, fecha_primera_visita) values (:1, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11)"
                cursor.execute(Insertar, (id, nombre_usuario, clave, nombre, apellido, fecha_nacimiento, telefono, email, tipo, comuna, fecha_primera_visita))
                self.conexion.connection.commit()
                print(f"[####]: Paciente con id {id} creado correctamente.")
                return True
        except Exception as e:
            print(f"[####]: Ocurrió un error al crear el paciente → {e}")
            return False
        finally:
            if cursor:
                cursor.close()

    def Editar_paciente(self, id, nombre_usuario, clave, nombre, apellido, fecha_nacimiento, telefono, email, tipo, comuna) -> bool:

        cursor = self.conexion.obtener_cursor()

        try:
            Validacion = "select * from LVMS_paciente where id = :1"
            cursor.execute(Validacion, (id,))

            if len(cursor.fetchall()) == 0:
                print(f"[####]: El paciente con el id {id} proporcionado no existe.")

                return False
            
            else: 
                Editar = "update LVMS_paciente set nombre_usuario = :1, clave = :2, nombre = :3, apellido = :4, fecha_nacimiento = :5, telefono = :6, email = :7, tipo = :8, comuna = :9 where id = :10"
                cursor.execute(Editar, (nombre_usuario, clave, nombre, apellido, fecha_nacimiento, telefono, email, tipo, comuna, id))
                self.conexion.connection.commit()
                print(f"[####]: Paciente con {id} editado correctamente.")
                return True
        except Exception as e:
            print(f"[####]: Ocurrió un error al editar el paciente → {e}")
            return False
        finally:
            if cursor:
                cursor.close()
    
    def Eliminar_paciente(self, id) -> bool:

        cursor = self.conexion.obtener_cursor()

        try:
            Validacion = "select * from LVMS_paciente where id = :1"
            cursor.execute(Validacion, (id,))

            if len(cursor.fetchall()) == 0:
                print(f"[####]: El paciente con el {id} proporcionado no existe.")
                return False
            
            else: 
                Eliminar = "delete from LVMS_paciente where id = :1"
                cursor.execute(Eliminar, (id,))
                self.conexion.connection.commit()
                print(f"[####]: Paciente con {id} eliminado correctamente.")
                return True
            
        except Exception as e:
            print(f"[####]: Ocurrió un error al eliminar el paciente → {e}")
            return False
        
        finally:
            if cursor:
                cursor.close()
    
    def Mostrar_paciente(self):

        cursor = self.conexion.obtener_cursor()

        try:
            Validacion = "select id, nombre_usuario, clave, nombre, apellido, fecha_nacimiento, telefono, email, tipo, comuna, fecha_primera_visita from LVMS_paciente"
            cursor.execute(Validacion)

            dato = cursor.fetchall()

            if len(dato) == 0:
                print(f"[####]: No hay pacientes")

                return []
            else: 
                print(f"[####]: Pacientes mostrados correctamente.")

                return dato
            
        except Exception as e:
            print(f"[####]: Ocurrió un error al mostrar el paciente → {e}")

            return []
        finally:
            if cursor:
                cursor.close()

class MedicoModel(UsuarioModel):

    def __init__(self, id: int, nombre_usuario: str, clave: str, nombre: str, apellido: str, fecha_nacimiento: str, telefono: int, email: str, tipo: str, especialidad: str, id_medico: int,horario_ingreso: time, conexion: ConexionOracle):
        super().__init__(id, nombre_usuario, clave, nombre, apellido, fecha_nacimiento, telefono, email, tipo, conexion)
        self.especialidad = especialidad
        self.id_medico = id_medico
        self.horario_ingreso = horario_ingreso
        self.conexion = conexion
    
    def Crear_medico(self, id, nombre_usuario, clave, nombre, apellido, fecha_nacimiento, telefono, email, tipo, especialidad, id_medico, horario_ingreso) -> bool:

        cursor = self.conexion.obtener_cursor()

        try:
            Validacion = "select * from LVMS_medico where id = :1"
            cursor.execute(Validacion, (id,))

            if len(cursor.fetchall()) > 0:
                print(f"[####]: El médico con el {id} proporcionado ya existe.")

                return False
            
            else: 
                Insertar = "insert into LVMS_medico (id, nombre_usuario, clave, nombre, apellido, fecha_nacimiento, telefono, email, tipo, especialidad, id_medico, horario_ingreso) values (:1, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11, :12)"
                cursor.execute(Insertar, (id, nombre_usuario, clave, nombre, apellido, fecha_nacimiento, telefono, email, tipo, especialidad, id_medico, horario_ingreso))
                self.conexion.connection.commit()
                print(f"[####]: Médico con {id} creado correctamente.")

                return True
        except Exception as e:
            print(f"[####]: Ocurrió un error al crear el médico → {e}")

            return False
        finally:
            if cursor:
                cursor.close()
    
    def editar_medico(self, id, nombre_usuario, clave, nombre, apellido,telefono, email, tipo, horario_ingreso) -> bool:

        cursor = self.conexion.obtener_cursor()

        try:
            Validacion = "select * from LVMS_medico where id = :1"
            cursor.execute(Validacion, (id,))

            if len(cursor.fetchall()) == 0:
                print(f"[####]: El médico con el {id} proporcionado no existe.")

                return False
            
            else: 
                Editar = "update LVMS_medico set nombre_usuario = :1, clave = :2, nombre = :3, apellido = :4, telefono = :5, email = :6, tipo = :7, horario_ingreso = :8 where id = :9"
                cursor.execute(Editar, (nombre_usuario, clave, nombre, apellido, telefono, email, tipo, horario_ingreso, id,))
                self.conexion.connection.commit()
                print(f"[####]: Médico con {id} editado correctamente.")

                return True
        except Exception as e:
            print(f"[####]: Ocurrió un error al editar el médico → {e}")

            return False
        finally:
            if cursor:
                cursor.close()  
    
    def eliminar_medico(self, id) -> bool:
        cursor = self.conexion.obtener_cursor()

        try:
            Validacion = "select * from LVMS_medico where id = :1"
            cursor.execute(Validacion, (id,))

            if len(cursor.fetchall()) == 0:
                print(f"[####]: El médico con el {id} proporcionado no existe.")

                return False
            
            else: 
                Eliminar = "delete from LVMS_medico where id = :1"
                cursor.execute(Eliminar, (id,))
                self.conexion.connection.commit()
                print(f"[####]: Médico con {id} eliminado correctamente.")

                return True
        except Exception as e:
            print(f"[####]: Ocurrió un error al eliminar el médico → {e}")

            return False
        finally:
            if cursor:
                cursor.close()
    
    def mostrar_medico(self):

        cursor = self.conexion.obtener_cursor()

        try:
            Validacion = "select id, nombre_usuario, clave, nombre, apellido, fecha_nacimiento, telefono, email, tipo, especialidad, id_medico, horario_ingreso from LVMS_medico"
            cursor.execute(Validacion)

            dato = cursor.fetchall()

            if len(dato) == 0:
                print(f"[####]: No existe el medico")

                return []
            else: 
                print(f"[####]: Médicos mostrados correctamente.")

                return dato
            
        except Exception as e:
            print(f"[####]: Ocurrió un error al mostrar el médico → {e}")

            return []
        finally:
            if cursor:
                cursor.close()

class AdministradorModel(UsuarioModel):
    def __init__(self, id: int, nombre_usuario: str, clave: str, nombre: str, apellido: str, fecha_nacimiento: date, telefono: int, email: str, tipo: str, comuna: str, fecha_primera_visita: date, conexion: ConexionOracle):
        super().__init__(id, nombre_usuario, clave, nombre, apellido, fecha_nacimiento, telefono, email, tipo, conexion)
        
    
    def Crear_administrador(self, id, nombre_usuario, clave, nombre, apellido, fecha_nacimiento, telefono, email, tipo, comuna, fecha_primera_visita) -> bool:

        cursor = self.conexion.obtener_cursor()

        try:
            Validacion = "select * from LVMS_administrador where id = :1"
            cursor.execute(Validacion, (id,))

            if len(cursor.fetchall()) > 0:
                print(f"[####]: El administrador con el id {id} proporcionado ya existe.")
                return False
            
            else: 
                Insertar = "insert into LVMS_administrador (id, nombre_usuario, clave, nombre, apellido, fecha_nacimiento, telefono, email, tipo) values (:1, :2, :3, :4, :5, :6, :7, :8, :9)"
                cursor.execute(Insertar, (id, nombre_usuario, clave, nombre, apellido, fecha_nacimiento, telefono, email, tipo))
                self.conexion.connection.commit()
                print(f"[####]: Administrador con id {id} creado correctamente.")
                return True
        except Exception as e:
            print(f"[####]: Ocurrió un error al crear el Administrador → {e}")
            return False
        finally:
            if cursor:
                cursor.close()

    def Editar_administrador(self, id, nombre_usuario, clave, nombre, apellido, fecha_nacimiento, telefono, email,tipo) -> bool:

        cursor = self.conexion.obtener_cursor()

        try:
            Validacion = "select * from LVMS_administrador where id = :1"
            cursor.execute(Validacion, (id,))

            if len(cursor.fetchall()) == 0:
                print(f"[####]: El administrador con el id {id} proporcionado no existe.")

                return False
            
            else: 
                Editar = "update LVMS_administrador set nombre_usuario = :1, clave = :2, nombre = :3, apellido = :4, fecha_nacimiento = :5, telefono = :6, email = :7, tipo = :8 where id = :9"
                cursor.execute(Editar, (nombre_usuario, clave, nombre, apellido, fecha_nacimiento, telefono, email, tipo, id))
                self.conexion.connection.commit()
                print(f"[####]: Adminsitrador con id {id} editado correctamente.")
                return True
        except Exception as e:
            print(f"[####]: Ocurrió un error al editar el paciente → {e}")
            return False
        finally:
            if cursor:
                cursor.close()
    
    def Eliminar_administrador(self, id) -> bool:

        cursor = self.conexion.obtener_cursor()

        try:
            Validacion = "select * from LVMS_administrador where id = :1"
            cursor.execute(Validacion, (id,))

            if len(cursor.fetchall()) == 0:
                print(f"[####]: El administrador con el {id} proporcionado no existe.")
                return False
            
            else: 
                Eliminar = "delete from LVMS_administrador where id = :1"
                cursor.execute(Eliminar, (id,))
                self.conexion.connection.commit()
                print(f"[####]: administrador con id {id} eliminado correctamente.")
                return True
            
        except Exception as e:
            print(f"[####]: Ocurrió un error al eliminar el administrador → {e}")
            return False
        
        finally:
            if cursor:
                cursor.close()
    
    def Mostrar_administrador(self):

        cursor = self.conexion.obtener_cursor()

        try:
            Validacion = "select id, nombre_usuario, clave, nombre, apellido, fecha_nacimiento, telefono, email, tipo from LVMS_administrador"
            cursor.execute(Validacion)

            dato = cursor.fetchall()

            if len(dato) == 0:
                print(f"[####]: No hay administradores")

                return []
            else: 
                print(f"[####]: Administradores mostrados correctamente.")

                return dato
            
        except Exception as e:
            print(f"[####]: Ocurrió un error al mostrar el administrador → {e}")

            return []
        finally:
            if cursor:
                cursor.close()


