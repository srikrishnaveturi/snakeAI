from snake import *

env = Game()
key = -1
while True:
    direction = cv2.waitKeyEx(1)

    if direction == 2490368:
        key = 0

    elif direction == 2621440:
        key = 1

    elif direction == 2424832:
        key = 2

    elif direction == 2555904:
        key = 3

    dead,int = env.play(key)
    if dead:
        cv2.destroyAllWindows()
        break