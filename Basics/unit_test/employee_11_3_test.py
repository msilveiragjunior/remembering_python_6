import unittest
from employee_11_3 import Employee


class EmployeeTest(unittest.TestCase):
    new_value = 10000

    def setUp(self):
        employee_01_data = ["Henry", "Mills", 10000]
        self.employee_01 = Employee(employee_01_data[0], employee_01_data[1],
                                    employee_01_data[2])
        self.new_value = 10000

    def test_give_default_raise(self):
        self.employee_01.give_raise()
        self.assertEqual(self.employee_01.salary, 15000)

    def test_give_custom_raise(self, new_raise=10000):
        self.employee_01.give_raise(new_raise)
        self.assertEqual(self.employee_01.salary, 20000)
    # Here we test if the give_raise with a new value is accepted
    # and returns the correct value for the new salary of employee_01


unittest.main()
