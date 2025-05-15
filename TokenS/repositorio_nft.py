import json
import os

class RepositorioNFT:
    def __init__(self, archivo="nfts.json"):
        self.archivo = archivo
        self.nfts = self.cargar_nfts()

    def cargar_nfts(self):
        """Carga NFTs desde el archivo JSON"""
        if os.path.exists(self.archivo):
            with open(self.archivo, "r") as f:
                return json.load(f)
        return []

    def guardar_nfts(self):
        """Guarda NFTs en el archivo JSON"""
        with open(self.archivo, "w") as f:
            json.dump(self.nfts, f, indent=4)

    def agregar_nft(self, nft):
        """Añade un NFT y lo guarda"""
        self.nfts.append(nft)
        self.guardar_nfts()

    def listar_nfts_usuario(self, propietario):
        """Lista todos los NFTs de un usuario"""
        return [nft for nft in self.nfts if nft["Propietario"] == propietario]
