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
        self.rect.x = float(self.rect.width)
        self.rect.y = float(self.rect.height)
        self.alien_height = self.rect.y
        # Storing the position of the alien
        self.x = float(self.rect.x)

    # Here we'll draw the image of the alien spaceship
    def blitme(self):
        self.screen.blit(self.image, self.rect)
    # Everything here is very similar to the ship class file

    def check_edges(self):
        # Returns true if the alien is on the edge of the screen
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            # This will check if the alien sprite rect
            # is higher or equal to the edge of the screen
            # By doing this, we can check if it's on the edge
            # of the screen
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        # Here we are making the alien move to the right
        # So we'll sum the speed factor from the alien
        self.rect.x += (self.alien_invasion_settings.alien_speed_factor *
                        self.alien_invasion_settings.fleet_direction)
        # By doing this, we'll update the position of the alien - rect -,
        # since the rect.x can store float - i.e. decimal values - to it.
