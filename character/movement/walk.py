import controllers.keyboardCtrl as kbd
import bindings.arrowKeys as ak

def walkRightFor(duration):
    kbd.Hold(duration, [ak.rightArrow])

def walkLeftFor(duration):
    kbd.Hold(duration, [ak.leftArrow])

def turnRight():
    kbd.Press(ak.rightArrow)
    kbd.Release(ak.rightArrow)

def turnLeft():
    kbd.Press([ak.leftArrow])
    kbd.Release([ak.leftArrow])