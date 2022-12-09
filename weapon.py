import pygame
import math


class weapon:
    def __init__(self):
        self.__weaponName: str = str("")
        self.__damageVal: int = int(0)
        self.__upgradeTier: int = int(0)
        self.__upgradePath: str = str("")
        self.__APCost: 0