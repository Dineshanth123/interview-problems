n=int(input("enter a number:"))
l=[]
while n!=0:
  l.append(n%2)
  n=n//2
l.reverse
for x in l:
  print(x,end='')
