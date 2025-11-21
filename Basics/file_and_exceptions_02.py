import json
# ---  Continuing the work with files and exceptions --- #
# Here we are writing the file with a list of numbers ranging from
# 0 to 30 and, after that, we dump it to a json file name in the
# file_01 variable.
# Now lets load it
file_01 = 'numbers.json'

with open(file_01) as file_obj:
    numbers = json.load(file_obj)
    file_obj.close()
# Here we are loading the numbers that we saved in the file before

# --- Refactoring --- #
# Sometimes we will reach a point where the code will work,
# but it'll be full of information and difficult to read.
# We can use the refactoring technique to rewrite the code.
# The technique is simple: we rewrite the code to make it
# more manageable and readable.
# The compartmentalization is fundamental when writing
# a clean code; an easy and understandable code that is
# easy to maintain
