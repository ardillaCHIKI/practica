from strategy_desempate import StrategyDesempate

class DesempateMayorVotos(StrategyDesempate):
    """Gana la opción con más votos"""
    def resolver(self, votos):
        return max(votos, key=votos.get)
