nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(1)
else:
   print("Fibonacci sequence:")
   while count < nterms+1:
       if n1 !=0:
           print(n1)
           nth = n1 + n2
           # update values
           n1 = n2
           n2 = nth
           count += 1
       else:
           nth = n1 + n2
           # update values
           n1 = n2
           n2 = nth
           count += 1