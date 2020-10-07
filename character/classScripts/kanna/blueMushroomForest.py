import time
import character.movement.teleport as tele
import character.movement.jump as jump
import character.movement.walk as walk


def main():
    ##### Go here ####
    for _ in range(40):
        tele._RightWithAttack_KannaFor(5)
        time.sleep(0.1)
        tele._LeftWithAttack_KannaFor(4)
        time.sleep(0.1)
        tele.UpWithJump()
        time.sleep(0.1)
        tele._RightWithAttack_KannaFor(1)
        time.sleep(0.1)
        tele.UpWithJump()
        time.sleep(0.1)
        tele._LeftWithAttack_KannaFor(2)
        jump.LeftFor(1)
        walk.turnRight()
        time.sleep(0.1)