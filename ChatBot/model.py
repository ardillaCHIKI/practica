from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

class ChatbotIA:
    def __init__(self, model_name="microsoft/DialoGPT-medium"):
        """Carga el modelo de Hugging Face"""
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)
        self.chat_history = []

    def responder(self, input_text):
        """Genera una respuesta basada en el texto de entrada"""
        self.chat_history.append(input_text)
        input_ids = self.tokenizer.encode(" ".join(self.chat_history) + self.tokenizer.eos_token, return_tensors="pt")

        with torch.no_grad():
            output = self.model.generate(input_ids, max_length=1000, pad_token_id=self.tokenizer.eos_token_id)
        
        response = self.tokenizer.decode(output[:, input_ids.shape[-1]:][0], skip_special_tokens=True)
        self.chat_history.append(response)
        return response
