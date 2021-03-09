import random

randomnum = random.randint(1, 9)

def guess(randomnum):
    while True:
        usernum = int(input('Enter a number: '))
        if usernum==randomnum:
            print('Exactly Right')
            break
        elif usernum > randomnum :
            print('Too High')
        elif usernum < randomnum :
            print('Too Low')

guess(randomnum)