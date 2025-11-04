from survey import AnonymousSurvey

question = "What language did you first learn to speak? \n"
my_survey = AnonymousSurvey(question)

my_survey.show_question()
print("Enter 'q' to quit when prompted\n")
while True:
    response = input("Language: \n")
    if response == 'q':
        break
    else:
        my_survey.store_response(response)

my_survey.show_results()
