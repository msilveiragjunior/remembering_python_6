class GameStats():

    def __init__(self, alien_invasion_settings):
        self.alien_invasion_settings = alien_invasion_settings
        # Initialize the game in an inactive state
        self.game_active = False
        self.reset_stats()
        # The highest score will never be reinitialized
        self.high_score = 0

    def reset_stats(self):
        self.ships_left = self.alien_invasion_settings.ship_limit
        self.score = 0
        # We put self.score here because it will run every time
        # the game initialize.
        # The level score will reinitialize every time the player
        # gets killed.
        self.level = 1
