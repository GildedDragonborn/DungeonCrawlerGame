import pygame
import random
import math
import weapon
import spell
from typing import List
import json


class enemy:  # TODO: Enemy Class
    def __init__(self, enemyID: int):
        with open('GameData/enemyData.json') as inFile:
            data = json.load(inFile)
            self.__enemyID: int = data[enemyID]["enemyID"]
            self.__name: str = data[enemyID]["name"]
            self.__MaxHealth: int = data[enemyID]["MaxHealth"]
            self.__currHealth: int = data[enemyID]["currHealth"]
            self.__expVal: int = data[enemyID]["expVal"]
            self.__behavior: int = data[enemyID]["behavior"] # behavior determined by an int
            self.__speed: int = data[enemyID]["speed"] # number of tiles movable per player move
            self.__patrolStart: tuple = tuple(data[enemyID]["patrolStart"])
            self.__patrolEnd: tuple = tuple(data[enemyID]["patrolEnd"])
            self.__attacks: List[weapon] = list(data[enemyID]["attacks"])
            self.__spells: List[spell] = list(data[enemyID]["spells"])
            self.__spriteName: str = data[enemyID]["spriteName"]
            self.__spritePath: str = data[enemyID]["spritePath"]

    @property
    def enemyID(self) -> int:
        return self.__enemyID

    @property
    def name(self) -> str:
        return self.__name

    @property
    def MaxHealth(self) -> int:
        return self.__MaxHealth

    @property
    def currHealth(self) -> int:
        return self.__currHealth

    @property
    def expVal(self) -> int:
        return self.__expVal

    @property
    def behavior(self) -> int:
        return self.__behavior

    @property
    def attacks(self):
        return self.__attacks

    @property
    def speed(self):
        return self.__speed

    @property
    def spells(self):
        return self.__spells
    @property
    def spritePath(self):
        return self.__spritePath

    @property
    def spriteName(self):
        return self.__spriteName

    def getAttack(self, i: int) -> weapon:
        return self.__attacks[i]

    def takeDamage(self, dmg: int) -> bool:
        self.currHealth = self.currHealth - dmg
        if self.currHealth <= 0:
            return True
        else:
            return False

    def dealDamage(self, dmg: int) -> int:
        multiplier: int = round(random.uniform(0.8, 1.2), 1)
        if random.randint(1, 20) == 20:
            multiplier = 2
        choice: int = random.randint(0, len(self.__attacks)-1)
        if self.getAttack(choice) is not none:
            return int(self.getAttack(choice) * multiplier)
        else:
            return 1

    def movement(self, behavior: int, speed: int, playerX: int, playerY: int):
        if behavior == 0 or speed == 0: # Stationary
            return 0
        elif behavior == 1: # Pursuer: moves shortest path to player
            pass
        elif behavior == 2: # Patroller: moves between 2 points (patrolStart and patrolEnd) at speed
            pass
        elif behavior == 3: # Miniboss
            pass
        elif behavior == 4: # Boss
            pass
        else: # ERROR: NO BEHAVIOR, PRINT TO CONSOLE AND DEFAULT TO STATIONARY
            print("BEHAVIORERROR: MISSING ENEMY BEHAVIOR")
            return 0
        pass