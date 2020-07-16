import numpy as np
import cv2
import random
import time
import math

def initialize():
    #the frame is divided into 20 boxes of 15 px rows and columns
    global snakeList,score
    xBlock = random.randint(0,19)
    yBlock = random.randint(0,19)
    x1 = xBlock * 15
    y1 = yBlock * 15
    snakeList = [[x1,y1]] #this list contains all the blocks that are accupied by the snake
    img = np.zeros((300,300,3), np.uint8)
    treatSpawn()
    score = 0

def treatSpawn():
    global treatX1, treatY1
    treatBlock = random.randint(0, 19)
    treatBlock = random.randint(0, 19)
    while ([treatBlock, treatBlock] in snakeList):
        treatBlock = random.randint(0, 19)
        treatBlock = random.randint(0, 19)
    treatX1 = treatBlock * 15
    treatY1 = treatBlock * 15

def move(direction):
    global snakeList
    for i in range(1,len(snakeList)):
        snakeList[len(snakeList)-i][1] = snakeList[len(snakeList)-i-1][1]
        snakeList[len(snakeList)-i][0] = snakeList[len(snakeList)-i-1][0]
    if direction == "up":
        snakeList[0][1]-=15
    elif direction == "down":
        snakeList[0][1]+=15
    elif direction == "left":
        snakeList[0][0]-=15
    elif direction == "right":
        snakeList[0][0]+=15

def play(key):
    global snakeList,img,treatX1,treatY1,score
    dir = ' '
    dead = 0
    #while idhar aayega
    img = np.zeros((300,300,3), np.uint8)
    cv2.rectangle(img,(treatX1, treatY1), (treatX1+15, treatY1+15), (0, 255, 255), -1)
    for i in range(len(snakeList)):
            cv2.rectangle(img,(snakeList[i][0], snakeList[i][1]), (snakeList[i][0]+15, snakeList[i][1]+15), (255, 255, 255), -1)
    if snakeList[0][0] < 0 or snakeList[0][0] + 15 > 300 or snakeList[0][1] < 0 or snakeList[0][1] + 15 > 300:
        cv2.destroyAllWindows()
        print("game over")
        print("Final score = {}".format(score))
        dead = 1
    elif key == 0:
        print("up")
        dir = 'up'
    elif key == 1:
        print("down")
        dir = 'down'
    elif key == 2:
        print("left")
        dir = 'left'
    elif key == 3:
        print("right")
        dir = 'right'
    if snakeList[0][0] == treatX1 and snakeList[0][1] == treatY1:
        score+=1
        print("score = {}".format(score))
        snakeList.append([treatX1,treatY1])
        treatSpawn()
    if dir != ' ':
        move(dir)
    if len(snakeList) > 1:
        if snakeList[0] in snakeList[1:]:
            cv2.destroyAllWindows()
            print("game over")
            print("final score = {}".format(score))
            dead = 1
    cv2.imshow("image",img)
    cv2.waitKeyEx(1)
    time.sleep(0.5)
    if dead:
        return score

def check(x,y):
    global snakeList,treatX1,treatY1
    if [x,y] in snakeList:
        return -1
    elif x == treatX1 and y == treatY1:
        return 1
    elif x < 0 or x > 300 or y < 0 or y > 300:
        return -1
    else:
        return 0

def observations():
    global snakeList,score
    headX = snakeList[0][0]
    headY = snakeList[0][1]
    x = headX - 45
    y = headY - 45
    surroundings = []
    while x <= headX + 45:
        y = headY - 45
        while y <= headY + 45:
            surroundings.append(check(x,y))
            y+=15
        x+=15
    surroundings = np.array([surroundings])
    return surroundings

class Game():
    def __init__(self):
        initialize()
        play(-1)

    def play(self,direction):
        return play(key=direction)

game = Game()
game.play(-1)