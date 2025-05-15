import json
from database import Database

class RepositorioEncuestas:
    def __init__(self, archivo_json="encuestas.json"):
        self.archivo_json = archivo_json
        self.db = Database()

    def guardar_encuesta_json(self, encuesta):
        """Guarda una encuesta en JSON"""
        encuestas = self.cargar_encuestas_json()
        encuestas.append(encuesta)
        with open(self.archivo_json, "w") as f:
            json.dump(encuestas, f, indent=4)

    def cargar_encuestas_json(self):
        """Carga encuestas desde JSON"""
        try:
            with open(self.archivo_json, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def guardar_encuesta_sqlite(self, encuesta_id, pregunta, opciones, duracion):
        """Guarda una encuesta en SQLite"""
        query = "INSERT INTO encuestas (id, pregunta, opciones, duracion) VALUES (?, ?, ?, ?)"
        self.db.ejecutar_query(query, (encuesta_id, pregunta, json.dumps(opciones), duracion))
