word = str(input("Please enter a word: "))
revsword = word[::-1]
print(revsword)

if word == revsword:
    print ('It is a palindrome')
else:
    print ('It is not a palindrome')
