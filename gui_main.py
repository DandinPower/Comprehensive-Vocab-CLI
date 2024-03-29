from src.gui.gui_controller import GuiController
from src.config import PORT
import gradio as gr

def main():
    app = GuiController()
    with gr.Blocks() as gradio_app:
        with gr.Row():
            txt = gr.Textbox(label="Word")
            word_audio = gr.Audio(label="Audio")
        word_explaination = gr.Markdown()                
        btn = gr.Button(value="Explain")
        btn.click(app.run, inputs=[txt], outputs=[word_explaination, word_audio])
        
    gradio_app.launch(server_name="0.0.0.0", server_port=PORT)

if __name__ == "__main__":
    main()