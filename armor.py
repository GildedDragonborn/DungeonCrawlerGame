import math
import json
from multipledispatch import dispatch

class armor:
    @dispatch(int)
    def __init__(self, armorID: int):
        with open('GameData/BaseArmor.json') as inFile:
            data = json.load(inFile)
            self.__armorName: str = data[armorID]["armorName"]
            self.__armorID: int = armorID
            self.__PhyRes: int = data[armorID]["PhyRes"] #Pyhsical damage
            self.__MagRes: int = data[armorID]["MagRes"] #Magical damage
            self.__FirRes: int = data[armorID]["FirRes"] #Fire damage
            self.__LgtRes: int = data[armorID]["LgtRes"] #Lightning damage
            self.__FrtRes: int = data[armorID]["FrtRes"] #Frost damage
            self.__HlyRes: int = data[armorID]["HlyRes"] #Holy damage
            self.__EldRes: int = data[armorID]["EldRes"] #Eldritch damage
            self.__special = []

    @dispatch(dict)
    def __init__(self, armorDict):
        self.__armorName: str = armorDict.get("armorName")
        self.__armorID: int = armorDict.get("armorID")
        self.__PhyRes: int = armorDict.get("PhyRes")
        self.__MagRes: int = armorDict.get("MagRes")
        self.__FirRes: int = armorDict.get("FirRes")
        self.__LgtRes: int = armorDict.get("LgtRes")
        self.__FrtRes: int = armorDict.get("FrtRes")
        self.__HlyRes: int = armorDict.get("HlyRes")
        self.__EldRes: int = armorDict.get("EldRes")
        self.__special = armorDict.get("special")

    @property
    def armorName(self):
        return self.__armorName

    @property
    def armorID(self):
        return self.__armorID

    @property
    def PhyRes(self):
        return self.__PhyRes

    @property
    def MagRes(self):
        return self.__MagRes

    @property
    def FirRes(self):
        return self.__FirRes

    @property
    def LgtRes(self):
        return self.__LgtRes

    @property
    def FrtRes(self):
        return self.__FrtRes

    @property
    def HlyRes(self):
        return self.__HlyRes

    @property
    def EldRes(self):
        return self.__EldRes


# Armor is measured in Damage resistance, which reduces damage by the armor value, to a minimum of 1