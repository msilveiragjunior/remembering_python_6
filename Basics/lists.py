# In python, we have to remember that a list is represented by the hooks
#  symbol ([]).
# So this countries = ['France', 'Guinea','Egypt'] is defined as a list
list_1 = ['france', 'guinea', 'egypt']
# With the command print(list_1[0]) we can access the first item of a list,
#  that is: france
print(list_1[0])
# With the method .title - i.e. the dot defining the method followed by the
#  name of the method that is associated with a function - we give a prettier
# output than before, making the first letter be in uppercase
print(list_1[0].title)
# In python, we can access the last item of a list using -1 between the hooks
#  symbol
print(list_1[-1].title)
# We can also define numbers other than -1, that being: -2; -3; -4. By doing
#  so, you'll output de second item from the end, the third and the forth and
#  so on
# We can concatenate a string with an item from a list with the plus (+)
#  symbol in a variable, then print it using print
message = "I'm from " + list_1[0].title()
print(message)

# ----- Adding, altering and removing items from a list ----- #
# Let's create another list and add some items to it
list_2 = ["ducati", "yamaha", "honda"]
print(list_2)
# We can modify elements in a dynamic list like this
list_2[0] = "honda"
print(list_2)

# --- Adding items to a list --- #
# We can concatenate an item to a list to add items to it. The straightforward
# way to do it is by using the method .append('item_to_be_added')
list_2.append('ducati')
# We can also create an empty list and append items to it using the same
# method. It's simple
list_3 = []
list_3.append('ducati')
list_3.append('honda')
list_3.append('yamaha')
print(list_3)

# --- Inserting elements to a list --- #
# We can also insert elements to a list using the method .insert(0*,
#  'item_to_be_added')
# *we can define the position in the list where the item will be added
list_3.insert(0, 'suzuki')

# --- Deleting a known item from a list --- #
# We can use the instruction del to delete an known positioned item from a list
del list_3[1]
# This will remove the second item from the list
# You can define any number and remove any item from any position that exists
# --- Using the method .pop() to remove items --- #
# With the method .pop() we can still work with the item from the list,
#  as it is stored in a variable. It will remove the last item from the list
# If you define the indice of the item that you want to remove, you can
#  remove the item in any position with the method .pop
motorcycles_pop = list_3.pop()

# --- Removing items according to a value --- #
# With the .remove('name_of_the_item_in_the_list') you can remove an item
#  from a list according to a value
list_2.remove('yamaha')
print(list_2)

# ----- Organizing a list ----- #
# Ordering permanently a list with the method .sort()
# The method sort() will sort a list in ascending order by default and returns
#  None as a result. The sort method is permanent
list_2.sort()
# We can also use arguments to reverse the method sort()
list_2.sort(reverse=True)
print(list_2)

# --- Temporarily ordering a list with the method .sorted() --- #
# We can use the .sorted method if we don't want to permanently modify the list
print(sorted(list_1))
# arguments like reverse=True can also be used

# --- Reversing a list with the method .reverse() --- #
# The .reverse() simply reverse the order of the original list, it does not
#  organize it in a descending order
list_3.reverse()
# It will permanently modify the list

# --- Discovering the size of a list --- #
# we can discover the size of a list with the len function
print(len(list_3))
# --------------------------------------------------------------------------- #
