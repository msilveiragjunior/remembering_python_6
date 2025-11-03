import unittest
from name_function import get_formatted_name


class NameTestCase(unittest.TestCase):
    # Here we test to see if the name of
    # that is going to be returned is the same
    # as we intended to be.

    def test_first_last_name(self):
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')
        # With assertEqual we verify if the output from the function
        # is the same as what we've written, so the method takes
        # two arguments.


unittest.main()
