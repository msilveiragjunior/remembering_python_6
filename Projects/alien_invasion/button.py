import pygame.font


class Button():

    def __init__(self, alien_invasion_settings, screen, msg):
        self.screen = screen
        # Here we get the values of the screen, to work with
        # its tuple of l,h
        self.screen_rect = screen.get_rect()
        # Here we use the method get_rect() to get the dimensions
        # of the screen.

        # Lets define de dimensions and attributes of the button
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        # the attribute font receive from the font class,
        # Sysfont.
        # We send the argument None, which makes it use the default
        # font, and the size, 48

        # Here we define the rectangle to place the button
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        # Rect() method needs a top, and left coordinates, followed
        # by the width and height arguments.
        self.rect.center = self.screen_rect.center
        # Here we make its self.rect.center attribute to be equal
        # to the center attribute of the screen.

        # Here we call the function that will show the message on
        # the button
        self.prep_msg(msg)

    def prep_msg(self, msg):
        # Here we'll use font.render() method to render the font
        # and transform it into an image
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
        # The render method takes a msg argument, an bool argument to
        # make an antialias true or false, a color and a background argument
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        # Here we make the msg_image rect center be equal to the
        # rect.center of the button

    def draw_button(self):
        # Now that we've rendered the message, we need to draw it on
        # the screen
        self.screen.fill(self.button_color, self.rect)
        # The fill method fills an object with a color,
        # with the optional argument to fill a specific rect.
        # In this case, the button rect.
        self.screen.blit(self.msg_image, self.msg_image_rect)
        # The blit method draws an surface, in this case the msg_image,
        # and draws onto another surface, in this case, the msg_image_rect
