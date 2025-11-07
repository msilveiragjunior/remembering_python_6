class GameStats():

    def __init__(self, alien_invasion_settings):
        self.alien_invasion_settings = alien_invasion_settings
        # Initialize the game in an inactive state
        self.game_active = False
        self.reset_stats()

    def reset_stats(self):
        self.ships_left = self.alien_invasion_settings.ship_limit
