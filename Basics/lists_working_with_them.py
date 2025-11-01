# Let's work with lists, following the Python Crash Course book by Eric Mathes
# --- Lets create a variable to work with --- #
magicians = ['alice', 'david', 'carolina']
# We will learn to work with the for loop
for magician in magicians:
    print(magician)
# In this loop the for loop will verify the if the conditions of the loop
# returns a True
# If so, the loop body runs, returning every item from magicians, temporarily,
# storing inside magician and printing it.
# It will continue running until the returning condition is false, in this
# case, None, or nothing in the list magicians is stored any longer - nothing
#  in the position
# that currently is.

# Indenting is very important when using Python. Because of that, we can
# do other things after for loops
print(sorted(magicians))

# --- Working with numbers --- #
# We can use the range(*number,*number) to show a series of numbers
# inside a for loop
for value in range(1, 10):
    print(value)
# The range function will now print the last number. The last number is
# non-inclusive

# --- Creating a list of numbers --- #
# We can create a list of numbers using the function list() with the
# range() function
numbers = list(range(1, 11))
print(numbers)
# Let's create an even number list
even_numbers = list(range(2, 11, 2))
# This will create a list beginning with 2 and, with the last argument (2),
# we will sum 2 to every number in the list created
print(even_numbers)
# We can also create a list with perfect squares using the exponential
# symbol **
squares = []
for values in range(1, 16):
    squares.append(values**2)
print(squares)

# --- Working with simple statistics functions in python --- #
# We can use the min() function to find the minimum value in a list, max() to
# find the maximum value and sum() to find the sum of all the values of a list
list_1 = []
for values in range(1, 21):
    list_1.append(values)
print(min(list_1), max(list_1), sum(list_1))

# --- Working with list comprehensions --- #
# List comprehensions can input a for loop inside a variable
squares_2 = [values**2 for values in range(1, 21)]
print(squares_2)
# Here we define the variable values to be the square of every number in
# the range between 1 and 21, with 21 non-inclusive. It returns a list
# because we defined that the for would be run inside a list that we
# created

# --- Working with part of a list --- #
# We can slice a list using the following notation
values = [value for value in range(1, 25)]
print(values[0:8])
# By doing this, we will only show the first 3 numbers in the list
# We can also define the first item of the list to be any number
# for example 1, 2 and so on
# If we omit the first index the slicing will begin with the
# first item in the list
# We can show only the 'n' items in a list by omitting the
# second number in the slicing notation, doing this
print(values[2:])
# this will print all the values after the second item in the
# index
# We can also show only the last 'n' number of items in a
# list by using this notation
print(values[-4:])
# this will show only the last, from the last to the next descending
# number

# --- Using slicing in a for loop --- #
# we can use the slicing technique in a for loop to show
# only the numbers that we want to be shown
for i in values[0:10]:
    print(i)
# This will show the first 10 numbers

# --- Copying a list --- #
# We can copy a list my using this notation
values_2 = values[:]
# This will create an exact copy of the first list
# because we omitted the first and last index
# This will not work: values_2 = values as we are only pointing to the
# interpreter and, basically, saying that the second list should be
# interpreted as the first list, so it will not be a separate copy

# --- Tuples --- #
# Tuples offer a way to store datasets of items that cannot be modified
# We define tuples in the following form
tuple_01 = (200, 50)
print(tuple_01[0] + " " + tuple_01[1])
# We cannot modify a tuple by simply redefining it's value like
# tuple_01[0] = 400; this will not only not work, but will show
# a TypeError, saying that a tuple does not support item
# assignment
# We cannot modify the single value of a tuple, but we can
# redefine the tuple in itself
tuple_01 = (400, 100)
print(tuple_01[0] + " " + tuple_01[1])
for x in tuple_01:
    print(x + "\n")
# This will print all values inside the tuple
