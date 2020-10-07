import controllers.keyboardCtrl as kbd
import bindings.middleLetterRow as mlr

def HoldAttack(duration):
    kbd.Hold(duration, mlr.a)
    kbd.Release([mlr.a])