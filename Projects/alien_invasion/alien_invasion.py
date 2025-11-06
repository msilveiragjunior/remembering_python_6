import pygame
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    # Initializes the game
    pygame.init()
    alien_invasion_settings = Settings()
    screen = pygame.display.set_mode((alien_invasion_settings.screen_width,
                                     alien_invasion_settings.screen_length))
    # Display.set_mode() represents all the game
    # screen, and it will be used to define the size
    # of the game screen. It accepts a tuple with two
    # arguments: x and y
    pygame.display.set_caption("Alien Invasion")
    # This will set the caption on the upper bar
    # to Alien Invasion

    # Creating the object ship
    ship = Ship(screen)

    # This will create the main loop of the game
    while True:
        gf.check_events()
        # This has check all the events that occurs with the mouse
        # and the keyboard.
        gf.update_screen(alien_invasion_settings, screen, ship)
        # Here we use the method update_screen from game_functions
        # to update the screen, define the background color and
        # draw the ship.


run_game()
