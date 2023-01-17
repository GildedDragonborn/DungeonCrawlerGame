import pygame
import math
import json
from multipledispatch import dispatch

class spell:
    def __init__(self, spellID: int):
        with open('GameData/Spells.json') as inFile:
            data = json.load(inFile)
            self.__spellName = data[spellID]["spellName"]
            self.__spellID = data[spellID]["spellID"]
            self.__spellDMG = data[spellID]["spellDMG"]
            self.__DMGType = data[spellID]["DMGType"]
            self.__SFX = data[spellID]["SFX"]
    @property
    def spellName(self):
        return self.__spellName

    @property
    def spellID(self):
        return self.__spellID

    @property
    def spellDMG(self):
        return self.__spellDMG

    @property
    def DMGType(self):
        return self.__DMGType

    @property
    def SFX(self):
        return self.__SFX