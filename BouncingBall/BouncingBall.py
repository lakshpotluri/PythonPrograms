import pygame
from pygame import mixer
import math
import ctypes

user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

pygame.init()

game_loop = True

screen = pygame.display.set_mode((1500, 800))

#engine = pygame.display.set_mode((screensize))


grey = (170,170,170)

icon = pygame.image.load('bouncy.png')
pygame.display.set_icon(icon)

pygame.display.set_caption(":Bouncy-Ball!:")

background1 = pygame.image.load("background1.jpg")

background2 = pygame.image.load("background2.jpg")

pic = pygame.image.load("pic .png")

paddle = pygame.image.load("paddle.png")

easy_button = pygame.image.load("easy button.png")

intermediate_button = pygame.image.load("intermediate button.png")

basketball = pygame.image.load("basketball-ball.png")

basketball2 = pygame.image.load("basketball-ball.png")

proffesional_button = pygame.image.load("proffesional button.png")

paddleX = 1350
paddleY = 300
paddleYC = 0

controls2 = pygame.font.Font('DS.otf',60)
rrr = '''Press 'E' for Easy level '''
def sr():
    ycr = controls2.render(rrr,True,(0,0,0 ))
    screen.blit(ycr,(100,700))
    
controls1 = pygame.font.Font('DS.otf',60)
rrs = '''Press 'I' for Intermediate level'''
def ss():
    ycp = controls1.render(rrs,True,(0,0,0 ))
    screen.blit(ycp,(520,700))

controls3 = pygame.font.Font('DS.otf',50)
rrj = '''Press 'P' for Proffesional level'''
def sl():
    ycj = controls3.render(rrj,True,(0,0,0 ))
    screen.blit(ycj,(1065,700))


efjewjkpwefipfej = pygame.font.Font('DS.otf',110)
fe = '''Welcome to Bouncing Ball'''
def opefjigwqjIup():
    dvteneh5h3 = efjewjkpwefipfej.render(fe,True,(0,0,0))
    screen.blit(dvteneh5h3,(90,150))

adf = pygame.font.Font('DS.otf',110)
fl = '''please enjoy!'''
def dS():
    sdv = adf.render(fl,True,(0,0,0))
    screen.blit(sdv,(50,250))

basketballX = 400
basketballY = 360

basketballX2 = 0
basketballY2 = 360


                

