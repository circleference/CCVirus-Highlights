@echo off
taskkill /f /im pythonw.exe
taskkill /f /im python.exe
cd .. && cd payload5
start payload5.py
exit