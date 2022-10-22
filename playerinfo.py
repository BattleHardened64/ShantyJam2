# The player class will go here.
from symbol import subscript
import pygame


class Player(pygame.sprite.Sprite):
    #Spawn a Player

    def __init__(self) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.movex = 0 # move along X
        self.movey = 0 # move along Y
        img = pygame.image.load('FireWizard.png').convert_alpha()
        self.images.append(img)
        self.image - self.images[0]
        #self.surf = pygame.image.load('FireWizard.png').convert_alpha()
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey
        #If I have time, I will make it change directions with multiple frames.
        """
          # moving left
        if self.movex < 0:
            self.frame += 1
            if self.frame > 3*ani:
                self.frame = 0
            self.image = pygame.transform.flip(self.images[self.frame // ani], True, False)

        # moving right
        if self.movex > 0:
            self.frame += 1
            if self.frame > 3*ani:
                self.frame = 0
            self.image = self.images[self.frame//ani]""" 

    def control(self,x,y):
        self.movex += x
        self.movey += y
        