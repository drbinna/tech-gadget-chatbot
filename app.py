import gradio as gr
from transformers import pipeline

# Load your chatbot model (adjust as necessary)
chatbot = pipeline("text-generation", model="gpt2")

def respond(message):
    response = chatbot(message, max_length=100, do_sample=True)[0]["generated_text"]
    return response

# Create Gradio interface
demo = gr.Interface(fn=respond, inputs="text", outputs="text", title="Tech Gadget Chatbot")

if __name__ == "__main__":
    demo.launch()
