# FantasticGliding
import pygame
import random
import math
from pygame import mixer
pygame.init()
screen = pygame.display.set_mode((1500, 800))
icon = pygame.image.load('hang-gliding.png')
pygame.display.set_icon(icon)
sky = pygame.image.load("sky.jpeg")
pygame.display.set_caption(":Fantastic Gliding:")
game_loop = True
playerX = 400
playerY = 400
playercy = 0
thuu = False
tusk = True
#rain clouds
Sclouds = []
ScloudsX = []
ScloudsY = []
ScloudsXC = 2
NumOfClouds = 70  

NumOfCloudsb = 1000 

#for i in range(NumOfClouds):
#    screen.blit(pygame.image.load('storm.png'),(700,200+i*100))

for i in range(NumOfClouds):
    Sclouds.append(pygame.image.load('storm.png'))    
    ScloudsX.append(random.randint(600,6000))
    ScloudsY.append(random.randint(10,700))
    


        

#game loop
while game_loop:
    screen.blit(sky,(0,0))
    #Cloud movement
    
    for i in range(NumOfClouds):
        ScloudsX[i] -= ScloudsXC
        screen.blit(Sclouds[i], (ScloudsX[i],ScloudsY[i]))

    #player
    
    playerX += 2
    player = pygame.image.load('helicopter.png')
    screen.blit(player, (playerX,playerY))        
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                playercy = -5
                thuu = True                
            if event.key == pygame.K_DOWN:
                playercy = 5
                thuu = True

    if thuu is True:
        playerY += playercy
        thuu = False

        
    #player border    
    
    if playerY < 0:
        playerY = 0
    if playerY > 715:
        playerY = 715
    if playerX > 1400:
        playerX = 0    
    screen.blit(player, (playerX,playerY))   


    pygame.display.update()
