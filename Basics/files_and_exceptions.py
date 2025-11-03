# --- Files and Exceptions --- #
# For the purposes of this synthesis we will need
# to download some files, the first of them is in
# the page https://www.nostarch.com/pythoncrashcourse
# We will use the file pi_digits.txt that is contained
# in the Python Crash Course, Eric Matthes github, repo.
# All credits due to him for making the file public
# We will use an example, from Eric Matthes book, of how to read the contents
# of a file and store them inside a variable.
with open("pi_digits.txt") as file_object:
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

# --- Folders, Relative and absolute path --- #
# When a file is inside a folder, you can't simply
# tell the python interpreter to find a file that
# is inside a folder. We need to tell the interpreter in
# what folder it's the file is located. This method is
# called defining relative path.
file_path = r"text_file\\pi_digits.txt"
with open(file_path) as file_object:
    contents = (file_object.read()).rstrip()
    print(contents)
# When using double backslashes we tell the interpreter
# that the next character should be treated as a normal
# character and not as a sequence
# We can also use absolute file paths
file_path = "E:/Projetos/Relembrando_Python/remembering_python_6/Basics/" \
            "pi_digits.txt"
with open(file_path) as file_object:
    contents = (file_object.read()).rstrip()
    print(contents)

# By defining the path where the file resides we can tell
# the interpreter to read directly from where it is
# but is almost never the best option

# --- Reading data by line --- #
# We may want to read data per line, with a for loop
# we can do it
with open("pi_digits.txt") as file_object:
    for line in file_object:
        print(line.rstrip())

# We can create a list with lines of data from a file
# with the method readlines()

with open("pi_digits.txt") as file_object:
    lines = file_object.readlines()
    file_object.close()
    # The close() method is redundant, but will give
    # us no problem whatsoever
for line in lines:
    print(line.rstrip())

# Now that we know how to open a file, we will know how
# to work with a file
with open("pi_digits.txt") as file_object:
    lines = file_object.readlines()
    file_object.close()
pi_string = ''
for line in lines:
    pi_string += line.strip()  # this will remove any leading
# and trailing whitespaces
print(pi_string + "\n" + str(len(pi_string)))
# This will show the string in only one line and the number of
# digits in the string

# --- Working with big files --- #
# We can also load large files
with open("pi_million_digits.txt") as file_object:
    lines = file_object.readlines()
    file_object.close()
pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string[:100] + "\n" + str(len(pi_string)))
# This will print the first 100 characters from the file
# and show the length of the line showing 1000002 digits
# - with the dot and the end of line included.

# Lets see if a number is in the first million digits of pi
number = input("enter a number with 4 digits\n")
if number in pi_string:
    print("The number is there")
else:
    print("The number isn't there")
# We can use the method replace() to replace this number with
# another number
if number in pi_string:
    pi_string.replace(number, str(123456))
    print("Number replaced")

# --- Writing data in a file --- #
# The open() function accepts arguments, with that we can write
# files by sending the right argument. With 'w' as a second
# argument we can tell the program not to read a file, but to
# write in it.
# We can write ('w'), read ('r'), read-write('r+'),
# concatenate ('a'), and more, a file.
# The open function automatically creates a new file if it does
# not exists, but it will erase everything it has if it already
# exists before giving back the file object
file = 'programming.txt'

with open(file, 'w') as file_object:
    # here we write something inside the file with the write()
    # method.
    file_object.write("This is programming")
    file_object.close()
    # It's redundant, I know.
# If you want to write numbers inside a text file, it will be
# necessary to convert it to a string using the str() function
# before writing it in the file.
with open(file, 'w') as file_object:

    file_object.write("This is programming\n")
    file_object.write("This is also programming.\n")
    # The '\n' here serves as an escape character
    # It will tell the interpreter to skip the current line
    # and began working using the next line in the document
    file_object.close()

# If we want to concatenate something to a file instead of
# overwriting it, we will have to use the 'a' argument
# so the new data will not overwrite the old data, but sum
# information to the file
with open(file, 'a') as file_object:
    file_object.write("This is a phrase written using"
                      "the concatenating argument.\n")
    file_object.close()
# By doing this, we concatenate the sentence to the end
# of the file

# --- Exceptions --- #
# When we use python, we can deal with special objects
# called exceptions to deal with error that can
# appear during the execution of the code. If you write
# a code that solves the exception, the python code
# will continue to execute.
# These exceptions are used with blocks of try-except
# Lets use two examples from Eric Matthes book
try:
    print(5/0)
    # This will cause a error called ZeroDivisionError
    # and we can treat it by using the block try-except
except ZeroDivisionError:
    print("You can't divide by zero.")

# Now we use this knowledge to create another program:
# a simple calculator that will use this try-except concept
# block of code.
print("This is a division calculator. Write two numbers and"
      "I'll divide them. \n Enter 'q' to quit.")

while True:
    first_number = input("Enter the first number:\n")
    if first_number == 'q':
        break
    second_number = input("Enter the second number:\n")
    try:
        answer = int(first_number)/int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero.")
    else:
        print(answer)

# Lets try to read a file that does not exists and use an
# try-exception block to deal it the FileNotFoundError
# This is another example from Eric Matthes book
file = 'alice.txt'
try:
    with open(file) as file_object:
        print(file_object.read())
except FileNotFoundError:
    print("The file " + file + " does not exist.")

# Now we saw how to deal with errors with the try-except block
