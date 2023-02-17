import pygame
import json
from typing import Tuple
from multipledispatch import dispatch

class item:
    @dispatch(int)
    def __init__(self, itemID: int):
        with open("GameData/consumables.json") as inFile:
            data = json.load(inFile)
            self.__itemID = itemID
            self.__itemName = data[itemID]["itemName"]
            self.__itemQuantity = 1 # data[itemID]["itemQuantity"]
            self.__effect = data[itemID]["effect"] # SEE BELOW FOR LIST OF EFFECTS
            self.__power = data[itemID]["power"] # [numDice, diceSize] OR [0, Buff Duration]

    @dispatch(int, int)
    def __init__(self, itemID: int, quantity: int):
        with open("GameData/consumables.json") as inFile:
            data = json.load(inFile)
            self.__itemID = itemID
            self.__itemName = data[itemID]["itemName"]
            self.__itemQuantity = quantity
            self.__effect = data[itemID]["effect"]  # SEE BELOW FOR LIST OF EFFECTS
            self.__power = data[itemID]["power"]  # [numDice, diceSize] OR [0, Buff Duration]



