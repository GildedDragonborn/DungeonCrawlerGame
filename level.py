import pygame
import random
import math
import json
from typing import Tuple
from room import room


class level:

    def __init__(self, seed: int):
        self.__maxWidth = 50 # max number of rooms high the map can be
        self.__maxHeight = 50 # max number of rooms wide the map can be
        self.__startX = 25 # origin X-coord for spawn room
        self.__startY = 25  # origin Y-coord for spawn room
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

    def getNextRoom(self, x, y) -> int:
        return int(self.__mapLayout[y][x])

    def mapGen(self, seed: int): # Level generation, *pain* TODO:Make a pregenned seed to test level generation
        if seed == 33667333:
            with open('GameData/pregennedLevels.json') as inFile:
                data = json.load(inFile)
                array = data[0]["levelLayout"]
                self.__startX = data[0]["startX"]
                self.__startY = data[0]["startY"]
                return array
        else:
            # makes an array of int "0" which is the id of blank rooms
            array = [[0] * self.maxWidth for i in range(self.__maxHeight)]
        return array
