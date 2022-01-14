import ctypes, random


ctypes.windll.user32.SetCursorPos(random.randrange(1,1000), random.randrange(1,1000))