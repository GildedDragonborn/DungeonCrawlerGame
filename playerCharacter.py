import pygame
import random
import math
import weapon
import os
from multipledispatch import dispatch
from typing import List
import json
import armor


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
        self.__MaxAP: int = int(inFile.get("MaxAP"))
        # Abilities
        self.__Ability: int = int(inFile.get("Ability"))  # TODO: find a synonym for Ability that starts with A
        self.__Agility: int = int(inFile.get("Agility"))  # Dexterity/movement abilities
        self.__Acumen: int = int(inFile.get("Acumen"))  # Intelligence/rate of XP gain and ability to use magic(?)
        self.__Appeal: int = int(inFile.get("Appeal"))  # Charisma/charm/status abilities
        self.__Adaptability: int = int(inFile.get("Adaptability"))  # Endurance/HP scaling
        # Attributes
        self.__currentXP: int = int(inFile.get("currentXP"))
        self.__currentGold: int = int(inFile.get("currentGold"))
        self.__currentWeapon: weapon = None
        self.__armor: armor = None
        self.__inventory: List = []
        self.__spellList: List = []
        self.__perksTaken: List[int] = inFile.get("perksTaken")  # perks stored as int values that modify parts of character.

    """
    def __init__(self): # default constructor, TODO: build proper constructor
        self.__playerName: str = str("")
        self.__sprite = pygame.image.load(os.path.join("Assets", "testPlayer.png"))
        self.__MaxHP: int = int(0)
        self.__CurrHP: int = int(0)
        self.__CurrLevel: int = int(0)
        # Abilities
        self.__Ability: int = int(0) # TODO: find a synonym for Ability that starts with A
        self.__Agility: int = int(0) # Dexterity/movement abilities
        self.__Acumen: int = int(0) # Intelligence/rate of XP gain and ability to use magic(?)
        self.__Appeal: int = int(0) # Charisma/charm/status abilities
        self.__Adaptability: int = int(0) # Endurance/HP scaling
        # Attributes
        self.__currentXP: int = int(0)
        self.__currentGold: int = int(0)
        self.__currentWeapon: weapon = None
        self.__inventory: List = []
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
    def Ability(self) -> int:
        return self.__Ability

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
    def armor(self):
        return self.__armor

    @property
    def perksTaken(self) -> List[int]:
        return self.__perksTaken

    @property
    def spritePath(self) -> str:
        return self.__spritePath

    @property
    def spriteName(self) -> str:
        return self.__spriteName

    @property
    def inventory(self):
        return self.__inventory

    @property
    def spellList(self):
        return self.__spellList

    @property
    def maxAP(self):
        return self.__MaxAP

    # Setters
    def setAbility(self, new: int):
        self.__Ability = new

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

    def addItemToInv(self, new):
        self.__inventory.append(new)

    def setXP(self, new):
        self.__currentXP = new

    def addXP(self, new):
        self.__currentXP = self.__currentXP + new

    def setLevel(self, new):
        self.__CurrLevel = new

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
            "MaxAP": self.__MaxAP,
            "Ability": self.__Ability,
            "Agility": self.__Agility,
            "Acumen": self.__Acumen,
            "Appeal": self.__Appeal,
            "Adaptability": self.__Adaptability,
            "currentXP": self.__currentXP,
            "currentGold": self.__currentGold,
            "currentWeapon": self.__currentWeapon,
            "armor": self.__armor,
            "inventory": self.__inventory,
            "spellList": self.__spellList,
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
            "MaxAP": 0,
            "Ability": 0,
            "Agility": 0,
            "Acumen": 0,
            "Appeal": 0,
            "Adaptability": 0,
            "currentXP": 0,
            "currentGold": 0,
            "currentWeapon": None,
            "armor": None,
            "inventory": [],
            "spellList": [],
            "perksTaken": []
        }
        with open(self.__fileName, "w") as outfile:
            json.dump(dictionary, outfile, indent=4)

    def levelUpCheck(self) -> bool:
        exponentGrowth: int = 2
        baseXP: int = 100
        leveledOnce = False
        while self.__currentXP >= math.floor(baseXP * (self.CurrLevel ** exponentGrowth)):
            #TODO LEVEL MENU: ALLOW PLAYER TO INCREASE ATTRIBUTES
            self.__CurrLevel = self.CurrLevel + 1
            self.__currentXP = self.currentXP - baseXP * (self.CurrLevel ** exponentGrowth)
            if self.__currentXP <= 0:
                self.__currentXP = 0
            leveledOnce = True
        else:
            return leveledOnce

    def deadCheck(self) -> bool:
        if self.__CurrHP <= 0:
            return True
        else:
            return False

    #Used in the battle phase, determines the damage dealt by the player to the enemy
    def damageDealt(self) -> int:
        multiplier: int = int(round(random.uniform(0.75, 1.25),1))
        if random.randint(1, 20) == 20:
            multiplier = 2
        if self.currentWeapon is not None:
            return int(self.currentWeapon.attack(self.Ability) * multiplier)  #see attack function in weapon for details
        else:
            return 1

    def weaponType(self) -> str:
        return self.currentWeapon.upgradePath

    def takeDamage(self, dmg: int, type: str): #for armor ignoring attacks, put blank or junk data for type
        if self.armor is not None:
            if type == "Phy":
                self.modHP(-1 * (dmg * (1 - (self.armor.PhyRes/100))))
            elif type == "Mag":
                self.modHP(-1 * (dmg * (1 - (self.armor.MagRes/100))))
            elif type == "Fir":
                self.modHP(-1 * (dmg * (1 - (self.armor.FirRes/100))))
            elif type == "Lgt":
                self.modHP(-1 * (dmg * (1 - (self.armor.LgtRes/100))))
            elif type == "Frt":
                self.modHP(-1 * (dmg * (1 - (self.armor.FrtRes/100))))
            elif type == "Hly":
                self.modHP(-1 * (dmg * (1 - (self.armor.HlyRes/100))))
            elif type == "Eld":
                self.modHP(-1 * (dmg * (1 - (self.armor.EldRes/100))))
            else:
                self.modHP(-1 * dmg)
        else:
            self.modHP(-1 * dmg)
        if self.deadCheck():
            pass # GAME OVER SCREEN





