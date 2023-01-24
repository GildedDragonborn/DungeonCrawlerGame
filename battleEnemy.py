import pygame
import random
import math
import weapon
import spell
from typing import List
import json
import os

class battleEnemy():
    def __init__(self, enemyID: int):
        with open('GameData/enemyData.json') as inFile:
            data = json.load(inFile)
            self.__enemyID: int = data[enemyID]["enemyID"]
            self.__name: str = data[enemyID]["name"]
            self.__MaxHealth: int = data[enemyID]["MaxHealth"]
            self.__currHealth: int = data[enemyID]["currHealth"]
            self.__expVal: int = data[enemyID]["expVal"]
            self.__attacks: List[weapon] = list(data[enemyID]["attacks"])
            self.__spells: List[spell] = list(data[enemyID]["spells"])
            self.__spriteName: str = data[enemyID]["spriteName"]
            self.__spritePath: str = data[enemyID]["spritePath"]

    @property
    def enemyID(self):
        return self.__enemyID

    @property
    def name(self):
        return self.__name

    @property
    def MaxHealth(self):
        return self.__MaxHealth

    @property
    def currHealth(self) -> int:
        return self.__currHealth

    @property
    def expVal(self) -> int:
        return self.__expVal

    @property
    def spells(self):
        return self.__spells

    @property
    def attacks(self):
        return self.__attacks

    @property
    def spritePath(self):
        return self.__spritePath

    @property
    def spriteName(self):
        return self.__spriteName

    def getAttack(self, i: int) -> weapon:
        return self.__attacks[i]

    def takeDamage(self, dmg: int) -> bool:
        self.__currHealth = self.__currHealth - i
        if self.currHealth <= 0:
            return True
        else:
            return False

    def dealDamage(self, dmg: int) -> int:
        multiplier: float = round(random.uniform(0.8, 1.2), 1)
        if random.randint(1, 20) == 20:
            multiplier = 2
        choice: int = random.randint(0, len(self.__attacks)-1)
        if self.getAttack(choice) is not None:
            return int(self.getAttack(choice) * multiplier)
        else:
            return 1