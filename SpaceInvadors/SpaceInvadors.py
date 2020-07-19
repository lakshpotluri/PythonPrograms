import pygame
import random
import math
from pygame import mixer

#initialize the pygame
pygame.init()
clock = pygame.time.Clock()

#create the screen
screen = pygame.display.set_mode((800, 600))

#Title and Icon
pygame.display.set_caption("Space Invadors")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)
background = pygame.image.load('background.jpg')
mixer.music.load('AmadeusLegendary.mp3')
#mixer.music.load('background.wav')
mixer.music.play(-1)
#Player
playerImg = pygame.image.load('space-invaders.png') 
playerX = 370
playerY = 480
playerX_change = 0
#Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('90.png')) 
    enemyX.append(random.randint(0,736))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(1.5)
    enemyY_change.append(60)

#bullet
bulletImg = pygame.image.load('bullet.png') 
bulletX = 0
bulletY = 480
bulletX_change = 1.5
bulletY_change = 10
bullet_state = "ready"

score1 = 0
font = pygame.font.Font('Restu Bundah.otf',92)
textX = 10
textY = 10




font2 = pygame.font.Font('Restu Bundah.otf',92)
ycs = pygame.font.Font('Restu Bundah.otf',50)
maxs = 0

game_over_text = pygame.font.Font('Restu Bundah.otf',300)
textX = 10
textY = 10
5
time = 0
super_bullet = 1
super_bullet = False

ttd = 'SUPER-BULLET available'
def st():
    ycr = ycs.render(ttd,True,(255,255,255 ))
    screen.blit(ycr,(300,20))

def ss(x,y):
    score = font.render("score :" + str(score1),True,(234,25,25 ))
    screen.blit(score,(x,y))
def got():
    game_over_text = font.render("GAME OVER",True,(234,25,25 ))
    screen.blit(game_over_text,(140,250))    
def player(x,y):
    screen.blit(playerImg,(x,y))
    
def enemy(x,y,i):
    screen.blit(enemyImg[i],(x,y))
    
def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x+16,y+10))

def collisions(enemyX,enemyY,bulletX,bulletY):
    distance = math.sqrt((math.pow(enemyX-bulletX,2)) + (math.pow(enemyY-bulletY,2)))
    if distance < 27:
        return True
    else:
        return False
    

#game loop
running = True
while running:
    
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -3
            if event.key == pygame.K_RIGHT:
                playerX_change = 3
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bullets = mixer.Sound('laser.wav')
                    bullets.play()
                    bulletX = playerX
                    fire_bullet(bulletX,bulletY)
                    bullet_state = "fire"
                    time += 1
            if super_bullet is True:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        for i in range (num_of_enemies):
                            if maxs < enemyY[i]:
                                maxs = enemyY[i]
                                maxind = i
                        enemyX[maxind] = random.randint(0,736)
                        enemyY[maxind] = random.randint(50,150)
                        super_bullet = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                playerX_change = 0
                
    
    player(playerX, playerY)

    #super bullet
    if time is 20:
        print ("You can now shoot a Super-Bullet.")
        super_bullet = True
        time = 0

    if super_bullet is True:
        st()

    #checking for boundaries
    playerX += playerX_change            
    if playerX <= 0:
        playerX = 1
    elif playerX >736:
        playerX = 736
        
    #enemy movement
    for i in range(num_of_enemies):
        if enemyY[i] > 440:
            for l in range(num_of_enemies):
                enemyY[l] = 2000
            got()
            break
        
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 3
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -3
            enemyY[i] += enemyY_change[i]
        collision = collisions(enemyX[i],enemyY[i],bulletX,bulletY)
        if collision:
            ex = mixer.Sound('explosion.wav')
            mixer.music.set_volume(100)
            ex.play()
            mixer.music.set_volume(1)
            bulletY = 480
            bullet_state = "ready"
            score1 += 1
            
            enemyX[i] = random.randint(0,736)
            enemyY[i] = random.randint(50,150)
        enemy(enemyX[i], enemyY[i],i)
        
    #bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state is "fire":
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_change
    ss(textX,textY)

    pygame.display.update()
