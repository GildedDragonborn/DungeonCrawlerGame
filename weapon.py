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
            self.__baseDMG: int = int(data[weaponID]["baseDMG"])
            self.__abilityREQ: int = int(data[weaponID]["abilityREQ"])
            self.__upgradeTier: int = int(0)
            self.__upgradePath: str = str("")
            self.__coefficientBase: int = int(data[weaponID]["coefficient"])
            self.__APCost: data[weaponID]["APCost"]
            self.__DMGVal: int = 0
            self.__coefficient: int = self.__coefficientBase

    @dispatch(dict)
    def __init__(self, weaponDict: dict):
        self.__weaponName: str = weaponDict.get("weaponName")
        self.__baseDMG: int = int(data[weaponID]["baseDMG"])
        self.__abilityREQ: int = int(weaponDict.get("abilityREQ"))
        self.__upgradeTier: int = int(weaponDict.get("upgradeTier"))
        self.__upgradePath: str = str(weaponDict.get("upgradePath"))
        self.__coefficientBase: int = int(weaponDict.get("coefficient"))
        self.__APCost: int(weaponDict.get("APCost"))
        self.__DMGVal: int = 0
        self.__coefficient: int = self.__coefficientBase

    @property
    def weaponName(self):
        return self.__weaponName

    @property
    def baseDMG(self):
        return self.__baseDMG

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
    def coefficient(self):
        return self.__coefficient

    @property
    def APCost(self):
        return self.__APCost

    def calculateCoefficient(self, ability: int):
        if ability < self.abilityREQ: # meet stat requirements
            self.__coefficient = -0.75
        else:
            scale1 = ((self.__coefficientBase * (ability - (self.abilityREQ-1)))/50) # Weapon Attribute scaling
            scale2 = (self.__coefficientBase * (1 + (self.__upgradeTier/10))) # Weapon Level scaling
            self.__coefficient = scale1 + scale2 # add them together

    def attack(self, ability: int) -> int:
        self.calculateCoefficient(ability)
        return int(self.baseDMG * (1.0 + (0.1 * self.upgradeTier) + self.baseDMG * (self.__coefficient)))


"""damage types/upgrade Paths:
Mag = magic
Phy = Physical
Fir = Fire
Lgt = Lightning
Frt = Frost/Cold
Hly = Holy
Eld = Eldritch


Scaling:
A: Low base, high scaling - (base DMG + SCALING)
B: Med base, medium scaling - (base DMG + SCALING)
C: High base, low scaling - (base DMG + SCALING)
D: Base only, no scaling - (base DMG*(1.0+(0.2*upgrade_tier)) TODO: The actual math lol

Coefficient_base range:
A: 101%+
B: 81%-100%
C: 50%-80%
D: 0% 
https://www.reddit.com/r/darksouls/comments/194vmt/comment/c8kw9wp/

coefficient calculation:
if abilityREQ > currAbility:
    coefficient = -0.75
else:
    scale1 = ((coefficient_base * (SCALING_ABILITY - (abilityREQ-1)))/50
    scale2 = (coefficient_base * (1 + (upgrade_tier/MAX_UPGRADE_TIER)))
    coefficient = (scale1 + scale2)/2   

*The Math*
DMGVal = (baseDMG * (1.0 + (0.1 * upgrade_tier) + baseDMG(coefficient)
"""

