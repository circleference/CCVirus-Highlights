@echo off
taskkill /f /im pythonw.exe
taskkill /f /im python.exe
taskkill /f /im wscript.exe
taskkill /f /im cscript.exe
pause >nul
exit