x=msgbox("Cut a hydras head, 2 will take its place", 0+16, "Degerence effect 1")
Dim objShell
Set objShell = WScript.CreateObject( "WScript.Shell" )
objShell.Run("hydra.vbs")
objShell.Run("hydra.vbs")
Set objShell = Nothing