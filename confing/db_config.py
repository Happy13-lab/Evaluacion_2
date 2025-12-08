import oracledb

class ConexionOracle:
    """
        Clase para conexion de BD.
    """
    def __init__(self, usuario: str, password: str, url: str):
        self.usuario = usuario
        self.password = password
        self.url = url
        self.connection = None

    def conectar(self):
        try:
            self.connection = oracledb.connect(
                user=self.usuario,
                password=self.password,
                dsn=self.url
            )
            print("[INFO]: Conectado a BD correctamente.")
            
        except oracledb.DatabaseError as e:
            error, = e.args
            print(f"[ERROR]: No se pudo conectar a BD → {error.message}")

    def desconectar(self):
        if self.connection:
            self.connection.close()
            print("[INFO]: Conexión a BD cerrada correctamente.")

    def obtener_cursor(self):
        if not self.connection:
            self.conectar()

        return self.connection.cursor()
    
def validar_tablas(db):
    

    LVMS_usuario = """
            BEGIN
                EXECUTE IMMEDIATE '
                    CREATE TABLE LVMS_usuarios (
                        id integer PRIMARY KEY,
                        nombre_usuario VARCHAR2(100),
                        clave VARCHAR2(100),
                        nombre VARCHAR2(100),
                        apellido VARCHAR2(100),
                        fecha_nacimiento date,
                        telefono VARCHAR2(100),
                        email VARCHAR2(100),
                        tipo VARCHAR2(100)
                    )
                ';
            EXCEPTION
                WHEN OTHERS THEN
                    IF SQLCODE != -955 THEN
                        RAISE;
                    END IF;
            END;
        """
    
    LVMS_paciente = """
            BEGIN
                EXECUTE IMMEDIATE '
                    CREATE TABLE LVMS_paciente (
                        id_paciente integer PRIMARY KEY,
                        comuna VARCHAR2(100),
                        fecha_primera_visita date,
                        constraint fk_usuario_paciente FOREIGN KEY (id_paciente) REFERENCES ms_usuarios(id)
                    )
                ';
            EXCEPTION
                WHEN OTHERS THEN
                    IF SQLCODE != -955 THEN
                        RAISE;
                    END IF;
            END;
        """
    
    LVMS_medico = """
            BEGIN
                EXECUTE IMMEDIATE '
                    CREATE TABLE LVMS_medico (
                        id_medico INTEGER PRIMARY KEY,
                        especialidad VARCHAR2(100),
                        horario_atencion TIMESTAMP,
                        fecha_ingreso DATE,
                        CONSTRAINT fk_usuario_medico FOREIGN KEY (id_medico) REFERENCES ms_usuarios(id)
                    )
                ';
            EXCEPTION
                WHEN OTHERS THEN
                    IF SQLCODE != -955 THEN
                        RAISE;
                    END IF;
            END;
        """

    LVMS_insumos = """
            BEGIN
                EXECUTE IMMEDIATE '
                    CREATE TABLE LVMS_insumos (
                        id INTEGER PRIMARY KEY,
                        nombre VARCHAR2(100),
                        tipo VARCHAR2(100),
                        stock INTEGER
                    )
                ';
            EXCEPTION
                WHEN OTHERS THEN
                    IF SQLCODE != -955 THEN
                        RAISE;
                    END IF;
            END;
        """

    LVMS_recetas = """
            BEGIN
                EXECUTE IMMEDIATE '
                    CREATE TABLE LVMS_recetas (
                        id_recetas INTEGER PRIMARY KEY,
                        id_paciente INTEGER,
                        id_medico INTEGER,
                        descripcion VARCHAR2(100),
                        CONSTRAINT fk_receta_paciente FOREIGN KEY (id_paciente) REFERENCES ms_paciente(id_paciente),
                        CONSTRAINT fk_receta_medico FOREIGN KEY (id_medico) REFERENCES ms_medico(id_medico)
                    )
                ';
            EXCEPTION
                WHEN OTHERS THEN
                    IF SQLCODE != -955 THEN
                        RAISE;
                    END IF;
            END;
        """
    LVMS_consultas = """
            BEGIN
                EXECUTE IMMEDIATE '
                    CREATE TABLE LVMS_consultas (
                        id_consultas INTEGER PRIMARY KEY,
                        id_paciente INTEGER,
                        id_medico INTEGER,
                        id_recetas INTEGER,
                        fecha DATE,
                        comentarios VARCHAR2(100),
                        CONSTRAINT fk_consultas_paciente FOREIGN KEY (id_paciente) REFERENCES ms_paciente(id_paciente),
                        CONSTRAINT fk_consultas_medico FOREIGN KEY (id_medico) REFERENCES ms_medico(id_medico),
                        CONSTRAINT fk_consultas_recetas FOREIGN KEY (id_recetas) REFERENCES ms_recetas(id_recetas)
                    )
                ';
            EXCEPTION
                WHEN OTHERS THEN
                    IF SQLCODE != -955 THEN
                        RAISE;
                    END IF;
            END;
        """
    LVMS_agenda = """
            BEGIN
                EXECUTE IMMEDIATE '
                    CREATE TABLE LVMS_agenda (
                        id_agenda INTEGER PRIMARY KEY,
                        id_paciente INTEGER,
                        id_medico INTEGER,
                        fecha_consulta DATE,
                        descripcion VARCHAR2(100),
                        CONSTRAINT fk_agenda_paciente FOREIGN KEY (id_paciente) REFERENCES ms_paciente(id_paciente),
                        CONSTRAINT fk_agenda_medico FOREIGN KEY (id_medico) REFERENCES ms_medico(id_medico)
                    )
                ';
            EXCEPTION
                WHEN OTHERS THEN
                    IF SQLCODE != -955 THEN
                        RAISE;
                    END IF;
            END;
        """
    
    LVMS_administrador = """
            BEGIN
                EXECUTE IMMEDIATE '
                    CREATE TABLE LVMS_administrador (
                        id integer PRIMARY KEY,
                        nombre_usuario VARCHAR2(100),
                        clave VARCHAR2(100),
                        nombre VARCHAR2(100),
                        apellido VARCHAR2(100),
                        fecha_nacimiento date,
                        telefono VARCHAR2(100),
                        email VARCHAR2(100),
                        tipo VARCHAR2(100)
                    )
                ';
            EXCEPTION
                WHEN OTHERS THEN
                    IF SQLCODE != -955 THEN
                        RAISE;
                    END IF;
            END;
        """
    cursor = db.obtener_cursor()

    sentencias = [
        LVMS_usuario,
        LVMS_paciente,
        LVMS_medico,
        LVMS_insumos,
        LVMS_recetas,
        LVMS_consultas,
        LVMS_agenda,
        LVMS_administrador
    ]

    try:
        for sql in sentencias:
            cursor.execute(sql)

        db.connection.commit()

        print("[INFO]: Tablas validadas/creadas correctamente")
    except Exception as e:
        db.connection.rollback()

        print("[ERROR]: Error al crear tablas:", e)
    finally:
        if cursor:
            cursor.close()