# --- Alien Invasion project from the book --- #
# Lets follow Eric Matthes book to create the project
# alien invasion. For that, we'll have to install
# pygame to windows
# To do that, we'll have to execute pip install pygame
# inside the windows terminal

# Lets follow Eric Matthes book, python crash course.
# We'll create alien_invasion.py file; with this first
# file we'll create an empty window so the module
# pygame can execute

# Now that we've created the game screen, we can modify
# the background color, following the book.

# Now lets create a class with configurations for the program.
# By doing this, we'll make the program cleaner and organized.
# Lets call it settings.py

# Following the Python Crash Course book, we'll now add the image
# of the spaceship to our game. We'll load it and use the method
# blot() from pygame to draw it.

# Lets create the class ship, so it will hold and load and draw
# the image of the ship.
# We'll call it ship.py, the same name the book uses

# Lets update the alien_invasion file and draw the ship,
# from the ship class inside ship.py file, inside it.

# Now we will refactor the main program. We need to make
# it cleaner: think about readability.
# Lets follow the book and create a module called game_functions.py,
# where we'll store all the functions from alien_invasion.
# We modified alien_invasion.py to import the game_functions.py and,
# now, use it's functions.
# We've updated the game_functions.py with all code pertaining to
# updating the screen, showing the background color and the drawing
# the ship.

# Now that we've refactored the game, we'll create a way for the player
# to command the ship. We'll update the game_functions.py to give
# the functions for the player to do so.
# We've now updated the game_functions file to let the player move the ship
# to the right side of the screen, by pressing the right arrow key.

# We have to let the player have a continuous movement. To do it, we
# need to update the check_events() function to make the keypress
# be detected until the player releases it. When we do it, we
# make the movement a continuous movement.

# Now we need to make the ship be able to move to the left.
# We'll update the Ship class and the function check_events()

# Lets adjust the speed of the spaceship. Right now,
# it moves a pixel per cycle of the while loop. Whoever,
# we can have the control over the speed that it will move
# across the screen. So lets create a new attribute inside
# settings.py to make it possible. All of this is inside
# the book from Eric Matthes, Python Crash Course, so all
# credits due to him.

# Now lets limit the range of movement of the spaceship
# We need to make the spaceship stop when it hits the border of
# the screen. We'll update the method update() inside the
# class Ship to do it.

# We need to refactor the function check_events(). It'll
# grow and it's going to be difficult to go through it's
# functions without getting lost.

# --- Shooting with the spaceship --- #
# Lets add the capability of shooting with the spaceship.
# To do so, we need to write a new code that will
# launch a little projectile when, and only when, the player press the
# space bar
# First we need to make adjustments to the settings.py file,
# so we can include the values that we'll need to create a new class:
# the Bullet class.

# Now we'll create an instantiation of the class pygame.sprite.Group
# This class, also called a container class - due to it's abilities
# to hold objects and be testable -, stores lists of sprites objects,
# like the projectiles that we are working with. By instantiating
# this class, we'll be able to manage active projectiles, and
# use this group to draw projectiles on the screen.

# Lets modify the check_keydown_events() to shoot a bullet when
# the space bar is pressed. We'll also need to modify the update_screen()
# before the display.flip() is called.

# Now that we've created functional bullets, we need to deal
# with the existing projects. Just because they don't show
# on the screen when they go up, does not mean they don't exist
# in the memory, consuming processing power and memory.
# We need to delete then when they reach the top of the screen,
# by checking if the rect.bottom value is less or equal than 0,
# that means: the y of the projectile value is not less or equal than 0:
# the top of the screen. But remember: this signifies the top
# of the screen because the value x,y increases as it goes to the right
# and down.

# We need to limit the number of projectiles on the screen.
# By doing it, the player needs to shoot in a precise way to
# hit the aliens.
# Lets define the number of bullets allowed inside settings.py
# We'll also need to modify the game_functions.py, so we can
# check if the number of bullets inside the group bullets is
# smaller than the number of bullets allowed. In that way,
# if the number of bullets is smaller than 4, we can shoot another
# one, because 3 bullets + 1 new bullet = 4 bullets.

# We want to maintain the main file of the game simple,
# so lets create a function inside game_functions called
# update_bullets(), so we can add the code from alien_invasion -
# the one that update the bullets - to the game_function
# file.

