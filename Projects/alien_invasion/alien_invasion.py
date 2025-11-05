import sys
import pygame


def run_game():
    # Initializes the game
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    # Display.set_mode() represents all the game
    # screen, and it will be used to define the size
    # of the game screen. It accepts a tuple with two
    # arguments: x and y
    pygame.display.set_caption("Alien Invasion")
    # This will set the caption on the upper bar
    # to Alien Invasion

    # This will define the background color in using rgb
    bg_color = (230, 230, 230)

    # This will create the main loop of the game
    while True:
        for event in pygame.event.get():
            # Here we'll watch all the events from the keyboard
            # and mouse, like button activations
            if event.type == pygame.QUIT:
                sys.exit()
                # This will exit the game if the event type
                # is equal to the method .QUIT from pygame

        # This will update the screen to the color that we choose
        screen.fill(bg_color)
        # Every time the screen updates, it will execute these codes

        pygame.display.flip()
        # The method .flip() from display module is
        # responsible for updating the screen of the game
        # So it will show the newly rendered frame of the game
        # This will constantly update the game screen


run_game()
