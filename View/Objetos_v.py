
class InsumoView:
    @staticmethod
    def Vista_insumo(insumo: list) -> None:

        if len(insumo) >0:
            print("\n[####]: - Insumos -")
            
            for i in insumo:
                 print(f"[INFO]:--- ID: {i['id']} | Nombre: {i['nombre']} | Tipo: {i['tipo']} | Stock: {i['stock']} | Costo_usd: {i['costo_usd']}")
        else:
            print("[####] Sin registro de insumos")               

class RecetasView:
    @staticmethod
    def Vista_recetas(recetas: list) -> None:

        if len(recetas) > 0:
            print("\n[####]: - Recetas -")

            for i in recetas:
                 print(f"[INFO]:--- Id: {i['id']} | Id_paciente {i['id_paciente']} | Id_medico: {i['id_medico']} | Descripcion: {i['descripcion']} | Medicamentos_recetados: {i['medicamentos_recetados']}, costo_clp: {i['costo_clp']} ")
        
        else:
            print("[####] Sin registro de recetas")

class ConsultaView:
    @staticmethod
    def Vista_consultas(consultas: list) -> None:

        if len(consultas) > 0:
            print("\n[####]: - Consultas -")

            for i in consultas:
                 print(f"[INFO]:--- Id: {i['id']} | Id_paciente {i['id_paciente']} | Id_medico: {i['id_medico']} | Id_receta: {i['id_receta']}  | Fecha: {i['fecha']} | Comentarios: {i['comentarios']} | valor: {i['valor']}")
        
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




