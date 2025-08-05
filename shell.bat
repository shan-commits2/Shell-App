@echo off
chcp 65001 >nul
title $ Sudo Shell CMD
color 0A

:: Enable QuickEdit mode automatically (optional but useful)
reg add "HKCU\Console" /v QuickEdit /t REG_DWORD /d 1 /f >nul

echo [*] Launching Shell CMD...
cd /d "%~dp0"
python main.py
pause
