n=int(input("enter number of rows:"))
x=1
for i in range(n):
  print(' '*i,end='')
  print('*'*((n*2)-x))
  x=x+2