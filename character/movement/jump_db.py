import time
import controllers.keyboardCtrl as kbd
import bindings.bottomLetterRow as blr
import bindings.middleLetterRow as mlr
import bindings.arrowKeys as ak


def Up():
    kbd.Press([blr.x, ak.upArrow], 2)
    kbd.Release([blr.x, ak.upArrow])


def Right():
    kbd.Press([blr.x, ak.rightArrow])
    time.sleep(0.02)
    kbd.Release([blr.x, ak.rightArrow])
    kbd.Press([blr.x])
    time.sleep(0.02)
    kbd.Release([blr.x])

def RightFor(duration):
    t_end = time.time() + duration
    while time.time() < t_end:
        Right()
        time.sleep(0.1)

def RightWithAttack():
    kbd.Press([blr.x, ak.rightArrow])
    time.sleep(0.02)
    kbd.Release([blr.x, ak.rightArrow])
    kbd.Press([blr.x])
    time.sleep(0.02)
    kbd.Press([mlr.a])
    kbd.Release([blr.x])
    kbd.Release([mlr.a])


def RightWithAttackFor(duration):
    t_end = time.time() + duration
    while time.time() < t_end:
        RightWithAttack()
        time.sleep(0.5)


def Left():
    kbd.Press([blr.x, ak.leftArrow])
    time.sleep(0.02)
    kbd.Release([blr.x, ak.leftArrow])
    kbd.Press([blr.x])
    time.sleep(0.02)
    kbd.Release([blr.x])

def LeftFor(duration):
    t_end = time.time() + duration
    while time.time() < t_end:
        Left()
        time.sleep(0.1)

def LeftWithAttack():
    kbd.Press([blr.x, ak.leftArrow])
    time.sleep(0.02)
    kbd.Release([blr.x, ak.leftArrow])
    kbd.Press([blr.x])
    time.sleep(0.02)
    kbd.Press([mlr.a])
    kbd.Release([blr.x])
    kbd.Release([mlr.a])

def LeftWithAttackFor(duration):
    t_end = time.time() + duration
    while time.time() < t_end:
        LeftWithAttack()
        time.sleep(0.5)






