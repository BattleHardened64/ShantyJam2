# The player class will go here.
from fireballinfo import fireball
import pygame


class Player(pygame.sprite.Sprite):
    #Spawn a Player

    def __init__(self) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.movex = 0 # move along X
        self.direction = "RIGHT"
        self.movey = 0 # move along Y
        img = pygame.image.load('assets\FireWizard.png').convert_alpha()
        self.images.append(img)
        self.image = self.images[0]
        #self.surf = pygame.image.load('assets\FireWizard.png').convert_alpha()
        self.rect = self.image.get_rect()

    def updatex(self):
        if (self.movex < 0 and self.direction == "RIGHT"):
            self.direction = "LEFT"
            self.image = pygame.transform.flip(self.image, True, False)
        elif (self.movex > 0 and self.direction == "LEFT"):
            self.direction = "RIGHT"
            self.image = pygame.transform.flip(self.image, True, False)
        self.rect.x = self.rect.x + self.movex

    def updatey(self):
        self.rect.y = self.rect.y + self.movey

    def createfireball(self):
        return fireball(self.rect.x+50,self.rect.y+25)


