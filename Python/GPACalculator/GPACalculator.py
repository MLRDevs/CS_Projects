# Alex Miller
# GPA Calculator, asks for semesters, grades, credits, calculates GPA by semester along with in total

import sys

def main(): # main method
    print()
    print('\t\t---GPA Calculator---')
    print()
    sem = input('Enter how many semesters: ') # ask user for amount of semesters
    while not sem.isdecimal() or int(sem) <= 0: # if they're being dumb
        print('That\'s not going to work, try again')
        print()
        sem = input('Enter how many semesters: ')
        print()

    sem = int(sem) # change the semester number to an int
    print()
    semnames = [] # names of the semesters
    for i in range(sem): # enter the names for the semesters
        semname = input('Enter the name for semester #{}: '.format(i+1))
        semnames.append(semname)
    semclasses = [] # all the classes for all semesters ==> ['C+4', 'C 4', 'A 4', 'B+4'] max of three chars per slot
    print()

    amountclasses = [] # amount of classes per semester ==> ['2', '2'] two semesters two classes each
    start = 0
    for i in range(sem): # enter the amount of classes for each semester
        amount = input('Enter the amount of classes for {}: '.format(semnames[i]))
        while not amount.isdecimal() or int(amount) <= 0: # not a positive number 
            print('That\'s not going to work, try again')
            print()
            amount = input('Enter the amount of classes for {}: '.format(semnames[i]))
        amount = int(amount)
        amountclasses.append(amount)
        for j in range(start,amount): # for each class in the semester
            gradecredit = input('Enter the grade and the amount of credits (ex: C+4 or C 4): ') # enter the grades and the credits gotten
            while len(gradecredit) != 3: # wrong format
                print('Wrong format, Try again')
                print()
                gradecredit = input('Enter the grade and the amount of credits (ex: C+4 or C 4): ')
            semclasses.append(gradecredit) # add the grade and credits to the list
        print()

    GradeToPoints = { # dictionary of the letter grades to points
        'A+': 4.0,
        'A ': 4.0,
        'A-': 3.7,
        'B+': 3.3,
        'B ': 3.0,
        'B-': 2.7,
        'C+': 2.3,
        'C ': 2.0,
        'C-': 1.7,
        'D+': 1.3,
        'D ': 1.0,
        'D-': 0.7,
        'F ': 0.0
    }

    CalcGPA(semclasses, GradeToPoints, amountclasses, semnames)
    
    '''
    Grade, Credits, Points, (Points*Credits)
    A+ == 4.0 == 4.0 == 16
    B+ == 4.0 == 3.3 == 13.2
    C- == 4.0 == 1.7 == 6.8

    Total Credits = 12
    Total Points = 36

    GPA = 36 / 12 == 3.0 == B average

    '''
def CalcGPA(semclasses, GradeToPoints, amountclasses, semnames): # calculate each semester GPA and the entire GPA

    # print the semester name and the classes with it
    amount = 0
    print()
    for i in range(len(semnames)):
        print('=== ' + semnames[i] + ' ===')
        for j in range(amountclasses[i]):
            course = semclasses[amount]
            grade = course[:2]
            credit = course[2:]
            print('Grade: ' + grade + ' Credits: ' + credit) # prints ==> Grade: A+ Credits: 4
            amount += 1
        print()



    # each semester overall GPA
    amount = 0
    print()
    print('=== Semester GPA\'s ===')
    for i in range(len(amountclasses)): # for each semester
        TCredits = 0
        TPoints = 0.0
        GPA = 0.00
        for j in range(int(amountclasses[i])): # for each class in a semester
            course = semclasses[amount] # get the course ==> C+4
            grade = course[:2] # get the grade ==> C+
            credit = course[2:] # get the credits ==> 4
            points = GradeToPoints.get(grade, 0) # change the letter grade to points ==> C+ = 2.3
            TCredits += int(credit) # add the credits ==> TCredits += 4
            TPoints += (float(points) * float(credit)) # Add the points ==> Tpoints += (2.3 * 4)
            GPA = (TPoints / TCredits) # calculate the GPA ==> (9.2 / 4) (total points / total credits)
            GPA = round(GPA, 2) # rounding the GPA to 2 decimal places
            amount += 1 # changing this so i don't look at repeat classes
        print('{} semester GPA is: {}'.format(semnames[i], GPA)) # printing the semester GPA

    # Full overall GPA, almost same code as per semester, just in total
    print()
    TPoints = 0.0
    TCredits = 0
    GPA = 0.00
    for i in range(len(semclasses)): # for every class
        course = semclasses[i]
        grade = course[:2]
        credit = course[2:]
        points = GradeToPoints.get(grade, 0)
        TCredits += int(credit)
        TPoints += (float(points) * float(credit))
    
    GPA = (TPoints / TCredits)
    GPA = round(GPA, 2)
    print()
    print('=== Total GPA ===')
    print('Total Overall GPA: {}'.format(GPA)) # printing the overall GPA
    print()
    again = input('Would you like to run it again? (yes or no): ')
    if again.startswith('y'): # run the program again
        print()
        main()
    else:
        print()
        print('Thanks!')
        print()
        sys.exit()

# run main()
if __name__ == '__main__':
    main()