#This is the main file where the Game Loop will be located.
from playerinfo import Player
from enemyinfo import Enemy
from houseinfo import House
import pygame
import sys
import random
from pygame import mixer

#window size in pixels
WIDTH = 1500
HEIGHT = 800

# Color Presets
Black = (0, 0, 0)
White = (255, 255, 255)
Orange = (255, 166, 49)

#Enemy Spawn Rate
enemy_interval = 10



#Maximum number of enemies on the screen at once
enemy_count = 50

pygame.init()

sfont = pygame.font.SysFont("Contrail One", 22)

pfont = pygame.font.SysFont("Contrail One", 115)

window = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()
"""
ADDPOINTS = pygame.USEREVENT + 10

pygame.time.set_timer(ADDPOINTS, )
"""
#house sprite

#STATISTICS
score = 0 
health = 3 #Max of 5

# Function for when the game is over, user can see their score and decide before pressing
def gameOverScreen(score):
    window.fill(Black)
    lmsg = sfont.render("Final Score: " + str(score), True, White)
    omsg = sfont.render("R = Reset or Q = Quit", True, White)
    window.blit(lmsg, (WIDTH//2 - 25, HEIGHT//2))
    window.blit(omsg, (WIDTH//3 + 200, HEIGHT//3 + 200))
    pygame.display.flip()

    # To wait for the action of the user at this losing screen
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    main()
                elif event.key == pygame.K_q:
                    pygame.quit()

def create_enemy() -> Enemy:
    enemy = Enemy()
    enemy.rect.x = random.randrange(0, 1500)
    if enemy.rect.x > 500 and enemy.rect.x < 1000:
        enemy.rect.x += 500
    enemy.rect.y = random.randrange(0, 1000)
    if enemy.rect.x > 1000:
        enemy.image = pygame.transform.flip(enemy.image, True, False)
    return enemy

# Displays the score
def displayScore(score):
    sVal = sfont.render("Score: " + str(score) + (" " * 20), True, White)
    window.blit(sVal, [0, 0])

def startScreen():
    bg_img = pygame.image.load('StartScreen.png')
    bg_img = pygame.transform.scale(bg_img,(WIDTH,HEIGHT))

    running = True
    while running:
        window.blit(bg_img,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                try:
                    sys.exit()
                finally:
                    running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = False
        pygame.display.update()


def pause():
    run2 = True
    while(run2 == True):
        pmsg = pfont.render("PAUSED", True, White)
        textRect = pmsg.get_rect()
        textRect.center = (750, 400)
        window.blit(pmsg, textRect)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                try:
                    sys.exit()
                finally:
                    run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    run2 = False
                    return

def main():

    startScreen()

    #enemy sprite
    SPAWNENEMY = pygame.USEREVENT
    enemy_interval = 1500
    pygame.time.set_timer(SPAWNENEMY, enemy_interval)
    speed = 50  #pixels per second?
    score = 0
    displayScore(score)
    
    #Create our player
    player = Player()
    player.rect.x = 730  # go to x
    player.rect.y = 500  # go to y
    player_list = pygame.sprite.Group()
    player_list.add(player)

    #Create our house
    house = House()
    house_list = pygame.sprite.Group()
    house_list.add(house)

    #Create Fireball group
    fireball_group = pygame.sprite.Group()
    #Create Enemy
    enemy_group = pygame.sprite.Group()

    run = True
    #MAIN GAME LOOP
    while run:
        pygame.time.delay(10)
        bg_img = pygame.image.load('Background.png')
        bg_img = pygame.transform.scale(bg_img,(WIDTH,HEIGHT))
        window.blit(bg_img,(0,0))

        smsg = sfont.render("Score: " + str(score), True, White)
        hmsg = sfont.render("House HP: " + str(house.health), True, White)
        window.blit(smsg, (0, 0))
        window.blit(hmsg, (100, 0))

        pygame.display.update()


        
        #Press X to quit!
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                try:
                    sys.exit()
                finally:
                    run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pause()
                
                if event.key == pygame.K_w:
                    player.movey = -speed
                    player.updatey()

                if event.key == pygame.K_a:
                    player.movex = -speed
                    player.updatex()

                if event.key == pygame.K_s:
                    player.movey = speed
                    player.updatey()

                if event.key == pygame.K_d:
                    player.movex = speed
                    player.updatex()

            if event.type == pygame.MOUSEBUTTONDOWN:
                fireball_group.add(player.createfireball())
            if event.type == SPAWNENEMY:
                enemy = create_enemy()
                enemy_group.add(enemy)
                del(enemy)


        house_list.update()
        house_list.draw(window)
        pygame.draw.rect(window, (0,255,0), pygame.Rect(650, 250, 200, 20))
        i=100
        j=0
        while i > house.health:
            i-=10
            j+=1
        pygame.draw.rect(window, (255,0,0), pygame.Rect((850-j*20), 250,j*20, 20))
        player_list.draw(window)
        enemy_group.draw(window)
        fireball_group.draw(window)

        for fireball in fireball_group:
            for enemy in enemy_group:
                if fireball.rect.y - fireball.radius < enemy.hitbox[1] + enemy.hitbox[3] and fireball.rect.y + fireball.radius > enemy.hitbox[1]:
                    if fireball.rect.x + fireball.radius > enemy.hitbox[0] and fireball.rect.x - fireball.radius < enemy.hitbox[0] + enemy.hitbox[2]:
                        fireball.kill()
                        enemy.kill()
                        score+=10
                        if score%100 == 0: 
                            enemy_interval -= 100
                            print(enemy_interval)
                            pygame.time.set_timer(SPAWNENEMY, enemy_interval)
        for enemy in enemy_group:
            if enemy.rect.y - enemy.height < house.hitbox[1] + house.hitbox[3] and enemy.rect.y + enemy.height > house.hitbox[1]:
                if enemy.rect.x + enemy.width > house.hitbox[0] and enemy.rect.x - enemy.width < house.hitbox[0] + house.hitbox[2]:
                    house.take_damage(10)
                    enemy.kill()
                    
        for enemy in enemy_group:
            enemy.update(house, score)
            #pygame.draw.rect(window, (255, 0, 0), enemy.hitbox, 2)
            if (house.isDead == True):
                gameOverScreen(score)


        #pygame.draw.rect(window, (255, 0, 0), house.hitbox, 2)
        fireball_group.update()
        pygame.display.flip()
        clock.tick(30)

main()


