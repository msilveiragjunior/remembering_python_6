import pygame.font


class Scoreboard():

    def __init__(self, alien_invasion_settings, screen, stats):
        # Initializing the scoreboard attributes
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.alien_invasion_settings = alien_invasion_settings
        self.stats = stats

        # Settings for the scoreboard font
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Calls prep_score from the Scoreboard class
        self.prep_score()

    def prep_score(self):
        a_i = self.alien_invasion_settings
        # Render the str points into an image
        rounded_score = int(round(self.stats.score, -1))
        # When we round up to a negative number, it'll
        # round the number to its nearest 10 (-1), 100 (-2), or 1000 (-3)
        # multiple, and so on.
        score_str = "{:,}".format(rounded_score)
        # By using this formatting way to format a string, we'll
        # place a comma every third number from right to left.
        self.score_image = self.font.render(score_str, True, self.text_color,
                                            a_i.bg_color)

        # Shows the score on the right superior side of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        # Here we put the score image 20 pixels before
        # the right border of the screen
        self.score_rect.top = 20
        # Here we place the score_rect 20 pixels on the y axis.
        # PS: remember, on the pygame, the y grows from the top to
        # the bottom.

    def show_score(self):
        # We need to draw the score on the screen
        # So we'll use the blit() method from pygame
        # to do it
        self.screen.blit(self.score_image, self.score_rect)
