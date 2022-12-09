import pygame
import random
import math
import weapon
import os
from multipledispatch import dispatch
from typing import List
import json


class PlayerCharacter:

    @dispatch(dict)
    def __init__(self, inFile: dict):
        self.__playerName: str = str(inFile.get("playerName"))
        self.__fileName: str = str(inFile.get("fileName"))
        self.__spritePath: str = str(inFile.get("spritePath"))
        self.__spriteName: str = str(inFile.get("spriteName"))
        self.__sprite = pygame.image.load(os.path.join(self.__spritePath, self.__spriteName))
        self.__MaxHP: int = int(inFile.get("MaxHP"))
        self.__CurrHP: int = int(inFile.get("CurrHP"))
        self.__CurrLevel: int = int(inFile.get("CurrLevel"))
        # Abilities
        self.__Strength: int = int(inFile.get("Strength"))  # TODO: find a synonym for strength that starts with A
        self.__Agility: int = int(inFile.get("Agility"))  # Dexterity/movement abilities
        self.__Acumen: int = int(inFile.get("Acumen"))  # Intelligence/rate of XP gain and ability to use magic(?)
        self.__Appeal: int = int(inFile.get("Appeal"))  # Charisma/charm/status abilities
        self.__Adaptability: int = int(inFile.get("Adaptability"))  # Endurance/HP scaling
        # Attributes
        self.__currentXP: int = int(inFile.get("currentXP"))
        self.__currentGold: int = int(inFile.get("currentGold"))
        self.__currentWeapon: weapon = None
        self.__perksTaken: List[int] = inFile.get("perksTaken")  # perks stored as int values that modify parts of character.

    """
    def __init__(self): # default constructor, TODO: build proper constructor
        self.__playerName: str = str("")
        self.__sprite = pygame.image.load(os.path.join("Assets", "testPlayer.png"))
        self.__MaxHP: int = int(0)
        self.__CurrHP: int = int(0)
        self.__CurrLevel: int = int(0)
        # Abilities
        self.__Strength: int = int(0) # TODO: find a synonym for strength that starts with A
        self.__Agility: int = int(0) # Dexterity/movement abilities
        self.__Acumen: int = int(0) # Intelligence/rate of XP gain and ability to use magic(?)
        self.__Appeal: int = int(0) # Charisma/charm/status abilities
        self.__Adaptability: int = int(0) # Endurance/HP scaling
        # Attributes
        self.__currentXP: int = int(0)
        self.__currentGold: int = int(0)
        self.__currentWeapon: weapon = None
        self.__perksTaken: List[int] = [] # perks stored as int values that modify parts of character.
        # TODO: Document perks and their IDs
        """


    # Getters
    @property
    def PlayerName(self) -> str:
        return self.__playerName

    @property
    def fileName(self) -> str:
        return self.__fileName

    @property
    def MaxHP(self) -> int:
        return self.__MaxHP

    @property
    def CurrHP(self) -> int:
        return self.__CurrHP

    @property
    def CurrLevel(self) -> int:
        return self.__CurrLevel

    @property
    def Strength(self) -> int:
        return self.__Strength

    @property
    def Agility(self) -> int:
        return self.__Agility

    @property
    def Acumen(self) -> int:
        return self.__Acumen

    @property
    def Appeal(self) -> int:
        return self.__Appeal

    @property
    def Adaptability(self) -> int:
        return self.__Adaptability

    @property
    def currentXP(self) -> int:
        return self.__currentXP

    @property
    def currentGold(self) -> int:
        return self.__currentGold

    @property
    def currentWeapon(self) -> weapon:
        return self.__currentWeapon

    @property
    def perksTaken(self) -> List[int]:
        return self.__perksTaken

    @property
    def spritePath(self) -> str:
        return self.__spritePath

    @property
    def spriteName(self) -> str:
        return self.__spriteName

    # Setters
    def setStength(self, new: int):
        self.__Strength = new

    def setAgility(self, new: int):
        self.__Agility = new

    def setAcumen(self, new: int):
        self.__Acumen = new

    def setAdaptability(self, new: int):
        self.__Adaptability = new

    def setAppeal(self, new: int):
        self.__Appeal = new

    def setCurrHP(self, new: int):
        self.__CurrHP = new

    def setMaxHP(self, new: int):
        self.__MaxHP = new

    def setName(self, name: str):
        self.__playerName = name

    # Modifiers
    def modHP(self, modVal: int):
        self.__CurrHP += modVal

    def addPerk(self, new: int):
        self.__perksTaken.append(new)

    # Other Methods
    def export(self):
        dictionary = {
            "playerName": self.__playerName,
            "fileName": self.__fileName,
            "spritePath": self.__spritePath,
            "spriteName": self.__spriteName,
            "MaxHP": self.__MaxHP,
            "CurrHP": self.__CurrHP,
            "CurrLevel": self.__CurrLevel,
            "Strength": self.__Strength,
            "Agility": self.__Agility,
            "Acumen": self.__Acumen,
            "Appeal": self.__Appeal,
            "Adaptability": self.__Adaptability,
            "currentXP": self.__currentXP,
            "currentGold": self.__currentGold,
            "currentWeapon": self.__currentWeapon,
            "perksTaken": self.__perksTaken
        }
        with open(self.__fileName, "w") as outfile:
            json.dump(dictionary, outfile, indent=4)

    def deleteChar(self):
        dictionary = {
            "playerName": "",
            "fileName": self.__fileName,
            "spritePath": self.__spritePath,
            "spriteName": self.__spriteName,
            "MaxHP": 0,
            "CurrHP": 0,
            "CurrLevel": 0,
            "Strength": 0,
            "Agility": 0,
            "Acumen": 0,
            "Appeal": 0,
            "Adaptability": 0,
            "currentXP": 0,
            "currentGold": 0,
            "currentWeapon": None,
            "perksTaken": []
        }
        with open(self.__fileName, "w") as outfile:
            json.dump(dictionary, outfile, indent=4)



