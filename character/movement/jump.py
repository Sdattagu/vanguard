import time
import controllers.keyboardCtrl as kbd
import bindings.bottomLetterRow as blr
import bindings.arrowKeys as ak


def Up():
    kbd.Press([blr.x])
    kbd.Release([blr.x])

def Down():
    kbd.Press([ak.downArrow, blr.x])
    kbd.Release([ak.downArrow, blr.x])

def Right():
    kbd.Press([ak.rightArrow, blr.x])
    kbd.Release([ak.rightArrow, blr.x])

def Left():
    kbd.Press([ak.leftArrow, blr.x])
    kbd.Release([ak.leftArrow, blr.x])

def InPlaceFor(duration):
    kbd.Hold(duration, [blr.x])


def Right():
    kbd.Press([blr.x, ak.rightArrow])
    kbd.Release([blr.x, ak.rightArrow])


def Left():
    kbd.Press([blr.x, ak.leftArrow])
    kbd.Release([blr.x, ak.leftArrow])


def RightFor(duration):
    kbd.Hold(duration, [blr.x, ak.rightArrow])
    kbd.Release(duration, [blr.x, ak.rightArrow])

def LeftFor(duration):
    kbd.Hold(duration, [blr.x, ak.leftArrow])
    kbd.Release(duration, [blr.x, ak.leftArrow])
