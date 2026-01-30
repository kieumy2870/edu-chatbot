@echo off
echo ========================================
echo    AI Math Tutor - Gradio UI
echo ========================================
echo.

cd /d "%~dp0"

REM Check if .env file exists
if not exist .env (
    echo ERROR: .env file not found!
    echo.
    echo Please create a .env file with your GEMINI_API_KEY
    pause
    exit /b 1
)

echo [1/2] Checking dependencies...
pip install -r requirements.txt --quiet

echo.
echo [2/2] Starting Gradio UI...
echo.
echo UI will be available at: http://localhost:7860
echo A shareable link will also be generated
echo.
echo Press Ctrl+C to stop the server
echo ========================================
echo.

python ui.py
