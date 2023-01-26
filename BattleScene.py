import pygame
import math
import playerCharacter
import enemy
import battleEnemy
from GameData.colorData import *
from multipledispatch import dispatch
import os

pygame.init()
class scene:
    #@dispatch([], playerCharacter)
    def __init__(self, enemies: [], pc: playerCharacter):
        if type(enemies) is not list:
            print("ERROR: enemies IS NOT LIST")
        self.__actors: [battleEnemy] = list(enemies)
        self.__player: playerCharacter = pc


    @property
    def actors(self) -> list:
        return self.__actors

    @property
    def player(self):
        return self.__player

    def drawScene(self):
        width = 800
        height = 600
        screen = pygame.display.set_mode((width, height))
        background = pygame.image.load(os.path.join("Assets", "testBackground.png"))
        screen.fill(background1)
        screen.blit(pygame.image.load(os.path.join(self.__player.spritePath, self.__player.spriteName)), (100, 100))
        num = 1
        for i in range(len(self.actors)):
            screen.blit(pygame.image.load(os.path.join(self.__actors[i].spritePath, self.__actors[i].spriteName)), (500, 50+100*num))
            num = num+1

    def runScene(self):
        self.drawScene()
        width = 800
        height = 600
        screen = pygame.display.set_mode((width, height))
        selectAttack = False
        battleOn = True
        print("It's Battle Time!")
        currentButton = 0
        while battleOn:
            self.drawScene()
            pygame.draw.rect(screen, buttonIdle, [100, 450, 600, 500])
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:  # HANDLES KEY PRESSES
                    if event.key == pygame.K_ESCAPE:
                        battleOn = False
                    elif event.key == pygame.K_d:
                        if currentButton == 2:
                            currentButton = 0
                        else:
                            currentButton = currentButton + 1
                    elif event.key == pygame.K_a:
                        if currentButton == 0:
                            currentButton = 2
                        else:
                            currentButton = currentButton - 1
                    elif event.key == pygame.K_SPACE:
                        #Fight, Item, Run
                        if currentButton == 0 and not selectAttack:
                            selectAttack = True
                        elif currentButton == 0 and selectAttack:
                            print("PUNCH")
                            selectAttack = False
                            currentButton = 0
                        elif currentButton == 1 and not selectAttack:
                            print("No Items to use!")
                        elif currentButton == 1 and selectAttack:
                            print("PEW")
                            selectAttack = False
                            currentButton = 0
                        elif currentButton == 2 and not selectAttack:
                            battleOn = False
                        elif currentButton == 2 and selectAttack:
                            selectAttack = False
                            currentButton = 0

            if not selectAttack:
                pygame.draw.rect(screen, buttonSelected, [125, 500, 150, 50])
                pygame.draw.rect(screen, buttonSelected, [325, 500, 150, 50])
                pygame.draw.rect(screen, buttonSelected, [525, 500, 150, 50])
                screen.blit(battleAttack, (157, 510))
                screen.blit(battleItem, (372, 510))
                screen.blit(battleFlee, (572, 510))
            elif selectAttack:
                pygame.draw.rect(screen, buttonIdle, [100, 450, 600, 500])
                pygame.draw.rect(screen, buttonSelected, [125, 500, 150, 50])
                pygame.draw.rect(screen, buttonSelected, [325, 500, 150, 50])
                pygame.draw.rect(screen, buttonSelected, [525, 500, 150, 50])
                screen.blit(battleStrike, (165, 510))
                screen.blit(battleCast, (372, 510))
                screen.blit(battleBack, (572, 510))
            if currentButton == 0:
                pygame.draw.rect(screen, selectColor, [125, 570, 150, 10])
            elif currentButton == 1:
                pygame.draw.rect(screen, selectColor, [325, 570, 150, 10])
            elif currentButton == 2:
                pygame.draw.rect(screen, selectColor, [525, 570, 150, 10])
            pygame.display.update()
        print("Battle Over")

#width = 800
#height = 600
#screen = pygame.display.set_mode((width, height))

