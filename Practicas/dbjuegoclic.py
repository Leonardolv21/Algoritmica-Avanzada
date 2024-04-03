import psycopg2
from psycopg2 import sql

class PostgreSQLDatabase:
    def __init__(self, dbname, user, password, host="localhost", port=5432):
        self.conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
        self.cur = self.conn.cursor()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS usuarios (
            id SERIAL PRIMARY KEY,
            nombre_usuario VARCHAR(50) UNIQUE NOT NULL,
            contraseña VARCHAR(100) NOT NULL
        );
        """
        self.cur.execute(query)
        self.conn.commit()

    def insert_usuario(self, nombre_usuario, contraseña, saldo=0, puntaje_maximo=0):
    # Verificar si el nombre de usuario ya existe
     if self.get_usuario_by_nombre(nombre_usuario) is not None:
        print("El nombre de usuario ya existe.")
        return  # Salir de la función si el nombre de usuario ya existe

     query = """
     INSERT INTO usuarios (nombre_usuario, contraseña, saldo, puntaje_maximo)
     VALUES (%s, %s, %s, %s)
     """
     self.cur.execute(query, (nombre_usuario, contraseña, saldo, puntaje_maximo))
     self.conn.commit()

 


    def get_usuario_by_nombre(self, nombre_usuario):
        query = """
        SELECT * FROM usuarios
        WHERE nombre_usuario = %s
        """
        self.cur.execute(query, (nombre_usuario,))
        return self.cur.fetchone()

    def close(self):
        self.cur.close()
        self.conn.close()

if __name__ == "__main__":
    db = PostgreSQLDatabase(dbname="juegoclick", user="postgres", password="123456789")

    # Crear la tabla de usuarios si no existe
    db.create_table()

    # Insertar un nuevo usuario
    db.insert_usuario(nombre_usuario="usuario1", contraseña="contraseña123")

    # Obtener un usuario por su nombre
    usuario = db.get_usuario_by_nombre("usuario1")
    print("Usuario encontrado:", usuario)

    # Cerrar la conexión a la base de datos
    db.close()
