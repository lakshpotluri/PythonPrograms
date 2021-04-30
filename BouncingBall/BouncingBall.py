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

bwhahaha = False

if bwhahaha is False:
    house_timing = 1.5
    
grey = (255)

icon = pygame.image.load('bouncy.png')
pygame.display.set_icon(icon)

pygame.display.set_caption(":Bouncy-Ball!:")

background1 = pygame.image.load("background1.png")

background4 = pygame.image.load("background4.jpg")

background5 = pygame.image.load("background3.jpg")

background12 = pygame.image.load("background12.png")

background3 = pygame.image.load("background5.jpg")

background2 = pygame.image.load("background2.jpg")

game_over_screen = pygame.image.load("game_over.jpg")

game2 = pygame.image.load("game2.jpg")


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

bouce = mixer.Sound('BASKETBL.wav')
impact = mixer.Sound('at_last.mp3')

score1 = 0

font = pygame.font.Font('Sweety Rasty (3).otf',200)

def score12(x,y):
    score = font.render("score :" + str(score1),True,(grey,grey,grey ))
    if lulu or pulu is True:                            
        screen.blit(score,(x,y))
    pygame.display.update()


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

lscreen = random.randint(1,1000)

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

basketballX = 600
basketballY = 360

basketballX2 = 51
basketballY2 = 360

lol = False
pol = False

gscreen = random.randint(1,200)

poop = True
soop = True                

for_the_other_one = False
for_the_other_one2 = False

lolly = True
polly = True

false = False
true = True
palse = False
prue = True

cmon = False
lmon = False

uhh = random.randint(1,2)

another_game_loop = True

mixer.music.load('EOTT.ogg')
mixer.music.play(-1)

kulja = False
sim_sim = False

prank = False
mang = False

kunt = False
punt = False

sutu = False
putu = False

print(lscreen)

