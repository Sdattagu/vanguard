import time
import controllers.keyboardCtrl as kbd
import bindings.arrowKeys as ak
import bindings.bottomLetterRow as blr
import bindings.bottomFnRow as bfr

def Up():
    kbd.Press([ak.upArrow])
    time.sleep(0.2)
    kbd.Press([blr.c])
    time.sleep(0.1)
    kbd.Release([ak.upArrow, blr.c])

def UpWithJump():
    kbd.Press([ak.upArrow, blr.x])
    time.sleep(0.2)
    kbd.Press([blr.c])
    time.sleep(0.1)
    kbd.Release([ak.upArrow, blr.c, blr.x])

def Right():
    kbd.Press([ak.rightArrow, blr.c])
    kbd.Release([ak.rightArrow, blr.c])

def RightFor(duration):
    kbd.Hold(duration, [blr.c, ak.rightArrow])
    kbd.Release([blr.c, ak.rightArrow])

def RightWithAttack():
    kbd.Press([ak.rightArrow])
    time.sleep(0.1)
    kbd.Press([blr.c])
    time.sleep(0.1)
    kbd.Press([bfr.left_ctrl])
    kbd.Release([bfr.left_ctrl, blr.c, ak.rightArrow])

def RightWithAttackFor(duration):
    t_end = time.time() + duration
    while time.time() < t_end:
        RightWithAttack()
        time.sleep(0.1)

def _RightWithAttack_KannaFor(duration):
    kbd.Press([ak.rightArrow])
    time.sleep(0.1)
    kbd.Hold(duration, [bfr.left_ctrl, blr.c])
    kbd.Release([ak.rightArrow, bfr.left_ctrl, blr.c])

def Left():
    kbd.Press([ak.leftArrow, blr.c])
    kbd.Release([ak.leftArrow, blr.c])

def LeftFor(duration):
    kbd.Hold(duration, [blr.c, ak.leftArrow])
    kbd.Release([blr.c, ak.leftArrow])


def LeftWithAttack():
    kbd.Press([ak.leftArrow])
    time.sleep(0.1)
    kbd.Press([blr.c])
    time.sleep(0.1)
    kbd.Press([bfr.left_ctrl])
    kbd.Release([bfr.left_ctrl, blr.c, ak.leftArrow])


def LeftWithAttackFor(duration):
    t_end = time.time() + duration
    while time.time() < t_end:
        LeftWithAttack()
        time.sleep(0.1)

def _LeftWithAttack_KannaFor(duration):
    kbd.Press([ak.leftArrow])
    time.sleep(0.1)
    kbd.Hold(duration, [bfr.left_ctrl, blr.c])
    kbd.Release([ak.leftArrow, bfr.left_ctrl, blr.c])
