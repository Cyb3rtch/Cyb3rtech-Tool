@echo off
echo Installation des modules..
echo.

if "%PROCESSOR_ARCHITECTURE%"=="x86" (
    set ARCHITECTURE=32
) else (
    set ARCHITECTURE=64
)

set PYTHON_VERSION=3.11.5
set PYTHON_EXE=python-%PYTHON_VERSION%-amd64.exe

where python >nul 2>nul
if %errorlevel% neq 0 (
    echo Python n'est pas installer installation en cours..
    echo.

    if %ARCHITECTURE%==32 (
        set PYTHON_EXE=python-%PYTHON_VERSION%-win32.exe
    )
    powershell -Command "Invoke-WebRequest https://www.python.org/ftp/python/%PYTHON_VERSION%/%PYTHON_EXE% -OutFile %PYTHON_EXE%"
    %PYTHON_EXE% /quiet InstallAllUsers=1 PrependPath=1 Include_test=0

    where python >nul 2>nul
    if %errorlevel% neq 0 (
        echo Installation de python impossible.
        pause
        exit /b 1
    )

    del %PYTHON_EXE%
)

where pip >nul 2>nul
if %errorlevel% neq 0 (
    echo pip is not installed. Installing pip...
    powershell -Command "Invoke-WebRequest https://bootstrap.pypa.io/get-pip.py -OutFile get-pip.py"
    python get-pip.py
    del get-pip.py
)

if exist requirements.txt (
    echo Installing packages from requirements.txt...
    pip install -r requirements.txt
) else (
    echo le fichier requirements.txt n'existe pas'
    pause
    exit /b 1
)

echo Setup complete.
pause