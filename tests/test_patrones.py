import pytest
from patrones.strategy_desempate import StrategyDesempate
from patrones.desempate_mayor_votos import DesempateMayorVotos

def test_desempate_mayor_votos():
    estrategia = DesempateMayorVotos()
    votos = {"Opción A": 3, "Opción B": 5}
    assert estrategia.resolver(votos) == "Opción B"
