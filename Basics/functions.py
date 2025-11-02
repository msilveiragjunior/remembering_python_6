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

# --- Keyword arguments --- #
# It's a name-value given to the function so there's
# no confusion when it's given to a function
# Using an example from Eric Mathes Book:


def describe_pet(animal_type, pet_name):
    print(animal_type + " " + pet_name)


describe_pet(animal_type='hamster', pet_name='harry')
# Here we define what will be the argument and to what
# parameter it will be defined

# --- Default Values --- #
# We can write default values to functions for each
# parameter. If an argument is specified in a function
# the function will use it's value, otherwise, it will
# use the default value


def describe_pet_two(animal_type, pet_name='batman'):
    print(animal_type + " " + pet_name)


describe_pet_two(animal_type='hamster')
# Here we define the default value in the parameter of
# the describe_pet_two function
# PS: the default value must always be defined after
# defining all other non-default parameters when defining
# a function

# --- Returning values --- #
# We can also make function return values when calling them.
# When doing it, we can attribute the returned value to a
# variable and can use it after


def name_of_car_formatted(name, brand):
    name_brand = name.title() + ", " + brand.title()
    return name_brand


name_formatted = name_of_car_formatted('pajero', 'mitsubishi')
print(name_formatted)

# We can also define default values to make argument optional


def example_function(first_name, last_name, middle_name=''):
    print(first_name.title() + " " + middle_name.title() +
          " " + last_name.title())


example_function("jimmy", "hendrix")

# By doing this, we can choose not to send certain arguments

# --- Creating a function with an arbitrary number of arguments --- #
# We can make it by adding the asterisk symbol before the name
# of the parameter in a function.
# By doing so, it'll create a tuple of arguments with the name
# of the parameter of the function
# Using an example of Eric Matthes book:


def make_pizza(*toppings):
    print("Making pizza with ")
    if toppings:
        for topping in toppings:
            print("- " + topping)
    else:
        print("no toppings.")


print(make_pizza("green pepper", "pepperoni"))
print(make_pizza("green pepper", "pepperoni", "cheese"))
# By doing this, we can send any number of arguments to
# the function and it will treat it's parameters as tuples

# --- Using double asterisks to pass a dictionary --- #
# We can use double asterisks (**) to pass an arbitrary
# number of named arguments to a function. By doing so
# we can, for example, pass a dictionary as a key-value
# keyword to a function and use it as we please
# We can use it when we don't know the number of arguments
# that will be sent to the function
# Lets use an example from Eric Matthes book


def build_profile(first, last, **user_info):
    profile = {

    }
    profile['first_name'] = first
    profile['last_name'] = last
    for k, v, in user_info.items():
        profile[k] = v
    return profile


user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)
# Here we send the first and last name of the user in the
# dictionary and send dictionary information using the double
# asterisk, explicitly defining the value to what key it should
# be assigned

# --- Modules --- #
# We can use the 'import' instruction to bring functions
# from other files, leaving the main program file clean
# and free of unnecessary information
# one example is 'import sys'
# We can also import specific functions by doing this:
# from 'name_of_the_module_file' import 'name_of_the_function'
# we can also use the comma (,) to import as many
# functions as we want from the file

# We can use aliases to attribute a function with a name
# for example: from 'module' import make_something as <- ( important) ms
# by doing this, we assign the to ms() the function make_something()

# We can also use aliases to attribute a name to a module
# for example: import 'module' as m
# so when we use the module, we will use as m.make_something()

# We can import all functions from a module using the asterisk symbol (*)
# from module import *
# by doing so, we do not need to use the dot before the function
# as all functions are imported to the file fom which the import
# came from, so we can just name the function
