
class InsumoView:
    @staticmethod
    def Vista_insumo(insumo: list) -> None:

        if len(insumo) >0:
            print("\n[####]: - Insumos -")
            
            for i in insumo:
                 print(f"[INFO]:--- ID: {i['id']} | Nombre: {i['nombre']} | Tipo: {i['tipo']} | Stock: {i['stock']}")
        else:
            print("[####] Sin registro de insumos")               

class RecetasView:
    @staticmethod
    def Vista_recetas(recetas: list) -> None:

        if len(recetas) > 0:
            print("\n[####]: - Recetas -")

            for i in recetas:
                 print(f"[INFO]:--- Id: {i['id']} | Id_paciente {i['id_paciente']} | Id_medico: {i['id_medico']} | Descripcion: {i['descripcion']}")
        
        else:
            print("[####] Sin registro de recetas")

class ConsultaView:
    @staticmethod
    def Vista_consultas(consultas: list) -> None:

        if len(consultas) > 0:
            print("\n[####]: - Consultas -")

            for i in consultas:
                 print(f"[INFO]:--- Id: {i['id']} | Id_paciente {i['id_paciente']} | Id_medico: {i['id_medico']} | Id_receta: {i['id_receta']}  | Fecha: {i['fecha']} | Comentarios: {i['comentarios']}")
        
        else:
            print("[####] Sin registro de consultas")

class AgendaView:
    @staticmethod
    def Vista_consultas(agenda: list) -> None:

        if len(agenda) > 0:
            print("\n[####]: - Agenda -")

            for i in agenda:
                 print(f"[INFO]:--- Id: {i['id']} | Id_paciente {i['id_paciente']} | Id_medico: {i['id_medico']} | Fecha_consulta: {i['fecha_consulta']}  | Estado: {i['estado']} ")
        
        else:
            print("[####] Sin registro de agendas")




