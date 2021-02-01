import pygame
from pygame import mixer
import math

pygame.init()

game_loop = True

screen = pygame.display.set_mode((1500, 800))

grey = (170,170,170)

icon = pygame.image.load('bouncy.png')
pygame.display.set_icon(icon)

pygame.display.set_caption(":Bouncing-Ball!:")

background1 = pygame.image.load("background1.jpg")

pic = pygame.image.load("pic .png")

easy_button = pygame.image.load("easy button.png")

intermediate_button = pygame.image.load("intermediate button.png")

proffesional_button = pygame.image.load("proffesional button.png")

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
    screen.blit(intermediate_button, (660,600))
    screen.blit(proffesional_button, (1220,600))
    pygame.display.update()
    for event in pygame.event.get():
         if event.type == pygame.quit:
            quit()
    


