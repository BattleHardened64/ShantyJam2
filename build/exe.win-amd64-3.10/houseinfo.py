# The house class will go here.
import pygame 

# The house class will go here.
class House(pygame.sprite.Sprite):
    def __init__(self)->None:
        pygame.sprite.Sprite.__init__(self)
        self.x = 750
        self.y = 400
        self.image = pygame.image.load('HouseAsset.png').convert_alpha()
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.hitbox = (self.x - 120, self.y - 110, 220, 240)
        self.health = 100
        self.isDead = False
        #self.health : int

    def take_damage(self, d):
        self.health -= d
        if (self.health <= 0):
            self.kill()
            self.isDead = True
    def heal_damage(self, h):
        self.health += h
    

#houseTest = House()