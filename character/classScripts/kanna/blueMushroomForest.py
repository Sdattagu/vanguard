import time
import character.movement.teleport as tele
import character.movement.jump as jump
import character.movement.walk as walk


def main():
    ##### Go here ####
    for _ in range(3):
        tele._RightWithAttack_KannaFor(2.5)
        time.sleep(0.1)
        tele._LeftWithAttack_KannaFor(2)
        time.sleep(0.1)
        tele.Up()
        time.sleep(0.1)
    walk.LeftFor(3)
    for _ in range(3):
        tele._RightWithAttack_KannaFor(2.5)
        time.sleep(0.1)
        tele._LeftWithAttack_KannaFor(2)
        time.sleep(0.1)
        tele.Up()
        time.sleep(0.1)
