import unittest
from survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):

    def setUp(self):
        question = "What language did you first learn to speak? \n"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']
        # Here we create the setUp() method that will instantiate
        # a object to test the methods inside this test class,
        # by doing this, we negate the need to create a program
        # just to test the class

    def test_store_single_response(self):
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)
        # The assertIn method tests if a given variable
        # is in a list

    def test_store_three_responses(self):
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)
    # Here we try to test more than one response and it works
    # flawlessly. Now we know how to test classes.


unittest.main()
