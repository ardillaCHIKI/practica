from datetime import datetime, timedelta

class Encuesta:
    def __init__(self, pregunta, opciones, duracion_minutos):
        """Inicializa la encuesta con una pregunta, opciones y duración"""
        self.pregunta = pregunta
        self.opciones = {opcion: 0 for opcion in opciones}  # Diccionario {opción: votos}
        self.duracion = timedelta(minutes=duracion_minutos)
        self.fecha_creacion = datetime.now()
        self.activa = True
        self.votos = {}  # Registro de votos por usuario

    def votar(self, usuario, opcion):
        """Registra el voto de un usuario si la encuesta está activa y no ha votado aún"""
        if not self.activa:
            return "La encuesta ya está cerrada."
        if usuario in self.votos:
            return "Ya has votado en esta encuesta."
        if opcion not in self.opciones:
            return "Opción no válida."

        self.opciones[opcion] += 1
        self.votos[usuario] = opcion
        return "Voto registrado con éxito."

    def obtener_resultados(self):
        """Devuelve los resultados actuales de la encuesta"""
        return self.opciones

    def cerrar_encuesta(self):
        """Cierra la encuesta manualmente"""
        self.activa = False

    def verificar_expiracion(self):
        """Comprueba si la encuesta debe cerrarse automáticamente"""
        if datetime.now() - self.fecha_creacion >= self.duracion:
            self.activa = False
