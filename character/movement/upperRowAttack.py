import controllers.keyboardCtrl as kbd
import bindings.upperLetterRow as ulr
import time

def Q():
    kbd.Press([ulr.q])
    time.sleep(0.1)
    kbd.Release([ulr.q])

def W():
    kbd.Press([ulr.w])
    time.sleep(0.1)
    kbd.Release([ulr.w])

def E():
    kbd.Tap([ulr.e])