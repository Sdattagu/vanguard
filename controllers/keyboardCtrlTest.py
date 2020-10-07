import controllers.keyboardCtrl as kbd
import bindings.bottomLetterRow as blr

def testHold(duration):
    kbd.Hold(duration, [blr.c])
    kbd.Release([blr.c])

def main():
    testHold(5)