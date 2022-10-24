# All enemy classes will go here.
import pygame
import math

class Enemy(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.movex = 0 # move along X
        self.direction = "RIGHT"
        self.movey = 0 # move along Y
        img = pygame.image.load('Broman.png').convert_alpha()
        self.images.append(img)
        self.image = self.images[0]
        #self.surf = pygame.image.load('assets\FireWizard.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.hitbox = (self.rect.x, self.rect.y, 50, 100)
        self.height = 50
        self.width = 25

    def update(self, house, score):
        dx,dy = house.rect.x+100 - self.rect.x, house.rect.y+100 - self.rect.y
        dist = math.hypot(dx,dy)
        if (dist == 0):
            self.kill()
            house.take_damage(10)
            #score-=10
            del(self.hitbox)
        else:
            dx,dy = dx/dist,dy/dist
            self.rect.x+=dx*5
            self.rect.y+=dy*5
            self.hitbox = (self.rect.x, self.rect.y, 50, 100)


