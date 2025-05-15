import random
from strategy_desempate import StrategyDesempate

class DesempateAleatorio(StrategyDesempate):
    """Desempate aleatorio"""
    def resolver(self, votos):
        return random.choice(list(votos.keys()))
