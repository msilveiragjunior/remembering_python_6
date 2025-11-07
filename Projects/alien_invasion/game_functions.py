import sys
# The module sys imports functions and methods pertaining to
# the system, allowing interaction from the system with the
# python interpreter
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep


def check_events(alien_invasion_settings, screen, stats, play_button,
                 ship, aliens, bullets):
    for event in pygame.event.get():
        # Here we'll watch all the events from the keyboard
        # and mouse, like button activations
        if event.type == pygame.QUIT:
            sys.exit()
            # This will exit the game if the event type
            # is equal to the method .QUIT from pygame
        # Here We update the check_events() function
        # to check key presses from the player. In this specific
        # case, we check if the player is pressing the right arrow key.
        # Every pressing event is registered as a KEYDOWN event.
        # When a KEYDOWN event is detected, we will verify, with
        # the constant K_RIGHT.
        if event.type == pygame.KEYDOWN:
            check_keydown_events(event, alien_invasion_settings, screen,
                                 stats, ship, aliens, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        # By doing this, we'll check the functions of
        # the events that are now separated, making
        # the file cleaner.

        # We'll create a event.type to activate the play button
        # when the mouse clicks on the play button.
        # To do it, we'll have to get the mouse position, and we'll
        # do that using mouse.get_pos() method. It returns a tuple
        # of (x,y) coordinates of the mouse.
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # Here we'll call a function that we are going to create.
            # This function will check if mouse, when clicked, collides
            # with the play button rect. If it does it, we'll set the
            # game_active flag to True, beginning the game.
            check_play_button(alien_invasion_settings, screen, stats,
                              play_button, ship, aliens, bullets, mouse_x,
                              mouse_y)


def start_game(alien_invasion_settings, screen, stats,
               ship, aliens, bullets):
    # Hide the mouse cursor
    pygame.mouse.set_visible(False)

    stats.reset_stats()
    stats.game_active = True

    # Empty the aliens and bullets group
    aliens.empty()
    bullets.empty()

    # Create a new fleet and centralize the spaceship
    create_fleet(alien_invasion_settings, screen, ship, aliens)
    ship.center_ship()


def check_play_button(alien_invasion_settings, screen, stats,
                      play_button, ship, aliens, bullets, mouse_x, mouse_y):
    button_click = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_click and not stats.game_active:

        # Hide the mouse cursor
        # pygame.mouse.set_visible(False)

        # stats.reset_stats()
        # stats.game_active = True

        # # Empty the aliens and bullets group
        # aliens.empty()
        # bullets.empty()

        # # Create a new fleet and centralize the spaceship
        # create_fleet(alien_invasion_settings, screen, ship, aliens)
        # ship.center_ship()
        start_game(alien_invasion_settings, screen, stats,
                   ship, aliens, bullets)


def check_keydown_events(event, alien_invasion_settings, screen,
                         stats, ship, aliens, bullets):
    if event.key == pygame.K_RIGHT:
        # If the attribute defined before in the for
        # loop - i.e. event - .key is equal to the constant K_RIGHT,
        # then we move the ship to the right, incrementing the
        # centerx with a value of + 1.
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
        # Here we almost repeat the code to move to the right,
        # but we use the constant K_LEFT to check if the arrow
        # pressed is the left arrow.
    elif event.key == pygame.K_SPACE:
        fire_bullets(alien_invasion_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()
        # When the interpreter sees that the player pressed
        # the letter Q, the game exit, using a sys method called
        # exit()
    # Here we'll start the game if the player press the 'P' button
    elif event.key == pygame.K_p and not stats.game_active:
        start_game(alien_invasion_settings, screen,
                   stats, ship, aliens, bullets)


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
        # Here we define the constant event KEYUP
        # together with the flag moving_right, so
        # we can implement the continuous movement.
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
        # Here we almost the repeat the code to
        # check if the keypress has stopped, but,
        # this time, we'll check if the keypress of the
        # left arrow has stopped.


def update_screen(alien_invasion_settings, screen, stats, ship, aliens,
                  bullets, play_button):
    # This will update the screen to the color that we choose
    screen.fill(alien_invasion_settings.bg_color)
    # Every time the screen updates, it will execute the code
    # above, updating the screen color to the contained rgb
    # 3-tuple contained inside bg_color

    # Drawing the Play button if the game_active flag is False
    if not stats.game_active:
        play_button.draw_button()

    # We draw all the bullets here
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)
    # The blitme method is inside the class Ship, that is inside
    # the object ship that we've instantiated. This
    # will draw the ship over the background.
    pygame.display.flip()
    # The method .flip() from display module is
    # responsible for updating the screen of the game
    # So it will show the newly rendered frame of the game
    # This will constantly update the game screen


def update_bullets(alien_invasion_settings, screen, ship, aliens, bullets):
    # Delete the bullets that disappear:
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # When we use the method copy() to create
    # a copy of the object bullets, we can
    # go through the object with the for loop
    # and verify if the bullet, in that moment,
    # holds the attribute self.y that is smaller
    # or equal to zero. Then we can use it's value
    # to use the method remove, removing any value
    # that is equal to the value contained inside the bullets
    # group.
    check_bullet_alien_collisions(alien_invasion_settings, screen, ship,
                                  aliens, bullets)


def check_bullet_alien_collisions(alien_invasion_settings, screen, ship,
                                  aliens, bullets):
    # Here we'll use the code groupcollide() to calculate
    # if the bullet hit any alien
    pygame.sprite.groupcollide(bullets, aliens,
                               True, True)
    # If we want to make the bullets go through all aliens behind,
    # and to the top border of the screen, we can make the first bool
    # value False, this way we'll deactivate the dokill1 parameter code.
    # By doing this, we'll not make the bullets disappear when it hits
    # a alien.

    # Here we can create a new fleet if aliens.Group() is empty.
    if len(aliens) == 0:
        # Destroys empty bullets and creates a new fleet
        bullets.empty()
        alien_invasion_settings.increase_speed()
        # Here we call the function increase_speed, so every time
        # the player kills every alien, the speedup_scale will
        # multiply the dynamic attributes, making the game harder.
        create_fleet(alien_invasion_settings, screen, ship, aliens)
        # The empty() method removes all the sprites remaining in a Group.
        # In this case, the bullets.Group(), before creating a new fleet.


def fire_bullets(alien_invasion_settings, screen, ship, bullets):
    if len(bullets) < alien_invasion_settings.bullets_allowed:
        new_bullet = Bullet(alien_invasion_settings, screen, ship)
        # Here we instantiate a bullet from the class Bullet, sending the
        # settings, screen and ship to it.
        bullets.add(new_bullet)
        # Here we add new bullets to the set bullets, inside
        # alien_invasion.py


def get_number_aliens_x(alien_invasion_settings, alien_width):
    # We'll use the formulae defined inside the alien_invasion_creation.py
    # to calculate the number of aliens in a line
    # The spacing between aliens are half of the width of a alien ship
    number_aliens_x = int((alien_invasion_settings.screen_width
                          - (1.7 * alien_width)) / (1.5 * alien_width))
    return number_aliens_x


def get_number_rows(alien_invasion_settings, ship_height, alien_height):
    # Define the number of aliens that fit on the screen
    number_rows = int(((alien_invasion_settings.screen_length - 3 *
                        alien_height - ship_height) / (2 * alien_height)))
    return number_rows


def create_alien(alien_invasion_settings, screen, aliens, alien_number,
                 row_number):
    alien = Alien(alien_invasion_settings, screen)
    alien_width = alien.rect.width
    alien = Alien(alien_invasion_settings, screen)
    alien.x = int(alien_width + 1.5 * alien_width * alien_number)
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 1.5 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(alien_invasion_settings, screen, ship, aliens):

    alien = Alien(alien_invasion_settings, screen)
    number_aliens_x = get_number_aliens_x(alien_invasion_settings,
                                          alien.rect.width)
    number_rows = get_number_rows(alien_invasion_settings, ship.rect.height,
                                  alien.alien_height)

    # Creating the first line of aliens
    # for alien_number in range(number_aliens_x):
    #    create_alien(alien_invasion_settings, screen, aliens,
    #                 alien_number)
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(alien_invasion_settings, screen, aliens,
                         alien_number, row_number)


def check_fleet_edges(alien_invasion_settings, aliens):
    # Check if the fleet is on the either border of the screen
    for alien in aliens.sprites():
        change_fleet_direction(alien_invasion_settings, aliens)
        break


def change_fleet_direction(alien_invasion_settings, aliens):
    # Make the fleet go down and change its direction
    # by altering the fleet direction
    for alien in aliens.sprites():
        alien.rect.y += float(alien_invasion_settings.fleet_drop_speed)
        alien.rect.y = float(alien.rect.y)
    # Then we multiply by -1. If it is 1, then the value goes
    # to -1; if it is -1, the value goes to 1. It's the logical
    # way to go it
    alien_invasion_settings.fleet_direction *= -1


def check_aliens_bottom(alien_invasion_settings, stats, screen, ship, aliens,
                        bullets):
    # Now we'll create a variable the will inherit the width and length of
    # the screen
    screen_rect = screen.get_rect()
    # Now we'll check if any alien, for any alien in the Group() aliens, has
    # hit the bottom of the screen, using the logic explained on
    # alien_invasion_creation file.
    for alien in aliens.sprites():
        # This will deal with the sprites from the aliens.
        if alien.rect.bottom >= screen_rect.bottom:
            # calls shit_hit() function
            ship_hit(alien_invasion_settings, stats, screen, ship, aliens,
                     bullets)
            break


def update_aliens(alien_invasion_settings, stats, screen, ship, aliens,
                  bullets):
    # Update the position of all aliens from the fleet
    # Now it also checks if the fleet is on the border of the screen
    check_fleet_edges(alien_invasion_settings, aliens)
    aliens.update()
    # Check if there's any collisions between the ship and the aliens
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(alien_invasion_settings, stats, screen, ship, aliens,
                 bullets)
    # Check if any alien has hit the bottom of the screen
    check_aliens_bottom(alien_invasion_settings, stats, screen, ship, aliens,
                        bullets)


def ship_hit(alien_invasion_settings, stats, screen, ship, aliens,
             bullets):
    # We'll implement the end of the game here, by seeing if the
    # ship has been hit 'n' times.
    if stats.ships_left > 0:
        # -1 to ships_left
        stats.ships_left -= 1

        # Empty the list of aliens and bullets
        aliens.empty()
        bullets.empty()

        # Creates a new fleet and centralize the spaceship
        create_fleet(alien_invasion_settings, screen, ship, aliens)
        ship.center_ship()

        # Uses the sleep function from the time module to
        # give a little time for the player
        sleep(1)
    else:
        stats.game_active = False
