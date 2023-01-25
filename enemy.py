import pygame
import random
import math
import weapon
import spell
import battleEnemy
from typing import List
import json


class enemy:  # TODO: Enemy Class
    def __init__(self, enemyID: int):
        with open('GameData/enemyData.json') as inFile:
            data = json.load(inFile)
            self.__enemyID: int = data[enemyID]["enemyID"]
            self.__name: str = data[enemyID]["name"]
            self.__currX: int = 0 # current X coord
            self.__currY: int = 0 # current Y coord
            self.__behavior: int = data[enemyID]["behavior"] # behavior determined by an int
            self.__speed: int = data[enemyID]["speed"] # number of tiles movable per player move
            self.__patrolStart: tuple = tuple(data[enemyID]["patrolStart"])
            self.__patrolEnd: tuple = tuple(data[enemyID]["patrolEnd"])
            self.__spriteName: str = data[enemyID]["spriteName"]
            self.__spritePath: str = data[enemyID]["spritePath"]
            encounterNum: int = random.randint(0, len(data[enemyID]["encounters"])-1) # assigns a random encounter value from list in json file
        with open('GameData/encounterPossibilities.json') as inFile:
            data = json.load(inFile)
            self.__encounter: [battleEnemy] = []
            temp: list = list(data[encounterNum]["enemies"])
            for i in range(len(temp)):
                newEnemy = battleEnemy.battleEnemy(temp[i])
                self.__encounter.append(newEnemy)

    @property
    def enemyID(self) -> int:
        return self.__enemyID

    @property
    def name(self) -> str:
        return self.__name

    @property
    def behavior(self) -> int:
        return self.__behavior

    @property
    def speed(self):
        return self.__speed

    @property
    def spritePath(self):
        return self.__spritePath

    @property
    def spriteName(self):
        return self.__spriteName

    @property
    def currX(self):
        return self.__currX

    @property
    def currY(self):
        return self.__currY

    @property
    def encounter(self) -> list:
        return self.__encounter

    def setX(self, x: int):
        self.__currX = x

    def setY(self, y: int):
        self.__currY = y

    def movement(self, playerX: int, playerY: int):
        if self.behavior == 0 or self.speed == 0: # Stationary
            return 0
        elif self.behavior == 1: # Pursuer: moves shortest path to player
            return 0
        elif self.behavior == 2: # Patroller: moves between 2 points (patrolStart and patrolEnd) at speed
            return 0
        elif self.behavior == 3: # Miniboss
            return 0
        elif self.behavior == 4: # Boss
            return 0
        else: # ERROR: NO BEHAVIOR, PRINT TO CONSOLE AND DEFAULT TO STATIONARY
            print("BEHAVIOR_ERROR: MISSING ENEMY BEHAVIOR")
            return 0
        pass