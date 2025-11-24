from confing.db_config import ConexionOracle
from datetime import date

class InsumoModel:
    def __init__(self, id: int,nombre: str, tipo: str, stock: int, conexion: ConexionOracle ):
        self.id = id
        self.nombre = nombre
        self.tipo = tipo
        self.stock = stock
        self.conexion = conexion
    
    def Crear_insumo(self, id, nombre, tipo, stock) -> bool:

        cursor = self.conexion.obterner_cursor()

        try:
            consulta_validacion = "select * from insumo where id = :1"
            cursor.execute(consulta_validacion, (id,))

            if len(cursor.fetchall()) >0:
                print(f"[####]: Ya existe un item con el nombre {id}")

                return  False
            
            else:
                Insertar = "insert into insumo (id,nombre, tipo, stock) values (:1, :2, :3, :4)"
                cursor.execute(Insertar, (id, nombre, tipo, stock))
                self.conexion.connection.commit()
                print(f"[####]: Item {id} guardado correctamente")
                return True
        
        except Exception as e:
            print(f"[####]: Error al guardar el item {id} -> {e}")
            return False
        
        finally:
            if cursor: 
                cursor.close()
    
    def editar_item( self, id: int, *datos: tuple) -> bool:

        cursor = self.conexion.obterner_cursor()

        try:
            consulta_validacion = "select * from insumo where id = :1"
            cursor.execute(consulta_validacion, (id,))

            if len(cursor.fetchall()) == 0:
                if datos:
                    Editar = "update insumo set id = :1, nombre = :2, tipo = :3, stock = :4 where id = :5"
                    cursor.execute(Editar, (id, datos[0], datos[1], datos[2], id))
                    self.conexion.connection.commit()
                    print(f"[####]: Item {id} editado correctamente")
            else:
                print(f"[####]: No existe un item con el id {id}")
                return False

        except Exception as e:
            print(f"[####]: Error al editar el item {id} -> {e}")
            return False
        
        finally:
            if cursor: 
                cursor.close()

    def eliminar_item(self, id: int) -> bool:

        cursor = self.conexion.obterner_cursor()

        try:
            consulta_validacion = "select * from insumo where id = :1"
            cursor.execute(consulta_validacion, (id,))
                           
            if len(cursor.fetchall()) >0:
                Eliminar = "delete from insumo where id = :1"
                cursor.execute(Eliminar, (id,))
                self.conexion.commit()
                print(f"[####]: Item {id} eliminado correctamente")
                return True
            else:
                print(f"[####]: No existe un item con el id {id}")
                return False
        except Exception as e:
            print(f"[####]: Error al eliminar el item {id} -> {e}")
        
        finally:
            if cursor: 
                cursor.close()
    
    def Mostrar_item(self) -> list:

        cursor = self.conexion.obterner_cursor()

        try:
            Mostrar = "select id,nombre,tipo,stock from insumo"
            cursor.execute(Mostrar)
            datos = cursor.fetchall()

            if len(datos) > 0:
                return datos
            else:
                print(f"[####]: No hay items registrados")
                return []   
        
        except Exception as e:
            print(f"[####]: Error al mostrar los items -> {e}")
            return []
        
        finally:
            if cursor: 
                cursor.close()


