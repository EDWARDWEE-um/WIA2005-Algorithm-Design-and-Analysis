name = input("Enter username:")
age = int(input("Enter age:"))

def ageCalculator(age):
    year = 2021
    while age != 100:
        age+=1
        year+=1
    return year
print('You will turn 100 at : ' + str(ageCalculator(age)))