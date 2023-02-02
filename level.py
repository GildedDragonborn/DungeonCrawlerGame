import pygame
import random
import math
import json
from typing import Tuple
from room import room


class level:

    def __init__(self, seed: int):
        self.__levelID = seed
        self.__maxWidth = 10 # max number of rooms high the map can be
        self.__maxHeight = 10 # max number of rooms wide the map can be
        self.__layer = 1 # Depth of the dungeon
        self.__levelSize = 25  # Number of rooms excluding boss room
        self.__startX = 25 # origin X-coord for spawn room
        self.__startY = 25  # origin Y-coord for spawn room
        self.__mapLayout = [[0,False,0,0,False,"a"] * self.maxWidth for i in range(self.__maxHeight)] # makes an array of int "0" which is the id of blank rooms
        self.__mapLayout = self.mapGen(seed)
        with open('GameData/currentFloor.json', "w") as outfile:
            dictionary = {
                "levelID": seed,
                "startX": self.__startX,
                "startY": self.__startY,
                "Level height": self.__maxHeight,
                "Level width": self.__maxWidth,
                "levelLayout": self.__mapLayout,
                "roomLayout": [[[]*12 for j in range(12)]*self.maxWidth for i in range(self.__maxHeight)]
            }
            json.dump(dictionary, outfile, indent=1)


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

    def getNextRoom(self, x, y) -> room: #gets the next room's roomID
        try:
            with open('GameData/currentFloor.json') as inFile:
                data = json.load(inFile)
                temp = room(data["levelLayout"][y][x][0],1,x,y,data["levelLayout"][y][x][1],data["levelLayout"][y][x][2], data["levelLayout"][y][x][3], data["levelLayout"][y][x][4], data["levelLayout"][y][x][5], data["levelLayout"][y][x][6])
                return temp
        except IndexError:
            return 0

    def getNextRoomHostile(self, x, y):
        try:
            return bool(self.__mapLayout[y][x][1])
        except IndexError:
            return False

    def getNextRoomNumEnemies(self, x, y):
        try:
            return int(self.__mapLayout[y][x][2])
        except IndexError:
            return 0

    def getNextRoomEnemyVar(self, x, y):
        try:
            return int(self.__mapLayout[y][x][3])
        except IndexError:
            return 0

    def getNextRoomID(self, x, y):
        try:
            return int(self.__mapLayout[y][x][0])
        except IndexError:
            return 0

    def getNextRoomVisited(self, x, y):
        try:
            return bool(self.__mapLayout[y][x][4])
        except IndexError:
            return True

    def getNextRoomVar(self, x, y):
        try:
            return str(self.__mapLayout[y][x][5])
        except IndexError:
            return "a"

    def markVisited(self, x, y):
        self.__mapLayout[y][x][4] = True
        with open('GameData/currentFloor.json', "w") as outfile:
            dictionary = {
                "levelID": self.__levelID,
                "startX": self.__startX,
                "startY": self.__startY,
                "Level height": self.__maxHeight,
                "Level width": self.__maxWidth,
                "levelLayout": self.__mapLayout
            }
            json.dump(dictionary, outfile, indent=4)

    def mapGen(self, seed: int): # Level generation, *pain*
        if seed == 33667333:
            with open('GameData/pregennedLevels.json') as inFile:
                data = json.load(inFile)
                array = data[0]["levelLayout"]
                self.__startX = data[0]["startX"]
                self.__startY = data[0]["startY"]
                self.__maxHeight = data[0]["Level height"]
                self.__maxWidth = data[0]["Level width"]
                return array
        else:
            array = self.primsDungeonGen()
            self.gamifyLevel(array)
        return array

    def primsDungeonGen(self):
        allRooms = []
        newMap = [[0] * self.maxWidth for i in range(self.__maxHeight)]
        randomCoord: int = random.randrange(3, 7)
        startingCoord = (randomCoord, 9)
        self.__startX = randomCoord
        self.__startY = 9

        allRooms.append((self.__startX, self.__startY))

        bossRoom = (random.randrange(6), random.randrange(3, 7))
        while bossRoom == (self.__startX, self.__startY):
            bossRoom = (random.randrange(6), random.randrange(3, 7))

        currentX = self.__startX
        currentY = self.__startY

        print("Boss:", bossRoom)
        print("StartingCoords:", self.__startX, self.__startY)
        #newMap[bossRoom[1]][bossRoom[0]] = 99
        i = 0
        try:
            while i <= self.__levelSize:
                found = False
                while not found:
                    if newMap[currentY][currentX] == 0:
                        newMap[currentY][currentX] = 1
                    direction = random.randrange(6)
                    if direction == 0:
                        if currentX > 0:
                            if newMap[currentY][currentX-1] == 0:
                                currentX = currentX-1
                                allRooms.append((currentY, currentX))
                                i = i+1
                                found = True
                            elif newMap[currentY][currentX-1] == 1:
                                currentX = currentX - 1
                                found = True
                    elif direction >= 1 and direction <= 3:
                        if currentY > 0:
                            if newMap[currentY-1][currentX] == 0:
                                currentY = currentY-1
                                allRooms.append((currentY, currentX))
                                i = i + 1
                                found = True
                            elif newMap[currentY-1][currentX] == 1:
                                currentY = currentY - 1
                                found = True
                    elif direction == 4:
                        if currentX < 9:
                            if newMap[currentY][currentX+1] == 0:
                                currentX = currentX+1
                                allRooms.append((currentY, currentX))
                                i = i+1
                                found = True
                            elif newMap[currentY][currentX+1] == 1:
                                currentX = currentX + 1
                                found = True
                    elif direction == 5:
                        if currentY < 9:
                            if newMap[currentY+1][currentX] == 0:
                                currentY = currentY+1
                                allRooms.append((currentY, currentX))
                                i = i + 1
                                found = True
                            elif newMap[currentY+1][currentX] == 1:
                                currentY = currentY + 1
                                found = True
            print(allRooms)
            return newMap
        except IndexError:
            pass

    def gamifyLevel(self, gamify):
        numConnections: [int] = []
        numberRooms = 0
        bossRoom = False
        numSpecialRooms = random.randrange(int(self.__levelSize/10))
        while not bossRoom:
            for i in range(len(gamify)):
                for j in range(len(gamify[i])):
                    numConnections = []
                    specialRoom = random.randrange
                    if gamify[j][i] == 17:
                        continue
                    if gamify[j][i] == 0:
                        continue
                    elif i == 0:
                        if j != 0:
                            if gamify[j-1][i] != 0:
                                numConnections.append(1)
                        if gamify[j][i + 1] != 0:
                            numConnections.append(2)
                        if j != 9:
                            if gamify[j+1][i] != 0:
                                numConnections.append(3)
                    elif i == 9:
                        if gamify[j][i-1] != 0:
                            numConnections.append(0)
                        if j != 0:
                            if gamify[j - 1][i] != 0:
                                numConnections.append(1)
                        elif j != 9:
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
                        if j != 9:
                            if gamify[j + 1][i] != 0:
                                numConnections.append(3)
                    # BELOW ASSIGNS ROOM DATA
                    if numConnections == []:
                        gamify[j][i] = 0
                    elif numConnections == [0]:
                        gamify[j][i] = 8
                        numberRooms = numberRooms + 1
                        if bossRoom == False and i < self.__levelSize/2:
                            gamify[j][i] = 17
                            bossRoom = True
                    elif numConnections == [1]:
                        gamify[j][i] = 6
                        numberRooms = numberRooms + 1
                        if bossRoom == False and i < self.__levelSize/2:
                            gamify[j][i] = 17
                            bossRoom = True
                    elif numConnections == [2]:
                        gamify[j][i] = 12
                        numberRooms = numberRooms + 1
                        if bossRoom == False and i < self.__levelSize/2:
                            gamify[j][i] = 17
                            bossRoom = True
                    elif numConnections == [3]:
                        gamify[j][i] = 7
                        numberRooms = numberRooms + 1
                        if bossRoom == False and i < self.__levelSize/2:
                            gamify[j][i] = 17
                            bossRoom = True
                    elif numConnections == [0, 1]:
                        gamify[j][i] = 4
                        numberRooms = numberRooms + 1
                    elif numConnections == [0, 2]:
                        gamify[j][i] = 13
                        numberRooms = numberRooms + 1
                    elif numConnections == [0, 3]:
                        gamify[j][i] = 5
                        numberRooms = numberRooms + 1
                    elif numConnections == [1, 2]:
                        gamify[j][i] = 10
                        numberRooms = numberRooms + 1
                    elif numConnections == [1, 3]:
                        gamify[j][i] = 3
                        numberRooms = numberRooms + 1
                    elif numConnections == [2, 3]:
                        gamify[j][i] = 11
                        numberRooms = numberRooms + 1
                    elif numConnections == [0, 1, 2]:
                        gamify[j][i] = 15
                        numberRooms = numberRooms + 1
                    elif numConnections == [0, 1, 3]:
                        gamify[j][i] = 2
                        numberRooms = numberRooms + 1
                    elif numConnections == [0, 2, 3]:
                        gamify[j][i] = 14
                        numberRooms = numberRooms + 1
                    elif numConnections == [1, 2, 3]:
                        gamify[j][i] = 9
                        numberRooms = numberRooms + 1
                    elif numConnections == [0, 1, 2, 3]:
                        gamify[j][i] = 1
                        numberRooms = numberRooms + 1
            for i in range(len(gamify)):
                temp = ""
                for j in range(len(gamify[i])):
                    temp = temp + str(gamify[i][j]) + ", "
                print(temp)
        return gamify

        def incrLayer(self, currLayer):
            self.__layer = currLayer + 1

        def incrLevel(self):
            #pass #TODO: SEND TO LOADING SCREEN, GENERATE NEW LEVEL
            print("Thanks for playing my demo!")
            return false