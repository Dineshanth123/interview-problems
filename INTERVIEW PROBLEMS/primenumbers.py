n=int(input("enter number to check whether prime or not:"))
l=[]
for x in range(1,10):
  if ((n%x)==0):
    l.append(x)
if sum(l)==(n+1):
  print("given number is prime")
else:
  print("given number is not prime")