while game_loop is True:
    screen.blit(background1, (0,0))
    screen.blit(easy_button, (200,600))
    pygame.draw.rect(screen,grey,(945,45,390,477))
    sr()
    ss()
    screen.blit(pic, (950 ,50)) 
    sl()
    dS()
    opefjigwqjIup()
    
    toll = False
    soll = True    

    for event in pygame.event.get():
         if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_e:
                 print ('E')
                 while game_loop is True:

                     if soll is True:
                         basketballX += 2
                         basketballY += 2
                     if soll is False:
                         basketballX += 2
                         basketballY -= 2


                     if toll is True:
                         basketballX2 += 2
                         basketballY2 += 2
                     if toll is False:
                         basketballX2 += 2
                         basketballY2 -= 2

                    
                     
                     screen.blit(background2, (0,0))

                     screen.blit(paddle, (1350,paddleY))
                     screen.blit(basketball, (basketballX,basketballY))
                     screen.blit(basketball2, (basketballX2,basketballY2))

                     pygame.display.update
                     
                     paddleY += paddleYC

                     
                     for event in pygame.event.get():
                         if event.type == pygame.KEYDOWN:
                             if event.key == pygame.K_UP:
                                 paddleYC = -2
                             if event.key == pygame.K_DOWN:
                                 paddleYC = 2
                         if event.type == pygame.KEYUP:
                             if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                                 paddleYC = 0
            
                     if paddleX == basketballX + 64:
                         if paddleY < basketballY + 64 < paddleY + 116:
                             while game_loop is True:
                                 basketballY -= 2
                                 basketballX -= 2
                                 

                     if paddleX == basketballX2 + 64:
                         if paddleY < basketballY2 + 64 < paddleY + 116:
                             while game_loop is True:
                                 basketballY2 -= 2
                                 basketballX2 -= 2
                                 
                                 

                                 
                     if paddleY < 51:
                         paddleY = 51
                     if paddleY > 510:
                         paddleY = 510

                         
                     if basketballY < 51:
                         basketballY = 51
                         soll = True
                     if basketballY > 650:
                         basketballY = 650
                         soll = False
                         
                     if basketballY2 < 51:
                         basketballY2 = 51
                         toll = True
                     if basketballY2 > 650:
                         basketballY2 = 650
                         toll = False           

                         
                        
                     pygame.display.update()
                     
             if event.key == pygame.K_i:
                print ('I')
                while game_loop is True:

                    if soll is True:
                        basketballX += 2
                        basketballY += 2
                    if soll is False:
                        basketballX += 2
                        basketballY -= 2

                    if toll is True:
                        basketballX2 += 2
                        basketballY2 += 2
                    if toll is False:
                        basketballX2 += 2
                        basketballY2 -= 2


                    screen.blit(background2, (0,0))
                    paddleY += paddleYC
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_UP:
                                paddleYC = -2
                            if event.key == pygame.K_DOWN:
                                paddleYC = 2
                        if event.type == pygame.KEYUP:
                            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                                paddleYC = 0
                                
                    if paddleY < 51:
                        paddleY = 51
                    if paddleY > 510:
                        paddleY = 510

                        
                    if paddleX == basketballX2 + 64:
                        if paddleY < basketballY2 + 64 < paddleY + 116:
                            while game_loop is True:
                                basketballY2 -= 2
                                basketballX2 -= 2
                    if paddleX == basketballX + 64:
                        if paddleY < basketballY + 64 < paddleY + 116:
                            while game_loop is True:
                                basketballY -= 2
                                basketballX -= 2                        
                    if basketballY < 51:
                        basketballY = 51
                        soll = True
                    if basketballY > 650:
                        basketballY = 650
                        soll = False

                    if basketballY2 < 51:
                        basketballY2 = 51
                        toll = True
                    if basketballY2 > 650:
                        basketballY2 = 650
                        toll = False
                        
                        
                    screen.blit(basketball, (basketballX,basketballY))
                    screen.blit(basketball2, (basketballX2,basketballY2))
                    screen.blit(paddle, (1350,paddleY))            
                    pygame.display.update()
                
             if event.key == pygame.K_p:
                print ('P')
                while game_loop is True:

                    if soll is True:
                        basketballX += 2
                        basketballY += 2
                    if soll is False:
                        basketballX += 2
                        basketballY -= 2


                    if toll is True:
                        basketballX2 += 2
                        basketballY2 += 2
                    if toll is False:
                        basketballX2 += 2
                        basketballY2 -= 2

                    screen.blit(background2, (0,0))
                    paddleY += paddleYC
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_UP:
                                paddleYC = -2
                            if event.key == pygame.K_DOWN:
                                paddleYC = 2
                        if event.type == pygame.KEYUP:
                            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                                paddleYC = 0                    
                        
                    if paddleY < 51:
                        paddleY = 51
                    if paddleY > 510:
                        paddleY = 510

                        
                    if basketballY < 51:
                        basketballY = 51
                        soll = True
                    if basketballY > 650:
                        basketballY = 650
                        soll = False

                    if basketballY2 < 51:
                        basketballY2 = 51
                        toll = True
                    if basketballY2 > 650:
                        basketballY2 = 650
                        toll = False
                        
                    if paddleX == basketballX2 + 64:
                        if paddleY < basketballY2 + 64 < paddleY + 116:
                            while game_loop is True:
                                basketballY2 -= 2
                                basketballX2 -= 2                        
                    if paddleX == basketballX + 64:
                        if paddleY < basketballY + 64 < paddleY + 116:
                            while game_loop is True:
                                basketballY -= 2
                                basketballX -= 2                        
                    screen.blit(basketball, (basketballX,basketballY))
                    screen.blit(basketball2, (basketballX2,basketballY2))                   
                    screen.blit(paddle, (1350,paddleY))                    
                    pygame.display.update()
                
             if event.type == pygame.QUIT:
                 pygame.display.quit()
                 pygame.quit()




    
    screen.blit(intermediate_button, (660,600))
    screen.blit(proffesional_button, (1220,600))
    pygame.display.update()
    
        
    


