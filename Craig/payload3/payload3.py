import cv2, os, time, pyautogui
import ctypes
import pygame

user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

pygame.init()
os.chdir("files")
os.startfile('boom.vbs')
time.sleep(0.7)
os.startfile('boom.vbs')
time.sleep(0.6)
os.startfile('boom.vbs')
time.sleep(0.6)
os.startfile('boom.vbs')
time.sleep(0.5)
os.startfile('boom.vbs')
time.sleep(0.3)
os.startfile('boom.vbs')
time.sleep(0.2)
os.startfile('boom.vbs')
time.sleep(0.2)
os.startfile('boom.vbs')
time.sleep(0.1)
os.startfile('boom.vbs')
time.sleep(0.1)
os.startfile('boom.vbs')
time.sleep(0.1)
os.startfile('boom.vbs')
os.startfile('boom.vbs')
os.startfile('boom.vbs')
os.startfile('boom.vbs')
os.startfile('boom.vbs')
os.startfile('boom.vbs')
os.startfile('boom.vbs')
os.system('taskkill /f /im wscript.exe')
os.system('taskkill /f /im cscript.exe')

SetWindowPos = ctypes.windll.user32.SetWindowPos

NOSIZE = 1
NOMOVE = 2
TOPMOST = -1
NOT_TOPMOST = -2

def alwaysOnTop(yesOrNo):
    zorder = (NOT_TOPMOST, TOPMOST)[yesOrNo]
    hwnd = pygame.display.get_wm_info()['window']
    SetWindowPos(hwnd, zorder, 0, 0, 0, 0, NOMOVE|NOSIZE)

cap = cv2.VideoCapture('98moment.mp4')
success, img = cap.read()
shape = img.shape[1::-1]
wn = pygame.display.set_mode(shape, pygame.NOFRAME)
clock = pygame.time.Clock()

sound = pygame.mixer.Channel(4)
audio = pygame.mixer.Sound('startup.mp3')

sound.play(audio)

os.chdir('..')
os.startfile('bg.py')
os.chdir('files')

NoneType = type(None)

pyautogui.click(x=user32.GetSystemMetrics(0) / 2, y=user32.GetSystemMetrics(1) / 2)

while success:

    alwaysOnTop(True)

    pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))
    clock.tick(24)
    success, img = cap.read()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pass # no quit for you

        if event.type == pygame.KEYDOWN:
               
            if event.key == pygame.K_LSUPER or event.key == pygame.K_RSUPER:
                pyautogui.click(x=user32.GetSystemMetrics(0) / 2, y=user32.GetSystemMetrics(1) / 2 + 300)
    if type(img) != NoneType:
        wn.blit(pygame.image.frombuffer(img, shape, "BGR"), (0, 0))
    else:
        os.chdir('..')
        os.system('taskkill /F /FI "WindowTitle eq  Craig" ')
        os.system('start /min leave.bat')
        quit()
    pygame.display.update()

os.chdir('..')
os.system('taskkill /F /FI "WindowTitle eq  Craig" ')
os.system('start /min leave.bat')
quit()