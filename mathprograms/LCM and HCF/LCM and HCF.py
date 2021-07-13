#lcm hcf
import pygame
import math
import ctypes


#Program Begining



user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

screen = pygame.display.set_mode((screensize))
pygame.display.set_caption("LCM and HCF")

loop = True

background1 = pygame.image.load("background1.jpg")

while loop is True:
    screen.blit(background1, (0,0))
    pygame.display.update()
