@echo off

:craig_NO
title NO CRAIG NO !!!!!!!!!!!!!!!!!!!!!
set /a files = %RANDOM%
cls
echo !!! Craig Is Eating Your Files !!!
echo.
echo craig is slowly eating all of your files
echo he will stop after he eats %files% ammount of files
echo.
echo press any key on this window to make him eat a new
echo random ammout of files, maybe it will be less then it is right now
echo.
echo %files%>files_to_eat.txt
pause >nul
goto craig_NO