#Let's work with lists, following the Python Crash Course book by Eric Mathes
# --- Lets create a variable to work with --- #
magicians = ['alice', 'david', 'carolina']
# We will learn to work with the for loop
for magician in magicians:
    print(magician)
# In this loop the for loop will verify the if the conditions of the loop returns a True
# If so, the loop body runs, returning every item from magicians, temporarily, storing inside magician and printing it.
# It will continue running until the returning condition is false, in this case, None, or nothing in the list magicians is stored anylonger - nothing in the position
# that currently is.

# Indenting is very important when using Python. Because of that, we can do other things after for loops
print(sorted(magicians))

# --- Working with numbers --- #
# We can use the range(*number,*number) to show a series of numbers inside a for loop
for value in range(1,10):
    print(value)