import pytest
from Persistencia.repositorio_encuestas import RepositorioEncuestas

def test_guardar_encuesta_json():
    repo = RepositorioEncuestas()
    encuesta = {"id": "1", "pregunta": "¿Te gusta Python?", "opciones": ["Sí", "No"], "duracion": 10}
    repo.guardar_encuesta_json(encuesta)
    encuestas = repo.cargar_encuestas_json()
    assert len(encuestas) > 0
