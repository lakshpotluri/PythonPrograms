import pygame
from pygame import mixer
import math
import sys
import ctypes
import random

user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

pygame.init()

game_loop = True

screen = pygame.display.set_mode((1500, 800))

#engine = pygame.display.set_mode((screensize))

house_timing = 1

grey = (255)

icon = pygame.image.load('bouncy.png')
pygame.display.set_icon(icon)

pygame.display.set_caption(":Bouncy-Ball!:")

background1 = pygame.image.load("background1.png")

background12 = pygame.image.load("background12.png")

background2 = pygame.image.load("background2.jpg")

game_over_screen = pygame.image.load("game_over.jpg")


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


balls = 2

controls2 = pygame.font.Font('DS.otf',60)
rrr = '''Press 'E' for Easy level '''
def sr():
    ycr = controls2.render(rrr,True,(grey,grey,grey ))
    screen.blit(ycr,(100,700))
    
controls1 = pygame.font.Font('DS.otf',60)
rrs = '''Press 'I' for Intermediate level'''
def ss():
    ycp = controls1.render(rrs,True,(grey,grey,grey))
    screen.blit(ycp,(520,700))

controls3 = pygame.font.Font('DS.otf',50)
rrj = '''Press 'P' for Proffesional level'''
def sl():
    ycj = controls3.render(rrj,True,(grey,grey,grey))
    screen.blit(ycj,(1065,700))

lscreen = random.randint(1,200)

efjewjkpwefipfej = pygame.font.Font('DS.otf',110)
fe = '''Welcome to Bouncing Ball'''
def opefjigwqjIup():
    dvteneh5h3 = efjewjkpwefipfej.render(fe,True,(grey,grey,grey))
    screen.blit(dvteneh5h3,(90,55))

adf = pygame.font.Font('DS.otf',110)
fl = '''please enjoy!'''
def dS():
    sdv = adf.render(fl,True,(grey,grey,grey))
    screen.blit(sdv,(50,130))

basketballX = 400
basketballY = 360

basketballX2 = 0
basketballY2 = 360

poop = True
soop = True                

for_the_other_one = False
for_the_other_one2 = False

lolly = True
polly = True

another_game_loop = True

mixer.music.load('EOTT.ogg')
mixer.music.play(-1)
    
