@echo off
setlocal
title Labelwin-Plugin einrichten
set "ROOT=%~dp0"
set "ZIEL=%USERPROFILE%\.claude"

echo.
echo  ==============================================
echo   Labelwin-Plugin fuer Claude einrichten
echo  ==============================================
echo.

rem --- 1. labelwin.env ausgefuellt? ---------------------------------------
findstr /R /C:"^LW_HOME=..*" "%ROOT%labelwin.env" >nul 2>nul
if errorlevel 1 (
  echo  [FEHLER] labelwin.env ist noch nicht ausgefuellt.
  echo           Datei mit dem Editor oeffnen, Werte eintragen, speichern
  echo           und einrichten.bat erneut starten.
  goto :ende
)

rem --- 2. Python vorhanden? ------------------------------------------------
python -c "import sys; sys.exit(0 if sys.version_info >= (3, 10) else 1)" >nul 2>nul
if errorlevel 1 (
  echo  [FEHLER] Python 3.10 oder neuer wurde nicht gefunden.
  echo           Python von https://www.python.org/downloads/ installieren und
  echo           bei der Installation "Add python.exe to PATH" anhaken.
  echo           Danach einrichten.bat erneut starten.
  goto :ende
)

rem --- 3. Pakete installieren --------------------------------------------
echo  Pakete werden installiert (mcp, pyodbc) ...
python -m pip install --user --quiet --disable-pip-version-check -r "%ROOT%plugin\labelwin\server\requirements.txt"
if errorlevel 1 (
  echo  [FEHLER] Pakete konnten nicht installiert werden ^(Internet/Proxy pruefen^).
  goto :ende
)

rem --- 4. Zugangsdaten an ihren festen Platz kopieren ----------------------
if not exist "%ZIEL%" mkdir "%ZIEL%"
copy /Y "%ROOT%labelwin.env" "%ZIEL%\labelwin.env" >nul
if errorlevel 1 (
  echo  [FEHLER] Konnte %ZIEL%\labelwin.env nicht schreiben.
  goto :ende
)
echo  Zugangsdaten gespeichert unter %ZIEL%\labelwin.env

rem --- 5. Verbindung testen ----------------------------------------------
python "%ROOT%werkzeuge\verbindung_testen.py"
if errorlevel 1 goto :ende

echo  Tipp: Das Passwort steht jetzt noch in der labelwin.env in diesem
echo  Download-Ordner. Die Kopie dort darf geloescht werden.

:ende
echo.
pause
endlocal
