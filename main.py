#This is the main file where the Game Loop will be located.
from playerinfo import Player
#from enemyinfo import Enemy
#from houseinfo import House
import pygame
import sys


#window size in pixels
WIDTH = 800
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
speed = 5  #pixels per second?



#Create our player
player = Player()


#MAIN GAME LOOP
while run:
    pygame.time.delay(10)
    window.fill((255, 170, 164))
    keys = pygame.key.get_pressed()
    #Press X to quit!
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == ord('x'):
                pygame.quit()
            try:
                sys.exit()
            finally:
                main = False

    if keys[pygame.K_w]:
        player.control(0,speed)
    if keys[pygame.K_a]:
        player.control(speed, 0)
    if keys[pygame.K_s]:
        player.control(0,-speed)
    if keys[pygame.K_d]:
        player.control(-speed, 0)

    pygame.display.update()
    clock.tick(30)







