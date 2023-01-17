import pygame
import math
import playerCharacter
import enemy
from multipledispatch import dispatch
import os

pygame.init()
class scene:
    #@dispatch([], playerCharacter)
    def __init__(self, enemies: [], pc: playerCharacter):
        self.__actors: [enemy] = enemies
        self.__player: playerCharacter = pc


    @property
    def actors(self):
        return self.__actors

    @property
    def player(self):
        return self.__player

    def drawScene(self):
        background = pygame.image.load(os.path.join("Assets", "testBackground.png"))
        screen.blit(pygame.image.load(os.path.join(self.__player.spritePath, self.__player.spriteName)), (100, 100))
        num = 1
        for i in self.__actors:
            screen.blit(pygame.image.load(os.path.join(self.__actors[i].spritePath, self.__actors[i].spriteName)), (500+100*num, 100))
            num = num+1

    def runScene(self):
        self.drawScene()
        battleOn = True
        print("It's Battle Time!")
        while battleOn:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:  # HANDLES KEY PRESSES
                    if event.key == pygame.K_ESCAPE:
                        battleOn = False
        print("Battle Over")

#width = 800
#height = 600
#screen = pygame.display.set_mode((width, height))

