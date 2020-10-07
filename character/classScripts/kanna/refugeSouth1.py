import time
import character.movement.teleport as tele
import character.movement.jump as jump
import character.movement.walk as walk
import controllers.keyboardCtrl as kbd
import bindings.bottomLetterRow as blr
import bindings.bottomFnRow as bfr
import bindings.arrowKeys as ak


def main():
    ##### Go here ####
    # Left, up, left, land
    tele._RightWithAttack_KannaFor(6)
    walk.turnLeft()
    tele._LeftWithAttack_KannaFor(0.8)
    time.sleep(0.5)
    walk.LeftFor(0.3)
    tele.UpWithJump()
    time.sleep(0.2)
    tele._LeftWithAttack_KannaFor(1.5)
    time.sleep(0.1)
    jump.Down()
    time.sleep(0.1)
    jump.Left()
    time.sleep(0.2)
    # cover skip, get on p2
    tele._LeftWithAttack_KannaFor(1)
    time.sleep(0.4)
    walk.LeftFor(0.3)
    tele.UpWithJump()
    time.sleep(0.2)
    #cover left platform til end, jump down, back to start.
    tele._LeftWithAttack_KannaFor(1.3)
    time.sleep(0.1)
    jump.Down()
    time.sleep(0.1)
    jump.Left()
    time.sleep(0.2)
    tele._LeftWithAttack_KannaFor(1.3)
    time.sleep(2)

