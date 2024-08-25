@echo off
setlocal
echo Installation des modules...
echo.

set "ARCHITECTURE=64"
if "%PROCESSOR_ARCHITECTURE%"=="x86" (
    if not defined ProgramFiles(x86) set "ARCHITECTURE=32"
)

set "PYTHON_VERSION=3.11.5"
set "PYTHON_EXE=python-%PYTHON_VERSION%-amd64.exe"

if "%ARCHITECTURE%"=="32" set "PYTHON_EXE=python-%PYTHON_VERSION%-win32.exe"

where python >nul 2>nul || (
    echo Python non trouvé. Installation...
    powershell -Command "Invoke-WebRequest https://www.python.org/ftp/python/%PYTHON_VERSION%/%PYTHON_EXE% -OutFile %PYTHON_EXE%" && (
        %PYTHON_EXE% /quiet InstallAllUsers=1 PrependPath=1 Include_test=0
        if errorlevel 1 (
            echo Échec de l'installation de Python.
            del "%PYTHON_EXE%"
            exit /b 1
        )
        del "%PYTHON_EXE%"
    ) || (
        echo Échec du téléchargement de Python.
        exit /b 1
    )
) || echo Python déjà installé.

where pip >nul 2>nul || (
    echo pip non trouvé. Installation...
    powershell -Command "Invoke-WebRequest https://bootstrap.pypa.io/get-pip.py -OutFile get-pip.py" && (
        python get-pip.py
        del get-pip.py
        if errorlevel 1 (
            echo Échec de l'installation de pip.
            exit /b 1
        )
    ) || (
        echo Échec du téléchargement de pip.
        exit /b 1
    )
) || echo pip déjà installé.

if exist requirements.txt (
    echo Installation des packages...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo Échec de l'installation des packages.
        exit /b 1
    )
) else (
    echo requirements.txt non trouvé.
    exit /b 1
)

echo Configuration terminée.
pause
endlocal
