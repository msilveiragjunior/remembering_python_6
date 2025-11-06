class Settings():
    # Lets initialize this class with the bg_color
    # configuration first

    def __init__(self):
        self.screen_width = 1200
        self.screen_length = 800
        self.bg_color = (230, 230, 230)
        # Here we've created the settings that
        # were inside the program, making a class
        # to hold all the information needed, and
        # making the main program cleaner.

        # Here we need to create a flag to make
        # possible for the game_functions detect
        # when we need to stop the ship
        self.moving_right = False

    def update(self):
        # Here we update the position of the spaceship
        # accordingly to the flag movement.
        if self.moving_right:
            self.rect.centerx += 1
