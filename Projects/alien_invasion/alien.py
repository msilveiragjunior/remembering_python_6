import pygame
from pygame.sprite import Sprite


class Alien(Sprite):

    def __init__(self, alien_invasion_settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.alien_invasion_settings = alien_invasion_settings
        # Here we'll load the image of the alien ship
        self.image = pygame.image.load('images/alienship.png')
        self.rect = self.image.get_rect()
        # Defining the alien position on the superior left side
        # of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.alien_height = self.rect.y
        # Storing the position of the alien
        self.x = float(self.rect.x)

    # Here we'll draw the image of the alien spaceship
    def blitme(self):
        self.screen.blit(self.image, self.rect)
    # Everything here is very similar to the ship class file
