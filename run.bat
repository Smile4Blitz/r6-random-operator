@echo off

rem Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed. Installing...
    REM Change the URL to the desired Python installer URL
    REM You can download Python installer from: https://www.python.org/downloads/windows/
    REM Replace "python-3.10.1-amd64.exe" with the name of the Python installer you downloaded
    curl -o python-installer.exe https://www.python.org/ftp/python/3.10.1/python-3.10.1-amd64.exe
    REM Change the installer name accordingly if you are using a different version
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

rem Run the Python script
python "%~dp0\main.py"
