"""Configuration module for AI service.

This module loads environment variables and validates API credentials.
"""
import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

MODEL_NAME = "gemini-2.5-flash-lite"

if not GEMINI_API_KEY:
    raise ValueError(
        "Lỗi: Không tìm thấy GEMINI_API_KEY. Vui lòng tạo file .env và thêm key vào."
    )
