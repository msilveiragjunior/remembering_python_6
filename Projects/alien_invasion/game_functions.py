import sys
# The module sys imports functions and methods pertaining to
# the system, allowing interaction from the system with the
# python interpreter
import pygame


def check_events():
    for event in pygame.event.get():
        # Here we'll watch all the events from the keyboard
        # and mouse, like button activations
        if event.type == pygame.QUIT:
            sys.exit()
            # This will exit the game if the event type
            # is equal to the method .QUIT from pygame


def update_screen(alien_invasion_settings, screen, ship):
    # This will update the screen to the color that we choose
    screen.fill(alien_invasion_settings.bg_color)
    # Every time the screen updates, it will execute the code
    # above, updating the screen color to the contained rgb
    # 3-tuple contained inside bg_color
    ship.blitme()
    # The blitme method is inside the class Ship, that is inside
    # the object ship that we've instantiated. This
    # will draw the ship over the background.
    pygame.display.flip()
    # The method .flip() from display module is
    # responsible for updating the screen of the game
    # So it will show the newly rendered frame of the game
    # This will constantly update the game screen
