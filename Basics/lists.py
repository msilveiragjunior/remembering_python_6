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
# ----- Adding, altering and removing items from a list ----- #
#Let's create another list and add some items to it
list_2 = ["ducati", "yamaha", "honda"]
print(list_2)
# We can modify elements in a dynamic list like this
list_2[0] = "honda"
print(list_2)
# --- Adding items to a list --- #
# We can concatenate an item to a list to add items to it. The straightforward way to do it is by using the method .append('item_to_be_added')
list_2.append('ducati')
# We can also create an empty list and append items to it using the same method. It's simple
list_3 = []
list_3.append('ducati')
list_3.append('honda')
list_3.append('yamaha')
print(list_3)
# --- Inserting elements to a list --- #
# We can also insert elements to a list using the method .insert(0*, 'item_to_be_added')
# *we can define the position in the list where the item will be added
list_3.insert(0, 'suzuki')
# --- Deleting a known item from a list --- #
# We can use the instruction del to delete an known positioned item from a list
