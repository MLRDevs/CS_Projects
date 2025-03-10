# Alex Miller
# creates quizzes with questions and answers in random order, along with answer key

import random

capitals = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock',
    'California': 'Sacramento',
    'Colorado': 'Denver',
    'Connecticut': 'Hartford',
    'Delaware': 'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
    'Hawaii': 'Honolulu',
    'Idaho': 'Boise',
    'Illinois': 'Springfield',
    'Indiana': 'Indianapolis',
    'Iowa': 'Des Moines',
    'Kansas': 'Topeka',
    'Kentucky': 'Frankfort',
    'Louisiana': 'Baton Rouge',
    'Maine': 'Augusta',
    'Maryland': 'Annapolis',
    'Massachusetts': 'Boston',
    'Michigan': 'Lansing',
    'Missesota': 'Saint Paul',
    'Mississippi': 'Jackson',
    'Missouri': 'Jefferson City',
    'Montana': 'Helena',
    'Nebraska': 'Lincoln',
    'Nevada': 'Carson City',
    'New Hampshire': 'Concord',
    'New Jersey': 'Trenton',
    'New Mexico': 'Santa Fe',
    'New York': 'Albany',
    'North Carolina': 'Raleigh',
    'North Dakota': 'Bismark',
    'Ohio': 'Columbus',
    'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem',
    'Pennsylvania': 'Harrisbury',
    'Rhode Island': 'Providence',
    'South Carolina': 'Columbia',
    'South Dakota': 'Pierre',
    'Tennessee': 'Nashville',
    'Texas': 'Autin',
    'Utah': 'Salt Lake City',
    'Vermont': 'Montpelier',
    'Virginia': 'Richmond',
    'Washington': 'Olympia',
    'West Virginia': 'Charleston',
    'Wisconsin': 'Madison',
    'Whyoming': 'Cheyenne'
}

for quizNum in range(5):
    quizFile = open(f'capitalsquiz{quizNum + 1}.txt', 'w')
    answerKeyFile = open(f'capitalsquiz_answers{quizNum + 1}.txt', 'w')

    # Header for Quiz
    quizFile.write('Name:\n\nDate:\n\n')
    quizFile.write((' ' * 20) + f'State Capitals Quiz (form {quizNum + 1})')
    quizFile.write('\n\n')

    # Shuffle the States
    states = list(capitals.keys())
    random.shuffle(states)

    # Loop through all states and make a question for it
    for questionNum in range(50):
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

        # write the question and answer options to the quiz file
        quizFile.write(f'{questionNum + 1} What is the capital of {states[questionNum]}?\n')
        for i in range(4):
            quizFile.write(f"   {'ABCD'[i]}. { answerOptions[i]}\n")
        quizFile.write('\n')

        # write the answer key to the file
        answerKeyFile.write(f"{questionNum + 1}. {'ABCD'[answerOptions.index(correctAnswer)]}")
        answerKeyFile.write('\n')
    quizFile.close()
    answerKeyFile.close()


