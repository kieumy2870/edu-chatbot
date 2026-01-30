@echo off
echo ========================================
echo   AI Math Tutor - React Frontend
echo ========================================
echo.

cd /d "%~dp0\..\frontend"

REM Check if node_modules exists
if not exist node_modules (
    echo [1/2] Installing dependencies...
    echo This may take a few minutes...
    call npm install
    if errorlevel 1 (
        echo.
        echo ERROR: Failed to install dependencies
        echo Make sure Node.js is installed: https://nodejs.org/
        pause
        exit /b 1
    )
)

echo.
echo [2/2] Starting React development server...
echo.
echo Frontend: http://localhost:3000
echo.
echo Make sure the backend is running at http://localhost:8000
echo ========================================
echo.

call npm run dev
