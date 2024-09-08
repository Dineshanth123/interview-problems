#similar to inverted right sided pyramid

n=int(input("enter number of rows:"))
x=0
for x in range(n):
  print(' '*x,end='')
  print('* '*n)       #here come spaces after *
  n=n-1
  x=x+1