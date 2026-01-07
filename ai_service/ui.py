import gradio as gr
from ai_service import solve_math_problem, initialize_chat

def create_interface():
    with gr.Blocks(theme=gr.themes.Soft()) as demo:
        gr.Markdown(
            """
            # 🤖 Chatbot Giải Toán 
            Nhập bài toán bằng văn bản hoặc tải ảnh lên để nhận lời giải chi tiết.
            """
        )
        
        chat_state = gr.State()

        with gr.Row():
            with gr.Column(scale=1):
                input_text = gr.Textbox(
                    label="Nhập bài toán dạng văn bản",
                    placeholder="Ví dụ: Giải phương trình x^2 - 5x + 6 = 0"
                )
                input_image = gr.Image(
                    label="Hoặc tải lên hình ảnh bài toán",
                    type="numpy"
                )
                submit_btn = gr.Button("Giải bài", variant="primary")

            with gr.Column(scale=2):
                output_markdown = gr.Markdown(label="Lời giải từ AI")

        submit_btn.click(
            fn=solve_math_problem,
            inputs=[input_text, input_image, chat_state],
            outputs=[output_markdown, chat_state]
        )
        
        demo.load(
            fn=initialize_chat,
            inputs=None,
            outputs=[chat_state]
        )
    
    return demo