"""AI Math Problem Solving Service.

This module provides the core functionality for solving math problems using
Google's Gemini AI with caching support.
"""
import io
from typing import Optional

from google import genai
from PIL import Image

from config import GEMINI_API_KEY, MODEL_NAME
from prompt import SYSTEM_INSTRUCTION
import db

# Khởi tạo database
db.init_db()

# Cấu hình Client mới của Google
client = genai.Client(api_key=GEMINI_API_KEY)


def solve_math_problem(
    text_problem: Optional[str], image_bytes: Optional[bytes] = None
) -> str:
    """Solve a math problem using Gemini AI with caching.

    Args:
        text_problem: Text description of the math problem.
        image_bytes: Optional image bytes containing the problem.

    Returns:
        str: The solution to the math problem, or error message.
    """
    # 1. Tạo hash để kiểm tra cache
    req_hash = db.generate_hash(text_problem, image_bytes)

    # 2. Kiểm tra trong Database xem đã giải bài này chưa
    cached = db.get_cached_response(req_hash)
    if cached:
        return f"[KẾT QUẢ TỪ CACHE]\n{cached}"

    try:
        # 3. Chuẩn bị nội dung gửi đi
        contents = []
        if text_problem:
            contents.append(text_problem)

        if image_bytes:
            img = Image.open(io.BytesIO(image_bytes))
            contents.append(img)

        # 4. Gọi API Gemini
        # Lưu ý: SDK mới dùng model='gemini-2.0-flash' hoặc 'gemini-1.5-pro'
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=contents,
            config={"system_instruction": SYSTEM_INSTRUCTION},
        )

        solution = response.text

        # 5. Lưu vào cache để lần sau không tốn phí API
        db.save_to_cache(req_hash, text_problem, solution)

        return solution

    except Exception as e:
        return f"Lỗi xử lý: {str(e)}"