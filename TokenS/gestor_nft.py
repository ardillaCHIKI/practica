from nft import NFT
from repositorio_nft import RepositorioNFT

class GestorNFT:
    def __init__(self):
        self.repositorio = RepositorioNFT()

    def generar_nft(self, encuesta_id, opcion, propietario):
        """Crea un NFT y lo guarda en el repositorio"""
        nft = NFT(encuesta_id, opcion, propietario)
        metadatos = nft.obtener_metadatos()
        self.repositorio.agregar_nft(metadatos)
        return metadatos

    def listar_nfts_usuario(self, propietario):
        """Lista los NFTs de un usuario"""
        return self.repositorio.listar_nfts_usuario(propietario)

    def transferir_nft(self, nft_id, nuevo_propietario):
        """Transfiere un NFT a otro usuario"""
        for nft in self.repositorio.nfts:
            if nft["ID"] == nft_id:
                nft["Propietario"] = nuevo_propietario
                self.repositorio.guardar_nfts()
                return f"NFT {nft_id} transferido a {nuevo_propietario}"
        return "NFT no encontrado."

