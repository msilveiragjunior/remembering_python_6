# --- The input function --- #
# In simple terms, the input() function tells the interpreter
# to pause any other code execution and awaits for the user
# to input information for the program to continue to execute
message = input("Let's receive some input and repeat it back to you: \n")
print(message)
# In this, we store the input in a memory address and return
# in the print bellow the variable message
# The input function receives everything as a string
# so when using numbers, use the int() function to modify a
# number, that's interpreted as a string and transform it in
# a number
number_input = input("Input number: \n")
number_input = int(number_input)
if number_input <= 18:
    print("Number less or equal than 18")
else:
    print("Number higher than 18")
# This way we transform the string of the user input and can
# use as a number

# --- Modulo operator --- #
# the modulo (%) operator receive numeric information,
# divides by another number and returns the remainder
print(4 % 3)
# This will return 1. Tha is: the remainder

# --- The while loop --- #
# The while loop executes a loop while a condition is true
# for example:
number = 1
while (number <= 10):
    print(number)
    number += 1
print(number)
# As you can see, the last time the number is printed is after
# the condition defined is met to stop the while loop
# showing the number 11
boolean_variable = True
while boolean_variable:
    message = input("Write 'quit' to quit the program: ")
    if message.lower() == "quit":
        boolean_variable = False
    else:
        print("Program is still active and will repeat itself. \n")
# Here we can use a boolean value - i.e. True or False -  to
# make the program continue to run while a word is not written
# we can also use the break instruction to stop the while loop
# to get out of the while loop when the word 'quit' is written
while True:
    message = input("Write 'quit' to quit the program: ")
    if message.lower() == "quit":
        break
    else:
        print("Program is still active and will repeat itself. \n")
# We can use the continue instruction to return to the beggining
# of the while loop without executing any other code
# This example comes from directly from the book Python Crash
# Course, from Eric Mathes
number_2 = 0
while number_2 < 10:
    number_2 += 1
    if number_2 % 2 == 0:
        continue
    print(number_2)
# This will skip every even number and print every odd number
