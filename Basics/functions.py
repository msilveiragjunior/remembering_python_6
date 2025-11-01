# --- Functions --- #
# Functions are blocks of code conceived to execute
# some lines of code written by the user, but
# only when they are "called" to be executed
# They are extremely important in a program, due to
# it's capabilities to replicate a code without writing
# the same code again.
# We define a function by using the instruction def,
# followed by the name of the function
# it also accepts arguments
def repeat_message(message):
    print(message + "." + "\n This is the message.")


repeat_message(input("Input a message to repeat: \n"))
# Here we send an argument, an input for the user
# and send to the function to be used inside it
# so every time we want to send an information, we
# can just call the function and it will repeat it's
# behavior. The message in repeat_message is a parameter
# while the input, when calling the function, is an
# argument