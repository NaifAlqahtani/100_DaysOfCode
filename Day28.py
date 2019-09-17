students = ['Naif','Mohammed', 'Ali','Abdullah','Omar']
scores = [95,98,60,43,80]

result = 'undefined'
student = 0
score = 0
length = len(students)-1

while student < length:
    student += 1
    score += 1
    if scores[score] > 60:
        result = 'passed'
    else:
        result = 'failed'
    print("{} scored {}. {} {}.".format(students[student],scores[score],students[student],result))
