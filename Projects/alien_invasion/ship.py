import pygame


class Ship():

    def __init__(self, screen):
        # It will initialize the initial position
        # of the ship
        self.screen = screen

        # Load the image of the spaceship
        self.image = pygame.image.load('images/ship.png')
        # To load the image of the spaceship we use
        # the function pygame.image.load(). This
        # will return a surface that represents the spaceship
        # and is stored in the self.image variable.
        self.rect = self.image.get_rect()
        # Then we access the attribute rect from the image.
        # This attribute - i.e. rect - is a abbreviation of the
        # word rectangle. Pygame treats elements from the game
        # as rectangles. When we work with rectangles, we can
        # define the superior and inferior, left and right
        # borders of the rectangle, as well as the center of it.
        # By doing this, we can determine the actual position of
        # the rectangle.
        self.screen_rect = screen.get_rect()
        # Here we are storing the rectangle of the screen.
        # Initialize a new spaceship on the central bottom
        # part of the screen
        self.rect.centerx = self.screen_rect.centerx
        # And here we are making the value of the rectangle coincide
        # with the value of the centerx value of the screen.
        self.rect.bottom = self.screen_rect.bottom
        # Here we make the rect.bottom attribute coincide with
        # the value of the bottom value of the rect of the screen.
        # By doing this, we'll make the spaceship appear centralized
        # on the screen.
        # PS: The origin x,y (0,0) of the screen, on pygame, is
        # on the left superior part of the screen, and the final
        # value defined is on the right bottom part of the screen:
        # (1200, 800)
        # So it's like we are making a 2x2 grid of a x,y grid that
        # goes clockwise and not counter clockwise.
        # When we work with pygame, we'll work with
        # the attributes center, centerx or centery from
        # a rectangle. When we work with the border of the screen,
        # we'll use the attributes top, bottom, left or right.

    def blitme(self):
        # This will draw the spaceship in its actual position
        self.screen.blot(self.image, self.rect)
