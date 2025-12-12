from config.db_config import ConexionOracle
from datetime import date

class InsumoModel:
    def __init__(self, id: int,nombre: str, tipo: str, stock: int, costo_usd: float, conexion: ConexionOracle ):
        self.id = id
        self.nombre = nombre
        self.tipo = tipo
        self.stock = stock
        self.costo_usd = costo_usd
        self.conexion = conexion
    
    def Crear_insumo(self, id, nombre, tipo, stock, costo_usd) -> bool:

        cursor = self.conexion.obtener_cursor()

        try:
            consulta_validacion = "select * from LVMS_insumos where id = :1"
            cursor.execute(consulta_validacion, (id,))

            if len(cursor.fetchall()) >0:
                print(f"[####]: Ya existe un item con el nombre {id}")

                return  False
            
            else:
                Insertar = "insert into LVMS_insumos (id,nombre, tipo, stock, costo_usd) values (:1, :2, :3, :4, :5)"
                cursor.execute(Insertar, (id, nombre, tipo, stock, costo_usd))
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

        cursor = self.conexion.obtener_cursor()

        try:
            consulta_validacion = "select * from MSLV_insumos where id = :1"
            cursor.execute(consulta_validacion, (id,))

            if len(cursor.fetchall()) > 0:
                if datos:
                    Editar = "update MSLV_insumos set nombre = :1, tipo = :2, stock = :3, costo_usd = :4 where id = :5"
                    cursor.execute(Editar, (datos[0], datos[1], datos[2], datos[3], id,))
                    self.conexion.connection.commit()
                    print(f"[####]: Item {id} editado correctamente")
                    return True
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

        cursor = self.conexion.obtener_cursor()

        try:
            consulta_validacion = "select * from LVMS_insumos where id = :1"
            cursor.execute(consulta_validacion, (id,))
                           
            if len(cursor.fetchall()) >0:
                Eliminar = "delete from LVMS_insumos where id = :1"
                cursor.execute(Eliminar, (id,))
                self.conexion.connection.commit()
                print(f"[####]: Item {id} eliminado correctamente")
                return True
            else:
                print(f"[####]: No existe un item con el id {id}")
                return False
        except Exception as e:
            print(f"[####]: Error al eliminar el item {id} -> {e}")
            return False
        
        finally:
            if cursor: 
                cursor.close()
    
    def Mostrar_item(self) -> list:

        cursor = self.conexion.obtener_cursor()

        try:
            Mostrar = "select id, nombre, tipo, stock, costo_usd from LVMS_insumos"
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


    def __init__(self, id: int, id_paciente: int, id_medico: int, descripcion: str, medicamentos_recetados: str, costo_clp: int, conexion: ConexionOracle):
        self.id = id
        self.id_paciente = id_paciente
        self.id_medico = id_medico 
        self.descripcion = descripcion
        self.conexion = conexion
        self.medicamentos_recetados = medicamentos_recetados
        self.costo_clp = costo_clp

    def insertar_receta(self, id, id_paciente, id_medico, descripcion,medicamentos_recetados, costo_clp) -> bool:
       
        cursor = self.conexion.obtener_cursor()


        try:
            consulta_validacion = "select * from LVMS_recetas where id = :1"
            cursor.execute(consulta_validacion, (id,))

            if len(cursor.fetchall()) >0:
                print(f"[####]: Ya existe una receta con el id {id}")

                return  False
            
            else:
                Insertar = "insert into LVMS_recetas (id, id_paciente, id_medico, descripcion, medicamentos_recetados, costo_clp) values (:1, :2, :3, :4, :5, :6 )"
                cursor.execute(Insertar, (id, id_paciente, id_medico, descripcion, medicamentos_recetados, costo_clp))
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
            consulta_validacion = "select * from LVMS_recetas where id = :1"
            cursor.execute(consulta_validacion, (id,))

            if len(cursor.fetchall()) > 0:
                if datos:
                    Editar = "update LVMS_recetas set  descripcion = :1, medicamentos_recetados = :2, costo_clp = :3 where id = :4"
                    cursor.execute(Editar, (datos[0], datos[1], datos[2], id,))
                    self.conexion.connection.commit()
                    print(f"[####]: Receta {id} editada correctamente")
                    return True
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
            consulta_validacion = "select * from LVMS_recetas where id = :1"
            cursor.execute(consulta_validacion, (id,))
                           
            if len(cursor.fetchall()) >0:
                Eliminar = "delete from LVMS_recetas where id = :1"
                cursor.execute(Eliminar, (id,))
                self.conexion.connection.commit()
                print(f"[####]: Receta {id} eliminada correctamente")
                return True
            else:
                print(f"[####]: No existe una receta con el id {id}")
                return False
        except Exception as e:
            print(f"[####]: Error al eliminar la receta {id} -> {e}")
            return False
        
        finally:
            if cursor: 
                cursor.close()

    def Mostrar_recetas(self) -> list:

        cursor = self.conexion.obtener_cursor()

        try:
            Mostrar = "select id, id_paciente, id_medico, descripcion, medicamentos_recetados, costo_clp from LVMS_recetas"
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

    def __init__(self, id: int, id_paciente: int, id_medico: int, id_receta: int, fecha: date, comentarios:str, valor : int, conexion: ConexionOracle):
        self.id = id
        self.id_paciente = id_paciente
        self.id_medico = id_medico
        self.id_receta = id_receta
        self.fecha = fecha
        self.comentarios = comentarios
        self.valor = valor
        self.conexion = conexion
        
    def insertar_consulta(self, id, id_paciente, id_medico, id_receta, fecha, comentarios, valor) -> bool: 

        cursor = self.conexion.obtener_cursor()

        try:
            consulta_validacion = "select * from LVMS_consultas where id = :1"
            cursor.execute(consulta_validacion, (id,))

            if len(cursor.fetchall()) >0:
                print(f"[####]: Ya existe una consulta con el id {id}")
                return  False
            
            else:
                Insertar = "insert into LVMS_consultas (id, id_paciente, id_medico, id_receta, fecha, comentarios, valor) values (:1, :2, :3, :4, :5, :6, :7)"
                cursor.execute(Insertar, (id, id_paciente, id_medico, id_receta, fecha, comentarios, valor))
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
            validacion_consulta = "select * from LVMS_consultas where id = :1"
            cursor.execute(validacion_consulta, (id,))

            if len(cursor.fetchall()) > 0:
                if datos:
                    Editar = "update LVMS_consultas set fecha = :1, comentarios = :2, valor = :3 where id = :4"
                    cursor.execute(Editar, ( datos[0], datos[1], datos[3], id,))
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
            consulta_validacion = "select * from LVMS_consultas where id = :1"
            cursor.execute(consulta_validacion, (id,))
                           
            if len(cursor.fetchall()) >0:
                Eliminar = "delete from LVMS_consultas where id = :1"
                cursor.execute(Eliminar, (id,))
                self.conexion.connection.commit()
                print(f"[####]: Consulta {id} eliminada correctamente")
                return True
            else:
                print(f"[####]: No existe una consulta con el id {id}")
                return False
        except Exception as e:
            print(f"[####]: Error al eliminar la consulta {id} -> {e}")
            return False
        
        finally:
            if cursor: 
                cursor.close()
    
    def mostrar_consultas(self) -> list:

        cursor = self.conexion.obtener_cursor()

        try:
            Mostrar = "select id, id_paciente, id_medico, id_receta, fecha, comentarios, valor from LVMS_consultas"
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
                consulta_validacion = "select * from LVMS_agenda where id = :1"
                cursor.execute(consulta_validacion, (id,))

                if len(cursor.fetchall()) >0:
                    print(f"[####]: Ya existe una agenda con el id {id}")

                    return  False
                
                else:
                    Insertar = "insert into LVMS_agenda (id, id_paciente, id_medico, fecha_consulta, estado) values (:1, :2, :3, :4, :5)"
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
                consulta_validacion = "select * from LVMS_agenda where id = :1"
                cursor.execute(consulta_validacion, (id,))

                if len(cursor.fetchall()) > 0:
                    if datos:
                        Editar = "update LVMS_agenda set fecha_consulta = :1, estado = :2 where id = :3"
                        cursor.execute(Editar, (datos[0], datos[1], id,))
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
                consulta_validacion = "select * from LVMS_agenda where id = :1"
                cursor.execute(consulta_validacion, (id,))
                               
                if len(cursor.fetchall()) >0:
                    Eliminar = "delete from LVMS_agenda where id = :1"
                    cursor.execute(Eliminar, (id,))
                    self.conexion.connection.commit()
                    print(f"[####]: Agenda {id} eliminada correctamente")
                    return True
                else:
                    print(f"[####]: No existe una agenda con el id {id}")
                    return False
            except Exception as e:
                print(f"[####]: Error al eliminar la agenda {id} -> {e}")
                return False
            
            finally:
                if cursor: 
                    cursor.close()
        
        def mostrar_agendas(self) -> list:

            cursor = self.conexion.obtener_cursor()

            try:
                Mostrar = "select id, id_paciente, id_medico, fecha_consulta, estado from LVMS_agenda"
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

