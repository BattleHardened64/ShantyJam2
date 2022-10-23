#This is where the fireball class will be located
import pygame


class fireball(pygame.sprite.Sprite):

    def __init__(self, x, y) -> None:
        super().__init__()
        self.images = []
        img = pygame.image.load('assets\Fireball.png').convert_alpha()
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect(center = (x,y))
        self.radius = 12.5
    
    def update(self):
        self.rect.x +=5

        if self.rect.x >= 1500:
            self.kill()




    




