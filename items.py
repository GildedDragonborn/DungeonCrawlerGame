import pygame
import json
import math
from multipledispatch import dispatch

class item:
    @dispatch(int)
    def __init__(self, itemID: int):
        with open("GameData/consumables.json") as inFile:
            data = json.load(inFile)
            self.__itemID = itemID
            self.__itemName = data[itemID]["itemName"]
            self.__itemQuantity = 1
            self.__invLimit = 99
            self.__baseCost = data[itemID]["baseCost"]
            self.__effect = data[itemID]["effect"] # SEE BELOW FOR LIST OF EFFECTS
            self.__power = data[itemID]["power"] # [numDice, diceSize] OR [0, Buff Duration]

    @dispatch(int, int)
    def __init__(self, itemID: int, quantity: int):
        with open("GameData/consumables.json") as inFile:
            data = json.load(inFile)
            self.__itemID = itemID
            self.__itemName = data[itemID]["itemName"]
            self.__itemQuantity = quantity
            self.__invLimit = 99
            self.__baseCost = data[itemID]["baseCost"]
            self.__effect = data[itemID]["effect"]  # SEE BELOW FOR LIST OF EFFECTS
            self.__power = data[itemID]["power"]  # [numDice, diceSize] OR [Buff Power, Buff Duration]

    @property
    def itemID(self):
        return self.__itemID

    @property
    def itemName(self):
        return self.__itemName

    @property
    def itemQuantity(self):
        return self.__itemQuantity

    @property
    def invLimit(self):
        return self.__invLimit

    @property
    def baseCost(self):
        return self.__baseCost

    @property
    def effect(self):
        return self.__effect

    @property
    def power(self):
        return self.__power

    def getNumDice(self):
        return self.__power[0]

    def getDiceSize(self):
        return self.__power[1]

    # These are duplicates, but make code more readible so they're staying
    def getBuffPower(self):
        return self.__power[0]

    def getBuffDuration(self):
        return self.__power[1]

    def increaseItems(self, add: int):
        self.__itemQuantity += add



"""
itemID = Effect
0 = Heal
1 = Harm(Phy)
2 = Harm(Mag)
3 = Harm(Fir)
4 = Harm(Frt)
5 = Harm(Lgt)
6 = Harm(Hly)
7 = Harm(Eld)
8 = BuffRes(Phy)
9 = BuffRes(Mag)
10 = BuffRes(Fir)
11 = BuffRes(Frt)
12 = BuffRes(Lgt)
13 = BuffRes(Hly)
14 = BuffRes(Eld)
15 = RestoreMP
16 = RestoreAP - EXTREMELY RARE ITEM
17 = RestoreSanity - TODO: SANITY MECHANICS
"""