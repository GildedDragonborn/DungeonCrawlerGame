import pygame
import math
import playerCharacter
import enemy
from multipledispatch import dispatch


class scene:
    #@dispatch([], playerCharacter)
    def __init__(self, enemies: [], pc: playerCharacter):
        actors: [enemy] = enemies
        player: playerCharacter = pc