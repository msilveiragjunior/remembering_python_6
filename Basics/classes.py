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

# Variables like self.age = age are called attributes
# By convention, we use self as the name of the prefix, but we can use
# anything else.
# For example, self.name = name stores the value inside the parameter
# name and stores the variable name and then the instance is created.
# Methods inside the class Dog that won't need any other parameters
# will only need the self prefix, so the interpreter knows that it belongs
# to the class Dog() that is instantiated
