import pygame
import random
import math
from pygame import mixer

#initialize the pygame

pygame.init()
clock = pygame.time.Clock()
tort = True

#create the screen
screen = pygame.display.set_mode((800, 600))
while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            troing = pygame.mouse.get_pos()
            print (troing)
    pygame.display.update()
