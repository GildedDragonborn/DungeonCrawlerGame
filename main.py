import pygame
import os
import random
import math
import json
from playerCharacter import PlayerCharacter
from level import level
from room import room
import BattleScene
from GameData.colorData import *

# initializes pygame
pygame.init()


width = 800
height = 600
# 12x9 w=800 h=600
seed = int(random.randint(0, 10_000_000_000))
random.seed(a=seed, version=2)
# Level setup
currLevel = level(seed) #demoseed = 33667333
roomArray = currLevel.mapLayout# [[0]*12 for i in range(9)] # each index represents the state of a square in the current room
print(seed)

# defining a font
smallfont = pygame.font.SysFont('franklingothicmedium', 35)

# rendering menu text
quitButton = smallfont.render('quit', True, (255,255,255))
startButton = smallfont.render('start game', True, (255,255,255))


with open("GameData/characterData.json") as infile: # DEFAULTS TO SLOT 1, COULD INTRODUCE POTENTIAL SAVESWAP BUG
    data = json.load(infile)
PC = PlayerCharacter(data)

# Player Positional Arguments
currentX = -15+67 # Starts Player at X = -15+67
currentY = 67 # Starts Player at Y = 67
xgridPosition = 1
ygridPosition = 1
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

def generate_enemies():
    if currEnemies is not None:
        if len(currEnemies) == 0:
            print("NO ENEMIES PRESENT")
        for i in currEnemies:
            if len(i) == 3:
                if i[2] is not None:
                    screen.blit(pygame.image.lodad(os.path.join(i[2].spriteName, i[2].spritePath),
                                                   (i[0] * 67 - 15, i[1] * 67)))
                else:
                    print("ERROR: NO ENEMY PRESENT")
            else:
                print("ERROR len(i) IS NOT 3")
# Player Character sprite
characterSprite = pygame.image.load(os.path.join(PC.spritePath, PC.spriteName))
characterSpriteWidth = characterSprite.get_rect().width
characterSpriteHeight = characterSprite.get_rect().height
characterSprite = pygame.transform.scale(characterSprite, (characterSpriteHeight/3, characterSpriteHeight/4))

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


currRoom = room(currLevel.getNextRoom(xRoomPos, yRoomPos), 1, xRoomPos, yRoomPos, False)
print(currLevel.getNextRoom(xRoomPos,yRoomPos), xRoomPos, yRoomPos)
    #screen.blit(pygame.image.load(os.path.join("Assets", "testRock.png")), (67, 67))



screen.fill((255, 255, 255))
currEnemies = []

