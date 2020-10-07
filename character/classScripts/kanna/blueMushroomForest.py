import time
import character.movement.teleport as tele
import character.movement.jump as jump
import character.movement.walk as walk
import character.movement.upperRowAttack as ura


def main():
    ##### Go here ####
    for _ in range(10):
        tele._RightWithAttack_KannaFor(3)
        time.sleep(0.1)
        tele._LeftWithAttack_KannaFor(2)
        time.sleep(0.1)
        tele.UpWithJump()
        time.sleep(0.1)
        walk.turnRight()
        ura.W()
        time.sleep(0.1)
        tele._RightWithAttack_KannaFor(1.5)
        time.sleep(0.1)
        walk.LeftFor(1)
        tele.UpWithJump()
        time.sleep(0.1)
        tele._LeftWithAttack_KannaFor(2)
        jump.LeftFor(1.5)
        walk.turnRight()
        time.sleep(0.1)