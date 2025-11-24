from confing.db_config import ConexionOracle
class UsuarioModel:
    def __init__(self, id: int, nombre_usuario: str, clave: str, nombre: str, apellido: str, fecha_nacimiento: str, telefono: int, email: str, tipo: str, conexion: ConexionOracle):
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
            Validacion = "select * from usuarios where id = :1"
            cursor.execute(Validacion, (id,))

            if len(cursor.fetchall()) > 0:
                print(f"[####]: El usuario con el {id} proporcionado ya existe.")

                return False
            
            else: 
                Insertar = "insert into usuarios (id, nombre_usuario, clave, nombre, apellido, fecha_nacimiento, telefono, email, tipo) values (:1, :2, :3, :4, :5, :6, :7, :8, :9)"
                cursor.execute(Insertar, (id, nombre_usuario, clave, nombre, apellido, fecha_nacimiento, telefono, email, tipo))
                self.conexion.commit()
                print(f"[####]: Usuario con {id} creado correctamente.")

                return True
        except Exception as e:
            print(f"[####]: Ocurrió un error al crear el usuario → {e}")

            return False
        finally:
            if cursor:
                cursor.close()

class PacienteModel(UsuarioModel):
    def __init__(self, id: int, nombre_usuario: str, clave: str, nombre: str, apellido: str, fecha_nacimiento: str, telefono: int, email: str, tipo: str, comuna: str, fecha_primera_visita: str, conexion: ConexionOracle):
        super().__init__(id, nombre_usuario, clave, nombre, apellido, fecha_nacimiento, telefono, email, tipo, conexion)
        
        self.id = id
        self.nombre_usuario = nombre_usuario
        self.clave = clave
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.telefono = telefono
        self.email = email
        self.tipo = tipo
        self.comuna = comuna
        self.fecha_primera_visita = fecha_primera_visita
        self.conexion = conexion
    
    def Crear_paciente(self, id, nombre_usuario, clave, nombre, apellido, fecha_nacimiento, telefono, email, tipo, comuna, fecha_primera_visita) -> bool:

        cursor = self.conexion.obtener_cursor()

        try:
            Validacion = "select * from pacientes where id = :1"
            cursor.execute(Validacion, (id,))

            if len(cursor.fetchall()) > 0:
                print(f"[####]: El paciente con el {id} proporcionado ya existe.")

                return False
            
            else: 
                Insertar = "insert into pacientes (id, nombre_usuario, clave, nombre, apellido, fecha_nacimiento, telefono, email, tipo, comuna, fecha_primera_visita) values (:1, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11)"
                cursor.execute(Insertar, (id, nombre_usuario, clave, nombre, apellido, fecha_nacimiento, telefono, email, tipo, comuna, fecha_primera_visita))
                self.conexion.commit()
                print(f"[####]: Paciente con {id} creado correctamente.")

                return True
        except Exception as e:
            print(f"[####]: Ocurrió un error al crear el paciente → {e}")

            return False
        finally:
            if cursor:
                cursor.close()

    def Editar_paciente(self, id, nombre_usuario, clave, nombre, apellido, fecha_nacimiento, telefono, email, tipo, comuna, fecha_primera_visita) -> bool:

        cursor = self.conexion.obtener_cursor()

        try:
            Validacion = "select * from pacientes where id = :1"
            cursor.execute(Validacion, (id,))

            if len(cursor.fetchall()) == 0:
                print(f"[####]: El paciente con el {id} proporcionado no existe.")

                return False
            
            else: 
                Editar = "update pacientes set nombre_usuario = :1, clave = :2, nombre = :3, apellido = :4, fecha_nacimiento = :5, telefono = :6, email = :7, tipo = :8, comuna = :9, fecha_primera_visita = :10 where id = :11"
                cursor.execute(Editar, (nombre_usuario, clave, nombre, apellido, fecha_nacimiento, telefono, email, tipo, comuna, fecha_primera_visita, id))
                self.conexion.commit()
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
            Validacion = "select * from pacientes where id = :1"
            cursor.execute(Validacion, (id,))

            if len(cursor.fetchall()) == 0:
                print(f"[####]: El paciente con el {id} proporcionado no existe.")

                return False
            
            else: 
                Eliminar = "delete from pacientes where id = :1"
                cursor.execute(Eliminar, (id,))
                self.conexion.commit()
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
            Validacion = "select * from pacientes where id, nombre_usuario, clave, nombre, apellido, fecha_nacimiento, telefono, email, tipo, comuna, fecha_primera_visita from pacientes"
            cursor.execute(Validacion)

            dato = cursor.fetchall()

            if len(dato) == 0:
                print(f"[####]: El paciente con el {id} proporcionado no existe.")

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

    def __init__(self, id: int, nombre_usuario: str, clave: str, nombre: str, apellido: str, fecha_nacimiento: str, telefono: int, email: str, tipo: str, especialidad: str, id_medico: int,horario_ingreso: int, conexion: ConexionOracle):
        super().__init__(id, nombre_usuario, clave, nombre, apellido, fecha_nacimiento, telefono, email, tipo, conexion)
        
        self.id = id
        self.nombre_usuario = nombre_usuario
        self.clave = clave
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.telefono = telefono
        self.email = email
        self.tipo = tipo
        self.especialidad = especialidad
        self.id_medico = id_medico
        self.horario_ingreso = horario_ingreso
        self.conexion = conexion
    
    def Crear_medico(self, id, nombre_usuario, clave, nombre, apellido, fecha_nacimiento, telefono, email, tipo, especialidad, id_medico, horario_ingreso) -> bool:

        cursor = self.conexion.obtener_cursor()

        try:
            Validacion = "select * from medicos where id = :1"
            cursor.execute(Validacion, (id,))

            if len(cursor.fetchall()) > 0:
                print(f"[####]: El médico con el {id} proporcionado ya existe.")

                return False
            
            else: 
                Insertar = "insert into medicos (id, nombre_usuario, clave, nombre, apellido, fecha_nacimiento, telefono, email, tipo, especialidad, id_medico, horario_ingreso) values (:1, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11, :12)"
                cursor.execute(Insertar, (id, nombre_usuario, clave, nombre, apellido, fecha_nacimiento, telefono, email, tipo, especialidad, id_medico, horario_ingreso))
                self.conexion.commit()
                print(f"[####]: Médico con {id} creado correctamente.")

                return True
        except Exception as e:
            print(f"[####]: Ocurrió un error al crear el médico → {e}")

            return False
        finally:
            if cursor:
                cursor.close()
    
    def editar_medico(self, id, nombre_usuario, clave, nombre, apellido, fecha_nacimiento, telefono, email, tipo, especialidad, id_medico, horario_ingreso) -> bool:

        cursor = self.conexion.obtener_cursor()

        try:
            Validacion = "select * from medicos where id = :1"
            cursor.execute(Validacion, (id,))

            if len(cursor.fetchall()) == 0:
                print(f"[####]: El médico con el {id} proporcionado no existe.")

                return False
            
            else: 
                Editar = "update medicos set nombre_usuario = :1, clave = :2, nombre = :3, apellido = :4, fecha_nacimiento = :5, telefono = :6, email = :7, tipo = :8, especialidad = :9, id_medico = :10, horario_ingreso = :11 where id = :12"
                cursor.execute(Editar, (nombre_usuario, clave, nombre, apellido, fecha_nacimiento, telefono, email, tipo, especialidad, id_medico, horario_ingreso, id))
                self.conexion.commit()
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
            Validacion = "select * from medicos where id = :1"
            cursor.execute(Validacion, (id,))

            if len(cursor.fetchall()) == 0:
                print(f"[####]: El médico con el {id} proporcionado no existe.")

                return False
            
            else: 
                Eliminar = "delete from medicos where id = :1"
                cursor.execute(Eliminar, (id,))
                self.conexion.commit()
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
            Validacion = "select * from medicos where id, nombre_usuario, clave, nombre, apellido, fecha_nacimiento, telefono, email, tipo, especialidad, id_medico, horario_ingreso from medicos"
            cursor.execute(Validacion)

            dato = cursor.fetchall()

            if len(dato) == 0:
                print(f"[####]: El médico con el {id} proporcionado no existe.")

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