n1=int(input("enter number 1:"))
n2=int(input("enter number 2:"))
l1=[]
l2=[]
for x in range(1,10):
  if ((n1%x)==0):
    l1.append(x)

for x in range(1,10):
  if ((n2%x)==0):
    l2.append(x)
fin=[]
for x in l1:
  if x in l2:
    fin.append(x)
print(fin)
print(max(fin))
