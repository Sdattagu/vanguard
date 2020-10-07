import controllers.keyboardCtrl as kbd
import bindings.bottomLetterRow as blr
import bindings.middleLetterRow as mlr
import bindings.arrowKeys as ak
import time


def Up():
    kbd.Press([blr.x])
    kbd.Release([blr.x])

def Down():
    kbd.Press([ak.downArrow])
    time.sleep(0.1)
    kbd.Press([blr.x])
    time.sleep(0.1)
    kbd.Release([ak.downArrow, blr.x])

def Left():
    kbd.Press([ak.leftArrow])
    time.sleep(0.1)
    kbd.Press([blr.x])
    time.sleep(0.1)
    kbd.Release([ak.leftArrow, blr.x])

def LeftFor(duration):
    kbd.Hold(duration, [blr.x, ak.leftArrow])
    kbd.Release([blr.x, ak.leftArrow])

def LeftWithAttack():
    kbd.Press([ak.leftArrow, blr.x])
    time.sleep(0.1)
    kbd.Press([mlr.a])
    kbd.Release([ak.leftArrow, blr.x, mlr.a])

def LeftWithAttackFor(duration):
    t_end = time.time() + duration
    while time.time() < t_end:
        LeftWithAttack()
        time.sleep(0.5)

def Right():
    kbd.Press([ak.rightArrow, blr.x])
    kbd.Release([ak.rightArrow, blr.x])

def RightFor(duration):
    kbd.Hold(duration, [blr.x, ak.rightArrow])
    kbd.Release([blr.x, ak.rightArrow])

def RightWithAttack():
    kbd.Press([ak.rightArrow, blr.x])
    time.sleep(0.1)
    kbd.Press([mlr.a])
    kbd.Release([ak.rightArrow, blr.x, mlr.a])

def RightWithAttackFor(duration):
    t_end = time.time() + duration
    while time.time() < t_end:
        RightWithAttack()
        time.sleep(0.5)

def InPlaceFor(duration):
    kbd.Hold(duration, [blr.x])