while game_loop is True:

    #pygame.draw.rect(screen,grey,(945,45,390,477))
    sr()
    ss()
    #screen.blit(pic, (950 ,50)) 
    sl()
    screen.blit(easy_button, (200,600))
    screen.blit(intermediate_button, (660,600))
    screen.blit(proffesional_button, (1220,600))
    pygame.display.update()

    if lscreen >= 0 and lscreen <= 100:
        screen.blit(background1, (0,0))
    if lscreen <=200 and lscreen >= 100:
        screen.blit(background12, (0,0))
        dS()
        opefjigwqjIup()
    
    toll = False
    soll = True    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:    
                print ('E')
                while game_loop is True:
            
                    if basketballX >= 1500:
                        if balls == 2:
                            balls == 1
                            poop = False
                            for_the_other_one = True
                    if basketballX2 >= paddleX:
                        if balls == 1:
                            screen.blit(game_over_screen, (0,0))
                            pygame.display.update()
                                        
                                                                
                    if basketballX2 >= 1500:
                        if balls == 2:
                            balls == 1
                            soop = False
                            for_the_other_one = True
                    if basketballX2 >= paddleX:
                        if balls == 1:
                            balls == 0
                            screen.blit(game_over_screen, (0,0))
                            pygame.display.update()                                 


                #detects paddle and ball touch


                    if paddleY < basketballY + 51 and paddleY + 116 >= basketballY + 51:
                        if basketballX == paddleX:
                            print('ok')
                    if paddleY + 116 < basketballY + 51 and paddleY + 232 >= basketballY + 51:
                        if basketballX == paddleX:
                            print('ok')
                            


                #detects paddle and ball2 touch

                    if paddleY < basketballY2 + 51 and paddleY + 116 >= basketballY2 + 51:
                        if basketballX2 == paddleX:
                            print('ok')                        
                    if paddleY + 116 < basketballY2 + 51 and paddleY + 232 >= basketballY2 + 51:
                        if basketballX2 == paddleX:
                            print('yeah!!!')

                    
                    if poop is True:        
                        if soll is True:
                            basketballX += house_timing
                            basketballY += house_timing
                        if soll is False:
                            basketballX += house_timing
                            basketballY -= house_timing

                    if soop is True:   
                        if toll is True:
                            basketballX2 += house_timing
                            basketballY2 += house_timing
                        if toll is False:
                            basketballX2 += house_timing
                            basketballY2 -= house_timing
                            
                    if soop is False:
                        balls = 1


                    if soop or poop is True:
                        screen.blit(background2, (0,0))

                    if soop or poop is True:
                        screen.blit(paddle, (1350,paddleY))
                    if poop or soop is True:
                        screen.blit(basketball, (basketballX,basketballY))
                    if soop or poop is True:
                        screen.blit(basketball2, (basketballX2,basketballY2))

                    pygame.display.update()
                     
                    paddleY += paddleYC
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_UP:
                                paddleYC = -house_timing
                            if event.key == pygame.K_DOWN:
                                paddleYC = house_timing
                        if event.type == pygame.KEYUP:
                            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                                paddleYC = 0
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                            
                            
                                 
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
                     
            if event.key == pygame.K_i:
                print ('I')
                while game_loop is True:
                    
            
                    if basketballX >= 1500:
                        if balls == 2:
                            balls == 1
                            poop = False
                            for_the_other_one = True
                    if basketballX2 >= paddleX:
                        if balls == 1:
                            screen.blit(game_over_screen, (0,0))
                            pygame.display.update()
                                        
                                                                
                    if basketballX2 >= 1500:
                        if balls == 2:
                            balls == 1
                            soop = False
                            for_the_other_one = True
                    if basketballX2 >= paddleX:
                        if balls == 1:
                            balls == 0
                            screen.blit(game_over_screen, (0,0))
                            pygame.display.update()                                 


                #detects paddle and ball touch


                    if paddleY < basketballY + 32 and paddleY + 116 >= basketballY + 32:
                        if basketballX == paddleX:
                            print('ok')
                    if paddleY + 116 < basketballY + 32 and paddleY + 232 >= basketballY + 32:
                        if basketballX == paddleX:
                            print('ok')
                            


                #detects paddle and ball2 touch

                    if paddleY < basketballY2 + 51 and paddleY + 116 >= basketballY2 + 51:
                        if basketballX2 == paddleX:
                            print('ok')                        
                    if paddleY + 116 < basketballY2 + 51 and paddleY + 232 >= basketballY2 + 51:
                        if basketballX2 == paddleX:
                            print('yeah!!!')

                    
                    if poop is True:        
                        if soll is True:
                            basketballX += house_timing
                            basketballY += house_timing
                        if soll is False:
                            basketballX += house_timing
                            basketballY -= house_timing

                    if soop is True:   
                        if toll is True:
                            basketballX2 += house_timing
                            basketballY2 += house_timing
                        if toll is False:
                            basketballX2 += house_timing
                            basketballY2 -= house_timing
                            
                    if soop is False:
                        balls = 1


                    if soop or poop is True:
                        screen.blit(background2, (0,0))

                    if soop or poop is True:
                        screen.blit(paddle, (1350,paddleY))
                    if poop or soop is True:
                        screen.blit(basketball, (basketballX,basketballY))
                    if soop or poop is True:
                        screen.blit(basketball2, (basketballX2,basketballY2))

                    pygame.display.update()
                     
                    paddleY += paddleYC
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_UP:
                                paddleYC = -house_timing
                            if event.key == pygame.K_DOWN:
                                paddleYC = house_timing
                        if event.type == pygame.KEYUP:
                            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                                paddleYC = 0
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                            
                            
                                 
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
                    
            if event.key == pygame.K_p:
                print ('P')
                while game_loop is True:
                    
            
                    if basketballX >= 1500:
                        if balls == 2:
                            balls == 1
                            poop = False
                            for_the_other_one = True
                    if basketballX2 >= paddleX:
                        if balls == 1:
                            screen.blit(game_over_screen, (0,0))
                            pygame.display.update()
                                        
                                                                
                    if basketballX2 >= 1500:
                        if balls == 2:
                            balls == 1
                            soop = False
                            for_the_other_one = True
                    if basketballX2 >= paddleX:
                        if balls == 1:
                            balls == 0
                            screen.blit(game_over_screen, (0,0))
                            pygame.display.update()                                 


                #detects paddle and ball touch


                    if paddleY < basketballY + 51 and paddleY + 116 >= basketballY + 51:
                        if basketballX == paddleX:
                            print('ok')
                    if paddleY + 116 < basketballY + 51 and paddleY + 232 >= basketballY + 51:
                        if basketballX == paddleX:
                            print('ok')
                            


                #detects paddle and ball2 touch

                    if paddleY < basketballY2 + 51 and paddleY + 116 >= basketballY2 + 51:
                        if basketballX2 == paddleX:
                            print('ok')                        
                    if paddleY + 116 < basketballY2 + 51 and paddleY + 232 >= basketballY2 + 51:
                        if basketballX2 == paddleX:
                            print('yeah!!!')

                    
                    if poop is True:        
                        if soll is True:
                            basketballX += house_timing
                            basketballY += house_timing
                        if soll is False:
                            basketballX += house_timing
                            basketballY -= house_timing

                    if soop is True:   
                        if toll is True:
                            basketballX2 += house_timing
                            basketballY2 += house_timing
                        if toll is False:
                            basketballX2 += house_timing
                            basketballY2 -= house_timing
                            
                    if soop is False:
                        balls = 1


                    if soop or poop is True:
                        screen.blit(background2, (0,0))

                    if soop or poop is True:
                        screen.blit(paddle, (1350,paddleY))
                    if poop or soop is True:
                        screen.blit(basketball, (basketballX,basketballY))
                    if soop or poop is True:
                        screen.blit(basketball2, (basketballX2,basketballY2))

                    pygame.display.update()
                     
                    paddleY += paddleYC
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_UP:
                                paddleYC = -house_timing
                            if event.key == pygame.K_DOWN:
                                paddleYC = house_timing
                        if event.type == pygame.KEYUP:
                            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                                paddleYC = 0
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                            
                            
                                 
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
                



    #pygame.draw.rect(screen,grey,(945,45,390,477))
    sr()
    ss()
    #screen.blit(pic, (950 ,50)) 
    sl()
    screen.blit(easy_button, (200,600))
    screen.blit(intermediate_button, (660,600))
    screen.blit(proffesional_button, (1220,600))
    
        
    


