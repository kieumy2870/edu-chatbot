"""Gradio UI for AI Math Tutor.

This module creates a beautiful web interface using Gradio for solving math problems.
"""
import gradio as gr
from ai_service import solve_math_problem


def solve_with_ui(text_input: str, image_input) -> str:
    """Process math problem from UI inputs.
    
    Args:
        text_input: Text description of the problem.
        image_input: Uploaded image file.
        
    Returns:
        str: The solution formatted for display.
    """
    if not text_input and image_input is None:
        return "⚠️ Vui lòng nhập đề bài hoặc tải lên hình ảnh!"
    
    image_bytes = None
    if image_input is not None:
        with open(image_input, 'rb') as f:
            image_bytes = f.read()
    
    try:
        solution = solve_math_problem(text_input, image_bytes)
        return solution
    except Exception as e:
        return f"❌ Lỗi: {str(e)}"


def create_interface() -> gr.Blocks:
    """Create and configure the Gradio interface.
    
    Returns:
        gr.Blocks: Configured Gradio interface.
    """
    # Custom CSS for a premium look
    custom_css = """
    .gradio-container {
        font-family: 'Inter', sans-serif;
        max-width: 900px !important;
        margin: auto;
    }
    .gr-button-primary {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        border: none !important;
        font-weight: 600 !important;
        transition: transform 0.2s !important;
    }
    .gr-button-primary:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 10px 20px rgba(102, 126, 234, 0.3) !important;
    }
    .output-markdown {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        border-radius: 12px;
        padding: 20px;
        border-left: 4px solid #667eea;
    }
    h1 {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 2.5em !important;
        font-weight: 800 !important;
        text-align: center;
        margin-bottom: 10px;
    }
    """
    
    with gr.Blocks(css=custom_css, theme=gr.themes.Soft()) as interface:
        gr.Markdown("# 🤖 AI Math Tutor")
        gr.Markdown(
            "Nhập đề bài hoặc tải ảnh lên, AI sẽ giải chi tiết từng bước!"
        )
        
        with gr.Row():
            with gr.Column(scale=1):
                text_input = gr.Textbox(
                    label="📝 Nhập đề bài",
                    placeholder="Ví dụ: Giải phương trình x² - 5x + 6 = 0",
                    lines=5,
                    max_lines=10,
                )
                
                image_input = gr.Image(
                    label="📷 Hoặc tải ảnh đề bài",
                    type="filepath",
                    sources=["upload", "clipboard"],
                )
                
                solve_btn = gr.Button(
                    "✨ Giải Bài Toán",
                    variant="primary",
                    size="lg",
                )
                
                gr.Markdown(
                    "**💡 Mẹo:** Bạn có thể nhập cả text và ảnh cùng lúc để AI hiểu rõ hơn!"
                )
        
        with gr.Row():
            output = gr.Markdown(
                label="📊 Lời Giải",
                elem_classes="output-markdown",
            )
        
        # Examples for quick testing
        gr.Examples(
            examples=[
                ["Tính đạo hàm của f(x) = x³ + 2x² - 5x + 1", None],
                ["Giải hệ phương trình: 2x + y = 5 và x - y = 1", None],
                ["Tính tích phân từ 0 đến 1 của x² dx", None],
                [
                    "Cho tam giác ABC vuông tại A, AB = 3cm, AC = 4cm. Tính BC",
                    None,
                ],
            ],
            inputs=[text_input, image_input],
            label="📚 Ví dụ nhanh - Click để thử:",
        )
        
        # Connect the button
        solve_btn.click(
            fn=solve_with_ui,
            inputs=[text_input, image_input],
            outputs=output,
        )
        
        # Footer
        gr.Markdown(
            "---\n"
            "💻 Được xây dựng bởi Python + FastAPI + Gradio + Google Gemini AI\n\n"
            "🔒 Dữ liệu được cache để tối ưu hiệu suất và tiết kiệm chi phí API"
        )
    
    return interface


if __name__ == "__main__":
    print("🚀 Starting AI Math Tutor UI...")
    app = create_interface()
    app.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=True,
        show_error=True,
    )
