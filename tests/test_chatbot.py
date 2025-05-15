import pytest
from ChatBot.model import ChatbotIA

def test_respuesta_chatbot():
    bot = ChatbotIA()
    respuesta = bot.responder("¿Cómo estás?")
    assert isinstance(respuesta, str)
