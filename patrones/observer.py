class Observador:
    """Interfaz para observadores"""
    def actualizar(self, encuesta_id):
        pass

class GestorObservadores:
    """Gestor que maneja la suscripción de módulos observadores"""
    def __init__(self):
        self.observadores = []

    def suscribir(self, observador):
        self.observadores.append(observador)

    def notificar(self, encuesta_id):
        for observador in self.observadores:
            observador.actualizar(encuesta_id)
