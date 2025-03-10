# Alex Miller
# Multiplication Quiz

import pyinputplus as pyip
import random, time

numberOfQuestions = 10
correctAnswers = 0
for questionNumber in range(numberOfQuestions):
    # Pick two random numbers
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)

    prompt = '#%s: %s X %s = ' % (questionNumber, num1, num2)

    try:
        pyip.inputStr(prompt, allowRegexes = ['^%s$' % (num1 * num2)], # right answers
                                blockRegexes = [('.*', 'Incorrect!')], # wrong answers
                                timeout = 8, limit = 3)
    except pyip.TimeoutException:
        print('Out of Time! ' + 'Answer was: ' + str((num1 * num2)))
    except pyip.RetryLimitException:
        print('Out of Tries! ' + 'Answer was: ' +  str((num1 * num2)))
    else: # if no exceptions are run by the try block
        print('Correct!')
        correctAnswers += 1
    time.sleep(1) # pause to let user see the result
print('Score: %s / %s' % (correctAnswers, numberOfQuestions))