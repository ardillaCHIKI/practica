class StrategyDesempate:
    """Interfaz para estrategias de desempate"""
    def resolver(self, votos):
        raise NotImplementedError("Este método debe ser implementado por subclases")
