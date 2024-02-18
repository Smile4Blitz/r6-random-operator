@echo off

rem Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed. Installing...
    curl -o python-installer.exe https://www.python.org/ftp/python/3.10.1/python-3.10.1-amd64.exe
    python-installer.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0
    del python-installer.exe
    echo Python has been installed.
)

rem Check if discord module is installed
python -c "import discord" >nul 2>&1
if %errorlevel% neq 0 (
    echo discord module is not installed. Installing...
    python -m pip install discord
    echo discord module has been installed.
)

rem Check for youtube dl
python -c "pip install pytube ffmpeg"

rem Run the Python script
python "%~dp0\main.py"
