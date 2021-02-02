# FantasticGliding
import pygame
import random
import math
from pygame import mixer
from pygame.rect import Rect
from tkinter import *
thres = 338

pygame.init()

black = (0,0,0)
white = (255,0,0)


screen = pygame.display.set_mode((1500, 800))
icon = pygame.image.load('hang-gliding.png')
pygame.display.set_icon(icon)
sky = pygame.image.load("sky.jpeg")
game_over = pygame.image.load("GameOver.png")
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


Play_Again = pygame.font.Font('DS.otf',70)
kkl = '~~Play Again~~'
def sFA():
    ycWDFF = Play_Again.render(kkl,True,(0,0,0 ))
    screen.blit(ycWDFF,(354,434))

froms = True
def jolly():
    while froms is True:
        troing = pygame.mouse.get_pos()
        break
        
    if 338 < troing[0] < 676 and 438 < troing[1] < 488:
        forms = False
        print ('it works')
        while froms is True:            
            pygame.draw.rect(screen,white,(338,338+100,338,50))
            sFA()
            pygame.display.update()
            forms = False
            
    #else:
        #pygame.draw.rect(screen,BLUE,(338,338+100,338,50))
        #forms = False
        
        
    
def sl():
    ycl = ycp.render(ttt,True,(0,0,0 ))
    screen.blit(ycl,(800,600))

    

controls1 = pygame.font.Font('DS.otf',100)
fff = 'Controls'
def sd():
    ycs = controls1.render(fff,True,(0,0,0 ))
    screen.blit(ycs,(20,20))

controls2 = pygame.font.Font('DS.otf',100)
rrr = 'Down arrow - move down'
def sr():
    ycr = controls2.render(rrr,True,(0,0,0 ))
    screen.blit(ycr,(20,180))


controls = pygame.font.Font('DS.otf',100)
kkk = 'Up arrow - move up'
def ss():
    yck = controls.render(kkk,True,(0,0,0 ))
    screen.blit(yck,(20,100))

    


sis = 632
BLUE=(0,0,255)
tk = Tk()

       
#Golden Stars
Stars = []
StarsX = []
StarsY = []
NumOfStars = 4
for i in range(NumOfStars):
    Stars.append(pygame.image.load('gold-medal.png'))    
    StarsX.append(random.randint(5,1500))
    StarsY.append(random.randint(10,700))
    screen.blit(Stars[i], (StarsX[i],StarsY[i]))
    
#Starting Screen
while top is False:
    screen.blit(startscreen, (0,0))
    sl()
    sd()
    ss()
    sr()
    pygame.display.update()    
    for event in pygame.event.get():
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
                                for i in range(NumOfStars):
                                    screen.blit(Stars[i], (StarsX[i],StarsY[i]))
                                if tingu is True:
                                    for i in range(NumOfClouds):
                                        Sclouds.append(pygame.image.load('storm.png'))    
                                        ScloudsX.append(random.randint(600,7000))
                                        ScloudsY.append(random.randint(10,700))
                                        tingu = False
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

                            
                            
                            fart = True
                            tulu = True
                            thres = 338
                            sis = 632
                            BLUE=(0,0,255)

                            #Collision
                            for i in range (NumOfClouds):
                                if playerX > ScloudsX[i] and playerX < ScloudsX[i] + 80:
                                    if playerY > ScloudsY[i] and playerY < ScloudsY[i] + 80:                    
                                        if 338 < troing[0] < 676 and 438 < troing[1] < 488:
      
                                            while fart is True:
                                                
                                                jolly()
                                                pygame.display.update()
                                                if tulu is True:
                                                    screen.blit(game_over , (0,0))
                                                    pygame.draw.rect(screen,BLUE,(thres,thres+100,338,50))
                                                    sFA()
                                                    pygame.display.update()
                                                                                           
                                                
                                                    #tistu = False
                                                    
                                    
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

    
