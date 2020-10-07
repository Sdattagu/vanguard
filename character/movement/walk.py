import controllers.keyboardCtrl as kbd
import bindings.arrowKeys as ak

def RightFor(duration):
    kbd.Hold(duration, [ak.rightArrow])
    kbd.Release([ak.rightArrow])

def LeftFor(duration):
    kbd.Hold(duration, [ak.leftArrow])
    kbd.Release([ak.leftArrow])

def turnRight():
    kbd.Press(ak.rightArrow)
    kbd.Release(ak.rightArrow)

def turnLeft():
    kbd.Press([ak.leftArrow])
    kbd.Release([ak.leftArrow])