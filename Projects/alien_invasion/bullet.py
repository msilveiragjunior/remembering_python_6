import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, alien_invasion_settings, screen, ship):
        super(Bullet, self).__init__()
        self.screen = screen
        # Defines the position to the projectile rectangle
        self.rect = pygame.Rect(0, 0, alien_invasion_settings.bullet_width,
                                alien_invasion_settings.bullet_length)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        # We need the projectile to be centered and to show up
        # from the top of the ship border.
        # So we define its value from the ship settings

        # Stores the projectile position with a float value
        self.y = float(self.rect.y)
        self.color = alien_invasion_settings.bullet_color
        self.speed_factor = alien_invasion_settings.bullet_speed_factor

    # We need to add two methods to this class:
    # One that updates its projectile position
    # value, and one that draws the projectile
    # on the screen.

    def update(self):
        self.y -= self.speed_factor
        self.rect.y = self.y

    # This method will draw the projectile on the screen

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        # The rect method from the draw module needs a surface
        # parameter to draw the rect - i.e self.screen -, a
        # parameter with a 3-tuple to paint it and a parameter
        # with rectangle to draw, position and dimensions.
