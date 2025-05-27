@echo off
setlocal

if not exist ".\venv" (
    echo Python venv dir not found. Create... Pls wait
    python -m venv venv
    call ".\venv\Scripts\activate.bat"
    python -m pip install -r src\requirements.txt
)

call ".\venv\Scripts\activate.bat"
python main.py

exit /b
endlocal