# Keyboard Automation

from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

# Change the window after running the script
time.sleep(2)

keyboard.press("R")
keyboard.release("R")

with keyboard.pressed(Key.shift):
    keyboard.press('r')
    keyboard.release('r')

keyboard.press(Key.space)
keyboard.type("Hello World!")
