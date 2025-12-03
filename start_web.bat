@echo off
echo ======================================
echo Budget Buddy Web Application
echo ======================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo X Python is not installed!
    echo Please install Python 3.6 or higher
    pause
    exit /b 1
)

echo [OK] Python found
echo.

REM Install dependencies
echo Installing dependencies...
pip install -r requirements.txt
echo.

echo Starting Budget Buddy Web Server...
echo.
echo Access the application at:
echo    http://localhost:5000
echo.
echo Press Ctrl+C to stop the server
echo ======================================
echo.

python app.py
pause
