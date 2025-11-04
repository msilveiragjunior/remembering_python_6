import unittest
from survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):

    def test_store_single_response(self):
        question = "What language did you first learn to speak? \n"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')

        self.assertIn('English', my_survey.responses)
        # The assertIn method tests if a given variable
        # is in a list

    def test_store_three_responses(self):
        question = "What language did you first learn to speak? \n"
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'Spanish', 'Mandarin']
        for response in responses:
            my_survey.store_response(response)
        for response in responses:
            self.assertIn(response, my_survey.responses)
    # Here we try to test more than one response and it works
    # flawlessly. Now we know how to test classes.


unittest.main()
