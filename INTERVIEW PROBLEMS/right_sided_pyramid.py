n=int(input("enter number of rows:"))
for x in range(n):
  n=n-1
  x=x+1
  print(' '*(n),end='')
  print('*'*x)
