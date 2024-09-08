n=int(input("enter number to check whether prime or not:"))
list=[]

for i in range(2,n+1):
  l=[]

  for x in range(1,10):
    
    if ((i%x)==0):
      l.append(x)
  if sum(l)==(i+1):
    
    list.append(i)
  else:
    pass
print(list)
list1=[]
for x in list:
  list1.append(x**(1/2))
print(list1)
