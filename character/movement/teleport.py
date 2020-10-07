import time
import controllers.keyboardCtrl as kbd
import bindings.arrowKeys as ak
import bindings.bottomLetterRow as blr
import bindings.bottomFnRow as bfr

def Right():
    kbd.Press([ak.rightArrow, blr.c])
    kbd.Release([ak.rightArrow, blr.c])

def RightFor(duration):
    kbd.Hold(duration, [bfr.left_ctrl, blr.c, ak.rightArrow])
    kbd.Release([bfr.left_ctrl, blr.c, ak.rightArrow])

def RightWithAttack():
    kbd.Press([bfr.left_ctrl, blr.c, ak.rightArrow])
    kbd.Release([bfr.left_ctrl, blr.c, ak.rightArrow])

def RightWithAttackFor(duration):
    t_end = time.time() + duration
    while time.time() < t_end:
        RightWithAttack()
        time.sleep(0.5)

def Left():
    kbd.Press([ak.leftArrow, blr.c])
    kbd.Release([ak.leftArrow, blr.c])

def LeftFor(duration):
    kbd.Hold(duration, [bfr.left_ctrl, blr.c, ak.leftArrow])
    kbd.Release([bfr.left_ctrl, blr.c, ak.leftArrow])


def LeftWithAttack():
    kbd.Press([bfr.left_ctrl, blr.c, ak.leftArrow])
    kbd.Release([bfr.left_ctrl, blr.c, ak.leftArrow])


def LeftWithAttackFor(duration):
    t_end = time.time() + duration
    while time.time() < t_end:
        LeftWithAttack()
        time.sleep(0.5)
