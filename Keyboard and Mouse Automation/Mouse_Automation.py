# Mouse Automation

from pynput.mouse import Button, Controller
import time

mouse = Controller()
time.sleep(2)

# To read your pointer position
print('The current pointer position is {0}'.format(mouse.position))

# The current pointer position is (229, 372)
# To set the position of pointer
mouse.position = (10, 20)
mouse.press(Button.left)
mouse.release(Button.left)

# for double click
mouse.click(Button.left, 2)

# for scroll
mouse.scroll(0, 2)
