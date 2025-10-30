# In python, we have to remember that a list is represented by the hooks symbol ([]).
# So this countries = ['France', 'Guinea','Egypt'] is defined as a list
list_1 = ['france', 'guinea','egypt']
# With the command print(list_1[0]) we can access the first item of a list, that is: france
print(list_1[0])
# With the method .title - i.e. the dot defining the method followed by the name of the method that is associated with a function - we give a prettier
# output than before, making the first letter be in uppercase
print(list_1[0].title)
# In python, we can access the last item of a list using -1 between the hooks symbol
print(list_1[-1].title)
# We can also define numbers other than -1, that being: -2; -3; -4. By doing so, you'll output de second item from the end, the third and the forth and so on
# We can concatenate a string with an item from a list with the plus (+) symbol in a variable, then print it using print
message = "I'm from " + list_1[0].title()
print(message)