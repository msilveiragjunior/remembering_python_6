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

        # Here we'll make an attribute that will
        # alter the spaceship speed factor
        self.ship_speed_factor = 1.5
        # Projectile information
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_length = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 4
