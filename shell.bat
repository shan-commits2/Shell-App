@echo off
chcp 65001 >nul
title $ Sudo Shell CMD
color 0A

:: Enable QuickEdit (optional for paste support)
reg add "HKCU\Console" /v QuickEdit /t REG_DWORD /d 1 /f >nul

cd /d "%~dp0"

:: Check if main.py exists
if not exist main.py (
    echo [!] main.py not found. Downloading from GitHub...
    curl -L -o main.py https://raw.githubusercontent.com/shan-commits2/Shell-App/main/main.py
    if exist main.py (
        echo [✓] Successfully downloaded main.py.
    ) else (
        echo [X] Failed to download main.py. Exiting.
        pause
        exit /b
    )
)

echo [*] Launching Shell CMD...
python main.py
pause
