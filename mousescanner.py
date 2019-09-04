import pyautogui
import time

while True:
    print(pyautogui.position())
    x, y = pyautogui.position()
    print(pyautogui.pixel(x,y))
    time.sleep(3)