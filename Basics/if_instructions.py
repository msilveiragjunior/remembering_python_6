# --- If instructions --- #
values_01 = [values for values in range(1, 50)]
# Here we are using list comprehension
# Let's use a simple if example
for x in values_01:
    if (x % 2 != 0):
        print("Not even")
    else:
        print("Even")
# This will check the even values
# To check a condition we use != for not equal and == for equal values
# Let's say we wanted to do the last check using the equal symbol
for x in values_01:
    if (x % 2 == 0):
        print("Even")
    else:
        print("Not Even")
# We can also use the operator and for using more than one condition in a if
# test
# --- Check if an object is in a list --- #
if 5 in values_01:
    print("It is inside the list")
else:
    print("It's not in")
# The operator not in is can also be used to check if a value is not inside
# a list or a tuple or a set
# PS: let's not forget that when using strings, the value of a string
# will differ if it's not completely equal, like 'uber' == 'Uber'
# we can use the method .lower() to make the two equal to check
# if they are the same, if only the name matters
# the else condition says to the interpreter that if the condition
# is not met, then it will use it to output the result
# --- elif --- #
age = 18
if age < 18:
    print("Less than 18")
elif age < 18 and age > 14:
    print("Age between 14 but less than 18")
else:
    print("Age higher or equal than 18")
