import json
import pygame
from spell import spell
from battleEnemy import battleEnemy
import random
from multipledispatch import dispatch

class spellTools:
    @dispatch(int)
    def __init__(self, toolID: int):
        with open('GameData/BaseSpellTools.json') as inFile:
            data = json.load(inFile)
            self.__name: str = data[toolID]["focusName"]
            self.__focusID: int = data[toolID]["focusID"]
            self.__baseFocus: str = data[toolID]["baseFocus"]
            self.__upgrade_level: int = data[toolID]["level"]
            self.__scaleFactor: str = data[toolID]["scaleFactor"]
            self.__apScale: float = data[toolID]["APscale"]

    @dispatch(int, bool)
    def __init__(self, toolID: int, isPlayer: bool):
        with open('GameData/playerFocci.json') as inFile:
            data = json.load(inFile)
            self.__name: str = data[toolID]["focusName"]
            self.__focusID: int = data[toolID]["focusID"]
            self.__baseFocus: str = data[toolID]["baseFocus"]
            self.__upgrade_level: int = data[toolID]["level"]
            self.__scaleFactor: str = data[toolID]["scaleFactor"]
            self.__apScale: float = data[toolID]["APscale"]

    @property
    def name(self) -> str:
        return self.__name

    @property
    def baseFocus(self) -> str:
        return self.__baseFocus

    @property
    def focusID(self) -> int:
        return self.__focusID

    @property
    def upgrade_level(self) -> int:
        return self.__upgrade_level

    @property
    def scaleMag(self) -> float:
        return self.__scaleMag

    @property
    def scaleFir(self) -> float:
        return self.__scaleFir

    @property
    def scaleLgt(self) -> float:
        return self.__scaleLgt

    @property
    def scaleFrt(self) -> float:
        return self.__scaleFrt

    @property
    def scaleHly(self) -> float:
        return self.__scaleHly

    @property
    def scaleEld(self) -> float:
        return self.__scaleEld

    @property
    def apScale(self) -> float:
        return self.__apScale

    def castSpell(self, accumen: int, assurance:int, spell: spell, target: battleEnemy) -> int:
        totalMod = 1
        totalDmg = 0
        toHit = 0
        for i in range(3):
            randNum = random.randint(1,6)
            toHit = toHit + randNum
            print(randNum)
        if toHit >= target.armor:
            print("hit!")
            if self.__scaleFactor == spell.DMGType:
                totalMod = 1.5
            for i in range(spell.numDice):
                randNum = random.randint(1, spell.diceSize)
                totalDmg = totalDmg + randNum
                print(randNum)
            return int(totalDmg * totalMod)
        else:
            print("Miss!")
            return 0



    """def calcScale(self, scaleFactor: str, acumen: int, assurance: int) -> float: # calculates the scaling factor
        if scaleFactor == "Mag":
            return (self.__scaleEld * acumen) / 50
        elif scaleFactor == "Fir":
            return (((self.__scaleFir * acumen) + (self.scaleFir * assurance))/2)/50
        elif scaleFactor == "Lgt":
            return (((self.__scaleLgt * acumen) + (self.scaleLgt * assurance))/2)/50
        elif scaleFactor == "Frt":
            return (((self.__scaleFrt * acumen) + (self.scaleFrt * assurance))/2)/50
        elif scaleFactor == "Hly":
            return (self.__scaleHly*assurance)/50
        elif scaleFactor == "Eld":
            return (self.__scaleEld*acumen)/50
        else:
            return 0.1"""
    """
    scaling = baseDMG*(scalingFactor * ability)/50
    Base = baseDMG*(1.0+(0.1*level))
    Total = Base+scaling
    """