# --- Files and Exceptions --- #
# For the purposes of this synthesis we will need
# to download some files, the first of them is in
# the page https://www.nostarch.com/pythoncrashcourse
# We will use the file pi_digits.txt that is contained
# in the Python Crash Course, Eric Matthes github, repo.
# All credits due to him for making the file public
# We will use an example, from Eric Matthes book, of how to read the contents
# of a file and store them inside a variable.
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)
# Here we use the function open(), with an necessary argument,
# to open the file pi_digits. The interpreter will search for the
# file inside the directory and return an object that represents,
# inside the computer memory, the file. Then, the interpreter will
# store it's content inside the variable file_object.
# The reserved word with closes the file when it's unnecessary to
# deal any longer with the file
# The method .read() will read all the contents of the variable
# and will store inside the variable contents
# we can use the method rstrip() with print(contents.rstrip())
# to remove the final blank line that the method .read()
# returns when reading the document contents.
# This will return an exact copy of the file contents.
