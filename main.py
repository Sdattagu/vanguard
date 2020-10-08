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
import keyTests.escapeProcessTest as escTest
import controllers.keyboardCtrlTest as kbd_test

import controllers.keyboardCtrl as kbd
import bindings.bottomLetterRow as blr
import bindings.bottomFnRow as bfr
import bindings.arrowKeys as ak

import keyboard

def killer():
    raise KeyboardInterrupt

keyboard.add_hotkey('ctrl+shift+s', killer)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ##### Tests here ######
    print("Entering")
    print("In app window...")
    w = wctrl()
    w.find_window_wildcard(".*Notepad.*")
    w.set_foreground()
    w.set_active()

