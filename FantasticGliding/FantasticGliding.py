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
game_over = pygame.image.load("GameOver.jfif")
pygame.display.set_caption(":Fantastic Gliding:")
startscreen = pygame.image.load("start screen.jfif")
game_loop = True
playerX = 400
playerY = 400
playercy = 0
thuu = False
tusk = True
ugh = False
top = False
ycp = pygame.font.Font('Restu Bundah.otf',100)
ttt = 'Press enter to start'
def sl():
    ycl = ycp.render(ttt,True,(0,0,0 ))
    screen.blit(ycl,(800,600))


#Starting Screen
while top is False:
    screen.blit(startscreen, (0,0))
    sl()
    pygame.display.update()    
    for event in pygame.event.get():
        sl()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                top = True

                    #rain clouds
                Sclouds = []
                ScloudsX = []
                ScloudsY = []
                ScloudsXC = 2
                NumOfClouds = 50
                
                tingu = True

                     

                if tingu is True:

                    for i in range(NumOfClouds):
                        Sclouds.append(pygame.image.load('storm.png'))    
                        ScloudsX.append(random.randint(600,7000))
                        ScloudsY.append(random.randint(10,700))
                        
                    tistu = True   

                    #game loop
                    if top is True:    
                        while game_loop:
                            if tistu is True:
                                screen.blit(sky,(0,0))
                            #mixer.music.load('helicopterS.wav')

                            
                            #Cloud movement
                            if tistu is True:
                                for i in range(NumOfClouds):
                                    ScloudsX[i] -= ScloudsXC 
                                    screen.blit(Sclouds[i], (ScloudsX[i],ScloudsY[i]))

                            #player
                            
                            playerX += 2
                            player = pygame.image.load('helicopter.png')
                            if tistu is True:
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

                            
                            


                            #Collision
                            for i in range (NumOfClouds):
                                if playerX > ScloudsX[i] and playerX < ScloudsX[i] + 80:
                                    if playerY > ScloudsY[i] and playerY < ScloudsY[i] + 80:
                                        screen.blit(game_over , (0,0))
                                        pygame.display.update()
                                        tistu = False
                                
                            #player border    
                            
                            if playerY < 0:
                                playerY = 0
                                
                            if playerY > 715:
                                playerY = 715
                            
                            if playerX > 1400:
                                playerX = 0
                                ugh = True
                            if ugh is True:
                                for i in range(NumOfClouds):
                                    ScloudsX[i] - 1400
                                ugh = False

                            if tistu is True:
                                screen.blit(player, (playerX,playerY))   


                        pygame.display.update()

    
