import pygame
from settings import Settings
from ship import Ship
# from alien import Alien
import game_functions as gf
from pygame.sprite import Group


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
    ship = Ship(alien_invasion_settings, screen)
    # Now we've added the speed factor to the ship, and
    # can change the rhythm of the game as the player
    # evolves in it.

    # Creating the object alienship
    # alien = Alien(alien_invasion_settings, screen)

    # Create the group for the bullets to be stored
    bullets = Group()
    # Create the group for the aliens to be stored
    aliens = Group()
    # Create the alien fleet
    gf.create_fleet(alien_invasion_settings, screen, ship, aliens)
    # This will create the main loop of the game
    while True:
        gf.check_events(alien_invasion_settings, screen, ship, bullets)
        # This has check all the events that occurs with the mouse
        # and the keyboard.
        ship.update()
        # Here we'll make the ship position be updated
        # every time we check the events from the ship, inside
        # the while loop.
        bullets.update()
        # Here we'll make sure every bullet is updated.
        # Whenever the code passes through this part, the
        # bullets trajectory we'll be updated on the screen
        # by the update() method from the module sprite, from
        # pygame.
        gf.update_bullets(bullets)
        gf.update_screen(alien_invasion_settings, screen, ship,
                         aliens, bullets)
        # Here we use the method update_screen from game_functions
        # to update the screen, define the background color and
        # draw the ship.


run_game()
