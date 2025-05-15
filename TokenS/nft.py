import uuid
from datetime import datetime

class NFT:
    def __init__(self, encuesta_id, opcion_elegida, propietario):
        """Genera un NFT único con metadatos asociados al voto"""
        self.id = str(uuid.uuid4())  # ID único del NFT
        self.encuesta_id = encuesta_id
        self.opcion_elegida = opcion_elegida
        self.propietario = propietario  # Usuario que votó
        self.fecha_creacion = datetime.now()

    def obtener_metadatos(self):
        """Devuelve los metadatos del NFT"""
        return {
            "ID": self.id,
            "Encuesta": self.encuesta_id,
            "Opción": self.opcion_elegida,
            "Propietario": self.propietario,
            "Fecha": self.fecha_creacion.strftime("%Y-%m-%d %H:%M:%S")
        }