pulu = True
lulu = True

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
        dS()
        opefjigwqjIup()
    if lscreen >= 200 and lscreen <= 301:
        screen.blit(background3, (0,0))
    if lscreen >= 300 and lscreen <= 401:
        screen.blit(background4, (0,0))
    if lscreen <= 201 and lscreen >= 99:
        screen.blit(background12, (0,0))
        dS()
        opefjigwqjIup()
    if lscreen >= 300 and lscreen <= 601:
        screen.blit(background4, (0,0))        
        dS()
        opefjigwqjIup()
    if lscreen >= 600:
        screen.blit(background5, (0,0))        
        dS()
        opefjigwqjIup()

        
    if uhh == 1:
        toll = True
        soll = False

        
    if uhh == 2:    
        toll = False
        soll = True



        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:    
                #print ('E')
                while game_loop is True:
                    
                    score12(900,20)

                        
                    if basketballX >= 1500:
                        if balls == 2:
                            balls == 1
                            poop = False
                            cmon = True
                            pulu = False
                            for_the_other_one = True
                    if basketballX2 >= paddleX:
                        if balls == 1:
                            cmon = True
                            pulu = False
                            if gscreen > 0 and gscreen < 101:                                    
                                screen.blit(game_over_screen, (0,0))
                            if gscreen > 100 and gscreen < 201:                                    
                                screen.blit(game2, (0,0))
                            pygame.display.update()
                                        
                                                                
                    if basketballX2 >= 1500:
                        if balls == 2:
                            balls == 1
                            soop = False
                            lulu = False
                            lmon = True
                            for_the_other_one2 = True
                    if for_the_other_one2 is False:
                        if basketballX2 >= paddleX:
                            if balls == 1:
                                lmon = True
                                lulu = False
                                balls == 0
                                if gscreen > 0 and gscreen < 101:                                    
                                    screen.blit(game_over_screen, (0,0))
                                if gscreen > 100 and gscreen < 201:                                    
                                    screen.blit(game2, (0,0))
                                pygame.display.update()                                 


                #detects paddle and ball touch


                    if paddleY < basketballY + 51 and paddleY + 116 >= basketballY + 51:
                        if basketballX + 51 == paddleX:
                            #print('ok')
                            impact.play()
                            score1 += 1
                            false = True
                            lol = True                            
                    if paddleY + 116 < basketballY + 51 and paddleY + 232 >= basketballY + 51:
                        if basketballX + 51 == paddleX:
                            #print('ok')
                            impact.play()
                            score1 += 1
                            false = True
                            
                            


                #detects paddle and ball2 touch

                    if paddleY < basketballY2 + 51 and paddleY + 116 >= basketballY2 + 51:
                        if basketballX2 + 51 == paddleX:
                            #print('ok')
                            score1 += 1
                            impact.play()
                            true = False
                            pol = True                            
                    if paddleY + 116 < basketballY2 + 51 and paddleY + 232 >= basketballY2 + 51:
                        if basketballX2 + 51 == paddleX:
                            #print('yeah!!!')
                            score1 += 1
                            impact.play()
                            true = False
                            
                    if prank is True:
                        prank = False
                    if mang is True:
                        mang = False                        

                    if basketballX < 51:
                        prank = True
                        
                    if basketballX2 < 51:
                        mang = True


                    if prank is True:
                        false = False
                        lol = False
                    if mang is True:
                        true = True
                        pol = False

 
                        
                    if false is True:
                        basketballX -= house_timing
                        if kulja is False:
                            basketballY -= house_timing
                        if kulja is True:
                            basketballY += house_timing                     
                            
                    if true is False:
                        basketballX2 -= house_timing
                        if sim_sim is False:
                            basketballY2 -= house_timing
                        if sim_sim is True:
                            basketballY2 += house_timing


                            

                        
                    if false is False:                        
                        if poop is True:        
                            if soll is True:
                                basketballX += house_timing
                                basketballY += house_timing
                            if soll is False:
                                basketballX += house_timing
                                basketballY -= house_timing
                                
                    if true is True:
                        if soop is True:   
                            if toll is True:
                                basketballX2 += house_timing
                                basketballY2 += house_timing
                            if toll is False:
                                basketballX2 += house_timing
                                basketballY2 -= house_timing


                                

                    if false is True:
                        if basketballY < 51:
                            kulja = True
                        if basketballY > 700:
                            kulja = False
                    if true is False:
                        if basketballY2 < 51:
                            sim_sim = True
                        if basketballY2 > 700:
                            sim_sim = False
                            


                            
                    if cmon and lmon is True:
                        if gscreen > 0 and gscreen < 101:                                    
                            screen.blit(game_over_screen, (0,0))
                        if gscreen > 100 and gscreen < 201:                                    
                            screen.blit(game2, (0,0))


                            
                    if soop or poop is True:
                        screen.blit(background2, (0,0))
                    if soop or poop is True:
                        screen.blit(paddle, (1350,paddleY))
                    if poop or soop is True:
                        screen.blit(basketball, (basketballX,basketballY))
                    if soop or poop is True:
                        screen.blit(basketball2, (basketballX2,basketballY2))

                    



                     
                    paddleY += paddleYC
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_UP:
                                paddleYC = -1.7
                            if event.key == pygame.K_DOWN:
                                paddleYC = 1.7
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
                        bouce.play()
                        basketballY = 51
                        soll = True
                        
                    if basketballY > 700:
                        bouce.play()
                        basketballY = 700
                        soll = False

                        
                    if basketballY2 < 51:
                        bouce.play()
                        basketballY2 = 51
                        toll = True
                        
                    if basketballY2 > 700:
                        bouce.play()
                        basketballY2 = 700
                        toll = False
                        
                     
            if event.key == pygame.K_i:
                #print ('I')
                
                while game_loop is True:

                    house_timing = 1.5

                    score12(900,20)
                                        
                    if basketballX >= 1500:
                        if balls == 2:
                            balls == 1
                            poop = False
                            cmon = True
                            pulu = False
                            for_the_other_one = True
                    if basketballX2 >= paddleX:
                        if balls == 1:
                            cmon = True
                            pulu = False
                            if gscreen > 0 and gscreen < 101:                                    
                                screen.blit(game_over_screen, (0,0))
                            if gscreen > 100 and gscreen < 201:                                    
                                screen.blit(game2, (0,0))
                            pygame.display.update()
                                        
                                                                
                    if basketballX2 >= 1500:
                        if balls == 2:
                            balls == 1
                            soop = False
                            lulu = False
                            lmon = True
                            for_the_other_one2 = True
                    if for_the_other_one2 is False:
                        if basketballX2 >= paddleX:
                            if balls == 1:
                                lmon = True
                                lulu = False
                                balls == 0
                                if gscreen > 0 and gscreen < 101:                                    
                                    screen.blit(game_over_screen, (0,0))
                                if gscreen > 100 and gscreen < 201:                                    
                                    screen.blit(game2, (0,0))
                                pygame.display.update()                                 


                #detects paddle and ball touch


                    if paddleY < basketballY + 51 and paddleY + 116 >= basketballY + 51:
                        if basketballX + 51 == paddleX:
                            #print('ok')
                            impact.play()
                            score1 += 1
                            false = True
                            lol = True                            
                    if paddleY + 116 < basketballY + 51 and paddleY + 232 >= basketballY + 51:
                        if basketballX + 51 == paddleX:
                            #print('ok')
                            score1 += 1
                            impact.play()
                            false = True
                            
                            


                #detects paddle and ball2 touch

                    if paddleY < basketballY2 + 51 and paddleY + 116 >= basketballY2 + 51:
                        if basketballX2 + 51 == paddleX:
                            #print('ok')
                            score1 += 1
                            impact.play()
                            true = False
                            pol = True                            
                    if paddleY + 116 < basketballY2 + 51 and paddleY + 232 >= basketballY2 + 51:
                        if basketballX2 + 51 == paddleX:
                            #print('yeah!!!')
                            score1 += 1
                            impact.play()
                            true = False
                            
                    if prank is True:
                        prank = False
                    if mang is True:
                        mang = False                        

                    if basketballX < 51:
                        prank = True
                        
                    if basketballX2 < 51:
                        mang = True


                    if prank is True:
                        false = False
                        lol = False
                    if mang is True:
                        true = True
                        pol = False

 
                        
                    if false is True:
                        basketballX -= house_timing
                        if kulja is False:
                            basketballY -= house_timing
                        if kulja is True:
                            basketballY += house_timing                     
                            
                    if true is False:
                        basketballX2 -= house_timing
                        if sim_sim is False:
                            basketballY2 -= house_timing
                        if sim_sim is True:
                            basketballY2 += house_timing


                            

                        
                    if false is False:                        
                        if poop is True:        
                            if soll is True:
                                basketballX += house_timing
                                basketballY += house_timing
                            if soll is False:
                                basketballX += house_timing
                                basketballY -= house_timing
                                
                    if true is True:
                        if soop is True:   
                            if toll is True:
                                basketballX2 += house_timing
                                basketballY2 += house_timing
                            if toll is False:
                                basketballX2 += house_timing
                                basketballY2 -= house_timing


                                

                    if false is True:
                        if basketballY < 51:
                            kulja = True
                        if basketballY > 700:
                            kulja = False
                    if true is False:
                        if basketballY2 < 51:
                            sim_sim = True
                        if basketballY2 > 700:
                            sim_sim = False
                            


                            
                    if cmon and lmon is True:
                        if gscreen > 0 and gscreen < 101:                                    
                            screen.blit(game_over_screen, (0,0))
                        if gscreen > 100 and gscreen < 201:                                    
                            screen.blit(game2, (0,0))


                            
                    if soop or poop is True:
                        screen.blit(background2, (0,0))
                    if soop or poop is True:
                        screen.blit(paddle, (1350,paddleY))
                    if poop or soop is True:
                        screen.blit(basketball, (basketballX,basketballY))
                    if soop or poop is True:
                        screen.blit(basketball2, (basketballX2,basketballY2))




                     
                    paddleY += paddleYC
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_UP:
                                paddleYC = -0.5
                            if event.key == pygame.K_DOWN:
                                paddleYC = 0.5
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
                        
                    #ummmmm me doing this in vs code                       

                         
                    if basketballY < 51:
                        bouce.play()
                        basketballY = 51
                        soll = True
                        
                    if basketballY > 700:
                        bouce.play()
                        basketballY = 700
                        soll = False

                        
                    if basketballY2 < 51:
                        bouce.play()
                        basketballY2 = 51
                        toll = True
                        
                    if basketballY2 > 700:
                        bouce.play()
                        basketballY2 = 700
                        toll = False

                        
            if event.key == pygame.K_p:
                print ('P')
                
                while game_loop is True:

                    house_timing = 3

                    score12(900,20)
                                        
                    if basketballX >= 1500:
                        if balls == 2:
                            balls == 1
                            poop = False
                            cmon = True
                            pulu = False
                            for_the_other_one = True
                    if basketballX2 >= paddleX:
                        if balls == 1:
                            cmon = True
                            pulu = False
                            if gscreen > 0 and gscreen < 101:                                                     
                                screen.blit(game_over_screen, (0,0))
                            if gscreen > 100 and gscreen < 201:                                    
                                screen.blit(game2, (0,0))
                            pygame.display.update()
                                        
                                                                
                    if basketballX2 >= 1500:
                        if balls == 2:
                            balls == 1
                            soop = False
                            lulu = False
                            lmon = True
                            for_the_other_one2 = True
                    if for_the_other_one2 is False:
                        if basketballX2 >= paddleX:
                            if balls == 1:
                                lmon = True
                                lulu = False
                                balls == 0
                                if gscreen > 0 and gscreen < 101:                                    
                                    screen.blit(game_over_screen, (0,0))
                                if gscreen > 100 and gscreen < 201:                                    
                                    screen.blit(game2, (0,0))
                                pygame.display.update()                                 


                #detects paddle and ball touch


                    if paddleY < basketballY + 51 and paddleY + 116 >= basketballY + 51:
                        if basketballX + 51 == paddleX:
                            score1 += 1
                            #print('ok')
                            impact.play()
                            false = True
                            lol = True                            
                    if paddleY + 116 < basketballY + 51 and paddleY + 232 >= basketballY + 51:
                        if basketballX + 51 == paddleX:
                            print('ok')
                            score1 += 1
                            impact.play()
                            false = True
                            
                            


                #detects paddle and ball2 touch

                    if paddleY < basketballY2 + 51 and paddleY + 116 >= basketballY2 + 51:
                        if basketballX2 + 51 == paddleX:
                            #print('ok')
                            score1 += 1
                            impact.play()
                            true = False
                            pol = True                            
                    if paddleY + 116 < basketballY2 + 51 and paddleY + 232 >= basketballY2 + 51:
                        if basketballX2 + 51 == paddleX:
                            print('yeah!!!')
                            score1 += 1
                            impact.play()
                            true = False
                            
                    if prank is True:
                        prank = False
                    if mang is True:
                        mang = False                        

                    if basketballX < 51:
                        prank = True
                        
                    if basketballX2 < 51:
                        mang = True


                    if prank is True:
                        false = False
                        lol = False
                    if mang is True:
                        true = True
                        pol = False

 
                        
                    if false is True:
                        basketballX -= house_timing
                        if kulja is False:
                            basketballY -= house_timing
                        if kulja is True:
                            basketballY += house_timing                     
                            
                    if true is False:
                        basketballX2 -= house_timing
                        if sim_sim is False:
                            basketballY2 -= house_timing
                        if sim_sim is True:
                            basketballY2 += house_timing


                            

                        
                    if false is False:                        
                        if poop is True:        
                            if soll is True:
                                basketballX += house_timing
                                basketballY += house_timing
                            if soll is False:
                                basketballX += house_timing
                                basketballY -= house_timing
                                
                    if true is True:
                        if soop is True:   
                            if toll is True:
                                basketballX2 += house_timing
                                basketballY2 += house_timing
                            if toll is False:
                                basketballX2 += house_timing
                                basketballY2 -= house_timing


                                

                    if false is True:
                        if basketballY < 51:
                            kulja = True
                        if basketballY > 700:
                            kulja = False
                    if true is False:
                        if basketballY2 < 51:
                            sim_sim = True
                        if basketballY2 > 700:
                            sim_sim = False
                            


                            
                    if cmon and lmon is True:
                        if gscreen > 0 and gscreen < 101:                                    
                            screen.blit(game_over_screen, (0,0))
                        if gscreen > 100 and gscreen < 201:                                    
                            screen.blit(game2, (0,0))


                            
                    if soop or poop is True:
                        screen.blit(background2, (0,0))
                    if soop or poop is True:
                        screen.blit(paddle, (1350,paddleY))
                    if poop or soop is True:
                        screen.blit(basketball, (basketballX,basketballY))
                    if soop or poop is True:
                        screen.blit(basketball2, (basketballX2,basketballY2))




                     
                    paddleY += paddleYC
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_UP:
                                paddleYC = -1
                            if event.key == pygame.K_DOWN:
                                paddleYC = 1
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
                        bouce.play()
                        basketballY = 51
                        soll = True
                        
                    if basketballY > 700:
                        bouce.play()
                        basketballY = 700
                        soll = False

                        
                    if basketballY2 < 51:
                        bouce.play()
                        basketballY2 = 51
                        toll = True
                        
                    if basketballY2 > 700:
                        bouce.play()
                        basketballY2 = 700
                        toll = False




                        
    #pygame.draw.rect(screen,grey,(945,45,390,477))
    sr()
    ss()
    #screen.blit(pic, (950 ,50)) 
    sl()
    screen.blit(easy_button, (200,600))
    screen.blit(intermediate_button, (660,600))
    screen.blit(proffesional_button, (1220,600))
    
        
    


