number = int(input("Enter a number:"))

def oddEven(number):
    if number%2 == 0:
        return 'This number is even'
    else:
        return 'This number is odd'
    
print(oddEven(number))