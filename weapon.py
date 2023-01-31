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
            self.__abilityREQ: int = int(data[weaponID]["abilityREQ"])
            self.__upgradeTier: int = int(0)
            self.__upgradePath: str = str("")
            self.__APCost: data[weaponID]["APCost"]

    @dispatch(dict)
    def __init__(self, weaponDict: dict):
        with open('GameData/PlayerWeapons.json') as inFile:
            data = json.load(inFile)
            self.__weaponName: str = weaponDict.get("weaponName")
            self.__DMGVal: int = int(weaponDict.get("damageVal"))
            self.__abilityREQ: int = int(weaponDict.get("abilityREQ"))
            self.__upgradeTier: int = int(weaponDict.get("upgradeTier"))
            self.__upgradePath: str = str(weaponDict.get("upgradePath"))
            self.__APCost: int(weaponDict.get("APCost"))

    @property
    def weaponName(self):
        return self.__weaponName

    @property
    def DMGVal(self):
        return self.__DMGVal

    @property
    def abilityREQ(self):
        return self.__abilityREQ

    @property
    def upgradeTier(self):
        return self.__upgradeTier

    @property
    def upgradePath(self):
        return self.__upgradePath

    @property
    def APCost(self):
        return self.__APCost


"""damage types:
Mag = magic
Phy = Physical
Fir = Fire
Lgt = Lightning
Frt = Frost/Cold
Hly = Holy
Eld = Eldritch


Scaling:
A: Low base, high scaling - (base DMG*upgrade_tier + 4*SCALING_ABILITY-20)
B: Med base, medium scaling - (base DMG*upgrade_tier + 3*SCALING_ABILITY-20)
C: High base, low scaling - (base DMG*upgrade_tier + 2*SCALING_ABILITY-20)
D: Base only, no scaling - (base DMG*upgrade_tier*1.3) TODO: The actual math lol"""