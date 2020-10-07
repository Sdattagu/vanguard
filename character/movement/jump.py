import time
import controllers.keyboardCtrl as keyboard
import bindings.bottomLetterRow as blr
import bindings.arrowKeys as ak

def Up():
    keyboard.Press([blr.x])

def Down():
    keyboard.Press([ak.downArrow, blr.x])
    keyboard.Release([ak.downArrow, blr.x])

def InPlaceFor(duration):
    keyboard.Hold(duration, [blr.x])

def Right():
    keyboard.Press([blr.x, ak.rightArrow])

def RightFor(duration):
    t_end = time.time() + duration
    while time.time() < t_end:
        keyboard.Press([blr.x, ak.rightArrow])
        time.sleep(0.1)
    keyboard.Release([blr.x, ak.rightArrow])