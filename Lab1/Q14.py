sentence = input("Enter a sentence: ")

def reverser(sentence):
    x = sentence.split()
    rev = ""
    while len(x) > 0:
        rev += x.pop(-1)+" "
    return rev

print(reverser(sentence))