# Lets refactor the code again, creating a function called
# fire_bullet(), simplifying the check_keydown_events().

# --- Creating aliens to shoot --- #
# We've created the base of the game, now we can create
# the rest of it (haha), meaning that we'll continue
# to follow Eric Matthes book, and try to explain the concepts
# behind every code in a more concise way. But remember, this
# is a personal study, to remember the concepts of python; as
# well as a way to help people understand certain concepts.
# So let's begin:
# Lets begin adding a keydown event that will check if the
# player wants to exit the game, this will be placed inside
# the game_functions.py

# We'll create the class Alien to represent our first alien ship.
# Lets create with within the alien.py file

# Now we have to make the alien appears on the screen.
# We'll call the method alien.blitme() after the ship.blitme()
# inside the game_functions.py

# Now we need to create a fleet of aliens. To do that,
# we need to know how many aliens can be put on the same
# vertical line.
# We can know that by knowing how much space is available
# to put alien ships, the width of a alien ship and a space
# between the alien ships. Let's say we want the space of half
# of the width of a alien ship between the alien ships.
# Knowing this, we can know the number of aliens that we can put
# on a vertical line by doing this calculation:
# number_of_aliens = ((alien_invasion_settings.screen_width
#                      - (1.5 * alien_width)) / (1.5 * alien_width)
# This way, we'll know the number of aliens available to be put on the screen

# --- Creating a fleet of aliens --- #
# To create the first line of aliens, we need an empty Group()
# called aliens inside alien_invasion and a function inside
# game_functions.py to call our fleet.

# Lets refactor the create_fleet() function
# We'll create two new functions to make the game_functions.py
# cleaner: get_number_aliens_x() and create_alien()
# We are doing this to make it easier to work with them.

# Lets add lines to our fleet. To do so, we need to determine
# the number of lines that fit on the screen, and then we will
# repeat the loop that creates aliens on a line.
# To determine this we can use this formulae:
# number_rows = ((alien_invasion_settings.screen_length - 3 *
#                 alien_height - ship_height)/ (1.5 * alien_height))
# Now that we know how many ships we can fit inside the screen,
# we can modify the game_functions.py to properly fit our formulae

# We've created our fleet of aliens, now we have to make them move.
# Lets follow the book from Eric Matthes and make them move
# to the right first.
# To move the aliens to the right, we'll use the method update().
# The method is inside alien.py and will be called for each alien
# of the fleet.

# Lets create a drop_speed for the fleet, so it can go down,
# and create a variable for its direction inside the settings.py
# We can alternate between 1 and -1 to define if it's going
# to the right or to the left. To use numbers make sense,
# because we can change the numbers and alternate the values
# every time the fleet changes direction.

# Now we can make the fleet go down and change its direction
# we'll do this by creating new functions, following the book
# instructions

# We'll make our spaceships shoot, and hit, the alien ships
# to do that, we'll use the method sprite.groupcollide(),
# so we can verify collisions between the members of the two
# groups.
# The method sprite.groupcollide(group1, group2, dokill1,
#                                dokill2, collided = none) method find all
# sprites that collide between two groups.
# The collision is determined comparing the sprite.rect attribute
# of each sprite.
# Every sprite in group1, is added to a return dict. The value of each item()
# is the list of sprites in group2 that intersect.
# If either dokill argument is True, sprites from those groups will be
# removed from their Group().
# Now we'll follow the book to add the new code to the game; this new
# code will calculate the intersection between the bullet and aliens.
# If we hit one, both will disappear.

# We've created the collision function. Now we need to repopulate
# the fleet of aliens so, if we destroy all of them, they will
# reappear.

# At least for my computer, the alien fleet is dropping too fast.
# So we'll update the frames per second, now we'll not follow
# Eric Matthes book.
# We'll do this by limiting the fps of the game.
# We've modified the ship speed, the bullet speed and the alien
# fleet speed to account for the limitation of fps.

# Now we're going to refactor the update_bullet() function,
# and create a new function to check the alien collision with
# bullets, AND to create a new fleet.

# We need to detect if the ship has been hit by any alien ship.
# To do so, we need to use the spritecollideany(sprite, group, collided = none)
# If the sprite collides with anything inside the group, if there's
# no collision, none is returned.
# It will take two sprites, one from sprite and one from group and
# calculate if the two intersect each other. It will return
# a boolean value showing if it has happened or not.
# So lets create a function to detect it
