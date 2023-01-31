import math
import json
from multipledispatch import dispatch

class armor:
    @dispatch(int)
    def __init__(self, armorID: int):
        with open('GameData/BaseArmor.json') as inFile:
            data = json.load(inFile)
            self.__armorName: str = data[armorID]["armorName"]
            self.__PhyRes: int = data[armorID]["PhyRes"]
            self.__MagRes: int = data[armorID]["MagRes"]
            self.__FirRes: int = data[armorID]["FirRes"]
            self.__LgtRes: int = data[armorID]["LgtRes"]
            self.__FrtRes: int = data[armorID]["FrtRes"]
            self.__HlyRes: int = data[armorID]["HlyRes"]
            self.__EldRes: int = data[armorID]["EldRes"]
            self.__special = []

    @dispatch(dict)
    def __init__(self, armorDict):
        self.__armorName: str = armorDict.get("armorName")
        self.__PhyRes: int = armorDict.get("PhyRes")
        self.__MagRes: int = armorDict.get("MagRes")
        self.__FirRes: int = armorDict.get("FirRes")
        self.__LgtRes: int = armorDict.get("LgtRes")
        self.__FrtRes: int = armorDict.get("FrtRes")
        self.__HlyRes: int = armorDict.get("HlyRes")
        self.__EldRes: int = armorDict.get("EldRes")
        self.__special = armorDict.get("special")