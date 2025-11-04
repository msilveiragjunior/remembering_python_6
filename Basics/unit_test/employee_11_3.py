class Employee():

    def __init__(self, name, last_name, salary):
        self.name = name
        self.last_name = last_name
        self.salary = salary
    # Here we create the init class

    def give_raise(self, new_raise=5000):
        self.salary += new_raise
    # Here we create the give_raise method with a default of 5000
    # for a new raise
