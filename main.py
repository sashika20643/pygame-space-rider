import pygame
import math
import random
from pygame import mixer

# initialize the pygame
pygame.init()
# create screen
screen = pygame.display.set_mode((800, 600))
# title and icon
pygame.display.set_caption("Space figter")
icon = pygame.image.load('startup(1).png')
pygame.display.set_icon(icon)

# player
playerImg = pygame.image.load('space-invaders(1).png')
playerx = 370
playery = 480
pincrease = 0

# enemy
enemyImg = []
enemyx = []
enemyy = []
eXChanage = []
eYChanage = []
num_of_enemies = 6
for i in range(num_of_enemies):

    enemyImg.append(pygame.image.load('alien.png'))
    enemyx.append(random.randint(0, 736))
    enemyy.append(random.randint(50, 150))
    if (i % 2 == 0):
        eXChanage.append(1)
    else:
        eXChanage.append(-1)
    eYChanage.append(30)
# background
background = pygame.image.load('Artboard 1.png')
mixer.music.load("background.wav")
mixer.music.play(-1)
# bullet
bulletImg = pygame.image.load('bullet.png')
bulletx = playerx + 32
bullety = 480
bXChanage = 0
bYChanage = 0
bullet_state = "ready"


def player(x, y):
    # blid mean draw
    screen.blit(playerImg, (x, y))
    # bullet draw


def bullet(x, y):
    # blid mean draw
    global bullet_state
    screen.blit(bulletImg, (x + 16, y + 10))
    bullet_state = "fire"
    # enemy draw function


def enemy(x, y, i):
    # blid mean draw
    screen.blit(enemyImg[i], (x[i], y[i]))


def isCollison(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + math.pow(enemyY - bulletY, 2))
    if distance < 27:
        return True
    else:
        return False


# GAME LOOP
score_val = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textx = 10
texty = 10

running = True


def show_score(x, y):
    score = font.render("Score :" + str(score_val), True, (255, 255, 255))
    screen.blit(score, (x, y))
def game_over_text():
    over_text = font.render("GAME OVER" , True,(255, 255, 255))
    screen.blit(over_text, (200, 250))

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if (bullet_state == "ready"):
                    bullet_sound=mixer.Sound("laser.wav")
                    bullet_sound.play()
                    bullet(playerx, bullety)

                    bYChanage = 2
                    bulletx = playerx

            if event.key == pygame.K_LEFT:
                pincrease = -4

            if event.key == pygame.K_RIGHT:
                pincrease = 4

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                pincrease = 0

        # change display color(RGB)
    screen.fill((130, 50, 70))
    screen.blit(background, (0, 0))
    playerx += pincrease
    if playerx <= 0:
        playerx = 0
    elif playerx >= 736:
        playerx = 736
    for i in range(num_of_enemies):
        #game over
        if enemyy[i]>450:
            for j in range(num_of_enemies):
                enemyy[j]=2000
            game_over_text()
        if enemyx[i] <= 0:
            eXChanage[i] *= -1
            enemyy[i] += 45
        if enemyx[i] >= 736:
            eXChanage[i] *= -1
            enemyy[i] += 45
        enemyx[i] += eXChanage[i]
        enemy(enemyx, enemyy, i)
        collision = isCollison(enemyx[i], enemyy[i], bulletx, bullety)

        if collision:
            collision_sound=mixer.Sound("explosion.wav")
            collision_sound.play()
            bullety = 480
            bullet_state = "ready"
            score_val += 1
            enemyx[i] = random.randint(0, 736)
            enemyy[i] = random.randint(50, 150)

    if bullet_state == "fire":
        bullet(bulletx, bullety)
        bullety -= 4
    if bullety < 0:
        bullet_state = "ready"
        bullety = 480
    # check collison


    player(playerx, playery)
    show_score(textx, texty)

    # bullet movement

    pygame.display.update()
