# --- Classes --- #
# When we use python, we can use object-oriented programming
# or OOP, we can use this approach to write software.
# When we use this approach, we define entities defined as
# classes and situations from the real world and we create
# objects based on these classes
# Classes have all the behavior that a category of objects
# can have.

# When we create a class we call this operation instantiation
# and when we work with this classes, we will work with
# instances of these classes.
# Lets use an example from Eric Matthes book
class Dog():
    # This will create the class dog
    def __init__(self, name, age):
        # By doing this we initialize the attributes name and age
        # By convention, classes are defined with an uppercase letter
        # The self attribute defines the instantiation of an object
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " is not sitting.")

    def roll_over(self):
        print(self.name.title() + " rolled over.")

# We define the method __init__(), with two underscores, before every class
# By doing this, the argument self will be passed automatically before every
# instantiation of an object associated to the class. So if we create an object
# called my_dog = Dog('Henry', 12), then my_dog is the self that is initiated
# When we do this, the interpreter knows that all the methods belong to the
# instantiated class, in this case: the object my_dog.
# The __init__ method is a (Constructor), or a set of attributes
# that will define a given object

# Variables like self.age = age are called attributes
# By convention, we use self as the name of the prefix, but we can use
# anything else.
# For example, self.name = name stores the value inside the parameter
# name and stores the variable name and then the instance is created.
# Methods inside the class Dog that won't need any other parameters
# will only need the self prefix, so the interpreter knows that it belongs
# to the class Dog() that is instantiated


my_dog = Dog('Henry', 12)
# When we do this, the self is attributed to my_dog.
# My dog has access to all the methods inside the class dog.
print(my_dog.name + "," + str(my_dog.age))
my_dog.roll_over()
my_dog.sit()

# The method __init__() creates an instance of the Dog() class
# and defines the attributes name and age with it's values.
# To access these attributes from init we use the dot(.) notation
# my_dog.name, my_dog.age and so on

# --- Default values to attributes --- #


class Bird():

    def __init__(self, wings, age):
        self.name = "No name"
        # We are attributing a default name to this attribute
        self.wings = wings
        self.age = age

# To modify an attribute with, it's best to use methods inside
# the class to update the attribute
# so lets create one
    def new_name(self, new_name):
        self.name = new_name


bird = Bird(2, 4)
print(bird.name)
bird.new_name("Harry")
print(bird.name)
# Now it has a name

# --- Inheritance --- #
# We can create daughter classes that will inherit all the
# attributes and methods from the father class. However,
# the new class is now free to define new methods and attributes to itself
# Lets create a daughter class


class My_bird(Bird):

    def __init__(self, wings, age, abilities):
        super().__init__(wings, age)
        # The super function is a function that will create a connection
        # between the father and daughter classes. It will tell the interpreter
        # to call the __init__ method from the father class
        self.abilities = abilities

    def abilities(self):
        print("It has" + str(self.abilities))
# Now we have a daughter class that inherits its father attributes
# but has a new attribute and a method that the father class don't have


my_bird_02 = My_bird(2, 5, 3)
my_bird_02.new_name("Charles")
print(str(my_bird_02.abilities) + ", " + str(my_bird_02.name))

# By doing this, we can access the new fathers function and the daughters
# function.

# --- Overwriting a method from the father class --- #


class My_bird_02(Bird):

    def __init__(self, wings, age, abilities, name):
        super().__init__(wings, age)
        # The super function is a function that will create a connection
        # between the father and daughter classes. It will tell the interpreter
        # to call the __init__ method from the father class
        self.abilities = abilities
        self.name = name

    def abilities(self):
        print("It has" + str(self.abilities))
# Now we have a daughter class that inherits its father attributes
# but has a new attribute and a method that the father class don't have

    def new_name(self):
        print("This bird already have a name!")
# By doing this we overwrite the father method inside the daughter class
# and the interpreter will ignore the father's code


my_bird_02 = My_bird_02(2, 5, 3, "Charles")
my_bird_02.new_name()
print(str(my_bird_02.abilities) + ", " + str(my_bird_02.name))

# --- Instances as attributes --- #
# We can use instances of classes to synthesize a bigger class
# by using them as attributes in their init. We only need to create
# the new class and initiate the new class, that can have new parameters
# as we can send arguments to it when we instantiate it when we
# create new objects


class Abilities():

    def __init__(self, abilities=["talk", "solve problems"]):
        self.abilities = abilities
        print(len(self.abilities))

    def describe_abilities(self):
        for i in self.abilities:
            print("This bird can" + " " + i.title())


class My_bird_03(Bird):

    def __init__(self, wings, age, abilities, name):
        super().__init__(wings, age)
        self.abilities = abilities
        self.name = name
        self.abilities_01 = Abilities()

    def abilities(self):
        print("It has" + str(self.abilities_01))

    def new_name(self):
        print("This bird already have a name!")


my_bird_03 = My_bird_03(2, 3, 2, "Charles")
my_bird_03.abilities_01.describe_abilities()
# By doing this we created an object that has an instance of a class
# inside it. This way, we can manage in better ways what it
# can and cannot do.

# --- Importing classes --- #
# We can import classes, and not only can but should, when
# a given program is getting bigger. So we can write the classes
# inside another file and import the classes that we need
# for example: from birds import My_bird_03
# this will ask the interpreter to import only the class
# My_bird_03 from the file birds
# We can also make all the classes stay in only one file,
# making it easier to find them when should we need to import them.
# We can import a group of classes using the comma symbol(,)
# for example: from birds import My_bird_02, Abilities, My_bird_03
# We can import all the module by doing import birds
# We can import all the classes inside the module:
# from birds import *
# Or we can divide the modules and import a module inside a module,
# so we can make things tidier
# PS: I made a mistake when writing the classes:
# They should be written using CamelCaps. In other words:
# They should have the each letter of the first word
# capitalized and should not have underscores, as I did
# This is a styling convention.
# They also shall all have a docstring - i.e. a concise description
# of what a class does.
# ----------------------------------------------------------------
