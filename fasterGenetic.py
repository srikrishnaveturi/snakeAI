#this is the same code for the algo, just using multiprocessing to make the scoring of each population faster

import concurrent.futures
import numpy as np
import cv2
import random
import time
import math

def initialize():
    #the frame is divided into 20 boxes of 15 px rows and columns
    global snakeList,score
    xBlock = random.randint(0,17)
    yBlock = random.randint(0,17)
    x1 = xBlock * 15
    y1 = yBlock * 15
    snakeList = [[x1,y1],[x1+15,y1],[x1+30,y1]] #this list contains all the blocks that are accupied by the snake
    img = np.zeros((300,300,3), np.uint8)
    treatSpawn()
    score = 0

def treatSpawn():
    global treatX1, treatY1
    treatBlockx = random.randint(0, 19)
    treatBlocky = random.randint(0, 19)
    while ([treatBlockx, treatBlocky] in snakeList):
        treatBlockx = random.randint(0, 19)
        treatBlocky = random.randint(0, 19)
    treatX1 = treatBlockx * 15
    treatY1 = treatBlocky * 15

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


def observations(dir):
    #print("in observations {}".format(dir))
    global snakeList,treatX1,treatY1
    flag = 0
    headX = snakeList[0][0]
    headY = snakeList[0][1]
    x = headX
    y = headY
    surroundings = []

    #left
    while (x > 0):


        if [x, y] in snakeList or (x < 0 or x > 300 or y < 0 or y > 300):
            surroundings.append(-1)
            flag = 1
            break
        elif x == treatX1 and y == treatY1:
            surroundings.append(1)
            flag = 1
            break
        x -= 15
    if flag == 0:
        surroundings.append(0.5)
    flag = 0
    x = headX
    y = headY

    #left-up
    while(x > 0 and y > 0):

        if [x, y] in snakeList or (x < 0 or x > 300 or y < 0 or y > 300):
            surroundings.append(-1)
            flag = 1
            break
        elif x - 15 == treatX1 and y - 15 == treatY1:
            surroundings.append(1)
            flag = 1
            break
        x -= 15
        y -= 15
    if flag == 0:
        surroundings.append(0.5)
    flag = 0
    x = headX
    y = headY

    #up
    while (y > 0):

        if [x, y] in snakeList or (x < 0 or x > 300 or y < 0 or y > 300):
            surroundings.append(-1)
            flag = 1
            break
        elif x == treatX1 and y == treatY1:
            surroundings.append(1)
            flag = 1
            break
        y -= 15
    if flag == 0:
        surroundings.append(0.5)
    flag = 0
    x = headX
    y = headY

    #right up
    while (x < 300 and y > 0):

        if [x, y] in snakeList or (x < 0 or x > 300 or y < 0 or y > 300):
            surroundings.append(-1)
            flag = 1
            break
        elif x + 15 == treatX1 and y - 15 == treatY1:
            surroundings.append(1)
            flag = 1
            break
        x += 15
        y -= 15
    if flag == 0:
        surroundings.append(0.5)
    flag = 0
    x = headX
    y = headY

    #right
    while (x < 300):


        if [x, y] in snakeList or (x < 0 or x > 300 or y < 0 or y > 300):
            surroundings.append(-1)
            flag = 1
            break
        elif x == treatX1 and y == treatY1:
            surroundings.append(1)
            flag = 1
            break
        x += 15

    if flag == 0:
        surroundings.append(0.5)
    flag = 0
    x = headX
    y = headY

    #right down
    while (x < 300 and y < 300):

        if [x, y] in snakeList or (x < 0 or x > 300 or y < 0 or y > 300):
            surroundings.append(-1)
            flag = 1
            break
        elif x + 15 == treatX1 and y + 15 == treatY1:
            surroundings.append(1)
            flag = 1
            break
        x += 15
        y += 15
    if flag == 0:
        surroundings.append(0.5)
    flag = 0
    x = headX
    y = headY

    #down
    while(y < 300):


        if [x,y] in snakeList or (x < 0 or x > 300 or y < 0 or y > 300):
            surroundings.append(-1)
            flag = 1
            break
        elif x == treatX1 and y == treatY1:
            surroundings.append(1)
            flag = 1
            break
        y += 15
    if flag == 0:
        surroundings.append(0.5)
    flag = 0
    x = headX
    y= headY

    #down left
    while (x > 0 and y < 300):

        if [x, y] in snakeList or (x < 0 or x > 300 or y < 0 or y > 300):
            surroundings.append(-1)
            flag = 1
            break
        elif x - 15 == treatX1 and y + 15 == treatY1:
            surroundings.append(1)
            flag = 1
            break
        x -= 15
        y += 15
    if flag == 0:
        surroundings.append(0.5)
    flag = 0
    x = headX
    y = headY

    if dir == 'up':
        surroundings.append(-1)
        surroundings.append(0)
        surroundings.append(0)
        surroundings.append(0)
    elif dir == 'down':
        surroundings.append(0)
        surroundings.append(-1)
        surroundings.append(0)
        surroundings.append(0)
    elif dir == 'left':
        surroundings.append(0)
        surroundings.append(0)
        surroundings.append(-1)
        surroundings.append(0)
    elif dir == 'right':
        surroundings.append(0)
        surroundings.append(0)
        surroundings.append(0)
        surroundings.append(-1)
    else:
        surroundings.append(+1)
        surroundings.append(+1)
        surroundings.append(-1)
        surroundings.append(+1)

    return surroundings

