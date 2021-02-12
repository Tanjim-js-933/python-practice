import pyautogui
import time
messege = 5
while messege > 0:
    time.sleep(4)
    pyautogui.write('i love you')
    time.sleep(2)
    pyautogui.press('enter')
    messege = messege - 1