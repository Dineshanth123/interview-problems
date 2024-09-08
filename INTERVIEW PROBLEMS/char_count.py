x=input()
l=input("enter alphabet to count:")
list1=list(x)
len=len(list1)
sum=0
i=0
for x in range(len):
  if l==list1[i]:
    sum=sum+1
  i=i+1
print(sum)

