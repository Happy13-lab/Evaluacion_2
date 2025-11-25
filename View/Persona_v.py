class UsuarioView:
    @staticmethod
    def Vista_usuario(usuario: list) -> None:

        if len(usuario) >0:
            print("\n[####]: - Usuarios -")
            
            for i in usuario:
                 print(f"[INFO]:--- ID: {i['id']} | Nombre_usuario: {i['nombre_usuario']} | Clave: {i['clave']} | Nombre: {i['nombre']} | Apellido: {i['apellido']} | Fecha_nacimiento: {i['fecha_nacimiento']} | Telefono: {i['telefono']} | Email: {i['email']} | Tipo: {i['tipo']}")
        else:
            print("[####] Sin registro de insumos")               

class PacienteView:
    @staticmethod
    def Vista_paciente(paciente: list) -> None:

        if len(paciente) >0:
            print("\n[####]: - Paciente -")
            
            for i in paciente:
                 print(f"[INFO]:--- ID: {i['id']} | Nombre_usuario: {i['nombre_usuario']} | Clave: {i['clave']} | Nombre: {i['nombre']} | Apellido: {i['apellido']} | Fecha_nacimiento: {i['fecha_nacimiento']} | Telefono: {i['telefono']} | Email: {i['email']} | Tipo: {i['tipo']} | Comuna: {i['comuna']}  | Fecha_primera_visita: {i['fecha_primera_visita']}")
        else:
            print("[####] Sin registro de paciente")      

class MedicoView:
    @staticmethod
    def Vista_medico(medico: list) -> None:

        if len(medico) >0:
            print("\n[####]: - Medico -")
            
            for i in medico:
                 print(f"[INFO]:--- ID: {i['id']} | Nombre_usuario: {i['nombre_usuario']} | Clave: {i['clave']} | Nombre: {i['nombre']} | Apellido: {i['apellido']} | Fecha_nacimiento: {i['fecha_nacimiento']} | Telefono: {i['telefono']} | Email: {i['email']} | Tipo: {i['tipo']} | Especialidad: {i['especialidad']}  | Horario_atencion: {i['horario_atencion']}| Fecha_Ingreso: {i['fecha_ingreso']} ")
        else:
            print("[####] Sin registro de medico")

    