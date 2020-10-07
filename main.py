# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import time
import controllers.keyboardCtrl as keyboard
from controllers.windowCtrl import WindowCtrl

q = 0x10
rightArrow = 0xCD
leftArrow = 0xCB

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    w = WindowCtrl()
    w.find_window_wildcard(".*MapleStory.*")
    w.set_foreground()
    w.set_active()
    time.sleep(1)
    keyboard.Hold(rightArrow, 2)
    keyboard.Press(q)
    keyboard.Hold(leftArrow, 2)
    keyboard.Press(q)

