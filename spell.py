import pygame
import math
import random
import json
from multipledispatch import dispatch

class spell:
    def __init__(self, spellID: int):
        with open('GameData/Spells.json') as inFile:
            data = json.load(inFile)
            self.__spellName: str = data[spellID]["spellName"]
            self.__spellID: int = data[spellID]["spellID"]
            self.__APCost: int = data[spellID]["APCost"]
            self.__diceSize: int = data[spellID]["diceSize"]
            self.__numDice: int = data[spellID]["numDice"]
            self.__acumenREQ: int = data[spellID]["acumenREQ"]
            self.__assuranceREQ: int = data[spellID]["assuranceREQ"]
            self.__spellCost: int = data[spellID]["spellCost"]
            self.__DMGType: str = data[spellID]["DMGType"]
            self.__SFX: tuple = data[spellID]["SFX"]
    @property
    def spellName(self):
        return self.__spellName

    @property
    def spellID(self):
        return self.__spellID

    @property
    def APCost(self):
        return self.__APCost
    @property
    def diceSize(self):
        return self.__diceSize

    @property
    def numDice(self) -> int:
        return self.__numDice

    @property
    def acumenREQ(self):
        return self.__acumenREQ

    @property
    def assuranceREQ(self):
        return self.__assuranceREQ

    @property
    def DMGType(self):
        return self.__DMGType

    @property
    def spellCost(self):
        return self.__spellCost
    @property
    def SFX(self):
        return self.__SFX

    def castSpell(self) -> int: #TODO: REPLACE WITH SPELL TOOLS FUNCTION
        total = 0
        for i in range(self.__numDice):
            randNum = random.randint(1, self.__diceSize)
            total = total + randNum
            print(randNum)
        return total

    """def cast_spell(self, dmgType: str, spellTool: spellTools, accumen: int, assurance: int) -> tuple:
        scaling = spellTool.calcScale(dmgType, accumen, assurance) # dmgType, accumen, assurance
        damage = (self.__spellDMG*(1+(0.1*spellTool.upgrade_level)) + (self.__spellDMG*scaling))
        return (damage,self.__SFX)"""

    """
    SFX:
    0 - None
    1 - Stun, chance, rounds (Stun enemies for X rounds)
    2 - Poison, chance, rounds (Poison enemies for X rounds)
    3 - Sleep, chance, rounds (Sleep enemies for X rounds)
    4 - Bleed, chance, rounds (Bleed enemies for X rounds)
    5 - Madness, chance, rounds (Give enemies madness for X rounds)
    6 - Eldritch, chance, rounds (Give enemies eldritch marked for X rounds)"""