import pygame
import random
import math
from typing import Tuple
from room import room


class level:

    def __init__(self, seed: int):
        self.__maxWidth = 50 # max number of rooms high the map can be
        self.__maxHeight = 50 # max number of rooms wide the map can be
        self.__origin = tuple((25, 25)) # origin coords for spawn room
        self.__mapLayout: [int] = self.mapGen(seed)

    @property
    def maxWidth(self) -> int:
        return self.__maxWidth

    @property
    def maxHeight(self) -> int:
        return self.__maxHeight

    @property
    def mapLayout(self):
        return self.__mapLayout

    def mapGen(self, seed: int): # Level generation, *pain*
        array = [[0]*self.maxWidth for i in range(self.__maxHeight)] # makes an array of int "0" which is the id of blank rooms
        return array
