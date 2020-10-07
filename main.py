# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import time
import character.movement.teleport as tele
import character.movement.jump as jump
import character.movement.jump_db as dbJump
import character.movement.upperRowAttack as ura
from controllers.windowCtrl import WindowCtrl as wctrl

import character.classScripts.kanna.blueMushroomForest as blueMushForestScript
import character.classScripts.kanna.desertOfSerenity as desertOfSerenScript
import character.classScripts.kanna.rockyRoad as rockyRoadScript
import character.classScripts.kanna.refugeSouth1 as refugeSouth1
import controllers.keyboardCtrlTest as kbd_test

q = 0x10
w = 0x11
e = 0x12
r = 0x13
t = 0x14
y = 0x15

a = 0x1E
s = 0x1F
d = 0x20
f = 0x21
g = 0x22

z = 0x2C
x = 0x2D
c = 0x2E
v = 0x2F

rightArrow = 0xCD
leftArrow = 0xCB
downArrow = 0xD0

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    w = wctrl()
    w.find_window_wildcard(".*MapleStory.*")
    w.set_foreground()
    w.set_active()
    time.sleep(1)
    ##### Tests here ######
    refugeSouth1.main()
