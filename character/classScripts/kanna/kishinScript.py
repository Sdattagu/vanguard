import bindings.upperLetterRow as ulr
import controllers.keyboardCtrl as kbd
import time

def main():
    for iteration in range(25):
        print(iteration)
        time.sleep(1)
        kbd.Tap([ulr.q])
        time.sleep(55)