import pygame
import random
import math
import weapon
from typing import List
import json


class enemy:  # TODO: Enemy Class
    def __init__(self):
        self.__enemyID: int = 0
        self.__name: str = ""
        self.__MaxHealth: int = 0
        self.__currHealth: int = 0
        self.__expVal: int = 0
        self.__behavior: int = 0  # behavior determined by an int
        self.__attacks: List[weapon] = []

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

    def getAttack(self, i: int) -> weapon:
        return self.__attacks[i]
