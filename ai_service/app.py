import os
import gradio as gr
import google.generativeai as genai
from PIL import Image
from dotenv import load_dotenv

load_dotenv()

try:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("Lỗi: Không tìm thấy GEMINI_API_KEY.")
    genai.configure(api_key=api_key)
except (ValueError, AttributeError) as e:
    print(e)
    exit()

system_instruction = """
Bạn là một gia sư toán học chuyên nghiệp và thân thiện, chuyên giải đáp các bài toán cho học sinh Việt Nam.
Nhiệm vụ của bạn là giải bài toán được đưa ra một cách chi tiết và dễ hiểu nhất.

YÊU CẦU ĐỊNH DẠNG ĐẦU RA:
1.  **Đáp án cuối cùng:** Bắt đầu bằng "**Đáp án:**" và in đậm.
2.  **Các bước giải chi tiết:** Bắt đầu bằng "**Các bước giải chi tiết:**" và in đậm. Liệt kê từng bước giải tuần tự, rõ ràng.
3.  **Giải thích:** Với mỗi bước, hãy giải thích ngắn gọn tại sao lại thực hiện bước đó.
4.  **Ngôn ngữ:** Sử dụng 100% tiếng Việt.
5.  **Lưu ý:** Nếu là câu hỏi trắc nghiệm, hãy chỉ ra đáp án đúng và giải thích.
"""

model = genai.GenerativeModel(model_name='gemini-2.5-flash-lite')

def initialize_chat():
    """Hàm này khởi tạo một phiên chat mới với các chỉ dẫn hệ thống."""
    chat = model.start_chat(history=[
        {
            "role": "user",
            "parts": [system_instruction]
        },
        {
            "role": "model",
            "parts": ["Vâng, tôi đã hiểu. Tôi là một gia sư toán học và sẵn sàng giúp bạn giải các bài toán theo đúng định dạng yêu cầu. Hãy đưa bài toán cho tôi."]
        }
    ])
    return chat

def solve_math_problem(text_problem, image_problem, chat_session):
    """
    Hàm xử lý yêu cầu, sử dụng ChatSession đã có.
    """
    if not text_problem and image_problem is None:
        return "Vui lòng nhập bài toán bằng văn bản hoặc tải lên hình ảnh.", chat_session

    try:
        user_content = []
        if text_problem:
            user_content.append(text_problem)
        else:
            user_content.append("Hãy giải bài toán trong hình ảnh này.")
        
        if image_problem is not None:
            pil_image = Image.fromarray(image_problem)
            user_content.append(pil_image)

        print("Đang gửi tin nhắn vào phiên chat...")
        response = chat_session.send_message(user_content)
        print("Đã nhận được phản hồi.")
        
        return response.text, chat_session

    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")
        error_message = f"Xin lỗi, đã có lỗi xảy ra. Chi tiết: {e}"
        return error_message, chat_session

# ----- GIAO DIỆN GRADIO -----
with gr.Blocks() as demo:
    gr.Markdown(
        """
        # 🤖 Chatbot Giải Toán 
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

print("Khởi chạy giao diện Gradio...")
demo.launch(share=True, theme=gr.themes.Soft())