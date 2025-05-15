from encuesta import Encuesta
from patrones.observer import GestorObservadores
from patrones.desempate_mayor_votos import DesempateMayorVotos

class GestorEncuestas:
    def __init__(self, strategy=DesempateMayorVotos()):
        self.strategy = strategy
        self.encuestas_activas = {}
        self.encuestas_cerradas = {}
        self.observadores = GestorObservadores()

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

    def desempatar(self, encuesta_id):
        encuesta = self.encuestas_cerradas.get(encuesta_id)
        return self.strategy.resolver(encuesta.obtener_resultados()) if encuesta else "Encuesta no encontrada."

    def cerrar_encuesta(self, encuesta_id):
        if encuesta_id in self.encuestas_activas:
            self.encuestas_cerradas[encuesta_id] = self.encuestas_activas.pop(encuesta_id)
            self.encuestas_cerradas[encuesta_id].cerrar_encuesta()
            self.observadores.notificar(encuesta_id)  # 🔔 Notificar módulos
            return "Encuesta cerrada y módulos notificados."
        return "Encuesta no encontrada."
