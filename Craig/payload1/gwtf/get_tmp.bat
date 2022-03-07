@echo off
powershell.exe -executionpolicy remotesigned -File  "gwtf.ps1" >nul
for /L %%i in (1,1,10) do ( echo %time% )
FOR /F "tokens=* delims=" %%x in (temp.tmp) DO echo %%x
pause >nul