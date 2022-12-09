import pygame
import random
import math
import weapon
from typing import List
import json


class PlayerCharacter:

    def __init__(self):
        """
        default constructor, TODO: build proper constructor
        """
        self.__playerName: str = str("")
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

    # Getters
    @property
    def PlayerName(self) -> str:
        return self.__playerName

    @property
    def MaxHP(self) -> int:
        return self.MaxHP

    @property
    def CurrHP(self) -> int:
        return self.CurrHP

    @property
    def CurrLevel(self) -> int:
        return self.CurrLevel

    @property
    def Strength(self) -> int:
        return self.Strength

    @property
    def Agility(self) -> int:
        return self.Agility

    @property
    def Acumen(self) -> int:
        return self.Acumen

    @property
    def Appeal(self) -> int:
        return self.Appeal

    @property
    def Adaptability(self) -> int:
        return self.Adaptability

    @property
    def currentXP(self) -> int:
        return self.currentXP

    @property
    def currentGold(self) -> int:
        return self.currentGold

    @property
    def currentWeapon(self) -> weapon:
        return self.currentWeapon

    @property
    def perksTaken(self) -> List[int]:
        return self.perksTaken

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
            "perksTaken": self.__perksTaken,
        }
        characterData = json.dumps(dictionary, indent=13)
        with open("characterData.json", "w") as outfile:
            json.dump(characterData, outfile)

