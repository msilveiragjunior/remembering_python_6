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

        # Ship limit
        self.ship_limit = 4

        # Projectile information
        self.bullet_width = 5
        self.bullet_length = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 10
        # Speed of the drop
        self.fleet_drop_speed = 1

        # The rate of the game speed
        self.speedup_scale = 1.1

        # This will call the function initialize_dynamic_settings().
        # It'll make possible for the game to change difficulty.
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        # Changes the settings as the game grow in difficulty
        # Here we'll make an attribute that will
        # alter the spaceship speed factor
        self.ship_speed_factor = 12
        self.bullet_speed_factor = 5
        # Speed of the alien
        self.alien_speed_factor = 4
        # Fleet = 1 goes to right; -1 goes to left
        self.fleet_direction = 1
        # Points to sum to the score
        self.alien_points = 50

    def increase_speed(self):
        # This method will be used to multiply the dynamic
        # attributes, from this class, by the speedup_scale.
        # So when the player reaches a new level, the dynamic
        # attributes will increase.
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
