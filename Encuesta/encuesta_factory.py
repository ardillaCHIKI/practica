from encuesta import Encuesta

class EncuestaFactory:
    """Fábrica para crear encuestas de diferentes tipos"""
    @staticmethod
    def crear_encuesta(tipo, pregunta, opciones, duracion):
        if tipo == "normal":
            return Encuesta(pregunta, opciones, duracion)
        elif tipo == "premium":
            return Encuesta(pregunta, opciones, duracion * 2)  # 🔥 Encuestas premium duran el doble
        else:
            raise ValueError("Tipo de encuesta no válido.")
