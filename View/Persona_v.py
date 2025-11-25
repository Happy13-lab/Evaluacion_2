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
    