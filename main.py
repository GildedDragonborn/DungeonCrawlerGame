import pygame
import os
import random
import math
from playerCharacter import PlayerCharacter
from level import level
from room import room

# initializes pygame
pygame.init()

width = 800
height = 600
# 12x9 w=800 h=600
roomArray = [[0]*12 for i in range(9)] # each index represents the state of a square in the current room

# creates the screen
screen = pygame.display.set_mode((width, height))

# background
background = pygame.image.load(os.path.join("Assets", "testBackground.png"))

# title and icon
pygame.display.set_caption("Rougelike Game")
icon = pygame.image.load(os.path.join("Assets", "tempicon.png"))  #logo goes here
pygame.display.set_icon(icon)

# playercharacter
PC = PlayerCharacter()
PC.export()


def DrawGrid(): # Temporary while room.py is being developed
    #blocksize = 20
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


screen.fill((200, 200, 200))
# screen.blit(background, (0, 0))
#game loop
running = True
while running:
    DrawGrid()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        pygame.display.update()


