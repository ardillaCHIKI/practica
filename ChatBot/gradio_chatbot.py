import gradio as gr
from model import ChatbotIA

chatbot = ChatbotIA()

def chat_interface(user_input):
    return chatbot.responder(user_input)

gr.Interface(fn=chat_interface, inputs="text", outputs="text", title="Chatbot IA").launch()