class RecetasModel:


    def __init__(self, id: int, id_paciente: int, id_medico: int, descripcion: str, conexion: ConexionOracle):
        self.id = id
        self.id_paciente = id_paciente
        self.id_medico = id_medico 
        self.descripcion = descripcion
        self.conexion = conexion
        
    def insertar_receta(self, id, id_paciente, id_medico, descripcion) -> bool:
       
        cursor = self.conexion.obtener_cursor()


        try:
            consulta_validacion = "select * from recetas where id = :1"
            cursor.execute(consulta_validacion, (id,))

            if len(cursor.fetchall()) >0:
                print(f"[####]: Ya existe una receta con el id {id}")

                return  False
            
            else:
                Insertar = "insert into recetas (id, id_paciente, id_medico, descripcion) values (:1, :2, :3, :4)"
                cursor.execute(Insertar, (id, id_paciente, id_medico, descripcion))
                self.conexion.connection.commit()
                print(f"[####]: Receta {id} guardada correctamente")
                return True
        
        except Exception as e:
            print(f"[####]: Error al guardar la receta {id} -> {e}")
            return False
        
        finally:
            if cursor: 
                cursor.close()

    def editar_receta(self, id: int, *datos:tuple) -> bool:

        cursor = self.conexion.obtener_cursor()

        try:
            consulta_validacion = "select * from recetas where id = :1"
            cursor.execute(consulta_validacion, (id,))

            if len(cursor.fetchall()) == 0:
                if datos:
                    Editar = "update recetas set id = :1, id_paciente = :2, id_medico = :3 descripcion = :4 where id = :5"
                    cursor.execute(Editar, (id, datos[0], datos[1], datos[2], datos[3], id))
                    self.conexion.connection.commit()
                    print(f"[####]: Receta {id} editada correctamente")
            else:
                print(f"[####]: No existe una receta con el id {id}")
                return False

        except Exception as e:
            print(f"[####]: Error al editar la receta {id} -> {e}")
            return False
        
        finally:
            if cursor: 
                cursor.close()
    
    def eliminar_receta(self, id: int) -> bool:

        cursor = self.conexion.obtener_cursor()

        try:
            consulta_validacion = "select * from recetas where id = :1"
            cursor.execute(consulta_validacion, (id,))
                           
            if len(cursor.fetchall()) >0:
                Eliminar = "delete from recetas where id = :1"
                cursor.execute(Eliminar, (id,))
                self.conexion.connection.commit()
                print(f"[####]: Receta {id} eliminada correctamente")
                return True
            else:
                print(f"[####]: No existe una receta con el id {id}")
                return False
        except Exception as e:
            print(f"[####]: Error al eliminar la receta {id} -> {e}")
        
        finally:
            if cursor: 
                cursor.close()

    def Mostrar_recetas(self) -> list:

        cursor = self.conexion.obtener_cursor()

        try:
            Mostrar = "select id, id_paciente, id_medico, descripcion from recetas"
            cursor.execute(Mostrar)
            datos = cursor.fetchall()

            if len(datos) > 0:
                return datos
            else:
                print(f"[####]: No hay recetas registradas")
                return []   
        
        except Exception as e:
            print(f"[####]: Error al mostrar las recetas -> {e}")
            return []
        
        finally:
            if cursor: 
                cursor.close()

class ConsultasModel:

    def __init__(self, id: int, id_paciente: int, id_medico: int, id_receta: int, fecha: date, comentarios:str, conexion: ConexionOracle):
        self.id = id
        self.id_paciente = id_paciente
        self.id_medico = id_medico
        self.id_receta = id_receta
        self.fecha = fecha
        self.comentarios = comentarios
        self.conexion = conexion
        
    def insertar_consulta(self, id, id_paciente, id_medico, id_receta, fecha, comentarios) -> bool: 

        cursor = self.conexion.obtener_cursor()

        try:
            consulta_validacion = "select * from consultas where id = :1"
            cursor.execute(consulta_validacion, (id,))

            if len(cursor.fetchall()) >0:
                print(f"[####]: Ya existe una consulta con el id {id}")

                return  False
            
            else:
                Insertar = "insert into consultas (id, id_paciente, id_medico, id_receta, fecha, comentarios) values (:1, :2, :3, :4, :5, :6)"
                cursor.execute(Insertar, (id, id_paciente, id_medico, id_receta, fecha, comentarios))
                self.conexion.connection.commit()
                print(f"[####]: Consulta {id} guardada correctamente")
                return True
        
        except Exception as e:
            print(f"[####]: Error al guardar la consulta {id} -> {e}")
            return False
        
        finally:
            if cursor: 
                cursor.close()
    
    def editar_consultas(self, id: int, *datos: tuple) -> bool:

        cursor = self.conexion.obtener_cursor()

        try:
            validacion_consulta = "select * from consultas where id = :1"
            cursor.execute(validacion_consulta, (id,))

            if len(cursor.fetchall()) == 0:
                if datos:
                    Editar = "update consultas set id = :1, id_paciente = :2, id_medico = :3, id_receta = :4, fecha = :5, comentarios = :6 where id = :7"
                    cursor.execute(Editar, (id, datos[0], datos[1], datos[2], datos[3], datos[4], id))
                    self.conexion.connection.commit()
                    print(f"[####]: Consulta {id} editada correctamente") 

                    return True 

                
                else:
                    print(f"[####]: sin datos ingresados en {id}")
                    return False
            else:
                print(f"[####]: No existe una consulta con el id {id}")
                return False
        except Exception as e:
            print(f"[####]: Error al editar la consulta {id} -> {e}")
            return False

        finally:
            if cursor: 
                cursor.close()
    
    def eliminar_consulta(self, id: int) -> bool:

        cursor = self.conexion.obtener_cursor()

        try:
            consulta_validacion = "select * from consultas where id = :1"
            cursor.execute(consulta_validacion, (id,))
                           
            if len(cursor.fetchall()) >0:
                Eliminar = "delete from consultas where id = :1"
                cursor.execute(Eliminar, (id,))
                self.conexion.connection.commit()
                print(f"[####]: Consulta {id} eliminada correctamente")
                return True
            else:
                print(f"[####]: No existe una consulta con el id {id}")
                return False
        except Exception as e:
            print(f"[####]: Error al eliminar la consulta {id} -> {e}")
        
        finally:
            if cursor: 
                cursor.close()
    
    def mostrar_consultas(self) -> list:

        cursor = self.conexion.obtener_cursor()

        try:
            Mostrar = "select id, id_paciente, id_medico, id_receta, fecha, comentarios from consultas"
            cursor.execute(Mostrar)
            datos = cursor.fetchall()

            if len(datos) > 0:
                return datos
            else:
                print(f"[####]: No hay consultas registradas")
                return []   
        
        except Exception as e:
            print(f"[####]: Error al mostrar las consultas -> {e}")
            return []
        
        finally:
            if cursor: 
                cursor.close()
    
