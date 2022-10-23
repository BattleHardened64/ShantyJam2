#This is the main file where the Game Loop will be located.
from playerinfo import Player
#from enemyinfo import Enemy
#from houseinfo import House
import pygame
import sys


#window size in pixels
WIDTH = 1000
HEIGHT = 800

#Enemy Spawn Rate
enemy_interval = 10


#Maximum number of enemies on the screen at once
enemy_count = 50

pygame.init()

window = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()
"""
ADDPOINTS = pygame.USEREVENT + 10

pygame.time.set_timer(ADDPOINTS, )
"""
run = True
#enemy sprite

#house sprite

#STATISTICS
score = 0 
health = 3 #Max of 5
speed = 25  #pixels per second?



#Create our player
player = Player()
player.rect.x = 0  # go to x
player.rect.y = 0  # go to y
player_list = pygame.sprite.Group()
player_list.add(player)

#Create Fireball group
fireball_group = pygame.sprite.Group()




#MAIN GAME LOOP
while run:
    pygame.time.delay(10)
    window.fill((100, 170, 164))
    
    #Press X to quit!
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            try:
                sys.exit()
            finally:
                run = False
        if event.type == pygame.KEYDOWN:
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


    pygame.display.update()
    player_list.draw(window)
    fireball_group.draw(window)
    fireball_group.update()
    pygame.display.flip()
    clock.tick()





