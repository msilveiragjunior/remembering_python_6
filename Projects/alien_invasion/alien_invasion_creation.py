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
