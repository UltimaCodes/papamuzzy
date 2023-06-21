@echo off
echo Checking for Python 3...
REM Check if Python is already installed
python --version >nul 2>&1
if %errorlevel% == 0 (
  REM Check if the installed Python version is compatible
  for /f "tokens=2*" %%a in ('python --version 2^>^&1') do (
    set version=%%a
    set version=!version:~0,3!
    if !version! geq 3.6 (
      echo Python 3 is already installed.
      goto :install_modules
    )
    echo An incompatible version of Python is installed.
  )
)
echo Installing Python 3...
REM Download the Python installer
powershell -Command "(New-Object Net.WebClient).DownloadFile('https://www.python.org/ftp/python/3.9.6/python-3.9.6-amd64.exe', 'python-3.9.6-amd64')"
REM Install Python with default options
python-3.9.6-amd64.exe /quiet InstallAllUsers=1 PrependPath=1
REM Check if the installation was successful
python --version >nul 2>&1
if %errorlevel% neq 0 (
  echo Failed install Python.
  goto :end
)
echo Python 3 has been installed successfully.

:install_modules
echo Installing required modules...
python -m pip install winshell shutil requests psutil
if %errorlevel% neq 0 (
  echo Failed to install some modules.
  goto :end
)
echo All required modules have been installed successfully.

:end
pause
exit
