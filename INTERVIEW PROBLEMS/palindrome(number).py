n=int(input("enter a number:"))
l=list(str(n))
len=len(l)
j=l.copy()   
j.reverse()
flag=0
for x in range(len):
  if l[x]==j[x]:
    flag=0
  else:
    flag=1
if(flag==1):
  print("not palindrome")
else:
  print("palindrome")