class AgendaModel:
    
        def __init__(self, id: int, id_paciente: int, id_medico: int, fecha_consulta: date, estado: str, conexion: ConexionOracle):
            self.id = id
            self.id_paciente = id_paciente
            self.id_medico = id_medico
            self.fecha_consulta = fecha_consulta
            self.estado = estado
            self.conexion = conexion
        
        def insertar_agenda(self,id,id_paciente,id_medico,fecha_consulta,estado) -> bool:

            cursor = self.conexion.obtener_cursor()

            try:
                consulta_validacion = "select * from agenda where id = :1"
                cursor.execute(consulta_validacion, (id,))

                if len(cursor.fetchall()) >0:
                    print(f"[####]: Ya existe una agenda con el id {id}")

                    return  False
                
                else:
                    Insertar = "insert into agenda (id, id_paciente, id_medico, fecha_consulta, estado) values (:1, :2, :3, :4, :5)"
                    cursor.execute(Insertar, (id, id_paciente, id_medico, fecha_consulta, estado))
                    self.conexion.connection.commit()
                    print(f"[####]: Agenda {id} guardada correctamente")
                    return True
            
            except Exception as e:
                print(f"[####]: Error al guardar la agenda {id} -> {e}")
                return False
            
            finally:
                if cursor: 
                    cursor.close()
        
        def editar_agenda(self, id: int, *datos: tuple) -> bool:

            cursor = self.conexion.obtener_cursor()

            try:
                consulta_validacion = "select * from agenda where id = :1"
                cursor.execute(consulta_validacion, (id,))

                if len(cursor.fetchall()) == 0:
                    if datos:
                        Editar = "update agenda set id = :1, id_paciente = :2, id_medico = :3, fecha_consulta = :4, estado = :5 where id = :6"
                        cursor.execute(Editar, (id, datos[0], datos[1], datos[2], datos[3], id))
                        self.conexion.connection.commit()
                        print(f"[####]: Agenda {id} editada correctamente")
                else:
                    print(f"[####]: No existe una agenda con el id {id}")
                    return False

            except Exception as e:
                print(f"[####]: Error al editar la agenda {id} -> {e}")
                return False
            
            finally:
                if cursor: 
                    cursor.close()
        
        def eliminar_agenda(self, id: int) -> bool:

            cursor = self.conexion.obtener_cursor()

            try:
                consulta_validacion = "select * from agenda where id = :1"
                cursor.execute(consulta_validacion, (id,))
                               
                if len(cursor.fetchall()) >0:
                    Eliminar = "delete from agenda where id = :1"
                    cursor.execute(Eliminar, (id,))
                    self.conexion.connection.commit()
                    print(f"[####]: Agenda {id} eliminada correctamente")
                    return True
                else:
                    print(f"[####]: No existe una agenda con el id {id}")
                    return False
            except Exception as e:
                print(f"[####]: Error al eliminar la agenda {id} -> {e}")
            
            finally:
                if cursor: 
                    cursor.close()
        
        def mostrar_agendas(self) -> list:

            cursor = self.conexion.obtener_cursor()

            try:
                Mostrar = "select id, id_paciente, id_medico, fecha_consulta, estado from agenda"
                cursor.execute(Mostrar)
                datos = cursor.fetchall()

                if len(datos) > 0:
                    return datos
                else:
                    print(f"[####]: No hay agendas registradas")
                    return []   
            
            except Exception as e:
                print(f"[####]: Error al mostrar las agendas -> {e}")
                return []
            
            finally:
                if cursor: 
                    cursor.close()

