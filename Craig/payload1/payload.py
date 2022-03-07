from PIL import ImageGrab
import keyboard, time, ctypes, os

screen = os.path.join(os.getcwd() + '\screen.png')
i = 0

def take_screenshot():
    global screen, i

    if i == 0:
        i += 1
        screen = screen.replace('.png', '1.png')
    else:
        i -= 1
        screen = screen.replace('1.png', '.png')

    myscreen = ImageGrab.grab()
    myscreen.save(screen)

# C:\Users\user\Desktop\new degerance payload\screen.png

while True:
    take_screenshot()
    print('Set Desktop Background')

    ctypes.windll.user32.SystemParametersInfoW(20, 0, screen, 0)

    if keyboard.is_pressed('q'):
        os.chdir('gwtf')
        os.system('start /min run.bat')

        with open('wallpath.txt') as f:
            walpath = f.readlines()

        os.chdir('..')
        
        ctypes.windll.user32.SystemParametersInfoW(20, 0, walpath[0], 0)
        break