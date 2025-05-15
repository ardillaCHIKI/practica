from nft import NFT

class NFTFactory:
    """Fábrica para crear diferentes tipos de NFTs"""
    @staticmethod
    def crear_nft(tipo, encuesta_id, opcion, propietario):
        nft = NFT(encuesta_id, opcion, propietario)
        if tipo == "rare":
            nft.id += "-RARE"  # 🔥 Agrega un identificador único
        return nft