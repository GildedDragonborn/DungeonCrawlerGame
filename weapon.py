import pygame
import json
import os
import time
from multipledispatch import dispatch
import math
import random

class weapon:
    @dispatch(int)
    def __init__(self, weaponID: int):
        with open('GameData/BaseWeapons.json') as inFile:
            data = json.load(inFile)
            self.__baseWeapon: str = str(data[weaponID]["baseWeapon"])
            self.__weaponName: str = str(data[weaponID]["weaponName"])
            self.__diceSize: int = int(data[weaponID]["diceSize"])
            self.__numDice: int = int(data[weaponID]["numDice"])
            self.__baseAccuracy: int = int(data[weaponID]["baseAccuracy"])
            self.__abilityREQ: int = int(data[weaponID]["abilityREQ"])
            self.__upgradeTier: int = int(0)
            self.__upgradePath: str = str("")
            self.__APCost: int = data[weaponID]["APCost"]

    @dispatch(int, bool)
    def __init__(self, weaponID: int, isPlayerInv: bool):
        with open('GameData/PlayerWeapons.json') as inFile:
            data = json.load(inFile)
            self.__baseWeapon: str = str(data[weaponID]["baseWeapon"])
            self.__weaponName: str = str(data[weaponID]["weaponName"])
            self.__diceSize: int = int(data[weaponID]["diceSize"])
            self.__numDice: int = int(data[weaponID]["numDice"])
            self.__abilityREQ: int = int(data[weaponID]["abilityREQ"])
            self.__upgradeTier: int = int(0)
            self.__upgradePath: str = str("")
            self.__APCost: int = data[weaponID]["APCost"]

    @dispatch(dict)
    def __init__(self, weaponDict: dict):
        self.__baseWeapon: str = str(weaponDict.get("baseWeapon"))
        self.__weaponName: str = weaponDict.get("weaponName")
        self.__diceSize: int = int(weaponDict.get("diceSize"))
        self.__numDice: int = int(weaponDict.get("numDice"))
        self.__abilityREQ: int = int(weaponDict.get("abilityREQ"))
        self.__upgradeTier: int = int(weaponDict.get("upgradeTier"))
        self.__upgradePath: str = str(weaponDict.get("upgradePath"))
        self.__coefficientBase: int = int(weaponDict.get("coefficient"))
        self.__APCost: int(weaponDict.get("APCost"))

    @property
    def weaponName(self) -> str:
        return self.__weaponName

    @property
    def baseWeapon(self) -> str:
        return self.__weaponName

    @property
    def baseAccuracy(self) -> int:
        return self.__baseAccuracy

    @property
    def diceSize(self) -> int:
        return self.__diceSize

    @property
    def numDice(self) -> int:
        return self.__numDice

    @property
    def abilityREQ(self) -> int:
        return self.__abilityREQ

    @property
    def upgradeTier(self) -> int:
        return self.__upgradeTier

    @property
    def upgradePath(self) -> str:
        return self.__upgradePath

    @property
    def APCost(self) -> int:
        return self.__APCost



    def rollToHit(self):
        total = 0
        for i in range(3):
            randNum = random.randint(1,6)
            total = total+randNum
            self.rollDice(i, randNum)
            print(randNum)
        return total + self.__baseAccuracy

    def rollDmg(self):
        total = 0
        for i in range(self.__numDice):
            randNum = random.randint(1,self.__diceSize)
            total = total+randNum
            print(randNum)
        return total


"""damage types/upgrade Paths:
Mag = magic
Phy = Physical
Fir = Fire
Lgt = Lightning
Frt = Frost/Cold
Hly = Holy
Eld = Eldritch
"""