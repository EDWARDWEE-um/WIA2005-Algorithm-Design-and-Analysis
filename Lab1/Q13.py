a = [1, 1, 2, 2, 3, 5, 8, 13, 21, 34, 55, 89,89]
result = []

def duperemove(a,result):
    [(result.append(i)) for i in a if i not in result]
    return result

print(duperemove(a,result))