import pygame
import os
import random
import math
import json
from playerCharacter import PlayerCharacter
from level import level
from room import room
from enemy import enemy
from BattleScene import scene
from GameData.colorData import *

# initializes pygame
pygame.init()


width = 800
height = 600
# 12x9 w=800 h=600
seed = int(random.randint(0, 10_000_000_000))
random.seed(a=seed, version=2)
# Level setup
currLevel = level(33667333) #demoseed = 33667333
roomArray = currLevel.mapLayout# [[0]*12 for i in range(9)] # each index represents the state of a square in the current room
print(seed)



# rendering menu text
quitButton = menuFont.render('quit', True, (255,255,255))
startButton = menuFont.render('start game', True, (255,255,255))


with open("GameData/characterData.json") as infile: # DEFAULTS TO SLOT 1, COULD INTRODUCE POTENTIAL SAVESWAP BUG
    data = json.load(infile)
PC = PlayerCharacter(data)

# Player Positional Arguments
xgridPosition = 1
ygridPosition = 4
currentX = 67*xgridPosition # Starts Player at X = 67
currentY = 67*ygridPosition # Starts Player at Y = 67
xRoomPos = currLevel.startX
yRoomPos = currLevel.startY
currLayer = 1

# creates the screen
screen = pygame.display.set_mode((width, height))

# background
background = pygame.image.load(os.path.join("Assets", "testBackground.png"))

# title and icon
pygame.display.set_caption("Rougelike Game")
icon = pygame.image.load(os.path.join("Assets", "tempicon.png"))  # logo goes here
pygame.display.set_icon(icon)



# playercharacter data
def loadChar(charFile: str):
    with open(charFile) as infile:
        data = json.load(infile)
    PC = PlayerCharacter(data)

def DrawGrid(): # Temporary while room.py is being developed
    screen.fill(background1)
    lineColor = pygame.Color(0, 0, 0, 255)  # RGB alpha
    x = 0
    y = 0
    increment = width/12
    while x <= width:
        start = [x, 0]
        end = [x, height]
        pygame.draw.line(screen, lineColor, start, end, width=2)
        x += increment
    while y <= height:
        start = [0, y]
        end = [width, y]
        pygame.draw.line(screen, lineColor, start, end, width=2)
        y += increment
    screen.blit(characterSprite, (currentX,currentY))

# Player Character sprite
characterSprite = pygame.image.load(os.path.join(PC.spritePath, PC.spriteName))
characterSpriteWidth = characterSprite.get_rect().width
characterSpriteHeight = characterSprite.get_rect().height
#characterSprite = pygame.transform.scale(characterSprite, (characterSpriteHeight/3, characterSpriteHeight/4))

currRoom = room(currLevel.getNextRoomID(xRoomPos, yRoomPos), 1, xRoomPos, yRoomPos,
                currLevel.getNextRoomHostile(xRoomPos, yRoomPos),currLevel.getNextRoomNumEnemies(xRoomPos, yRoomPos),
                currLevel.getNextRoomEnemyVar(xRoomPos, yRoomPos),currLevel.getNextRoomVisited(xRoomPos, yRoomPos),
                currLevel.getNextRoomVar(xRoomPos, yRoomPos))
currRoom.markVisited()
print(currLevel.getNextRoomID(xRoomPos,yRoomPos), xRoomPos, yRoomPos)
    #screen.blit(pygame.image.load(os.path.join("Assets", "testRock.png")), (67, 67))

screen.fill((255, 255, 255))
tempEnemy = enemy(0)
currEnemies = [tempEnemy]

running = True
menuMode = True
debugMode = False
character = "GameData/characterData.json"
loadChar(character)

