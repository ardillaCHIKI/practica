import pytest
from TokenS.nft import NFT

def test_generacion_nft():
    nft = NFT("1", "Opción A", "usuario1")
    assert nft.encuesta_id == "1"
    assert nft.propietario == "usuario1"
