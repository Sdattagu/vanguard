import time
import controllers.keyboardCtrl as kbd
import bindings.bottomLetterRow as blr
import bindings.bottomFnRow as bfr
import bindings.arrowKeys as ak


def Left():
    kbd.Press([bfr.left_ctrl, blr.c, ak.leftArrow])
    kbd.Release([bfr.left_ctrl, blr.c, ak.leftArrow])


def Right():
    kbd.Press([bfr.left_ctrl, blr.c, ak.rightArrow])
    kbd.Release([bfr.left_ctrl, blr.c, ak.rightArrow])


def LeftFor(duration):
    kbd.Hold(duration, [bfr.left_ctrl, blr.c, ak.leftArrow])
    kbd.Release([bfr.left_ctrl, blr.c, ak.leftArrow])


def RightFor(duration):
    kbd.Hold(duration, [bfr.left_ctrl, blr.c, ak.rightArrow])
    kbd.Release([bfr.left_ctrl, blr.c, ak.rightArrow])
