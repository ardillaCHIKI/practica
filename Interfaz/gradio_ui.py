import gradio as gr
from Encuesta.gestor_encuestas import GestorEncuestas
from ChatBot.model import ChatbotIA
from TokenS.gestor_nft import GestorNFT

gestor_encuestas = GestorEncuestas()
chatbot = ChatbotIA()
gestor_nft = GestorNFT()

def listar_encuestas():
    return gestor_encuestas.listar_encuestas_activas()

def votar_encuesta(encuesta_id, opcion, usuario):
    return gestor_encuestas.votar_encuesta(encuesta_id, opcion, usuario)

def chat_bot(mensaje):
    return chatbot.responder(mensaje)

def galeria_nft(usuario):
    return gestor_nft.listar_nfts_usuario(usuario)

def iniciar_gradio():
    """Función que inicia la interfaz Gradio"""
    gr.Interface(
        [
            gr.Textbox(label="Usuario"),
            gr.Dropdown(choices=listar_encuestas, label="Encuestas activas"),
            gr.Dropdown(label="Opciones de encuesta"),
            gr.Button("Votar", fn=votar_encuesta),
            gr.Textbox(label="Chatbot IA", interactive=True),
            gr.Button("Enviar", fn=chat_bot),
            gr.Button("Ver NFTs", fn=galeria_nft),
        ],
        title="Interfaz de espectadores"
    ).launch()

if __name__ == "__main__":
    iniciar_gradio()