#game loop
while running:
    #DrawGrid()
    # stores the (x,y) coordinates into
    # the variable as a tuple
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN: # HANDLES KEY PRESSES
            if event.key == pygame.K_ESCAPE:
                if menuMode:
                    running = False
                else:
                    menuMode = True
            if event.key == pygame.K_F2:
                if debugMode:
                    debugMode = False
                else:
                    debugMode = True
            # For all actions in the game
            if not menuMode:
                # Movement Keys
                try:
                    if event.key == pygame.K_w and currRoom.playerMoveCheck(xgridPosition, ygridPosition-1): # and ygridPosition < 4: # and currentY >= 67
                        print(xgridPosition, ygridPosition)
                        currentY = currentY-67
                        ygridPosition = ygridPosition - 1
                        # Redraw the room
                        currRoom.drawRoom()
                        if len(currEnemies) != 0:
                            encounterComplete = False
                            for i in range(len(currEnemies)):
                                currEnemies[i].movement(xgridPosition, ygridPosition)
                                if currEnemies[i].currX == xgridPosition and currEnemies[i].currY == ygridPosition and not encounterComplete:
                                    print("hit!")
                                    battleScene = scene(currEnemies[i].encounter, PC)
                                    if not battleScene.runScene(): # Returns true if won
                                        pass
                                    else:
                                        currRoom.setTile(xgridPosition, ygridPosition, 0)
                                        encounterComplete = True
                                        currLevel.markVisited(xRoomPos, yRoomPos)
                                        #currEnemies.remove(i)
                                        currRoom.removeEnemy(i)
                                    currRoom.drawRoom()
                                #else:
                                    #currEnemies.remove(i)
                                    #currRoom.removeEnemy(i)
                        screen.blit(characterSprite, (currentX, currentY))
                        if currRoom.getTile(xgridPosition, ygridPosition) == 99: # BOSSROOM TRAPDOOR
                            print("Thank you for playing my demo!")
                            running = False
                        if currRoom.getTile(xgridPosition, ygridPosition) == 6:
                            # TELEPORT TO SOUTH DOOR
                            currentX = (67 * 5)
                            currentY = 67*7
                            xgridPosition = 5
                            ygridPosition = 7
                            yRoomPos = yRoomPos - 1
                            currRoom = room(currLevel.getNextRoomID(xRoomPos, yRoomPos), 1, xRoomPos, yRoomPos,
                                            currLevel.getNextRoomHostile(xRoomPos, yRoomPos),
                                            currLevel.getNextRoomNumEnemies(xRoomPos, yRoomPos),
                                            currLevel.getNextRoomEnemyVar(xRoomPos, yRoomPos),
                                            currLevel.getNextRoomVisited(xRoomPos, yRoomPos),
                                            currLevel.getNextRoomVar(xRoomPos, yRoomPos))
                            currRoom.drawRoom()
                            if currRoom.visited == False:
                                currEnemies = currRoom.getEnemies
                                #generate_enemies()
                            currLevel.markVisited(xRoomPos, yRoomPos)
                            screen.blit(characterSprite, (currentX, currentY))
                        if currRoom.getTile(xgridPosition, ygridPosition) == 17:
                            # TELEPORT TO SOUTH DOOR
                            currentX = (67 * 6)
                            currentY = 67*7
                            xgridPosition = 6
                            ygridPosition = 7
                            # MOVES TO ROOM BELOW
                            yRoomPos = yRoomPos - 1
                            currRoom = room(currLevel.getNextRoomID(xRoomPos, yRoomPos), 1, xRoomPos, yRoomPos,
                                            currLevel.getNextRoomHostile(xRoomPos, yRoomPos),
                                            currLevel.getNextRoomNumEnemies(xRoomPos, yRoomPos),
                                            currLevel.getNextRoomEnemyVar(xRoomPos, yRoomPos),
                                            currLevel.getNextRoomVisited(xRoomPos, yRoomPos),
                                            currLevel.getNextRoomVar(xRoomPos, yRoomPos))
                            currRoom.drawRoom()
                            if currRoom.visited == False:
                                currEnemies = currRoom.getEnemies
                                #generate_enemies()
                            currLevel.markVisited(xRoomPos, yRoomPos)
                            screen.blit(characterSprite, (currentX, currentY))
                    if event.key == pygame.K_a and currRoom.playerMoveCheck(xgridPosition-1, ygridPosition):  # and currentX >= 52 and xgridPosition > -6
                        print(xgridPosition, ygridPosition)
                        currentX = currentX-67
                        xgridPosition = xgridPosition - 1
                        # Redraw the room
                        currRoom.drawRoom()
                        if len(currEnemies) != 0:
                            encounterComplete = False
                            for i in range(len(currEnemies)):
                                currEnemies[i].movement(xgridPosition, ygridPosition)
                                if currEnemies[i].currX == xgridPosition and currEnemies[i].currY == ygridPosition and not encounterComplete:
                                    print("hit!")
                                    battleScene = scene(currEnemies[i].encounter, PC)
                                    if not battleScene.runScene():  # Returns true if won
                                        pass
                                    else:
                                        currRoom.setTile(xgridPosition, ygridPosition, 0)
                                        encounterComplete = True
                                        currLevel.markVisited(xRoomPos, yRoomPos)
                                        # currEnemies.remove(i)
                                        currRoom.removeEnemy(i)
                                    currRoom.drawRoom()
                                #else:
                                    #currEnemies.remove(i)
                                    #currRoom.removeEnemy(i)
                        screen.blit(characterSprite, (currentX, currentY))
                        if currRoom.getTile(xgridPosition, ygridPosition) == 99: # BOSSROOM TRAPDOOR
                            #currLevel.incrLayer(currLayer)
                            #currLayer = currLayer + 1
                            print("Thank you for playing my demo!")
                            running = False
                        if currRoom.getTile(xgridPosition, ygridPosition) == 12:
                            # TELEPORT TO EAST DOOR
                            currentX = 67*10
                            currentY = 67*4
                            xgridPosition = 10
                            ygridPosition = 4
                            xRoomPos = xRoomPos - 1
                            currRoom = room(currLevel.getNextRoomID(xRoomPos, yRoomPos), 1, xRoomPos, yRoomPos,
                                            currLevel.getNextRoomHostile(xRoomPos, yRoomPos),
                                            currLevel.getNextRoomNumEnemies(xRoomPos, yRoomPos),
                                            currLevel.getNextRoomEnemyVar(xRoomPos, yRoomPos),
                                            currLevel.getNextRoomVisited(xRoomPos, yRoomPos),
                                            currLevel.getNextRoomVar(xRoomPos, yRoomPos))
                            currRoom.drawRoom()
                            if currRoom.visited == False:
                                currEnemies = currRoom.getEnemies
                                #generate_enemies()
                            currLevel.markVisited(xRoomPos, yRoomPos)
                            screen.blit(characterSprite, (currentX, currentY))
                    if event.key == pygame.K_s and currRoom.playerMoveCheck(xgridPosition, ygridPosition+1): # ygridPosition > -4: # and currentY <= height-67
                        print(xgridPosition, ygridPosition)
                        currentY = currentY+67
                        ygridPosition = ygridPosition + 1
                        #Redraw The Room
                        currRoom.drawRoom()
                        if len(currEnemies) != 0:
                            encounterComplete = False
                            for i in range(len(currEnemies)):
                                currEnemies[i].movement(xgridPosition, ygridPosition)
                                if currEnemies[i].currX == xgridPosition and currEnemies[i].currY == ygridPosition and not encounterComplete:
                                    print("hit!")
                                    battleScene = scene(currEnemies[i].encounter, PC)
                                    if not battleScene.runScene():  # Returns true if won
                                        pass
                                    else:
                                        currRoom.setTile(xgridPosition, ygridPosition, 0)
                                        encounterComplete = True
                                        currLevel.markVisited(xRoomPos, yRoomPos)
                                        # currEnemies.remove(i)
                                        currRoom.removeEnemy(i)
                                    currRoom.drawRoom()
                                #else:
                                    #currEnemies.remove(i)
                                    #currRoom.removeEnemy(i)
                        screen.blit(characterSprite, (currentX, currentY))
                        if currRoom.getTile(xgridPosition, ygridPosition) == 99: # BOSSROOM TRAPDOOR
                            print("Thank you for playing my demo!")
                            running = False
                        if currRoom.getTile(xgridPosition, ygridPosition) == 10:
                            # TELEPORT TO NORTH DOOR LEFT
                            currentX = (67*5)
                            currentY = 67
                            xgridPosition = 5
                            ygridPosition = 1
                            yRoomPos = yRoomPos + 1
                            currRoom = room(currLevel.getNextRoomID(xRoomPos, yRoomPos), 1, xRoomPos, yRoomPos,
                                            currLevel.getNextRoomHostile(xRoomPos, yRoomPos),
                                            currLevel.getNextRoomNumEnemies(xRoomPos, yRoomPos),
                                            currLevel.getNextRoomEnemyVar(xRoomPos, yRoomPos),
                                            currLevel.getNextRoomVisited(xRoomPos, yRoomPos),
                                            currLevel.getNextRoomVar(xRoomPos, yRoomPos))
                            currRoom.drawRoom()
                            if currRoom.visited == False:
                                currEnemies = currRoom.getEnemies
                                #generate_enemies()
                            currLevel.markVisited(xRoomPos, yRoomPos)
                            screen.blit(characterSprite, (currentX, currentY))
                        if currRoom.getTile(xgridPosition, ygridPosition) == 18:
                            # TELEPORT TO NORTH DOOR RIGHT
                            currentX = (67*6)
                            currentY = 67
                            xgridPosition = 6
                            ygridPosition = 1
                            yRoomPos = yRoomPos + 1
                            currRoom = room(currLevel.getNextRoomID(xRoomPos, yRoomPos), 1, xRoomPos, yRoomPos,
                                            currLevel.getNextRoomHostile(xRoomPos, yRoomPos),
                                            currLevel.getNextRoomNumEnemies(xRoomPos, yRoomPos),
                                            currLevel.getNextRoomEnemyVar(xRoomPos, yRoomPos),
                                            currLevel.getNextRoomVisited(xRoomPos, yRoomPos),
                                            currLevel.getNextRoomVar(xRoomPos, yRoomPos))
                            currRoom.drawRoom()
                            if currRoom.visited == False:
                                currEnemies = currRoom.getEnemies
                                #generate_enemies()
                            currLevel.markVisited(xRoomPos, yRoomPos)
                            screen.blit(characterSprite, (currentX, currentY))
                    if event.key == pygame.K_d and currRoom.playerMoveCheck(xgridPosition+1, ygridPosition): # and xgridPosition < 5: # and currentX <= width-82
                        print(xgridPosition, ygridPosition)
                        currentX = currentX+67
                        xgridPosition = xgridPosition + 1
                        #Redraw The Room
                        currRoom.drawRoom()
                        if len(currEnemies) != 0:
                            encounterComplete = False
                            for i in range(len(currEnemies)):
                                currEnemies[i].movement(xgridPosition, ygridPosition)
                                if currEnemies[i].currX == xgridPosition and currEnemies[i].currY == ygridPosition and not encounterComplete:
                                    print("hit!")
                                    battleScene = scene(currEnemies[i].encounter, PC)
                                    if not battleScene.runScene():  # Returns true if won
                                        pass
                                    else:
                                        currRoom.setTile(xgridPosition, ygridPosition, 0)
                                        encounterComplete = True
                                        currLevel.markVisited(xRoomPos, yRoomPos)
                                        # currEnemies.remove(i)
                                        currRoom.removeEnemy(i)
                                    currRoom.drawRoom()
                                #else:
                                    #dcurrEnemies.remove(i)
                                #    currRoom.removeEnemy(i)
                        screen.blit(characterSprite, (currentX, currentY))
                        if currRoom.getTile(xgridPosition, ygridPosition) == 99: # BOSSROOM TRAPDOOR
                            print("Thank you for playing my demo!")
                            running = False
                        if currRoom.getTile(xgridPosition, ygridPosition) == 8:
                            # TELEPORT TO EAST DOOR
                            currentX = 67
                            currentY = 67 * 4
                            xgridPosition = 1
                            ygridPosition = 4
                            xRoomPos = xRoomPos + 1
                            currRoom = room(currLevel.getNextRoomID(xRoomPos, yRoomPos), 1, xRoomPos, yRoomPos,
                                            currLevel.getNextRoomHostile(xRoomPos, yRoomPos),
                                            currLevel.getNextRoomNumEnemies(xRoomPos, yRoomPos),
                                            currLevel.getNextRoomEnemyVar(xRoomPos, yRoomPos),
                                            currLevel.getNextRoomVisited(xRoomPos, yRoomPos),
                                            currLevel.getNextRoomVar(xRoomPos, yRoomPos))
                            currRoom.drawRoom()
                            if currRoom.visited == False and len(currRoom.getEnemies) != 0:
                                currEnemies = currRoom.getEnemies
                                #generate_enemies()
                            currLevel.markVisited(xRoomPos, yRoomPos)
                            screen.blit(characterSprite, (currentX, currentY))
                except IndexError:
                    currRoom = room(0, 0, 0, 0, False, 0, 0, True, "a")
                    #currEnemies = currRoom.getEnemies()
                    currRoom.drawRoom()
                    xgridPosition = 6
                    ygridPosition = 2
                    currentX = 67*6
                    currentY = 67*2
                    screen.blit(characterSprite, (currentX, currentY))
                # Action Keys (interact/item)
                if event.key == pygame.K_e:
                    print('E')

                if event.key == pygame.K_SPACE:
                    print("SPACE")
        if event.type == pygame.MOUSEBUTTONDOWN:
            if menuMode:
                if width / 2 <= mouse[0] <= width / 2 + 300 and height / 2 <= mouse[1] <= height / 2 + 40:
                    currRoom.drawRoom()
                    screen.blit(characterSprite, (currentX, currentY))
                    menuMode = False
                # if the mouse is clicked on the
                # button the game is terminated
                elif width / 2 <= mouse[0] <= width / 2 + 300 and height / 2 + 40 <= mouse[1] <= height / 2 + 80:
                    running = False
    if debugMode:
        yRoomStr = str(yRoomPos)
        xRoomStr = str(xRoomPos)
        roomXCoords = menuFont.render(yRoomStr, True, pureBlack)
        roomYCoords = menuFont.render(xRoomStr, True, pureBlack)
        pygame.draw.rect(screen, debugBoxColor, [10, 10, 200, 40])
        screen.blit(roomXCoords, (20, 10))
        screen.blit(roomYCoords, (60, 10))
    #MENU
    if menuMode:
        # fills the screen with a color
        screen.fill(menuColor)

        # if mouse is hovered on a button it
        # changes to lighter shade
        if width / 2 <= mouse[0] <= width / 2 + 300 and height / 2 <= mouse[1] <= height / 2 + 40:
            pygame.draw.rect(screen, buttonSelected, [width / 2, height / 2, 200, 40])
        else:
            pygame.draw.rect(screen, buttonIdle, [width/2, height/2, 200, 40])

        if width / 2 <= mouse[0] <= width / 2 + 300 and height / 2 + 40 <= mouse[1] <= height / 2 + 80:
            pygame.draw.rect(screen, buttonSelected, [width / 2, height / 2 + 40 , 200, 40])
        else:
            pygame.draw.rect(screen, buttonIdle, [width / 2, height / 2 + 40, 200, 40])

        # superimposing the text onto our button
        screen.blit(startButton, (width / 2 + 20, height / 2))
        screen.blit(quitButton, (width / 2 + 65, height / 2 + 40))
    else:
        pass
    pygame.display.update()