#game loop
running = True
menuMode = True
debugMode = False
character = "GameData/characterData.json"
loadChar(character)
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
                            for i in currEnemies:
                                i[2].movement(currentX, currentY)
                                if i[2].currX == currentX and i[2].currY == currentY and not encounterComplete:
                                    battleScene = scene(enemy.encounter, PC)
                                    battleScene.runScene()
                                    encounterComplete = True
                                    currEnemies.remove(i)
                                    currRoom.drawRoom()
                                elif i[2].currX == currentX and i[2].currY == currentY and encounterComplete:
                                    currEnemies.remove(i)
                        screen.blit(characterSprite, (currentX, currentY))
                        if currRoom.getTile(xgridPosition, ygridPosition) == 99: # BOSSROOM TRAPDOOR
                            currLevel.incrLevel(currLayer)
                            currLayer = currLayer + 1
                        if currRoom.getTile(xgridPosition, ygridPosition) == 6:
                            # TELEPORT TO SOUTH DOOR
                            currentX = (67 * 5) - 15
                            currentY = 67*7
                            xgridPosition = 5
                            ygridPosition = 7
                            yRoomPos = yRoomPos - 1
                            currRoom = room(currLevel.getNextRoom(xRoomPos, yRoomPos), 1, xRoomPos, yRoomPos, currRoom.getNextRoomHostile)
                            currRoom.drawRoom()
                            if currRoom.visited == False:
                                currEnemies = currRoom.getEnemies
                                generate_enemies()
                            currRoom.markVisited()
                            screen.blit(characterSprite, (currentX, currentY))
                        if currRoom.getTile(xgridPosition, ygridPosition) == 17:
                            # TELEPORT TO SOUTH DOOR
                            currentX = (67 * 6) - 15
                            currentY = 67*7
                            xgridPosition = 6
                            ygridPosition = 7
                            # MOVES TO ROOM BELOW
                            yRoomPos = yRoomPos - 1
                            currRoom = room(currLevel.getNextRoom(xRoomPos, yRoomPos), 1, xRoomPos, yRoomPos, currRoom.getNextRoomHostile)
                            currRoom.drawRoom()
                            if currRoom.visited == False:
                                currEnemies = currRoom.getEnemies
                                generate_enemies()
                            currRoom.markVisited()
                            screen.blit(characterSprite, (currentX, currentY))
                    if event.key == pygame.K_a and currRoom.playerMoveCheck(xgridPosition-1, ygridPosition):  # and currentX >= 52 and xgridPosition > -6
                        print(xgridPosition, ygridPosition)
                        currentX = currentX-67
                        xgridPosition = xgridPosition - 1
                        # Redraw the room
                        currRoom.drawRoom()
                        if len(currEnemies) != 0:
                            encounterComplete = False
                            for i in currEnemies:
                                i[2].movement(currentX, currentY)
                                if i[2].currX == currentX and i[2].currY == currentY and not encounterComplete:
                                    battleScene = scene(enemy.encounter, PC)
                                    battleScene.runScene()
                                    encounterComplete = True
                                    currEnemies.remove(i)
                                else:
                                    currEnemies.remove(i)
                        screen.blit(characterSprite, (currentX, currentY))
                        if currRoom.getTile(xgridPosition, ygridPosition) == 99: # BOSSROOM TRAPDOOR
                            #currLevel.incrLayer(currLayer)
                            #currLayer = currLayer + 1
                            print("Thank you for playing my demo!")
                            running = False
                        if currRoom.getTile(xgridPosition, ygridPosition) == 12:
                            # TELEPORT TO EAST DOOR
                            currentX = 67*10-15
                            currentY = 67*4
                            xgridPosition = 10
                            ygridPosition = 4
                            xRoomPos = xRoomPos - 1
                            currRoom = room(currLevel.getNextRoom(xRoomPos, yRoomPos), 1, xRoomPos, yRoomPos, currRoom.getNextRoomHostile)
                            currRoom.drawRoom()
                            if currRoom.visited == False:
                                currEnemies = currRoom.getEnemies
                                generate_enemies()
                            currRoom.markVisited()
                            screen.blit(characterSprite, (currentX, currentY))
                    if event.key == pygame.K_s and currRoom.playerMoveCheck(xgridPosition, ygridPosition+1): # ygridPosition > -4: # and currentY <= height-67
                        print(xgridPosition, ygridPosition)
                        currentY = currentY+67
                        ygridPosition = ygridPosition + 1
                        #Redraw The Room
                        currRoom.drawRoom()
                        if len(currEnemies) != 0:
                            encounterComplete = False
                            for i in currEnemies:
                                i[2].movement(currentX, currentY)
                                if i[2].currX == currentX and i[2].currY == currentY and not encounterComplete:
                                    battleScene = scene(enemy.encounter, PC)
                                    battleScene.runScene()
                                    encounterComplete = True
                                    currEnemies.remove(i)
                                else:
                                    currEnemies.remove(i)
                        screen.blit(characterSprite, (currentX, currentY))
                        if currRoom.getTile(xgridPosition, ygridPosition) == 99: # BOSSROOM TRAPDOOR
                            currLevel.incrLevel(currLayer)
                            currLayer = currLayer + 1
                        if currRoom.getTile(xgridPosition, ygridPosition) == 10:
                            # TELEPORT TO NORTH DOOR LEFT
                            currentX = (67*5) - 15
                            currentY = 67
                            xgridPosition = 5
                            ygridPosition = 1
                            yRoomPos = yRoomPos + 1
                            currRoom = room(currLevel.getNextRoom(xRoomPos, yRoomPos), 1, xRoomPos, yRoomPos, currRoom.getNextRoomHostile)
                            currRoom.drawRoom()
                            if currRoom.visited == False:
                                currEnemies = currRoom.getEnemies
                                generate_enemies()
                            currRoom.markVisited()
                            screen.blit(characterSprite, (currentX, currentY))
                        if currRoom.getTile(xgridPosition, ygridPosition) == 18:
                            # TELEPORT TO NORTH DOOR RIGHT
                            currentX = (67*6) - 15
                            currentY = 67
                            xgridPosition = 6
                            ygridPosition = 1
                            yRoomPos = yRoomPos + 1
                            currRoom = room(currLevel.getNextRoom(xRoomPos, yRoomPos), 1, xRoomPos, yRoomPos, currRoom.getNextRoomHostile)
                            currRoom.drawRoom()
                            if currRoom.visited == False:
                                currEnemies = currRoom.getEnemies
                                generate_enemies()
                            currRoom.markVisited()
                            screen.blit(characterSprite, (currentX, currentY))
                    if event.key == pygame.K_d and currRoom.playerMoveCheck(xgridPosition+1, ygridPosition): # and xgridPosition < 5: # and currentX <= width-82
                        print(xgridPosition, ygridPosition)
                        currentX = currentX+67
                        xgridPosition = xgridPosition + 1
                        #Redraw The Room
                        currRoom.drawRoom()
                        if len(currEnemies) != 0:
                            encounterComplete = False
                            for i in currEnemies:
                                i[2].movement(currentX, currentY)
                                if i[2].currX == currentX and i[2].currY == currentY and not encounterComplete:
                                    battleScene = scene(enemy.encounter, PC)
                                    battleScene.runScene()
                                    encounterComplete = True
                                    currEnemies.remove(i)
                                else:
                                    currEnemies.remove(i)
                        screen.blit(characterSprite, (currentX, currentY))
                        if currRoom.getTile(xgridPosition, ygridPosition) == 99: # BOSSROOM TRAPDOOR
                            currLevel.incrLevel(currLayer)
                            currLayer = currLayer + 1
                        if currRoom.getTile(xgridPosition, ygridPosition) == 8:
                            # TELEPORT TO EAST DOOR
                            currentX = 67 - 15
                            currentY = 67 * 4
                            xgridPosition = 1
                            ygridPosition = 4
                            xRoomPos = xRoomPos + 1
                            currRoom = room(currLevel.getNextRoom(xRoomPos, yRoomPos), 1, xRoomPos, yRoomPos, currRoom.getNextRoomHostile)
                            currRoom.drawRoom()
                            if currRoom.visited == False:
                                currEnemies = currRoom.getEnemies
                                generate_enemies()
                            currRoom.markVisited()
                            screen.blit(characterSprite, (currentX, currentY))
                except IndexError:
                    currRoom = room(0, 0, 0, 0, False)
                    currEnemies = currRoom.getEnemies()
                    currRoom.drawRoom()
                    xgridPosition = 6
                    ygridPosition = 2
                    currentX = 67*6 - 15
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
        roomXCoords = smallfont.render(yRoomStr, True, pureBlack)
        roomYCoords = smallfont.render(xRoomStr, True, pureBlack)
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

