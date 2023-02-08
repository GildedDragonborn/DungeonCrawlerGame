import pygame
import json
from multipledispatch import dispatch
#import math


class weapon:
    @dispatch(int)
    def __init__(self, weaponID: int):
        with open('GameData/BaseWeapons.json') as inFile:
            data = json.load(inFile)
            self.__baseWeapon: str = str(data[weaponID]["baseWeapon"])
            self.__weaponName: str = str(data[weaponID]["weaponName"])
            self.__baseDMG: int = int(data[weaponID]["baseDMG"])
            self.__baseAccuracy: int = int(data[weaponID]["baseAccuracy"])
            self.__abilityREQ: int = int(data[weaponID]["abilityREQ"])
            self.__upgradeTier: int = int(0)
            self.__upgradePath: str = str("")
            self.__coefficientBase: int = int(data[weaponID]["coefficient"])
            self.__APCost: data[weaponID]["APCost"]
            self.__DMGVal: int = 0

    @dispatch(int, bool)
    def __init__(self, weaponID: int, isPlayerInv: bool):
        with open('GameData/PlayerWeapons.json') as inFile:
            data = json.load(inFile)
            self.__baseWeapon: str = str(data[weaponID]["baseWeapon"])
            self.__weaponName: str = str(data[weaponID]["weaponName"])
            self.__baseDMG: int = int(data[weaponID]["baseDMG"])
            self.__abilityREQ: int = int(data[weaponID]["abilityREQ"])
            self.__upgradeTier: int = int(0)
            self.__upgradePath: str = str("")
            self.__coefficientBase: int = int(data[weaponID]["coefficient"])
            self.__APCost: data[weaponID]["APCost"]
            self.__DMGVal: int = 0

    @dispatch(dict)
    def __init__(self, weaponDict: dict):
        self.__baseWeapon: str = str(data[weaponID]["baseWeapon"])
        self.__weaponName: str = weaponDict.get("weaponName")
        self.__baseDMG: int = int(data[weaponID]["baseDMG"])
        self.__abilityREQ: int = int(weaponDict.get("abilityREQ"))
        self.__upgradeTier: int = int(weaponDict.get("upgradeTier"))
        self.__upgradePath: str = str(weaponDict.get("upgradePath"))
        self.__coefficientBase: int = int(weaponDict.get("coefficient"))
        self.__APCost: int(weaponDict.get("APCost"))
        self.__DMGVal: int = 0

    @property
    def weaponName(self) -> str:
        return self.__weaponName

    @property
    def baseWeapon(self) -> str:
        return self.__weaponName

    @property
    def baseDMG(self) -> int:
        return self.__baseDMG

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

    def calculateCoefficient(self, ability: int) -> float:
        if ability < self.abilityREQ: # meet stat requirements
            #self.__coefficient = -0.75
            return -0.75
        else:
            #self.__coefficient = (self.__coefficientBase * ability) / 50 # Weapon Attribute scaling
            return (self.__coefficientBase * ability) / 50


    def attack(self, ability: int, acumen: int, assurance: int) -> int:
        if self.__upgradePath == "Mag":
            coef = self.calculateCoefficient(acumen)
            return int(self.baseDMG*(1.0+(0.15*self.upgradeTier))+(self.baseDMG*coef)) # Scales with Acumen

        elif self.__upgradePath == "Fir":
            coef1 = self.calculateCoefficient(acumen)
            coef2 = self.calculateCoefficient(assurance)
            return int(self.baseDMG*(1.0+(0.15*self.upgradeTier))+((self.baseDMG*coef1)+(self.baseDMG*coef2))/2) # Scales with Assurance and Acumen

        elif self.__upgradePath == "Lgt":
            coef1 = self.calculateCoefficient(acumen)
            coef2 = self.calculateCoefficient(assurance)
            return int(self.baseDMG*(1.0+(0.15*self.upgradeTier))+((self.baseDMG*coef1)+(self.baseDMG*coef2))/2) # Scales with Assurance and Acumen

        elif self.__upgradePath == "Frt":
            coef1 = self.calculateCoefficient(acumen)
            coef2 = self.calculateCoefficient(assurance)
            return int(self.baseDMG*(1.0+(0.15*self.upgradeTier))+(self.baseDMG*coef1+self.baseDMG*coef2)/2) # Scales with Assurance and Acumen

        elif self.__upgradePath == "Hly":
            coef = self.calculateCoefficient(assurance)
            return int((self.baseDMG*(1.0+(0.15*self.upgradeTier)))/2+1.5*(self.baseDMG*coef)) # Scales Heavy with Assurance

        elif self.__upgradePath == "Eld":
            coef = self.calculateCoefficient(acumen)
            return int(self.baseDMG*(1.0+(0.15*self.upgradeTier))/2+1.5*(self.baseDMG*coef)) # Scales Heavy with Acumen

        elif self.__upgradePath == "Flat":
            return int(self.baseDMG*(1.25+(0.20*self.upgradeTier))) # Removes scaling

        elif self.__upgradePath == "Enchanted":
            coef = self.calculateCoefficient(ability)
            return int((self.baseDMG*(1.0+(0.15*self.upgradeTier)))/2+1.5*(self.baseDMG*coef)) # scales Heavy with ability

        else:
            coef = self.calculateCoefficient(ability)
            return int(self.baseDMG*(1.0+(0.15*self.upgradeTier))+(self.baseDMG*coef)) # Base weapon


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
    coefficient = ((coefficient_base * (SCALING_ABILITY)/50)

*The Math*
DMGVal = (baseDMG * (1.0 + (0.15 * upgrade_tier) + baseDMG * (coefficient)
"""

