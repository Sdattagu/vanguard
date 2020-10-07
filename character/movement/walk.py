import controllers.keyboardCtrl as kbd
import bindings.arrowKeys as ak

def walkRightFor(time):
    kbd.Hold(ak.rightArrow, time)

def walkLeftFor(time):
    kbd.Hold(ak.leftArrow, time)

def turnRight():
    kbd.Press(ak.rightArrow)
    kbd.Release(ak.rightArrow)

def turnLeft():
    kbd.Press([ak.leftArrow])
    kbd.Release([ak.leftArrow])