import json
from database import Database

class RepositorioNFT:
    def __init__(self, archivo_json="nfts.json"):
        self.archivo_json = archivo_json
        self.db = Database()

    def guardar_nft_json(self, nft):
        """Guarda un NFT en JSON"""
        nfts = self.cargar_nfts_json()
        nfts.append(nft)
        with open(self.archivo_json, "w") as f:
            json.dump(nfts, f, indent=4)

    def cargar_nfts_json(self):
        """Carga NFTs desde JSON"""
        try:
            with open(self.archivo_json, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def guardar_nft_sqlite(self, nft_id, encuesta_id, opcion, propietario, fecha):
        """Guarda un NFT en SQLite"""
        query = "INSERT INTO nfts (id, encuesta_id, opcion, propietario, fecha) VALUES (?, ?, ?, ?, ?)"
        self.db.ejecutar_query(query, (nft_id, encuesta_id, opcion, propietario, fecha))
