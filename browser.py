import pyautogui
import time
import sys
import os
from subprocess import call

url = sys.argv[1]
path = sys.argv[2]

print("args: " + str(sys.argv))

call(["firefox", url])

time.sleep(3) # wait for it to load

pyautogui.hotkey('ctrl', 's') # save

time.sleep(1)

pyautogui.hotkey('ctrl', 'a') # get text in save path
pyautogui.hotkey('backspace')

pyautogui.typewrite(path)

pyautogui.hotkey('enter')

time.sleep(1)

pyautogui.hotkey('enter') # incase you have to overwrite

time.sleep(3)

pyautogui.hotkey("ctrl", "w") # close tab