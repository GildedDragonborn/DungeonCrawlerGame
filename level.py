import pygame
import random
import math
import json
from typing import Tuple
from room import room


class level:

    def __init__(self, seed: int):
        self.__maxWidth = 20 # max number of rooms high the map can be
        self.__maxHeight = 20 # max number of rooms wide the map can be
        self.__levelSize = 50  # Number of rooms excluding boss room
        self.__startX = 25 # origin X-coord for spawn room
        self.__startY = 25  # origin Y-coord for spawn room
        self.__mapLayout = [[0] * self.maxWidth for i in range(self.__maxHeight)] # makes an array of int "0" which is the id of blank rooms
        self.__mapLayout = self.mapGen(seed)


    @property
    def maxWidth(self) -> int:
        return self.__maxWidth

    @property
    def maxHeight(self) -> int:
        return self.__maxHeight

    @property
    def mapLayout(self):
        return self.__mapLayout

    @property
    def startX(self) -> int:
        return self.__startX

    @property
    def startY(self) -> int:
        return self.__startY

    @property
    def levelSize(self) -> int:
        return self.__levelSize

    def getNextRoom(self, x, y) -> int:
        try:
            return int(self.__mapLayout[y][x])
        except IndexError:
            return 0

    def mapGen(self, seed: int): # Level generation, *pain* TODO:Make a pregenned seed to test level generation
        if seed == 33667333:
            with open('GameData/pregennedLevels.json') as inFile:
                data = json.load(inFile)
                array = data[0]["levelLayout"]
                self.__startX = data[0]["startX"]
                self.__startY = data[0]["startY"]
                return array
        else:
            array = self.primsDungeonGen()
            self.gamifyLevel(array)
        return array

    def primsDungeonGen(self):
        allRooms = []
        newMap = [[0] * self.maxWidth for i in range(self.__maxHeight)]
        startingEdge: int = random.randrange(3)
        if startingEdge == 0:
            randomCoord: int = random.randrange(19)
            startingCoord = (0, randomCoord)
            self.__startX = 0
            self.__startY = randomCoord
        elif startingEdge == 1:
            randomCoord: int = random.randrange(19)
            startingCoord = (randomCoord, 0)
            self.__startX = randomCoord
            self.__startY = 0
        elif startingEdge == 2:
            randomCoord: int = random.randrange(19)
            startingCoord = (19, randomCoord)
            self.__startX = 19
            self.__startY = randomCoord
        elif startingEdge == 3:
            randomCoord: int = random.randrange(19)
            startingCoord = (randomCoord, 19)
            self.__startX = randomCoord
            self.__startY = 19

        allRooms.append((self.__startX, self.__startY))

        bossRoom = (random.randrange(19), random.randrange(19))
        while bossRoom == (self.__startX, self.__startY):
            bossRoom = (random.randrange(19), random.randrange(19))

        currentX = self.__startX
        currentY = self.__startY
        newMap[currentY][currentX] = 1
        print(currentX, currentY)
        i = 0
        try:
            while i <= self.__levelSize:
                found = False
                while not found:
                    if newMap[currentY][currentX] == 0:
                        newMap[currentY][currentX] = 1
                    direction = random.randrange(4)
                    if direction == 0:
                        if currentX > 0:
                            if newMap[currentY][currentX-1] == 0:
                                #newMap[currentY][currentX] = newMap[currentY][currentX] + 1
                                currentX = currentX-1
                                allRooms.append((currentY, currentX))
                                i = i+1
                                found = True
                            elif newMap[currentY][currentX-1] == 1:
                                currentX = currentX - 1
                                found = True
                    elif direction == 1:
                        if currentY > 0:
                            if newMap[currentY-1][currentX] == 0:
                                #newMap[currentY][currentX] = newMap[currentY][currentX] + 1
                                currentY = currentY-1
                                allRooms.append((currentY, currentX))
                                i = i + 1
                                found = True
                            elif newMap[currentY-1][currentX] == 1:
                                currentY = currentY - 1
                                found = True
                    elif direction == 2:
                        if currentX < 19:
                            if newMap[currentY][currentX+1] == 0:
                                #newMap[currentY][currentX] = newMap[currentY][currentX] + 1
                                currentX = currentX+1
                                allRooms.append((currentY, currentX))
                                i = i+1
                                found = True
                            elif newMap[currentY][currentX+1] == 1:
                                currentX = currentX + 1
                                found = True
                    elif direction == 3:
                        if currentY < 19:
                            if newMap[currentY+1][currentX] == 0:
                                #newMap[currentY][currentX] = newMap[currentY][currentX] + 1
                                currentY = currentY+1
                                allRooms.append((currentY, currentX))
                                i = i + 1
                                found = True
                            elif newMap[currentY+1][currentX] == 1:
                                currentY = currentY + 1
                                found = True
        except IndexError:
            pass
        print(allRooms)
        return newMap

    def gamifyLevel(self, gamify):
        numConnections: [int] = []
        for i in range(len(gamify)):
            for j in range(len(gamify[i])):
                numConnections = []
                if gamify[j][i] == 0:
                    continue
                elif i == 0:
                    if j != 0:
                        if gamify[j-1][i] != 0:
                            numConnections.append(1)
                    if gamify[j][i + 1] != 0:
                        numConnections.append(2)
                    if j != 19:
                        if gamify[j+1][i] != 0:
                            numConnections.append(3)
                elif i == 19:
                    if gamify[j][i-1] != 0:
                        numConnections.append(0)
                    if j != 0:
                        if gamify[j - 1][i] != 0:
                            numConnections.append(1)
                    elif j != 19:
                        if gamify[j + 1][i] != 0:
                            numConnections.append(3)
                else:
                    if gamify[j][i-1] != 0:
                        numConnections.append(0)
                    if j != 0:
                        if gamify[j - 1][i] != 0:
                            numConnections.append(1)
                    if gamify[j][i + 1] != 0:
                        numConnections.append(2)
                    if j != 19:
                        if gamify[j + 1][i] != 0:
                            numConnections.append(3)
                # BELOW ASSIGNS ROOM DATA
                if numConnections == []:
                    gamify[j][i] = 0
                elif numConnections == [0]:
                    gamify[j][i] = 8
                elif numConnections == [1]:
                    gamify[j][i] = 7
                elif numConnections == [2]:
                    gamify[j][i] = 12
                elif numConnections == [3]:
                    gamify[j][i] = 6
                elif numConnections == [0, 1]:
                    gamify[j][i] = 4
                elif numConnections == [0, 2]:
                    gamify[j][i] = 13
                elif numConnections == [0, 3]:
                    gamify[j][i] = 5
                elif numConnections == [1, 2]:
                    gamify[j][i] = 10
                elif numConnections == [1, 3]:
                    gamify[j][i] = 3
                elif numConnections == [2, 3]:
                    gamify[j][i] = 11
                elif numConnections == [0, 1, 2]:
                    gamify[j][i] = 15
                elif numConnections == [0, 1, 3]:
                    gamify[j][i] = 2
                elif numConnections == [0, 2, 3]:
                    gamify[j][i] = 14
                elif numConnections == [1, 2, 3]:
                    gamify[j][i] = 9
                elif numConnections == [0, 1, 2, 3]:
                    gamify[j][i] = 1
        print(gamify)
        return gamify