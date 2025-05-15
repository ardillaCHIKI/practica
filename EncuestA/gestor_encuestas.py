from encuesta import Encuesta

class GestorEncuestas:
    def __init__(self):
        """Inicializa el gestor de encuestas con listas de activas y cerradas"""
        self.encuestas_activas = {}
        self.encuestas_cerradas = {}

    def crear_encuesta(self, pregunta, opciones, duracion):
        """Crea una nueva encuesta y la registra en encuestas activas"""
        encuesta = Encuesta(pregunta, opciones, duracion)
        encuesta_id = len(self.encuestas_activas) + 1  # Generar un ID simple
        self.encuestas_activas[encuesta_id] = encuesta
        return encuesta_id

    def listar_encuestas_activas(self):
        """Devuelve las encuestas activas"""
        return {eid: e.pregunta for eid, e in self.encuestas_activas.items() if e.activa}

    def ver_resultados(self, encuesta_id):
        """Obtiene los resultados parciales de una encuesta"""
        encuesta = self.encuestas_activas.get(encuesta_id) or self.encuestas_cerradas.get(encuesta_id)
        return encuesta.obtener_resultados() if encuesta else "Encuesta no encontrada."

    def cerrar_encuesta(self, encuesta_id):
        """Cierra manualmente una encuesta y la mueve a cerradas"""
        encuesta = self.encuestas_activas.pop(encuesta_id, None)
        if encuesta:
            encuesta.cerrar_encuesta()
            self.encuestas_cerradas[encuesta_id] = encuesta
            return "Encuesta cerrada con éxito."
        return "Encuesta no encontrada o ya cerrada."
