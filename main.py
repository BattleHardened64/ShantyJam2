#This is the main file where the Game Loop will be located.
from playerinfo import Player
#from enemyinfo import Enemy
from houseinfo import House
import pygame
import sys


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

window = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()
"""
ADDPOINTS = pygame.USEREVENT + 10

pygame.time.set_timer(ADDPOINTS, )
"""
#enemy sprite

#house sprite

#STATISTICS
score = 0 
health = 3 #Max of 5

# Function for when the game is over, user can see their score and decide before pressing
def gameOverScreen():
    window.fill(Black)
    lmsg = sfont.render("Final Score: " + str(score), True, White)
    omsg = sfont.render("R = Reset or Q = Quit", True, White)
    window.blit(lmsg, (WIDTH/2.5, HEIGHT/2.5))
    window.blit(omsg, (WIDTH/2.5 - 200 * 1.25, HEIGHT/2.5 + 200))
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

def main():
    speed = 25  #pixels per second?
    
    #Create our player
    player = Player()
    player.rect.x = 0  # go to x
    player.rect.y = 0  # go to y
    player_list = pygame.sprite.Group()
    player_list.add(player)

    #Create our house
    house = House()
    house_list = pygame.sprite.Group()
    house_list.add(house)

    #Create Fireball group
    fireball_group = pygame.sprite.Group()
    run = True
    #MAIN GAME LOOP
    while run:
        pygame.time.delay(10)
        window.fill((100, 170, 164))
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


        house_list.update()
        house_list.draw(window)
        pygame.draw.rect(window, (255, 0, 0), house.hitbox, 2)
        player_list.draw(window)
        pygame.draw.rect(window, (255, 0, 0), player.hitbox, 2)
        fireball_group.draw(window)

        for fireball in fireball_group:
            if fireball.rect.y - fireball.radius < house.hitbox[1] + house.hitbox[3] and fireball.rect.y + fireball.radius > house.hitbox[1]:
                if fireball.rect.x + fireball.radius > house.hitbox[0] and fireball.rect.x - fireball.radius < house.hitbox[0] + house.hitbox[2]:
                    house.take_damage(10)
                    print("I HAVE BEEN HIT AND I CANT GET UP")
                    fireball.kill()
                    if (house.isDead == True):
                        gameOverScreen()

        fireball_group.update()
        pygame.display.flip()
        clock.tick(30)

main()





