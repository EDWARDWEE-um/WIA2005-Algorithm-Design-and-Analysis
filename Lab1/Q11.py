a = [5, 10, 15, 20, 25]
newlist = []

def firstlast (a):
    newlist.append(a.pop(0))
    newlist.append(a.pop(-1))
    return newlist
    
print(firstlast(a))