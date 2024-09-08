x=int(input("enter a number:"))
l=len(str(x))
sum=0
for i in range(l):
  n=x%10
  sum=sum+n
  x=x//10
print(sum)
