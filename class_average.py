def calcualte_average(scores):
    iterator = 0
    accumulator = 0
    student_count = len(scores)

    while iterator < len(scores):
        accumulator += scores[iterator]
        iterator += 1
    average = accumulator/student_count
    return average


output = calcualte_average([100, 80, 90, 70, 50, 95])
print("The average of total scores in the class is: ", output)