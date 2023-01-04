import pygame
import json
from multipledispatch import dispatch
#import math


class weapon:
    @dispatch(int)
    def __init__(self, weaponID: int):
        with open('GameData/BaseWeapons.json') as inFile:
            data = json.load(inFile)
            self.__weaponName: str = str(data[weaponID]["weaponName"])
            self.__DMGVal: int = int(data[weaponID]["damageVal"])
            self.__upgradeTier: int = int(0)
            self.__upgradePath: str = str("")
            self.__APCost: data[weaponID]["APCost"]

    """"@dispatch(dict)
    def __init__(self, weaponDict: dict):
        with open('GameData/PlayerWeapons.json') as inFile:
            data = json.load(inFile)
            self.__weaponName: str = str(data[weaponID]["weaponName"])
            self.__DMGVal: int = int(data[weaponID]["damageVal"])
            self.__upgradeTier: int = int(0)
            self.__upgradePath: str = str("")a
            self.__APCost: data[weaponID]["APCost"]"""

    @property
    def weaponName(self):
        return self.__weaponName

    @property
    def DMGVal(self):
        return self.__DMGVal

    @property
    def upgradeTier(self):
        return self.__upgradeTier

    @property
    def upgradePath(self):
        return self.__upgradePath

    @property
    def APCost(self):
        return self.__APCost
