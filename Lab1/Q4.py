number = int(input("Enter a number:"))

def divisor(number):
    divisorz = []
    count = 1
    while count != number+1:
        if number%count==0:
            divisorz.append(count)
        count+=1
    return divisorz

print(divisor(number))
        