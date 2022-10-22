# The player class will go here.
import pygame


class Player(pygame.sprite.Sprite):
    #Spawn a Player

    def __init__(self) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        img = pygame.image.load('FireWizard.png')
        self.images.append(img)
        

