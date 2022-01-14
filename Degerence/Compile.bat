rmdir x64
rmdir x32
mkdir x64
mkdir x32
xcopy /e data\* x64
xcopy /e data\* x32
bat2exe /bat uncompiled\hydra.bat /exe x32\hydra.exe /invisible
bat2exe /bat uncompiled\hydra4x.bat /exe x32\hydra4x.exe /invisible
bat2exe /bat uncompiled\hydra8x.bat /exe x32\hydra8x.exe /invisible
bat2exe /bat uncompiled\runner.bat /exe x32\runner.exe /invisible
bat2exe /bat uncompiled\sound.bat /exe x32\sound.exe /invisible
bat2exe /bat uncompiled\sound2.bat /exe x32\sound2.exe /invisible
bat2exe /bat uncompiled\hydra.bat /exe x64\hydra.exe /invisible /x64
bat2exe /bat uncompiled\hydra4x.bat /exe x64\hydra4x.exe /invisible /x64
bat2exe /bat uncompiled\hydra8x.bat /exe x64\hydra8x.exe /invisible /x64
bat2exe /bat uncompiled\runner.bat /exe x64\runner.exe /invisible /x64
bat2exe /bat uncompiled\sound.bat /exe x64\sound.exe /invisible /x64
bat2exe /bat uncompiled\sound2.bat /exe x64\sound2.exe /invisible /x64