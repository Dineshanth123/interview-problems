n=int(input("enter number of rows:"))
x=0
for x in range(n):
  print(' '*x,end='')
  print('*'*n)
  n=n-1
  x=x+1