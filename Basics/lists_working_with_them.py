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
# The range function will now print the last number. The last number is non-inclusive

# --- Creating a list of numbers --- #
# We can create a list of numbers using the function list() with the range() function
numbers = list(range(1,11))
print(numbers)
# Let's create an even number list
even_numbers = list(range(2,11,2))
# This will create a list beggining with 2 and, with the last argument (2), we will sum 2 to every number in the list created
print(even_numbers)
# We can also create a list with perfect squares using the exponential symbol **
squares = []
for values in range(1,16):
    squares.append(values**2)
print(squares)

# --- Wroking with simple statistics functions in python --- #
# We can use the min() function to find the minimum value in a list, max() to find the maximum value and sum() to find the sum of all the values of a list
list_1 = []
for values in range(1,21):
    list_1.append(values)
print(min(list_1), max(list_1), sum(list_1))
