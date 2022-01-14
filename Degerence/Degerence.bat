@echo off
title Degerence
if not exist "x64" goto no64
if not exist "x32" goto no32
echo Type 1 if you are running on a 64 bit computer
set /p ttt=
cls
cd 32x
if %ttt%==1 cd x64
cls
echo Warning!
echo.
echo After running this file you have to restart your computer
echo This does nothing to damage ypur computer, but it still causes catastrophe
echo.
echo Press any key 10x to continue . . . 
pause >nul
pause >nul
pause >nul
pause >nul
pause >nul
pause >nul
pause >nul
pause >nul
pause >nul
pause >nul
start runner.exe
exit

:no64
echo Error: %cd%\x64 does not exist
if not exist "32x" echo Error: %cd%\32x does not exist
echo Please run Compile.bat
ping localhost -t >nul

:no32
echo Error: %cd%\x32 does not exist
echo Please run Compile.bat
ping localhost -t >nul