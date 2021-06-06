testScore = 95 #<------------ change this value for a different result!
passingScore = 70
retakeScore = 60

print('Your score is {}'.format(testScore))

if testScore >= passingScore and testScore >= 95:
    print('Congrats! You passed the Exam with an exceptional score!')
elif testScore >= passingScore:
    print('Congrats! You passed.')
elif testScore < passingScore:
    print('Sorry, you failed the exam.', end = ' ')
    if testScore >= retakeScore:
        print('However, you scored a retake score. You can retake the exam!')
    else:
        print('And you cannot retake it :(')
