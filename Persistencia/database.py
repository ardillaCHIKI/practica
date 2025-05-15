import sqlite3

class Database:
    def __init__(self, db_name="streamer_data.db"):
        """Inicializa la conexión a la base de datos"""
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def ejecutar_query(self, query, params=()):
        """Ejecuta una consulta en la base de datos"""
        self.cursor.execute(query, params)
        self.conn.commit()

    def obtener_datos(self, query, params=()):
        """Obtiene datos de la base de datos"""
        self.cursor.execute(query, params)
        return self.cursor.fetchall()
