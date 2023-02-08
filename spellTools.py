import json
import pygame
from multipledispatch import dispatch

class spellTools:
    @dispatch(int)
    def __init__(self, toolID: int):
        with open('GameData/BaseSpellTools.json') as inFile:
            data = json.load(inFile)
            self.__name: str = data[toolID]["focusName"]
            self.__baseFocus: str = data[toolID]["baseFocus"]
            self.__upgrade_level: int = data[toolID]["level"]
            self.__scaleMag: float = data[toolID]["scaleMag"]
            self.__scaleFir: float = data[toolID]["scaleFir"]
            self.__scaleLgt: float = data[toolID]["scaleLgt"]
            self.__scaleFrt: float = data[toolID]["scaleFrt"]
            self.__scaleHly: float = data[toolID]["scaleHly"]
            self.__scaleEld: float = data[toolID]["scaleEld"]
            self.__apScale: float = data[toolID]["APscale"]

    @dispatch(int, bool)
    def __init__(self, toolID: int, isPlayer: bool):
        with open('GameData/playerFocci.json') as inFile:
            data = json.load(inFile)
            self.__name: str = data[toolID]["focusName"]
            self.__baseFocus: str = data[toolID]["baseFocus"]
            self.__upgrade_level: int = data[toolID]["level"]
            self.__scaleMag: float = data[toolID]["scaleMag"]
            self.__scaleFir: float = data[toolID]["scaleFir"]
            self.__scaleLgt: float = data[toolID]["scaleLgt"]
            self.__scaleFrt: float = data[toolID]["scaleFrt"]
            self.__scaleHly: float = data[toolID]["scaleHly"]
            self.__scaleEld: float = data[toolID]["scaleEld"]
            self.__apScale: float = data[toolID]["APscale"]

    @property
    def name(self) -> str:
        return self.__name

    @property
    def baseFocus(self) -> str:
        return self.__baseFocus

    @property
    def upgrade_level(self) -> int:
        return self.__upgrade_level

    @property
    def scaleMag(self) -> float:
        return self.__scaleMag

    @property
    def scaleFir(self) -> float:
        return self.__scaleFir

    @property
    def scaleLgt(self) -> float:
        return self.__scaleLgt

    @property
    def scaleFrt(self) -> float:
        return self.__scaleFrt

    @property
    def scaleHly(self) -> float:
        return self.__scaleHly

    @property
    def scaleEld(self) -> float:
        return self.__scaleEld

    @property
    def apScale(self) -> float:
        return self.__apScale


    def calcScale(self, scaleFactor: str):
        pass

    """
    
    
    """