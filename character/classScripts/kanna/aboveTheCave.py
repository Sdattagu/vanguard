import time
import character.movement.teleport as tele
import character.movement.jump as jump
import character.movement.walk as walk
import controllers.keyboardCtrl as kbd
import bindings.bottomLetterRow as blr
import bindings.bottomFnRow as bfr
import bindings.arrowKeys as ak
import character.movement.upperRowAttack as upperRowAttack

def main():
    # /Start bottom row
    tele._RightWithAttack_KannaFor(2.5)
    time.sleep(0.2)
    upperRowAttack.W()
    time.sleep(0.2)
    tele._RightWithAttack_KannaFor(2.5)
    time.sleep(0.2)
    upperRowAttack.W()
    time.sleep(1.3)
    upperRowAttack.Q()
    time.sleep(0.3)
    tele._RightWithAttack_KannaFor(2)
    time.sleep(0.2)
    upperRowAttack.W()
    time.sleep(0.5)
    tele._RightWithAttack_KannaFor(1)
    time.sleep(0.5)
    # /End bottom row
    walk.LeftFor(2)
    tele.UpWithJump()
    time.sleep(0.2)
    tele._LeftWithAttack_KannaFor(2.5)
    time.sleep(0.1)
    jump.Down()
    time.sleep(0.1)
    jump.Left()
    time.sleep(0.2)
    # cover skip, get on p2
    tele._LeftWithAttack_KannaFor(1)
    time.sleep(0.4)
    walk.LeftFor(1.5)
    tele.UpWithJump()
    time.sleep(0.2)
    # run p2 left, get on triple plat top
    tele._LeftWithAttack_KannaFor(3)
    time.sleep(0.2)
    jump.Down()
    time.sleep(0.1)
    jump.Left()
    time.sleep(0.2)
    upperRowAttack.W()
    tele.Down()
    time.sleep(0.2)
    tele.Down()
    time.sleep(0.5)
    upperRowAttack.E()