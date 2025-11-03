# --- Unit Testing --- #
# When we write code we can make mistakes.
# with the unittest module we have the tools
# to test if our code works how it should,
# with the inputs that he was made to receive.
# Lets use some examples from Eric Matthes book.

# We have create two files, name_function.py
# and names.py. Both files work as a program,
# now we have to test them. The module unittest offers
# tools to test your code. A unit test verifies if the
# behavior of a function is correct. A test case
# It's a collection of unit tests that verifies if the
# function works with all possible entries that a function
# could receive and include tests to represent each
# of these situations.

# Lets create a file to test these two files:
# the name will follow the same name from Eric Matthes book.
# test_name_function.py

# We've created the file and tested the function.
# When we call unittest.main(), every function beginning
# with 'test' will be tested without arguments
# and the response for it's tests will be shown on the
# terminal.

# Lets do the exercise 11.1 from the book.
