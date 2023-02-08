import pygame
import math
import playerCharacter
import enemy
import battleEnemy
from GameData.colorData import *
from multipledispatch import dispatch
import os

pygame.init()
width = 800
height = 600
screen = pygame.display.set_mode((width, height))

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

    def selectEnemy(self) -> int:
        enemySelected = False
        enemyIndex = 0
        while not enemySelected:
            self.drawScene()
            pygame.draw.rect(screen, buttonSelected, [500, 220+100*enemyIndex, 70, 10])
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        enemySelected = True
                        return 0
                    elif event.key == pygame.K_s:
                        if enemyIndex == len(self.actors)-1:
                            enemyIndex = 0
                        else:
                            enemyIndex += 1
                    elif event.key == pygame.K_w:
                        if enemyIndex == 0:
                            enemyIndex = len(self.actors)-1
                        else:
                            enemyIndex -= 1
                    elif event.key == pygame.K_SPACE:
                        return enemyIndex
            pygame.display.update()
        pass #draw a blinking square around highest enemy, pressing space returns an int of the index of the enemy in actors

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

    def runScene(self) -> bool:
        self.drawScene()
        selectAttack = False
        spellMenu = False
        battleOn = True
        spellSelection: int = 0
        print("It's Battle Time!")
        currentButton = 0
        gainedXP = 0
        playerAP = self.player.maxAP
        while battleOn:
            self.drawScene()
            pygame.draw.rect(screen, buttonIdle, [100, 450, 600, 500])
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:  # HANDLES KEY PRESSES
                    if event.key == pygame.K_ESCAPE:
                        battleOn = False
                        return True
                    elif event.key == pygame.K_d:
                        if (currentButton == 2 and not spellMenu) or (currentButton == 3 and spellMenu):
                            currentButton = 0
                        else:
                            currentButton = currentButton + 1
                    elif event.key == pygame.K_a:
                        if currentButton == 0 and not spellMenu:
                            currentButton = 2
                        elif currentButton == 0 and spellMenu:
                            currentButton = 3
                        else:
                            currentButton = currentButton - 1
                    elif event.key == pygame.K_SPACE:
                        #Fight, Item, Run
                        enemyPick = 0
                        if currentButton == 0 and not selectAttack:
                            selectAttack = True
                        elif currentButton == 0 and selectAttack and not spellMenu:
                            # check if player has enough AP to strike
                            # select enemy
                            enemyPick = self.selectEnemy()
                            toHit = self.player.currentWeapon.rollToHit()
                            if self.actors[enemyPick].armor > toHit:
                                print("miss")
                            else:
                                print("Hit!")
                                dmgDealt = self.player.currentWeapon.rollDmg()
                                self.actors[enemyPick].takeDamage(dmgDealt)
                            print()

                            # self.actors[0].currHP = self.actors[0].currHP - self.player.damageDealt() #Deals damage to enemy
                            # TODO: Enemy selection, end of turn
                            if self.actors[enemyPick].currHP == 0:
                                gainedXP = gainedXP + self.actors[enemyPick].expVal
                                pass  # delete enemy, they died
                            if len(self.actors) == 0:
                                battleOn = False
                                self.player.addXP(gainedXP)
                            selectAttack = False
                            currentButton = 0
                        elif currentButton == 0 and spellMenu: # Previous Spell
                            print("PREVIOUS SPELL")
                            if spellSelection == 0:
                                spellSelection = len(self.player.spellList)-1
                            else:
                                spellSelection = spellSelection - 1
                        elif currentButton == 1 and not selectAttack:
                            print("No Items to use!")
                        elif currentButton == 1 and selectAttack and not spellMenu:
                            spellMenu = True
                            currentButton = 0
                        elif currentButton == 1 and spellMenu: #Next Spell
                            print("NEXT SPELL")
                            if spellSelection == len(self.player.spellList) - 1:
                                spellSelection = 0
                            else:
                                spellSelection = spellSelection + 1
                        elif currentButton == 2 and not selectAttack:
                            battleOn = False
                            return False
                        elif currentButton == 2 and selectAttack and not spellMenu:
                            selectAttack = False
                            currentButton = 0
                        elif currentButton == 2 and spellMenu: #SELECT
                            # check if player has enough AP to cast
                            spellMenu = False
                            selectAttack = False
                            currentButton = 0
                            print("PEW")
                        elif currentButton == 3 and not spellMenu and not selectAttack:
                            pass # end turn
                        elif currentButton == 3 and spellMenu: #BACK
                            spellMenu = False
                            currentButton = 1

            if not selectAttack:
                pygame.draw.rect(screen, buttonSelected, [125, 500, 150, 50])
                pygame.draw.rect(screen, buttonSelected, [325, 500, 150, 50])
                pygame.draw.rect(screen, buttonSelected, [525, 500, 150, 50])
                screen.blit(battleAttack, (157, 510))
                screen.blit(battleItem, (372, 510))
                screen.blit(battleFlee, (572, 510))
            elif selectAttack and not spellMenu:
                pygame.draw.rect(screen, buttonIdle, [100, 450, 600, 500])
                pygame.draw.rect(screen, buttonSelected, [125, 500, 150, 50])
                pygame.draw.rect(screen, buttonSelected, [325, 500, 150, 50])
                pygame.draw.rect(screen, buttonSelected, [525, 500, 150, 50])
                screen.blit(battleStrike, (165, 510))
                screen.blit(battleCast, (372, 510))
                screen.blit(battleBack, (572, 510))
            elif selectAttack and spellMenu:
                pygame.draw.rect(screen, buttonIdle, [100, 450, 600, 500])
                pygame.draw.rect(screen, buttonSelected, [125, 500, 100, 50])
                pygame.draw.rect(screen, buttonSelected, [275, 500, 100, 50])
                pygame.draw.rect(screen, buttonSelected, [425, 500, 100, 50])
                pygame.draw.rect(screen, buttonSelected, [575, 500, 100, 50])
                screen.blit(battlePrev, (143, 510))
                screen.blit(battleNext, (293, 510))
                screen.blit(battleSelect, (438, 510))
                screen.blit(battleBack, (593, 510))
            if currentButton == 0 and not spellMenu:
                pygame.draw.rect(screen, selectColor, [125, 570, 150, 10])
            elif currentButton == 1 and not spellMenu:
                pygame.draw.rect(screen, selectColor, [325, 570, 150, 10])
            elif currentButton == 2 and not spellMenu:
                pygame.draw.rect(screen, selectColor, [525, 570, 150, 10])
            elif currentButton == 0 and spellMenu:
                pygame.draw.rect(screen, selectColor, [125, 570, 100, 10])
            elif currentButton == 1 and spellMenu:
                pygame.draw.rect(screen, selectColor, [275, 570, 100, 10])
            elif currentButton == 2 and spellMenu:
                pygame.draw.rect(screen, selectColor, [425, 570, 100, 10])
            elif currentButton == 3 and spellMenu:
                pygame.draw.rect(screen, selectColor, [575, 570, 100, 10])
            pygame.display.update()
        print("Battle Over")

