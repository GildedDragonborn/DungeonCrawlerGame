import pygame
import random
import math
from playerCharacter import PlayerCharacter

# initializes pygame
pygame.init()

# creates the screen
screen = pygame.display.set_mode((600, 600))

# background
background = pygame.image.load("testBackground.png")

# title and icon
pygame.display.set_caption("Rougelike Game")
icon = pygame.image.load("tempicon.png")  #logo goes here
pygame.display.set_icon(icon)

# playercharacter
PC = PlayerCharacter()
PC.export()

#game loop
running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False