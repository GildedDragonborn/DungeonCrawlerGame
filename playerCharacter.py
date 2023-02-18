import sys
import pygame
import random
import math
import weapon
import spell
import spellTools
from items import item
import os
from multipledispatch import dispatch
from typing import List
import json
import armor
from sys import exit


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
        self.__MaxMP: int = 0
        self.__currMP: int = 0
        self.__currAP: int = int(inFile.get("MaxAP"))
        self.__currSanity: int = int(inFile.get("currSanity"))
        # Abilities
        self.__Ability: int = int(inFile.get("Ability"))  # TODO: find a synonym for Ability that starts with A
        self.__Agility: int = int(inFile.get("Agility"))  # Dexterity/movement abilities
        self.__Acumen: int = int(inFile.get("Acumen"))  # Intelligence/rate of XP gain and ability to use magic(?)
        self.__Appeal: int = int(inFile.get("Appeal"))  # Charisma/charm/status abilities
        self.__Adaptability: int = int(inFile.get("Adaptability"))  # Endurance/HP scaling
        self.__Assurance: int = int(inFile.get("Assurance"))
        # Attributes
        self.__currentXP: int = int(inFile.get("currentXP"))
        self.__currentGold: int = int(inFile.get("currentGold"))
        self.__currentWeapon: weapon = weapon.weapon(1)
        self.__armor: armor = armor.armor(int(inFile.get("armor")))
        self.__inventory: [List] = self.genItems(inFile.get("inventory"))
        self.__spellList: List = self.getSpells(inFile.get("spellList"))
        self.__spellTool: spellTools = self.getSpellTool(int(inFile.get("spellTool")))
        self.__perksTaken: List[int] = inFile.get("perksTaken")  # perks stored as int values that modify parts of character.
        self.__MaxHP = self.calcHP()
        self.__MaxAP = self.calcAP()
        self.__MaxMP = self.calcMP()
        self.__currMP = self.__MaxMP
        self.export()

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
    def currMP(self) -> int:
        return self.__currMP

    def setCurrMP(self, new):
        self.__currMP = new

    @property
    def MaxMP(self) -> int:
        return self.__MaxMP

    @property
    def currSanity(self) -> int:
        return self.__currSanity

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
    def Assurance(self) -> int:
        return self.__Assurance

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
    def currAP(self):
        return self.__currAP

    def setCurrAP(self, new):
        self.__currAP = new

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

    def modSanity(self, mod: int):
        self.__currSanity += mod

    # Other Methods
    def export(self):
        spells = []
        for i in self.__spellList:
            spells.append(i.spellID)
        dictionary = {
            "playerName": self.__playerName,
            "fileName": self.__fileName,
            "spritePath": self.__spritePath,
            "spriteName": self.__spriteName,
            "MaxHP": self.__MaxHP,
            "CurrHP": self.__CurrHP,
            "CurrLevel": self.__CurrLevel,
            "MaxAP": self.__MaxAP,
            "MaxMP": self.__MaxMP,
            "currMP": self.__currMP,
            "currSanity": self.__currSanity,
            "Ability": self.__Ability,
            "Agility": self.__Agility,
            "Acumen": self.__Acumen,
            "Appeal": self.__Appeal,
            "Adaptability": self.__Adaptability,
            "Assurance": self.__Assurance,
            "currentXP": self.__currentXP,
            "currentGold": self.__currentGold,
            "currentWeapon": None,# self.__currentWeapon.baseWeapon,
            "spellTool": self.__spellTool.focusID,
            "armor": self.__armor.armorID,
            "inventory": [[0,1]],
            "spellList": spells,
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
            "MaxHP": 15,
            "CurrHP": 15,
            "CurrLevel": 1,
            "MaxAP": 0,
            "MaxMP": 5,
            "currMP": 5,
            "currSanity": 20,
            "Ability": 1,
            "Agility": 1,
            "Acumen": 1,
            "Appeal": 1,
            "Adaptability": 1,
            "Assurance": 1,
            "currentXP": 0,
            "currentGold": 0,
            "currentWeapon": None,
            "spellTool": None,
            "armor": 0,
            "inventory": [[]],
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
        if self.__CurrHP <= 0 or self.__currSanity <= 0:
            return True
        else:
            return False

    #Used in the battle phase, determines the damage dealt by the player to the enemy
    def damageDealt(self, crit: bool, ultracrit: bool) -> int:
        addition = 0
        if crit and ultracrit:
            multiplier = 5
        elif crit:
            multiplier = 2
        else:
            multiplier = 1
        if self.currentWeapon is not None:
            if self.currentWeapon.upgradePath == "Phy":
                addition = int(self.Ability/2)
            elif self.currentWeapon.upgradePath == "Mag":
                addition = int(self.Acumen/2)
            elif self.currentWeapon.upgradePath == "Fir":
                addition = int((self.Acumen/2 + self.Assurance/2)/2)
            elif self.currentWeapon.upgradePath == "Lgt":
                addition = int((self.Acumen/2 + self.Assurance/2)/2)
            elif self.currentWeapon.upgradePath == "Frt":
                addition = int((self.Acumen/2 + self.Assurance/2)/2)
            elif self.currentWeapon.upgradePath == "Hly":
                addition = int(self.Assurance/2)
            elif self.currentWeapon.upgradePath == "Eld":
                addition = int(self.Assurance/2)
            elif self.currentWeapon.upgradePath == "Flt":
                addition = 0
                multiplier += 2
            elif self.currentWeapon.upgradePath == "Enc":
                addition = int(self.Ability/2)
            return int(self.currentWeapon.rollDmg()*multiplier + addition)
        else:
            return 1

    def weaponType(self) -> str:
        return self.currentWeapon.upgradePath

    def takeDamage(self, dmg: int, type: str): #for armor ignoring attacks, put blank or junk data for type
        if self.armor is not None:
            if type == "Phy":
                if (dmg - self.armor.PhyRes) <= 0:
                    self.modHP(-1)
                else:
                    self.modHP(-1 * (dmg - self.armor.PhyRes))
            elif type == "Mag":
                if (dmg - self.armor.MagRes) <= 0:
                    self.modHP(-1)
                else:
                    self.modHP(-1 * (dmg - self.armor.MagRes))
            elif type == "Fir":
                if (dmg - self.armor.FirRes) <= 0:
                    self.modHP(-1)
                else:
                    self.modHP(-1 * (dmg - self.armor.FirRes))
            elif type == "Lgt":
                if (dmg - self.armor.LgtRes) <= 0:
                    self.modHP(-1)
                else:
                    self.modHP(-1 * (dmg - self.armor.LgtRes))
            elif type == "Frt":
                if (dmg - self.armor.FrtRes) <= 0:
                    self.modHP(-1)
                else:
                    self.modHP(-1 * (dmg - self.armor.FrtRes))
            elif type == "Hly":
                if (dmg - self.armor.HlyRes) <= 0:
                    self.modHP(-1)
                else:
                    self.modHP(-1 * (dmg - self.armor.HlyRes))
            elif type == "Eld":
                if (dmg - self.armor.EldRes) <= 0:
                    self.modHP(-1)
                else:
                    self.modHP(-1 * (dmg - self.armor.EldRes))
            else:
                self.modHP(-1 * dmg)
        else:
            self.modHP(-1 * dmg)
        if self.deadCheck():
            pygame.quit() # GAME OVER SCREEN
            exit() # TODO IMPLEMENT GAME OVER SCREEN, CURRENTLY CRASHES GAME TO DESKTOP

    def calcHP(self) -> int:
        return int((10*self.__Adaptability/4)+((self.__CurrLevel+5)/2) + 10)

    def calcAP(self) -> int:
        return int(10+(self.Agility/2)+(self.__CurrLevel/10))

    def calcMP(self) -> int:
        return int(((self.Acumen*5)+(self.Assurance*5))/2 + self.CurrLevel/4)

    def getSpells(self, spellList: List):
        spells = []
        for i in spellList:
            temp = spell.spell(i)
            spells.append(temp)
        return spells

    def getSpellTool(self, tool: int):
        print("Tool: " + str(tool))
        return spellTools.spellTools(tool, True)

    def genItems(self, input):
        tempList = []
        for i in input:
            tempList.append(item(i[0], i[1]))
        return tempList


