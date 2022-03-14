import math
def calculate(sheet):
    answer = sheet/5
    rounded = math.ceil(answer)
    print("Sheet is: ", sheet)
    print("The answer is: ", answer)
    print("Rounded is: ", rounded)
    return rounded

output = calculate(16)
print("The return statement is: ", output)