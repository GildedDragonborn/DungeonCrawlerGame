import pygame
import os
import random
import math
import json
from playerCharacter import PlayerCharacter
from level import level
from room import room

# initializes pygame
pygame.init()

width = 800
height = 600
# 12x9 w=800 h=600
roomArray = [[0]*12 for i in range(9)] # each index represents the state of a square in the current room

# defining a font
smallfont = pygame.font.SysFont('franklingothicmedium', 35)

# rendering a text written in
# this font
quitButton = smallfont.render('quit', True, (255,255,255))
startButton = smallfont.render('start game', True, (255,255,255))
color_light = (145,145,145)
color_dark = (75,75,75)

with open("GameData/characterData.json") as infile: # DEFAULTS TO SLOT 1, COULD INTRODUCE POTENTIAL SAVESWAP BUG
    data = json.load(infile)
PC = PlayerCharacter(data)

# creates the screen
screen = pygame.display.set_mode((width, height))

# background
background = pygame.image.load(os.path.join("Assets", "testBackground.png"))

# title and icon
pygame.display.set_caption("Rougelike Game")
icon = pygame.image.load(os.path.join("Assets", "tempicon.png"))  # logo goes here
pygame.display.set_icon(icon)


# playercharacter
def loadChar(charFile: str):
    with open(charFile) as infile:
        data = json.load(infile)
    PC = PlayerCharacter(data)


def DrawGrid(): # Temporary while room.py is being developed
    screen.fill((200, 200, 200))
    lineColor = pygame.Color(0, 0, 0, 255)  # RGB alpha
    x = 0
    y = 0
    increment = width/12
    #for x in range(0, width, blocksize):
    #    for y in range(0, height, blocksize):
    #        rect = pygame.Rect(x, y, blocksize, blocksize)
    #        pygame.draw.rect(screen, lineColor, rect, 1)
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

    def generateDungeonLevel(seed: int) -> level:
        pass


screen.fill((255, 255, 255))
# screen.blit(background, (0, 0))


#game loop
running = True
menuMode = True
character = "GameData/characterData.json"
loadChar(character)
while running:
    DrawGrid()
    # stores the (x,y) coordinates into
    # the variable as a tuple
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN: # HANDLES KEY PRESSES
            if event.key == pygame.K_ESCAPE:
                if menuMode == True:
                    running = False
                else:
                    menuMode = True
            # For all actions in the game
            if not menuMode:
                # Movement Keys
                if event.key == pygame.K_w:
                    print('W')
                if event.key == pygame.K_a:
                    print('A')
                if event.key == pygame.K_s:
                    print('S')
                if event.key == pygame.K_d:
                    print('D')
                # Action Keys (interact/item)
                if event.key == pygame.K_e:
                    print('E')
                if event.key == pygame.K_SPACE:
                    print("SPACE")
        if event.type == pygame.MOUSEBUTTONDOWN:
            if menuMode:
                if width / 2 <= mouse[0] <= width / 2 + 300 and height / 2 <= mouse[1] <= height / 2 + 40:
                    DrawGrid()
                    menuMode = False
                # if the mouse is clicked on the
                # button the game is terminated
                elif width / 2 <= mouse[0] <= width / 2 + 300 and height / 2 + 40 <= mouse[1] <= height / 2 + 80:
                    running = False
    #MENU
    if menuMode:
        # fills the screen with a color
        screen.fill((60,25,60))

        # if mouse is hovered on a button it
        # changes to lighter shade
        if width / 2 <= mouse[0] <= width / 2 + 300 and height / 2 <= mouse[1] <= height / 2 + 40:
            pygame.draw.rect(screen, color_light, [width / 2, height / 2, 200, 40])
        else:
            pygame.draw.rect(screen, color_dark, [width/2, height/2, 200, 40])

        if width / 2 <= mouse[0] <= width / 2 + 300 and height / 2 + 40 <= mouse[1] <= height / 2 + 80:
            pygame.draw.rect(screen, color_light, [width / 2, height / 2 + 40 , 200, 40])
        else:
            pygame.draw.rect(screen, color_dark, [width / 2, height / 2 + 40, 200, 40])

        # superimposing the text onto our button
        screen.blit(startButton, (width / 2 + 20, height / 2))
        screen.blit(quitButton, (width / 2 + 65, height / 2 + 40))
    else:
        pass
    pygame.display.update()

