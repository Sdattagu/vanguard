import controllers.keyboardCtrl as kbd
import bindings.arrowKeys as ak
import bindings.bottomLetterRow as blr
import character.movement.walk as walk

def Right():
    kbd.Press([ak.rightArrow, blr.c])
    kbd.Release([ak.rightArrow, blr.c])

def Left():
    kbd.Press([ak.leftArrow, blr.c])
    kbd.Release([ak.leftArrow, blr.c])

def RightFor(duration):
    kbd.Hold(duration, [ak.rightArrow, blr.c])
    kbd.Release([ak.rightArrow, blr.c])

def LeftFor(duration):
    kbd.Hold(duration, [ak.leftArrow, blr.c])
    kbd.Release([ak.leftArrow, blr.c])
