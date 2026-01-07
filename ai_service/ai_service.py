import google.generativeai as genai
from PIL import Image
from config import GEMINI_API_KEY, MODEL_NAME, SYSTEM_INSTRUCTION

try:
    genai.configure(api_key=GEMINI_API_KEY)
except (ValueError, AttributeError) as e:
    print(e)
    exit()

model = genai.GenerativeModel(model_name=MODEL_NAME)

def initialize_chat():
    print("Khởi tạo phiên chat mới...")
    chat = model.start_chat(history=[
        {
            "role": "user",
            "parts": [SYSTEM_INSTRUCTION]
        },
        {
            "role": "model",
            "parts": ["Vâng, tôi đã hiểu. Tôi là một gia sư toán học và sẵn sàng giúp bạn giải các bài toán theo đúng định dạng yêu cầu. Hãy đưa bài toán cho tôi."]
        }
    ])
    return chat

def solve_math_problem(text_problem, image_problem, chat_session):
    if not text_problem and image_problem is None:
        return "Vui lòng nhập bài toán bằng văn bản hoặc tải lên hình ảnh.", chat_session

    try:
        user_content = []
        prompt = text_problem if text_problem else "Hãy giải bài toán trong hình ảnh này."
        user_content.append(prompt)
        
        if image_problem is not None:
            pil_image = Image.fromarray(image_problem)
            user_content.append(pil_image)

        print("Đang gửi yêu cầu đến Gemini...")
        response = chat_session.send_message(user_content)
        print("Đã nhận được phản hồi từ Gemini.")
        
        return response.text, chat_session

    except Exception as e:
        print(f"Đã xảy ra lỗi trong quá trình gọi API: {e}")
        error_message = f"Xin lỗi, đã có lỗi xảy ra trong quá trình xử lý. Chi tiết: {e}"
        return error_message, chat_session