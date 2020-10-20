import bindings.upperLetterRow as ulr
import controllers.keyboardCtrl as kbd
import character.movement.walk as walk
import time

def main():
    for i in range(30):
        t = 0
        print("iteration: ", i)
        kbd.Tap([ulr.q])
        time.sleep(1.5)
        kbd.Tap([ulr.w])
        time.sleep(1.5)
        kbd.Tap([ulr.e])
        time.sleep(1.5)
        kbd.Tap([ulr.r])
        time.sleep(1)
        kbd.Tap([ulr.t])
        time.sleep(1)
        walk.RightFor(1)
        time.sleep(1)
        walk.LeftFor(1)
        time.sleep(1)
        while t < 45:
            print("elapsed time: ", t)
            t += 1
            time.sleep(1)