import sys
# The module sys imports functions and methods pertaining to
# the system, allowing interaction from the system with the
# python interpreter
import pygame


def check_events(ship):
    for event in pygame.event.get():
        # Here we'll watch all the events from the keyboard
        # and mouse, like button activations
        if event.type == pygame.QUIT:
            sys.exit()
            # This will exit the game if the event type
            # is equal to the method .QUIT from pygame
        # Here We update the check_events() function
        # to check key presses from the player. In this specific
        # case, we check if the player is pressing the right arrow key.
        # Every pressing event is registered as a KEYDOWN event.
        # When a KEYDOWN event is detected, we will verify, with
        # the constant K_RIGHT.
        if event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        # By doing this, we'll check the functions of
        # the events that are now separated, making
        # the file cleaner.


def check_keydown_events(event, ship):
    if event.key == pygame.K_RIGHT:
        # If the attribute defined before in the for
        # loop - i.e. event - .key is equal to the constant K_RIGHT,
        # then we move the ship to the right, incrementing the
        # centerx with a value of + 1.
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
        # Here we almost repeat the code to move to the right,
        # but we use the constant K_LEFT to check if the arrow
        # pressed is the left arrow.


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
        # Here we define the constant event KEYUP
        # together with the flag moving_right, so
        # we can implement the continuous movement.
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
        # Here we almost the repeat the code to
        # check if the keypress has stopped, but,
        # this time, we'll check if the keypress of the
        # left arrow has stopped.


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
