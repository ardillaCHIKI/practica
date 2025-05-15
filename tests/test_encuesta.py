import pytest
from Encuesta.encuesta import Encuesta

def test_creacion_encuesta():
    encuesta = Encuesta("¿Te gusta Python?", ["Sí", "No"], 10)
    assert encuesta.pregunta == "¿Te gusta Python?"
    assert len(encuesta.opciones) == 2

def test_votar_encuesta():
    encuesta = Encuesta("¿Café o té?", ["Café", "Té"], 5)
    respuesta = encuesta.votar("usuario1", "Café")
    assert respuesta == "Voto registrado con éxito."
    assert encuesta.opciones["Café"] == 1
