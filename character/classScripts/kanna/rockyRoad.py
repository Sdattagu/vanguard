import time
import character.movement.teleport as tele
import character.movement.jump as jump
import character.movement.walk as walk
import character.movement.upperRowAttack as upperRowAttack


def main():
    ##### Go here ####
    for _ in range(2):
        upperRowAttack.Q()
        time.sleep(1)
        upperRowAttack.W()
        time.sleep(1)
        tele._RightWithAttack_KannaFor(4.5)
        time.sleep(0.1)
        tele._LeftWithAttack_KannaFor(0.8)
        time.sleep(0.5)
        upperRowAttack.E()
        time.sleep(0.5)
        tele.UpWithJump()
        walk.turnLeft()
        tele._LeftWithAttack_KannaFor(1)
        time.sleep(0.1)
        jump.LeftFor(0.8)
        time.sleep(0.1)
        tele._LeftWithAttack_KannaFor(2)
        time.sleep(0.1)
        jump.LeftFor(1.5)
        walk.turnRight()