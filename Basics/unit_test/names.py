from name_function import get_formatted_name
# Secondly, we create a function that is the program to
# be tested
print("Enter the letter 'q' to quit")
while True:
    first = input("Please, give me a first name: \n")
    if first == 'q':
        break
    last = input("Please, give me a last name: \n")
    if last == 'q':
        break

formatted_name = get_formatted_name(first, last)
print(formatted_name)
