#This is where the fireball class will be located
from xmlrpc.client import Boolean
import pygame


class fireball(pygame.sprite.Sprite):

    def __init__(self, x, y,facing) -> None:
        super().__init__()
        self.images = []
        img = pygame.image.load('assets\Fireball.png').convert_alpha()
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect(center = (x,y))
        self.radius = 12.5
        self.facing : Boolean
        self.facing = facing
        self.speed = 20
        fireball.hitbox = (self.rect.x, self.rect.y, 25, 25)
    
    def update(self):
        if self.facing == True:
            self.rect.x += self.speed
            self.hitbox = (self.rect.x, self.rect.y, 25, 25)
            if self.rect.x >= 1500:
                self.kill()

        elif self.facing == False:
            self.rect.x += self.speed * (-1)
            self.hitbox = (self.rect.x, self.rect.y, 25, 25)
            if self.rect.x <= -1500:
                self.kill()





    