####################################
#####################################

import heapq

def generateBrain():
    hiddenLayer1 = np.array([[random.uniform(-1,1) for _ in range(12)] for _ in range(8)])
    hiddenLayer2 = np.array([[random.uniform(-1,1) for _ in range(9)] for _ in range(8)])
    outputLayer = np.array([[random.uniform(-1,1) for _ in range(9)] for _ in range(4)])
    return[hiddenLayer1,hiddenLayer2,outputLayer]

def getMove(currentBrain):
    global snakeList, img, treatX1, treatY1, score,dir
    dir = ' '
    dead = 0
    turns = 0
    initialize()
    #print("in current brainzzzzzzz")
    while not dead and turns < 150:
        turns+=1
        inputVector = observations(dir)
        hiddenLayer1 = currentBrain[0]
        hiddenLayer2 = currentBrain[1]
        outputLayer = currentBrain[2]
        #print("in current brain")
        # forward propogation
        hiddenResult1 = np.array(
            [math.tanh(np.dot(inputVector, hiddenLayer1[i])) for i in range(hiddenLayer1.shape[0])] + [1])
        hiddenResult2 = np.array(
            [math.tanh(np.dot(hiddenResult1, hiddenLayer2[i])) for i in range(hiddenLayer2.shape[0])] + [1])
        outputResult = np.array([math.tanh(np.dot(hiddenResult2, outputLayer[i])) for i in range(outputLayer.shape[0])])
        key = np.argmax(outputResult)
        img = np.zeros((300, 300, 3), np.uint8)
        cv2.rectangle(img, (treatX1, treatY1), (treatX1 + 15, treatY1 + 15), (0, 255, 255), -1)
        for i in range(len(snakeList)):
            cv2.rectangle(img, (snakeList[i][0], snakeList[i][1]), (snakeList[i][0] + 15, snakeList[i][1] + 15),
                          (255, 255, 255), -1)
        if snakeList[0][0] < 0 or snakeList[0][0] + 15 > 300 or snakeList[0][1] < 0 or snakeList[0][1] + 15 > 300:
            cv2.destroyAllWindows()
            #print("game over")
            #print("Final score = {}".format(score))
            dead = 1
        elif key == 0:
            #print("up")
            dir = 'up'
        elif key == 1:
            #print("down")
            dir = 'down'
        elif key == 2:
            #print("left")
            dir = 'left'
        elif key == 3:
            #print("right")
            dir = 'right'
        if snakeList[0][0] == treatX1 and snakeList[0][1] == treatY1:
            score += 1
            turns = 0
            #print("score = {}".format(score))
            snakeList.append([treatX1, treatY1])
            treatSpawn()
        if dir != ' ':
            move(dir)
        if len(snakeList) > 1:
            if snakeList[0] in snakeList[1:]:
                cv2.destroyAllWindows()
                #print("game over")
                #print("final score = {}".format(score))
                dead = 1
        cv2.imshow("image", img)
        cv2.waitKeyEx(1)
        time.sleep(0.1)

    return score


def mutate(brain):
    newBrain = []
    for layer in brain:
        newLayer = np.copy(layer)
        for i in range(newLayer.shape[0]):
            #for j in range(newLayer.shape[1]):
            if random.uniform(0,1) < 0.5: #mutation chance
                newLayer[i] += random.uniform(0,1)*(0.25) #mutation size
        newBrain.append(newLayer)
    return newBrain

def reproduce(top_25,populationSize):
    newPopulation =[]
    for brain in top_25:
        newPopulation.append(brain)
    for brain in mutate(top_25):
        newPopulation.append(brain)
    for _ in range(populationSize-2*len(top_25)):
        newPopulation.append(generateBrain())
    return newPopulation

def oneGeneration(populationSize,population,numTrials):
    scores = []

    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = executor.map(getMove,population)
        for result in results:
             scores.append(result)
        print(scores)


    # for i in range(populationSize):
    #     maxScore = 0
    #
    #
    #     for j in range(numTrials):
    #         currentBrain = population[i]
    #         score = getMove(currentBrain)



        #     if maxScore < score:
        #          maxScore = score
        # scores.append(maxScore)


    top_25_scores = heapq.nlargest(int(populationSize/4), range(len(scores)), scores.__getitem__)
    #print(len(top_25_scores))
    #print(len(scores))
    #print(top_25_scores)
    #print(len(population))
    #print(populationSize)
    top25 = [population[i] for i in top_25_scores][::-1]
    #population = reproduce(top25,populationSize)
    return top25,scores


def GeneticPlayer(populationSize):
    population = [generateBrain() for _ in range(populationSize)]
    for i in range(1000):
        print('Gen {} :'.format(i))
        if i == 999:
            inp = input("last generation")
        top25,scores = oneGeneration(populationSize,population,1)
        cv2.destroyAllWindows()
        population = reproduce(top25,populationSize)



if __name__ == '__main__':
    GeneticPlayer(100)
