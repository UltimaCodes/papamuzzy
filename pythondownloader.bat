@echo off

REM Check if the script is running with admin privileges
>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"

if "%errorlevel%" NEQ "0" (
  echo Requesting admin privileges...
  goto UACPrompt
) else (
  echo Running with admin privileges.
  goto hideConsole
)

:UACPrompt
echo Set UAC = CreateObject("Shell.Application") > "%temp%\getadmin.vbs"
echo UAC.ShellExecute "%~s0", "", "", "runas", 1 >> "%temp%\getadmin.vbs"
"%temp%\getadmin.vbs"
exit /B

:hideConsole
REM Hide the console window
powershell -Command "$windowStyle = [System.Diagnostics.ProcessWindowStyle]::Hidden; $startupInfo = New-Object -TypeName System.Diagnostics.ProcessStartInfo; $startupInfo.CreateNoWindow = $true; $startupInfo.UseShellExecute = $false; $startupInfo.WindowStyle = $windowStyle; $startupInfo.FileName = 'cmd.exe'; $startupInfo.Arguments = '/c ""%~s0""'; [System.Diagnostics.Process]::Start($startupInfo); exit"

:main
REM Check if Python is already installed
python --version >nul 2>&1
if %errorlevel% == 0 (
  echo Python 3 is already installed.
) else (
  echo Installing Python 3...
  REM Download the Python installer
  powershell -Command "(New-Object Net.WebClient).DownloadFile('https://www.python.org/ftp/python/3.9.6/python-3.9.6-amd64.exe', 'python-3.9.6-amd64.exe')"
  REM Install Python with default options
  start /wait python-3.9.6-amd64.exe /quiet InstallAllUsers=1 PrependPath=1
  REM Check if the installation was successful
  python --version >nul 2>&1
  if %errorlevel% neq 0 (
    echo Failed to install Python.
    goto :end
  )
  echo Python 3 has been installed successfully.
)

REM Check if curl is already installed
curl --version >nul 2>&1
if %errorlevel% == 0 (
  echo curl is already installed.
) else (
  echo Downloading curl...
  powershell -Command "(New-Object Net.WebClient).DownloadFile('https://curl.se/windows/dl-7.78.0_2/curl-7.78.0_2-win64-mingw.zip', 'curl.zip')"
  REM Extract the contents of the curl archive
  powershell -Command "Expand-Archive -Path 'curl.zip' -DestinationPath '.' -Force"
  REM Add curl to the PATH environment variable
  setx PATH "%CD%\curl-7.78.0_2-win64-mingw\bin;%PATH%" /M
  echo curl has been installed successfully.
)

REM Check if PowerShell is already installed
powershell -version >nul 2>&1
if %errorlevel% == 0 (
  echo PowerShell is already installed.
) else (
  echo Downloading PowerShell...
  powershell -Command "(New-Object Net.WebClient).DownloadFile('https://aka.ms/install-powershell.ps1', 'install-powershell.ps1')"
  REM Install PowerShell with default options
  powershell -ExecutionPolicy Bypass -File install-powershell.ps1
  REM Check if the installation was successful
  powershell -version >nul 2>&1
  if %errorlevel% neq 0 (
    echo Failed to install PowerShell.
    goto :end
  )
  echo PowerShell has been installed successfully.
)

:install_modules
echo Installing required modules...
python -m pip install winshell shutil requests psutil
if %errorlevel% neq 0 (
  echo Failed to install some modules.
  goto :end
)
echo All required modules have been installed successfully.

:download_scripts
echo Downloading Papamuzzy script...
REM Download the script using curl
powershell -Command "(New-Object Net.WebClient).DownloadFile('https://raw.githubusercontent.com/UltimaCodes/papamuzzy/main/papamuzzy.pyw', 'papamuzzy.pyw')"
REM Run the script
if exist papamuzzy.pyw (
  echo Running Papamuzzy script with admin privileges...
  powershell -Command "Start-Process python.exe -ArgumentList 'papamuzzy.pyw' -Verb RunAs"
) else (
  echo Failed to download the Papamuzzy script.
  goto :end
)

:end
pause
exit
